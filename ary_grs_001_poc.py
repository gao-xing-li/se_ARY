"""
ARY GRS 001 PoC - Public Yard, Private Race Source.

This single file defines two FastAPI apps:
  1. organizer_app: Private Race Source. It owns complete Race data and
     persists source facts such as submissions, riding records, execution logs,
     DCR judgement traces, review evidence, and retro notes.
  2. ary_app: Public Yard. It stores only Public Metadata / Public Projection
     and provides a stateless Registration Proxy.

Security focus:
  Registration count, public RiderID / nickname, and public participant summaries
  may be disclosed by Organizer as Public Projection. The protected source facts
  are code, full riding records, execution logs, DCR judgement chains, review
  evidence, retro material, and private rule details.

Install:
  pip install fastapi uvicorn

Run Organizer Server:
  uvicorn ary_grs_001_poc:organizer_app --port 9001

Run ARY Server in another terminal:
  uvicorn ary_grs_001_poc:ary_app --port 8000

Try:
  # Journey 1 + 2: ask Organizer to generate public payloads and submit them to ARY
  POST http://127.0.0.1:9001/demo/disclose-to-ary

  # Or call ARY directly with Organizer-generated payloads
  POST http://127.0.0.1:8000/api/races/metadata
  POST http://127.0.0.1:8000/api/races/{race_public_id}/projection

  # Public page, registration proxy, and debug checks
  GET  http://127.0.0.1:8000/explore/race/001
  POST http://127.0.0.1:8000/proxy/race/001/register
       {"race_public_id":"race_001","rider_id":"rider_demo_001","client_request_id":"req_001"}
  GET  http://127.0.0.1:8000/debug/demo-journey
  GET  http://127.0.0.1:8000/debug/privacy-check
  GET  http://127.0.0.1:8000/debug/ary-store
  GET  http://127.0.0.1:9001/debug/organizer-store
"""

from __future__ import annotations

import json
import html
import os
import urllib.error
import urllib.parse
import urllib.request
from copy import deepcopy
from datetime import datetime, timezone
from typing import Any, Dict, Literal, Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field


ORGANIZER_BASE_URL = os.getenv("ORGANIZER_BASE_URL", "http://127.0.0.1:9001")
ARY_BASE_URL = os.getenv("ARY_BASE_URL", "http://127.0.0.1:8000")

organizer_app = FastAPI(title="Organizer Server - Private Race Source", version="1.0.0")
ary_app = FastAPI(title="ARY Server - Public Yard", version="1.0.0")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def model_to_dict(model: BaseModel) -> Dict[str, Any]:
    if hasattr(model, "model_dump"):
        return model.model_dump(exclude_none=True)
    return model.dict(exclude_none=True)


# ---------------------------------------------------------------------------
# Organizer domain: complete Race data and registration facts live here only.
# ---------------------------------------------------------------------------

local_organizer_db: Dict[str, Any] = {
    "private_race_source": {
        "race_internal_id": "org-local-race-001",
        "race_public_id": "race_001",
        "private_rulebook": {
            "full_rules": ["private eligibility rules", "private scoring rules"],
            "internal_capacity": 30,
            "review_policy": "private review and dispute process",
        },
        "private_submissions": [
            {
                "rider_id": "rider_alpha",
                "nickname": "Neon Alpha",
                "submission_code": "def private_agent_strategy():\n    return 'full private racing code'",
                "submitted_at": "2026-06-05T09:20:00Z",
            }
        ],
        "execution_plan": {
            "private_checkpoints": ["checkpoint-alpha", "checkpoint-beta"],
            "safety_protocol": "private safety protocol",
        },
        "public_registration_disclosure_note": "Registration count and public aliases may be disclosed by Organizer.",
        "registered_public_aliases": ["Neon Alpha"],
        "riding_records": [
            {
                "rider_id": "rider_alpha",
                "gps_trace": "local://dcr/riding/rider_alpha/full_trace.fit",
                "lap_events": ["private lap event stream"],
                "telemetry": {"speed": [31.2, 32.1], "cadence": [88, 91]},
            }
        ],
        "execution_logs": [
            {
                "event": "DCR_EXECUTION_STEP",
                "detail": "private execution chain log",
                "created_at": "2026-06-05T10:00:00Z",
            }
        ],
        "dcr_judgement_trace": {
            "chain": ["private DCR reasoning step 1", "private DCR reasoning step 2"],
            "private_score_basis": "private code and riding-record comparison",
        },
        "review_evidence": [
            {
                "type": "screenshot",
                "uri": "local://dcr/evidence/rider_alpha/review.png",
                "full_result_evidence": "private evidence payload",
            }
        ],
        "retro_notes": "private Organizer and DCR retrospective material",
    },
    "race_001_registered_riders": [],
}


class RegisterRequest(BaseModel):
    race_public_id: str
    rider_id: str
    client_request_id: str


class OrganizerPublicProfile(BaseModel):
    name: str
    public_id: str


class PublicMetadataPayload(BaseModel):
    race_public_id: Optional[str] = None
    series_id: str = "ary-grs-001"
    title: str
    public_summary: str
    organizer_public_profile: OrganizerPublicProfile
    public_status: Literal["Draft", "Open", "Active", "Completed", "Archived", "Withdrawn", "Suspended"] = "Open"
    entry_mode: Literal["proxy_to_organizer", "external_organizer_channel"] = "proxy_to_organizer"
    organizer_endpoints: Dict[str, str] = Field(default_factory=dict)
    time_window: Dict[str, str] = Field(default_factory=dict)
    tags: list[str] = Field(default_factory=list)
    projection_version: Optional[str] = None
    updated_at: Optional[str] = None


class DisplaySectionPayload(BaseModel):
    type: str
    visibility: Literal["public"] = "public"
    content: str
    link: Optional[str] = None


class PublicProjectionPayload(BaseModel):
    race_public_id: str
    series_id: str = "ary-grs-001"
    projection_version: str
    projection_type: str = "race_profile"
    title: str
    public_registration_count: Optional[int] = None
    public_participant_aliases: list[str] = Field(default_factory=list)
    public_participation_status: Optional[str] = None
    display_sections: list[DisplaySectionPayload]
    source: Dict[str, str]
    published_at: Optional[str] = None


def parse_projection_version(version: str) -> tuple[int, ...]:
    cleaned = version.strip().lower()
    if cleaned.startswith("v"):
        cleaned = cleaned[1:]
    parts = cleaned.split(".")
    parsed: list[int] = []
    for part in parts:
        if not part.isdigit():
            raise HTTPException(status_code=400, detail=f"Invalid projection_version: {version}")
        parsed.append(int(part))
    return tuple(parsed)


@organizer_app.get("/health")
def organizer_health() -> Dict[str, str]:
    print("[Organizer Server] Health check received. Organizer is online.")
    return {"status": "ok", "source": "organizer_server"}


@organizer_app.post("/api/race/register")
def organizer_register_rider(payload: RegisterRequest) -> Dict[str, Any]:
    """
    Private Race Source writes the registration fact.

    This is the only place where rider_id is persisted.
    """
    if payload.race_public_id != "race_001":
        raise HTTPException(status_code=404, detail="Race not found in Organizer domain.")

    riders = local_organizer_db["race_001_registered_riders"]
    if payload.rider_id not in riders:
        riders.append(payload.rider_id)

    local_organizer_db["private_race_source"]["private_participants"] = riders
    print(f"[Organizer Server] commit(): rider_id={payload.rider_id} stored in local_organizer_db.")
    print("[Organizer Server] Registration fact is now inside Private Race Source.")

    return {
        "status": "registered",
        "race_public_id": payload.race_public_id,
        "rider_id": payload.rider_id,
        "registration_count": len(riders),
        "data_owner": "organizer_server",
        "stored_in": "local_organizer_db",
    }


@organizer_app.get("/debug/organizer-store")
def debug_organizer_store() -> Dict[str, Any]:
    return {
        "boundary": "Private Race Source",
        "local_organizer_db": deepcopy(local_organizer_db),
    }


# ---------------------------------------------------------------------------
# ARY domain: public metadata/projection only. No registration facts.
# ---------------------------------------------------------------------------

ary_public_metadata_store: Dict[str, Dict[str, Any]] = {
    "race_001": {
        "race_public_id": "race_001",
        "series_id": "ary-grs-001",
        "title": "ARY GRS 001 Genesis Ride",
        "public_summary": "Organizer-disclosed public race page.",
        "organizer_public_profile": {
            "name": "DevCompass Racing",
            "public_id": "org_devcompass_racing",
        },
        "public_status": "Open",
        "entry_mode": "proxy_to_organizer",
        "organizer_endpoints": {
            "health_check": f"{ORGANIZER_BASE_URL}/health",
            "registration_proxy_target": f"{ORGANIZER_BASE_URL}/api/race/register",
        },
        "time_window": {
            "start": "2026-06-01",
            "end": "2026-06-30",
            "precision": "date",
        },
        "tags": ["genesis", "riding", "agent-era"],
        "projection_version": "v1.0.0",
        "updated_at": utc_now(),
    }
}

ary_public_projection_store: Dict[str, Dict[str, Any]] = {
    "race_001": {
        "race_public_id": "race_001",
        "series_id": "ary-grs-001",
        "projection_version": "v1.0.0",
        "projection_type": "race_profile",
        "title": "ARY GRS 001 Genesis Ride",
        "public_registration_count": 1,
        "public_participant_aliases": ["Neon Alpha"],
        "public_participation_status": "Open for disclosed public registration",
        "display_sections": [
            {
                "type": "summary",
                "visibility": "public",
                "content": "Organizer-approved public summary for ARY display.",
            },
            {
                "type": "public_entry",
                "visibility": "public",
                "content": "Use the ARY public entry button. The registration fact will be written only to Organizer Server.",
            },
        ],
        "source": {
            "organizer_public_id": "org_devcompass_racing",
            "projection_hash": "sha256:mock-public-projection",
            "signature": "mock-organizer-signature",
        },
        "published_at": utc_now(),
    }
}

# This is deliberately not a registration store. It contains only public
# connectivity state, which the PRD allows ARY to display.
ary_public_connectivity_state: Dict[str, Dict[str, Any]] = {}

FORBIDDEN_ARY_KEYS = {
    "private_race_source",
    "private_rulebook",
    "private_submissions",
    "submission_code",
    "full_rules",
    "internal_capacity",
    "execution_plan",
    "private_checkpoints",
    "safety_protocol",
    "riding_records",
    "gps_trace",
    "lap_events",
    "telemetry",
    "execution_logs",
    "dcr_judgement_trace",
    "private_score_basis",
    "review_evidence",
    "full_result_evidence",
    "retro_notes",
}


class PublicPage(BaseModel):
    boundary: Literal["Public Yard, Private Race Source"] = "Public Yard, Private Race Source"
    page: Dict[str, Any]
    projection: Optional[Dict[str, Any]] = None
    notice: str


def assert_ary_public_stores_are_clean() -> None:
    payload = {
        "metadata": ary_public_metadata_store,
        "projection": ary_public_projection_store,
        "connectivity": ary_public_connectivity_state,
    }
    leaks = find_forbidden_leaks(payload)
    if leaks["forbidden_key_paths"] or leaks["suspicious_value_paths"]:
        raise RuntimeError(f"ARY public stores contain private source facts: {leaks}")


def assert_payload_has_no_private_source_facts(payload: Dict[str, Any]) -> None:
    leaks = find_forbidden_leaks(payload)
    if leaks["forbidden_key_paths"] or leaks["suspicious_value_paths"]:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "ARY rejected payload containing private Race Source Facts.",
                "forbidden_key_paths": leaks["forbidden_key_paths"],
                "suspicious_value_paths": leaks["suspicious_value_paths"],
            },
        )


def find_forbidden_keys(payload: Any, path: str = "$") -> list[str]:
    found: list[str] = []
    if isinstance(payload, dict):
        for key, value in payload.items():
            current_path = f"{path}.{key}"
            if key in FORBIDDEN_ARY_KEYS:
                found.append(current_path)
            found.extend(find_forbidden_keys(value, current_path))
    elif isinstance(payload, list):
        for index, item in enumerate(payload):
            found.extend(find_forbidden_keys(item, f"{path}[{index}]"))
    return found


FORBIDDEN_VALUE_MARKERS = [
    "def private_agent_strategy",
    "local://dcr/",
    "private execution chain log",
    "private DCR reasoning",
    "full private racing code",
    "full_trace.fit",
    "private evidence payload",
]


def find_suspicious_values(payload: Any, path: str = "$") -> list[str]:
    found: list[str] = []
    if isinstance(payload, dict):
        for key, value in payload.items():
            found.extend(find_suspicious_values(value, f"{path}.{key}"))
    elif isinstance(payload, list):
        for index, item in enumerate(payload):
            found.extend(find_suspicious_values(item, f"{path}[{index}]"))
    elif isinstance(payload, str):
        for marker in FORBIDDEN_VALUE_MARKERS:
            if marker in payload:
                found.append(f"{path} contains marker: {marker}")
    return found


def find_forbidden_leaks(payload: Any) -> Dict[str, list[str]]:
    return {
        "forbidden_key_paths": find_forbidden_keys(payload),
        "suspicious_value_paths": find_suspicious_values(payload),
    }


@ary_app.post("/api/races/metadata")
def create_public_metadata(payload: PublicMetadataPayload) -> Dict[str, Any]:
    """
    PRD Journey 1: Organizer creates the public Race object in ARY.

    ARY stores only Public Metadata. It must not accept complete Race fields.
    """
    metadata = model_to_dict(payload)
    assert_payload_has_no_private_source_facts(metadata)

    race_public_id = metadata.get("race_public_id") or "race_001"
    metadata["race_public_id"] = race_public_id
    metadata["updated_at"] = metadata.get("updated_at") or utc_now()
    metadata.setdefault("organizer_endpoints", {})

    ary_public_metadata_store[race_public_id] = metadata
    assert_ary_public_stores_are_clean()

    print(f"[ARY] Public Metadata stored for {race_public_id}.")
    print("[ARY] stored_in=ary_public_metadata_store. No complete Race data persisted.")
    return {
        "race_public_id": race_public_id,
        "stored_in": "ary_public_metadata_store",
        "boundary": "Public Yard stores Public Metadata only",
        "public_status": metadata["public_status"],
    }


@ary_app.post("/api/races/{race_public_id}/projection")
def submit_public_projection(race_public_id: str, payload: PublicProjectionPayload) -> Dict[str, Any]:
    """
    PRD Journey 2: Organizer discloses a redacted Public Projection.

    ARY stores only Public Projection and rejects old versions / private fields.
    """
    projection = model_to_dict(payload)
    assert_payload_has_no_private_source_facts(projection)

    if payload.race_public_id != race_public_id:
        raise HTTPException(status_code=400, detail="Path race_public_id does not match projection body.")
    if race_public_id not in ary_public_metadata_store:
        raise HTTPException(status_code=404, detail="Public Metadata must be created before projection disclosure.")

    incoming_version = parse_projection_version(payload.projection_version)
    current_projection = ary_public_projection_store.get(race_public_id)
    if current_projection:
        current_version = parse_projection_version(current_projection.get("projection_version", "v0.0.0"))
        current_hash = current_projection.get("source", {}).get("projection_hash")
        incoming_hash = projection.get("source", {}).get("projection_hash")
        if incoming_version < current_version:
            raise HTTPException(
                status_code=409,
                detail=f"Projection version {payload.projection_version} is older than current {current_projection.get('projection_version')}.",
            )
        if incoming_version == current_version and incoming_hash == current_hash:
            print(f"[ARY] Idempotent Public Projection submit for {race_public_id} {payload.projection_version}.")
            return {
                "race_public_id": race_public_id,
                "projection_version": payload.projection_version,
                "stored_in": "ary_public_projection_store",
                "boundary": "Public Yard stores Organizer-disclosed Public Projection only",
                "idempotent": True,
            }
        if incoming_version == current_version and incoming_hash != current_hash:
            raise HTTPException(
                status_code=409,
                detail="Projection version already exists with a different projection_hash. Refusing same-version content drift.",
            )

    projection["published_at"] = projection.get("published_at") or utc_now()
    ary_public_projection_store[race_public_id] = projection
    ary_public_metadata_store[race_public_id]["projection_version"] = payload.projection_version
    ary_public_metadata_store[race_public_id]["updated_at"] = utc_now()
    assert_ary_public_stores_are_clean()

    print(f"[ARY] Public Projection {payload.projection_version} stored for {race_public_id}.")
    print("[ARY] stored_in=ary_public_projection_store. Private Race facts are not accepted.")
    return {
        "race_public_id": race_public_id,
        "projection_version": payload.projection_version,
        "stored_in": "ary_public_projection_store",
        "boundary": "Public Yard stores Organizer-disclosed Public Projection only",
        "idempotent": False,
    }


def http_get_json(url: str, timeout_seconds: float = 2.0) -> Dict[str, Any]:
    request = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
        return json.loads(response.read().decode("utf-8"))


def http_post_json(url: str, payload: Dict[str, Any], timeout_seconds: float = 5.0) -> Dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
        return json.loads(response.read().decode("utf-8"))


def build_public_metadata_from_private_source() -> Dict[str, Any]:
    """
    Organizer-side local function.

    Reads complete Race facts locally, emits only Public Metadata.
    """
    private_source = local_organizer_db["private_race_source"]
    print("[Organizer] Generating Public Metadata from local private source.")
    print("[Organizer] private_rulebook / private_participants / execution_records stay local.")
    return {
        "race_public_id": private_source["race_public_id"],
        "series_id": "ary-grs-001",
        "title": "ARY GRS 001 Genesis Ride",
        "public_summary": "Organizer-disclosed public race page.",
        "organizer_public_profile": {
            "name": "DevCompass Racing",
            "public_id": "org_devcompass_racing",
        },
        "public_status": "Open",
        "entry_mode": "proxy_to_organizer",
        "organizer_endpoints": {
            "health_check": f"{ORGANIZER_BASE_URL}/health",
            "registration_proxy_target": f"{ORGANIZER_BASE_URL}/api/race/register",
        },
        "time_window": {
            "start": "2026-06-01",
            "end": "2026-06-30",
            "precision": "date",
        },
        "tags": ["genesis", "riding", "agent-era"],
        "projection_version": "v1.0.0",
        "updated_at": utc_now(),
    }


def build_public_projection_from_private_source(race_public_id: str) -> Dict[str, Any]:
    """
    Organizer-side local function.

    Reads complete Race facts locally, emits only a redacted Public Projection.
    """
    private_source = local_organizer_db["private_race_source"]
    registered_riders = local_organizer_db["race_001_registered_riders"]
    public_aliases = list(dict.fromkeys(private_source.get("registered_public_aliases", []) + registered_riders))
    print("[Organizer] Generating redacted Public Projection from local private source.")
    print("[Organizer] Disclosure allowed: registration count, public aliases, public status, public summary.")
    print("[Organizer] Redaction active: no code, riding_records, execution_logs, judgement trace, review evidence, retro notes.")
    return {
        "race_public_id": race_public_id,
        "series_id": "ary-grs-001",
        "projection_version": "v1.0.1",
        "projection_type": "race_profile",
        "title": "ARY GRS 001 Genesis Ride",
        "public_registration_count": len(public_aliases),
        "public_participant_aliases": public_aliases,
        "public_participation_status": "Open for disclosed public registration",
        "display_sections": [
            {
                "type": "summary",
                "visibility": "public",
                "content": "Organizer-approved public summary for ARY display.",
            },
            {
                "type": "public_entry",
                "visibility": "public",
                "content": "Use the ARY public entry button. Registration is proxied, then stored only by Organizer Server.",
            },
            {
                "type": "public_status",
                "visibility": "public",
                "content": "Public registration is open while Organizer Server is reachable.",
            },
            {
                "type": "public_registration_count",
                "visibility": "public",
                "content": f"Public registration count disclosed by Organizer: {len(public_aliases)}.",
            },
            {
                "type": "public_participant_aliases",
                "visibility": "public",
                "content": "Public participant aliases: " + (", ".join(public_aliases) if public_aliases else "No public aliases disclosed yet."),
            },
        ],
        "source": {
            "organizer_public_id": "org_devcompass_racing",
            "projection_hash": "sha256:mock-generated-by-organizer",
            "signature": "mock-organizer-signature-over-public-projection",
        },
        "published_at": utc_now(),
    }


@organizer_app.post("/demo/disclose-to-ary")
def organizer_demo_disclose_to_ary() -> Dict[str, Any]:
    """
    Simulates PRD Journey 1 and Journey 2 from Organizer side:
    - Generate Public Metadata locally.
    - POST it to ARY.
    - Generate redacted Public Projection locally.
    - POST it to ARY.
    """
    print("\n========== Organizer Disclosure Demo Start ==========")
    metadata = build_public_metadata_from_private_source()
    metadata_result = http_post_json(f"{ARY_BASE_URL}/api/races/metadata", metadata)
    race_public_id = metadata_result["race_public_id"]

    projection = build_public_projection_from_private_source(race_public_id)
    projection_result = http_post_json(f"{ARY_BASE_URL}/api/races/{race_public_id}/projection", projection)

    print("[Organizer] Disclosure complete. Complete Race facts never left local_organizer_db.")
    print("========== Organizer Disclosure Demo End ==========\n")
    return {
        "boundary": "Organizer owns Private Race Source; ARY stores public disclosure only.",
        "metadata_result": metadata_result,
        "projection_result": projection_result,
        "organizer_private_source_still_local": True,
    }


def organizer_is_online() -> bool:
    try:
        http_get_json(f"{ORGANIZER_BASE_URL}/health", timeout_seconds=1.5)
        return True
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return False


@ary_app.get("/explore/race/001", response_class=HTMLResponse)
def explore_race_001() -> HTMLResponse:
    """
    Public page reads only ARY public metadata/projection.

    If Organizer Server is unreachable, ARY marks the public display state as
    Suspended. This is connectivity state, not private Race state.
    """
    metadata = deepcopy(ary_public_metadata_store["race_001"])
    projection = deepcopy(ary_public_projection_store["race_001"])

    if organizer_is_online():
        metadata["public_status"] = "Open"
        metadata["organizer_connectivity"] = "online"
        ary_public_connectivity_state["race_001"] = {
            "public_status": "Open",
            "organizer_connectivity": "online",
            "checked_at": utc_now(),
        }
        print("[ARY] Organizer Server reachable. Public page status remains Open.")
    else:
        metadata["public_status"] = "Suspended"
        metadata["organizer_connectivity"] = "offline"
        metadata["suspended_reason"] = "Organizer Server unreachable"
        ary_public_connectivity_state["race_001"] = {
            "public_status": "Suspended",
            "organizer_connectivity": "offline",
            "checked_at": utc_now(),
        }
        print("[ARY] Organizer Server unreachable. Public page status changed to Suspended.")
        print("[ARY] No private Race data read. No registration facts inferred.")

    assert_ary_public_stores_are_clean()

    race_public_id = html.escape(metadata["race_public_id"])
    series_id = html.escape(metadata["series_id"])
    title = html.escape(metadata["title"])
    summary = html.escape(metadata["public_summary"])
    public_status = html.escape(metadata["public_status"])
    status_lower = public_status.lower()
    projection_version = html.escape(metadata.get("projection_version", "n/a"))
    last_update = html.escape(metadata.get("updated_at", "n/a"))
    tags = metadata.get("tags", [])
    tag_html = "".join(
        f'<span class="rounded-full border border-cyan-400/20 bg-cyan-400/10 px-3 py-1 text-xs font-medium text-cyan-200">#{html.escape(str(tag))}</span>'
        for tag in tags
    )
    organizer = metadata.get("organizer_public_profile", {})
    organizer_name = html.escape(organizer.get("name", "Unknown Organizer"))
    organizer_public_id = html.escape(organizer.get("public_id", "unknown"))
    organizer_connectivity = html.escape(metadata.get("organizer_connectivity", "unknown"))
    entry_target = "#ride-agent"

    sections = projection.get("display_sections", []) if projection else []
    section_html = ""
    for index, section in enumerate(sections, start=1):
        section_type = html.escape(str(section.get("type", "public_section")).replace("_", " ").title())
        section_content = html.escape(str(section.get("content", "")))
        section_link = section.get("link")
        link_html = ""
        if section_link:
            safe_link = html.escape(str(section_link))
            link_html = f'<a class="mt-4 inline-flex items-center gap-2 text-sm font-semibold text-cyan-200 hover:text-white" href="{safe_link}"><i class="fa-solid fa-arrow-up-right-from-square"></i> Open disclosed link</a>'
        section_html += f"""
        <article class="group relative overflow-hidden rounded-lg border border-slate-700/70 bg-slate-900/55 p-5 shadow-2xl shadow-cyan-950/20 backdrop-blur-md transition hover:border-cyan-300/40">
          <div class="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-cyan-300/70 to-transparent opacity-70"></div>
          <div class="flex items-start gap-4">
            <div class="flex h-9 w-9 shrink-0 items-center justify-center rounded-md border border-purple-300/20 bg-purple-400/10 font-mono text-sm text-purple-100">{index:02d}</div>
            <div>
              <h3 class="text-sm font-semibold uppercase tracking-[0.22em] text-cyan-200">{section_type}</h3>
              <p class="mt-3 text-[15px] leading-7 text-slate-200">{section_content}</p>
              {link_html}
            </div>
          </div>
        </article>
        """

    if not section_html:
        section_html = """
        <article class="rounded-lg border border-slate-700/70 bg-slate-900/55 p-5 text-slate-300 backdrop-blur-md">
          No public projection sections have been disclosed by the Organizer yet.
        </article>
        """

    is_open = public_status == "Open"
    status_light = "bg-cyan-300 shadow-cyan-300/70" if is_open else "bg-amber-300 shadow-amber-300/70"
    status_ring = "border-cyan-300/40 bg-cyan-300/10 text-cyan-100" if is_open else "border-amber-300/40 bg-amber-300/10 text-amber-100"

    page_html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} · ARY GRS 001</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Inter', 'ui-sans-serif', 'system-ui'],
            mono: ['JetBrains Mono', 'ui-monospace', 'SFMono-Regular']
          }},
          animation: {{
            'status-pulse': 'statusPulse 1.8s ease-in-out infinite',
            'flow': 'flow 5s linear infinite'
          }},
          keyframes: {{
            statusPulse: {{
              '0%, 100%': {{ opacity: '0.55', transform: 'scale(0.88)' }},
              '50%': {{ opacity: '1', transform: 'scale(1.08)' }}
            }},
            flow: {{
              '0%': {{ backgroundPosition: '0% 50%' }},
              '100%': {{ backgroundPosition: '200% 50%' }}
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    body {{
      background:
        radial-gradient(circle at 18% 8%, rgba(34, 211, 238, 0.16), transparent 28%),
        radial-gradient(circle at 82% 12%, rgba(168, 85, 247, 0.16), transparent 30%),
        linear-gradient(180deg, #020617 0%, #0f172a 55%, #020617 100%);
    }}
    .grid-surface {{
      background-image:
        linear-gradient(rgba(148, 163, 184, 0.08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(148, 163, 184, 0.08) 1px, transparent 1px);
      background-size: 26px 26px;
    }}
    .gradient-frame {{
      position: relative;
    }}
    .gradient-frame::before {{
      content: "";
      position: absolute;
      inset: 0;
      border-radius: 0.75rem;
      padding: 1px;
      background: linear-gradient(135deg, rgba(34, 211, 238, 0.68), rgba(168, 85, 247, 0.58), rgba(34, 211, 238, 0.2));
      -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      pointer-events: none;
    }}
  </style>
</head>
<body class="min-h-screen font-sans text-slate-100">
  <header class="border-b border-slate-800/90 bg-slate-950/75 backdrop-blur-xl">
    <div class="mx-auto max-w-7xl px-5 py-4">
      <div class="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
        <div class="min-w-0">
          <div class="flex flex-wrap items-center gap-2 text-sm text-slate-400">
            <i class="fa-brands fa-github text-slate-300"></i>
            <span class="font-mono text-cyan-200">{series_id}</span>
            <span class="text-slate-600">/</span>
            <span class="truncate font-semibold text-slate-100">{title}</span>
          </div>
          <div class="mt-2 flex flex-wrap items-center gap-3">
            <span class="rounded-md border border-slate-700 bg-slate-900 px-2 py-1 font-mono text-xs text-slate-300">{race_public_id}</span>
            <span class="inline-flex items-center gap-2 rounded-full border px-3 py-1 text-xs font-bold uppercase {status_ring}">
              <span class="h-2.5 w-2.5 animate-status-pulse rounded-full {status_light} shadow-lg"></span>
              {public_status}
            </span>
          </div>
        </div>
        <div class="flex items-center gap-2 rounded-lg border border-slate-700 bg-slate-900/70 p-1 text-sm text-slate-300">
          <a class="rounded-md bg-slate-800 px-4 py-2 text-white" href="#"><i class="fa-regular fa-circle-dot mr-2 text-cyan-300"></i>Overview</a>
          <a class="rounded-md px-4 py-2 hover:bg-slate-800" href="#"><i class="fa-solid fa-timeline mr-2"></i>Public Logs</a>
          <a class="rounded-md px-4 py-2 hover:bg-slate-800" href="#"><i class="fa-solid fa-chart-line mr-2"></i>Insights</a>
        </div>
      </div>
    </div>
  </header>

  <main class="mx-auto max-w-7xl px-5 py-8">
    <section class="gradient-frame overflow-hidden rounded-xl bg-slate-900/45 p-5 shadow-2xl shadow-purple-950/25 backdrop-blur-md">
      <div class="grid gap-4 md:grid-cols-3">
        <div class="rounded-lg border border-slate-700/70 bg-slate-950/45 p-4">
          <div class="text-xs uppercase tracking-[0.2em] text-slate-500">Projection Version</div>
          <div class="mt-2 font-mono text-lg font-bold text-cyan-200">{projection_version}</div>
        </div>
        <div class="rounded-lg border border-slate-700/70 bg-slate-950/45 p-4">
          <div class="text-xs uppercase tracking-[0.2em] text-slate-500">Last Update</div>
          <div class="mt-2 font-mono text-lg font-bold text-slate-100">{last_update}</div>
        </div>
        <div class="rounded-lg border border-slate-700/70 bg-slate-950/45 p-4">
          <div class="text-xs uppercase tracking-[0.2em] text-slate-500">Series Tags</div>
          <div class="mt-3 flex flex-wrap gap-2">{tag_html}</div>
        </div>
      </div>
    </section>

    <div class="mt-8 grid gap-8 lg:grid-cols-[minmax(0,7fr)_minmax(320px,3fr)]">
      <section class="space-y-6">
        <div class="grid-surface gradient-frame overflow-hidden rounded-xl bg-slate-900/45 p-6 shadow-2xl shadow-cyan-950/20 backdrop-blur-md">
          <div class="flex items-center gap-3 border-b border-slate-700/70 pb-4">
            <i class="fa-regular fa-file-lines text-cyan-300"></i>
            <h1 class="text-xl font-extrabold tracking-tight text-white">Public Summary</h1>
          </div>
          <p class="mt-5 max-w-3xl text-base leading-8 text-slate-200">{summary}</p>
        </div>

        <div class="space-y-4">
          {section_html}
        </div>
      </section>

      <aside class="space-y-6">
        <div class="gradient-frame rounded-xl bg-slate-900/50 p-5 shadow-2xl shadow-purple-950/20 backdrop-blur-md">
          <div class="flex items-center gap-4">
            <div class="flex h-14 w-14 items-center justify-center rounded-xl bg-gradient-to-br from-cyan-300 to-purple-500 text-xl font-black text-slate-950">DC</div>
            <div>
              <div class="text-xs uppercase tracking-[0.22em] text-slate-500">Organizer</div>
              <h2 class="mt-1 text-lg font-bold text-white">{organizer_name}</h2>
              <p class="font-mono text-xs text-cyan-200">{organizer_public_id}</p>
            </div>
          </div>
          <div class="mt-5 rounded-lg border border-slate-700/70 bg-slate-950/45 p-4">
            <div class="flex items-center justify-between text-sm">
              <span class="text-slate-400">Organizer Link</span>
              <span class="font-mono text-cyan-200">{organizer_connectivity}</span>
            </div>
            <div class="mt-3 h-2 rounded-full bg-slate-800">
              <div class="h-2 rounded-full bg-gradient-to-r from-cyan-300 to-purple-400" style="width: {'100%' if organizer_connectivity == 'online' else '42%'}"></div>
            </div>
          </div>
        </div>

        <form id="ride-agent" method="post" action="/proxy/race/001/register-form" class="group relative block overflow-hidden rounded-xl p-[1px] shadow-2xl shadow-cyan-950/30">
          <span class="absolute inset-0 animate-flow bg-[linear-gradient(90deg,#22d3ee,#a855f7,#22d3ee)] bg-[length:200%_200%]"></span>
          <div class="relative rounded-xl bg-slate-950 p-5 transition group-hover:bg-slate-900">
            <div class="mb-4 text-center text-lg font-black tracking-wide text-white">⚡ RIDE AGENT</div>
            <label class="block text-xs font-semibold uppercase tracking-[0.2em] text-cyan-200" for="rider_id">Public Rider ID / nickname</label>
            <input class="mt-2 w-full rounded-lg border border-slate-700 bg-slate-900 px-3 py-2 font-mono text-sm text-white outline-none focus:border-cyan-300" id="rider_id" name="rider_id" value="rider_demo_001" />
            <input type="hidden" name="client_request_id" value="form_req_001" />
            <button class="mt-4 w-full rounded-lg bg-gradient-to-r from-cyan-300 to-purple-400 px-4 py-3 font-black text-slate-950" type="submit">Submit via ARY Proxy</button>
            <p class="mt-4 text-xs leading-5 text-cyan-50">公开报名摘要可以由 Organizer 披露；代码、完整骑行记录和评审证据仍留在 Organizer / DCR。</p>
          </div>
        </form>

        <div class="rounded-xl border border-slate-700/70 bg-slate-900/50 p-5 text-sm leading-6 text-slate-300 backdrop-blur-md">
          <div class="mb-2 font-mono text-xs uppercase tracking-[0.2em] text-purple-200">Boundary</div>
          ARY renders public disclosures only. Public registration summaries may appear here, but code, riding records, execution logs, judgement traces, review evidence, and retro notes remain in the Organizer-controlled DCR node.
        </div>
      </aside>
    </div>
  </main>

  <footer class="mx-auto max-w-7xl px-5 pb-8">
    <div class="rounded-xl border border-cyan-300/20 bg-cyan-300/10 px-5 py-4 text-sm font-semibold text-cyan-100 backdrop-blur-md">
      🛡️ This Race follows Decentralized Data Sovereignty. Source facts are safely stored in Organizer's local DCR node.
    </div>
  </footer>
</body>
</html>"""

    return HTMLResponse(page_html)


@ary_app.post("/proxy/race/001/register")
def ary_stateless_registration_proxy(payload: RegisterRequest) -> Dict[str, Any]:
    """
    Registration Proxy from PRD 6.5 / 8.6.

    ARY validates request shape and forwards it. There is intentionally:
      - no ARY registration list
      - no save()
      - no commit()
      - no local persistence of rider_id
    """
    if payload.race_public_id != "race_001":
        raise HTTPException(status_code=400, detail="Invalid race_public_id for ARY public route.")

    request_payload = model_to_dict(payload)
    print("[ARY Stateless Proxy] Received registration intent.")
    print("[ARY Stateless Proxy] No save(). No commit(). No local registration DB.")
    print("[ARY Stateless Proxy] Forwarding transient payload to Organizer Server.")

    try:
        organizer_result = http_post_json(
            f"{ORGANIZER_BASE_URL}/api/race/register",
            request_payload,
            timeout_seconds=5.0,
        )
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        ary_public_connectivity_state["race_001"] = {
            "public_status": "Suspended",
            "organizer_connectivity": "offline",
            "checked_at": utc_now(),
        }
        print("[ARY Stateless Proxy] Organizer unavailable. Marking public connectivity as Suspended.")
        raise HTTPException(status_code=503, detail="Organizer Server unavailable; registration is suspended.") from exc

    assert_ary_public_stores_are_clean()
    print("[ARY Stateless Proxy] Returning Organizer result without persisting registration facts.")

    return {
        "boundary": "Public Yard, Private Race Source",
        "ary_persistence": "none",
        "ary_registration_store": "does_not_exist",
        "result_from_organizer": organizer_result,
    }


@ary_app.post("/proxy/race/001/register-form")
async def ary_registration_form_proxy(request: Request) -> Dict[str, Any]:
    raw_body = (await request.body()).decode("utf-8")
    form = urllib.parse.parse_qs(raw_body)
    rider_id = form.get("rider_id", [""])[0]
    client_request_id = form.get("client_request_id", [""])[0]
    if not rider_id or not client_request_id:
        raise HTTPException(status_code=400, detail="rider_id and client_request_id are required.")
    print("[ARY Form Proxy] Received HTML form submission. Converting to JSON proxy payload.")
    return ary_stateless_registration_proxy(
        RegisterRequest(
            race_public_id="race_001",
            rider_id=rider_id,
            client_request_id=client_request_id,
        )
    )


@ary_app.get("/debug/ary-store")
def debug_ary_store() -> Dict[str, Any]:
    assert_ary_public_stores_are_clean()
    return {
        "boundary": "Public Yard",
        "ary_public_metadata_store": deepcopy(ary_public_metadata_store),
        "ary_public_projection_store": deepcopy(ary_public_projection_store),
        "ary_public_connectivity_state": deepcopy(ary_public_connectivity_state),
        "explicitly_absent": [
            "ary_registration_store",
            "ary_rider_db",
            "ary_race_fact_db",
        ],
    }


@ary_app.get("/debug/demo-journey")
def debug_demo_journey() -> Dict[str, Any]:
    """
    One-shot state view for the complete PoC journey.

    It verifies that Organizer private source exists, ARY public disclosure
    stores exist, and ARY still has no registration store / Race fact DB.
    """
    assert_ary_public_stores_are_clean()
    race_public_id = "race_001"
    metadata_exists = race_public_id in ary_public_metadata_store
    projection_exists = race_public_id in ary_public_projection_store
    private_source = local_organizer_db["private_race_source"]
    projection = ary_public_projection_store.get(race_public_id, {})
    leaks = find_forbidden_leaks(
        {
            "metadata": ary_public_metadata_store,
            "projection": ary_public_projection_store,
            "connectivity": ary_public_connectivity_state,
        }
    )
    return {
        "boundary": "Public Yard, Private Race Source",
        "journey": {
            "organizer_private_source_exists": "private_race_source" in local_organizer_db,
            "organizer_holds_complete_race_source_facts": all(
                key in private_source
                for key in [
                    "private_submissions",
                    "riding_records",
                    "execution_logs",
                    "dcr_judgement_trace",
                    "review_evidence",
                    "retro_notes",
                ]
            ),
            "ary_metadata_exists": metadata_exists,
            "ary_projection_exists": projection_exists,
            "html_public_page": f"/explore/race/{race_public_id.split('_')[-1]}",
            "current_public_page_race_public_id": race_public_id,
        },
        "ary_privacy_check": {
            "contains_core_private_source_facts": bool(
                leaks["forbidden_key_paths"] or leaks["suspicious_value_paths"]
            ),
            "forbidden_key_paths": leaks["forbidden_key_paths"],
            "suspicious_value_paths": leaks["suspicious_value_paths"],
            "has_race_source_fact_db": False,
        },
        "public_registration_disclosure": [
            section
            for section in projection.get("display_sections", [])
            if section.get("type") in {"public_registration_count", "public_participant_aliases"}
        ],
        "stores": {
            "ary_public_metadata_keys": list(ary_public_metadata_store.keys()),
            "ary_public_projection_keys": list(ary_public_projection_store.keys()),
            "organizer_registered_rider_count": len(local_organizer_db["race_001_registered_riders"]),
        },
        "next_steps": [
            "POST http://127.0.0.1:9001/demo/disclose-to-ary",
            "GET http://127.0.0.1:8000/explore/race/001",
            "GET http://127.0.0.1:8000/debug/privacy-check",
        ],
    }


@ary_app.get("/debug/rejection-demo")
def debug_rejection_demo() -> Dict[str, Any]:
    malicious_projection = {
        "race_public_id": "race_001",
        "series_id": "ary-grs-001",
        "projection_version": "v9.9.9",
        "projection_type": "race_profile",
        "title": "恶意泄露演示",
        "display_sections": [
            {
                "type": "leaked_source_fact",
                "visibility": "public",
                "content": "def private_agent_strategy(): return 'full private racing code'; local://dcr/riding/rider_alpha/full_trace.fit",
            }
        ],
        "source": {
            "organizer_public_id": "org_devcompass_racing",
            "projection_hash": "sha256:malicious",
            "signature": "mock-malicious-signature",
        },
        "published_at": utc_now(),
    }
    leaks = find_forbidden_leaks(malicious_projection)
    rejected = bool(leaks["forbidden_key_paths"] or leaks["suspicious_value_paths"])
    return {
        "rejected": rejected,
        "reason": "Payload contains private Race Source Fact value markers and was not stored.",
        "forbidden_key_paths": leaks["forbidden_key_paths"],
        "suspicious_value_paths": leaks["suspicious_value_paths"],
        "stored_in_ary": False,
    }


@ary_app.get("/debug/privacy-check")
def debug_privacy_check() -> Dict[str, Any]:
    leaks = find_forbidden_leaks(
        {
            "metadata": ary_public_metadata_store,
            "projection": ary_public_projection_store,
            "connectivity": ary_public_connectivity_state,
        }
    )
    return {
        "ary_public_stores_contain_core_private_source_facts": bool(
            leaks["forbidden_key_paths"] or leaks["suspicious_value_paths"]
        ),
        "forbidden_key_paths": leaks["forbidden_key_paths"],
        "suspicious_value_paths": leaks["suspicious_value_paths"],
        "organizer_store_contains_complete_source_facts": True,
        "registration_disclosure_policy": "Registration count and public aliases may be disclosed by Organizer as Public Projection.",
        "note": "Organizer facts are shown here only because this is a same-process PoC debug endpoint; ARY runtime stores do not reference code, riding records, execution logs, judgement trace, review evidence, or retro notes.",
    }


if __name__ == "__main__":
    print("This file defines two apps. Start them with:")
    print("  uvicorn ary_grs_001_poc:organizer_app --port 9001")
    print("  uvicorn ary_grs_001_poc:ary_app --port 8000")
