"""
ARY GRS 001 minimal PoC.

Run:
  pip install fastapi uvicorn
  python ary_grs_001_poc.py

Try:
  GET  http://127.0.0.1:8000/demo/run
  GET  http://127.0.0.1:8000/ary/races/{race_public_id}/page

This file intentionally keeps complete Race facts inside the Organizer domain.
ARY stores only Public Metadata and Public Projection objects.
"""

from __future__ import annotations

import hashlib
import json
import uuid
from copy import deepcopy
from datetime import datetime, timezone
from typing import Any, Dict, List, Literal, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="ARY GRS 001 PoC", version="1.0.0")

# ---------------------------------------------------------------------------
# Organizer-controlled local facts. This is NOT an ARY database.
# ---------------------------------------------------------------------------

ORGANIZER_PRIVATE_RACE_STORE: Dict[str, Dict[str, Any]] = {}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(
        microsecond=0).isoformat().replace("+00:00", "Z")


def as_dict(model: BaseModel) -> Dict[str, Any]:
    """Pydantic v1/v2 compatible model-to-dict helper."""
    if hasattr(model, "model_dump"):
        return model.model_dump(exclude_none=True)
    return model.dict(exclude_none=True)


def init_organizer_private_race() -> Dict[str, Any]:
    """
    Journey step 1:
    Organizer initializes complete private Race data locally.

    This object contains private rules, participants, execution telemetry,
    evidence, review data, and retrospective notes. It must never be stored
    in ARY_METADATA_STORE or ARY_PROJECTION_STORE.
    """
    private_race = {
        "race_internal_id":
        "org-local-race-2026-0001",
        "series_id":
        "ary-grs-001",
        "organizer": {
            "internal_org_id": "org-internal-devcompass-racing",
            "public_id": "org_devcompass_racing",
            "public_name": "DevCompass Racing",
            "legal_contact": {
                "name": "Private Organizer Operator",
                "email": "private-ops@example.internal",
                "phone": "+86-PRIVATE",
            },
        },
        "private_race_definition": {
            "full_rulebook": {
                "version":
                "v1.3.0",
                "eligibility_rules":
                ["private eligibility rule A", "private eligibility rule B"],
                "route_rules": ["private route constraint A"],
                "scoring_rules": ["private scoring formula"],
                "dispute_rules": ["private dispute handling process"],
            },
            "execution_plan": {
                "internal_start_at": "2026-06-01T08:00:00+08:00",
                "internal_end_at": "2026-06-30T23:59:59+08:00",
                "checkpoint_policy": "private checkpoint validation logic",
                "safety_protocol": "private emergency protocol",
            },
        },
        "participants": [{
            "participant_internal_id":
            "rider-0001",
            "real_name":
            "Private Rider A",
            "identity_document_hash":
            "sha256:private-id-hash",
            "contact": {
                "email": "rider-a@example.internal",
                "phone": "+86-PRIVATE",
            },
            "registration_status":
            "approved",
            "private_notes":
            "medical or operational private notes",
        }],
        "execution_records": [{
            "record_id":
            "exec-0001",
            "participant_internal_id":
            "rider-0001",
            "started_at":
            "2026-06-05T07:30:00+08:00",
            "finished_at":
            "2026-06-05T10:30:00+08:00",
            "telemetry": {
                "gps_trace_ref": "local://race-data/gps/rider-0001.fit",
                "distance_km": 68.4,
                "moving_time_seconds": 9120,
                "avg_speed_kmh": 27.0,
                "heart_rate_ref": "local://race-data/hr/rider-0001.json",
            },
            "evidence": [{
                "type": "photo",
                "uri":
                "local://race-data/evidence/rider-0001/checkpoint-1.jpg",
                "captured_at": "2026-06-05T08:12:00+08:00",
            }],
            "review_status":
            "pending_internal_review",
        }],
        "review_and_retro": {
            "internal_scores": [{
                "participant_internal_id": "rider-0001",
                "score": 91.5,
                "judge_notes": "private judge notes",
            }],
            "disputes": [],
            "retro_notes":
            "private organizer retrospective",
        },
    }

    ORGANIZER_PRIVATE_RACE_STORE[
        private_race["race_internal_id"]] = private_race
    print(
        "[Organizer] Initialized complete private Race data in Organizer-controlled local store."
    )
    print(
        "[Organizer] Private fields now held locally: participants, execution_records, review_and_retro."
    )
    return private_race


# ---------------------------------------------------------------------------
# ARY-controlled public stores. These are the only ARY persistence structures.
# They must contain only Public Metadata and Public Projection objects.
# ---------------------------------------------------------------------------

ARY_METADATA_STORE: Dict[str, Dict[str, Any]] = {}
ARY_PROJECTION_STORE: Dict[str, Dict[str, Any]] = {}

FORBIDDEN_ARY_KEYS = {
    "race_internal_id",
    "internal_org_id",
    "legal_contact",
    "private_race_definition",
    "full_rulebook",
    "execution_plan",
    "participants",
    "participant_internal_id",
    "real_name",
    "identity_document_hash",
    "execution_records",
    "telemetry",
    "gps_trace_ref",
    "heart_rate_ref",
    "evidence",
    "review_and_retro",
    "internal_scores",
    "judge_notes",
    "retro_notes",
}


def assert_no_private_keys(payload: Any, path: str = "$") -> None:
    """
    Defensive ARY-side schema guard.

    ARY refuses payloads containing fields that belong to Organizer facts.
    This keeps the mock stores structurally unable to persist complete Race data.
    """
    if isinstance(payload, dict):
        for key, value in payload.items():
            if key in FORBIDDEN_ARY_KEYS:
                raise HTTPException(
                    status_code=400,
                    detail=
                    f"ARY rejected private Organizer field at {path}.{key}",
                )
            assert_no_private_keys(value, f"{path}.{key}")
    elif isinstance(payload, list):
        for index, item in enumerate(payload):
            assert_no_private_keys(item, f"{path}[{index}]")


# ---------------------------------------------------------------------------
# Public Metadata Schema, PRD 9.1 aligned.
# ---------------------------------------------------------------------------


class OrganizerPublicProfile(BaseModel):
    name: str
    public_id: str
    avatar_url: Optional[str] = None


class TimeWindow(BaseModel):
    start: Optional[str] = None
    end: Optional[str] = None
    precision: Literal["date", "datetime", "month", "quarter", "text"] = "date"


class PublicMetadataCreate(BaseModel):
    series_id: str = "ary-grs-001"
    title: str
    public_summary: str
    organizer_public_profile: OrganizerPublicProfile
    public_status: Literal["Draft", "Open", "Active", "Completed", "Archived",
                           "Withdrawn"] = "Draft"
    time_window: Optional[TimeWindow] = None
    tags: List[str] = Field(default_factory=list)
    entry_link: Optional[str] = None


class PublicMetadataStored(PublicMetadataCreate):
    race_public_id: str
    projection_version: Optional[str] = None
    created_at: str
    updated_at: str


# ---------------------------------------------------------------------------
# Public Projection Schema, PRD 9.2 aligned.
# ---------------------------------------------------------------------------


class DisplaySection(BaseModel):
    type: str
    visibility: Literal["public"] = "public"
    content: str
    link: Optional[str] = None


class ProjectionSource(BaseModel):
    organizer_public_id: str
    projection_hash: str
    signature_algorithm: Literal["mock-sha256", "ed25519"] = "mock-sha256"
    signature: str


class DisclosurePolicy(BaseModel):
    contains_complete_race_data: Literal[False] = False
    contains_participant_personal_data: Literal[False] = False
    contains_execution_telemetry: Literal[False] = False
    contains_review_or_retro_data: Literal[False] = False


class PublicProjection(BaseModel):
    race_public_id: str
    series_id: str = "ary-grs-001"
    projection_version: str
    projection_type: str
    title: str
    display_sections: List[DisplaySection]
    source: ProjectionSource
    disclosure_policy: DisclosurePolicy = Field(
        default_factory=DisclosurePolicy)
    published_at: str


def canonical_json(payload: Dict[str, Any]) -> str:
    return json.dumps(payload,
                      ensure_ascii=False,
                      sort_keys=True,
                      separators=(",", ":"))


def mock_sign_projection(
        unsigned_projection: Dict[str, Any],
        organizer_private_signing_key: str) -> ProjectionSource:
    """
    Mock signature for PoC only.

    In a real implementation, Organizer would sign canonical JSON with a private
    key, and ARY would verify using Organizer's public key.
    """
    projection_hash = "sha256:" + hashlib.sha256(
        canonical_json(unsigned_projection).encode("utf-8")).hexdigest()
    signature = "mock-signature:" + hashlib.sha256(
        f"{projection_hash}:{organizer_private_signing_key}".encode(
            "utf-8")).hexdigest()
    return ProjectionSource(
        organizer_public_id="org_devcompass_racing",
        projection_hash=projection_hash,
        signature_algorithm="mock-sha256",
        signature=signature,
    )


def organizer_create_public_metadata(
        private_race: Dict[str, Any]) -> PublicMetadataCreate:
    """
    Organizer prepares only minimal public metadata.
    No private facts are copied into this object.
    """
    print("[Organizer] Creating Public Metadata from public-safe fields only.")
    return PublicMetadataCreate(
        title="ARY GRS 001 Genesis Ride",
        public_summary=
        "A public-facing genesis riding challenge disclosed by the Organizer.",
        organizer_public_profile=OrganizerPublicProfile(
            name=private_race["organizer"]["public_name"],
            public_id=private_race["organizer"]["public_id"],
            avatar_url="https://ary.example/assets/org_devcompass_racing.png",
        ),
        public_status="Open",
        time_window=TimeWindow(start="2026-06-01",
                               end="2026-06-30",
                               precision="date"),
        tags=["genesis", "riding", "agent-era"],
        entry_link="https://organizer.example/races/ary-grs-001",
    )


def organizer_generate_public_projection(
    private_race: Dict[str, Any],
    race_public_id: str,
    projection_version: str = "v1.0.0",
) -> PublicProjection:
    """
    Journey step 3:
    Organizer transforms private Race facts into an approved public projection.

    Notice that this function reads private data locally, but emits only
    summary/display sections. It does not expose participants, telemetry,
    evidence, review scores, or retrospective notes.
    """
    print(
        "[Organizer] Generating Public Projection locally from private Race data."
    )
    print(
        "[Organizer] Redacting participants, execution telemetry, evidence, review, and retro fields."
    )

    unsigned_projection = {
        "race_public_id":
        race_public_id,
        "series_id":
        private_race["series_id"],
        "projection_version":
        projection_version,
        "projection_type":
        "race_profile",
        "title":
        "ARY GRS 001 Genesis Ride",
        "display_sections": [
            {
                "type": "summary",
                "visibility": "public",
                "content":
                "Organizer-approved public summary for ARY display.",
            },
            {
                "type": "public_schedule",
                "visibility": "public",
                "content": "Public window: June 1 to June 30, 2026.",
            },
            {
                "type":
                "public_rules_summary",
                "visibility":
                "public",
                "content":
                "A high-level public rules summary disclosed by the Organizer.",
            },
            {
                "type": "public_entry",
                "visibility": "public",
                "content":
                "Use the Organizer-controlled entry channel for participation.",
                "link": "https://organizer.example/races/ary-grs-001",
            },
            {
                "type": "public_progress",
                "visibility": "public",
                "content": "Organizer-disclosed progress: active.",
            },
        ],
        "disclosure_policy": {
            "contains_complete_race_data": False,
            "contains_participant_personal_data": False,
            "contains_execution_telemetry": False,
            "contains_review_or_retro_data": False,
        },
        "published_at":
        utc_now(),
    }
    source = mock_sign_projection(
        unsigned_projection,
        organizer_private_signing_key="organizer-local-secret")
    return PublicProjection(**unsigned_projection, source=source)


# ---------------------------------------------------------------------------
# ARY API: creates public object, stores public projection, renders public page.
# ---------------------------------------------------------------------------


@app.post("/ary/races", response_model=PublicMetadataStored)
def create_public_race_object(
        metadata: PublicMetadataCreate) -> PublicMetadataStored:
    """
    Journey step 2:
    Organizer submits Public Metadata. ARY generates Race Public ID and persists
    only the public metadata.
    """
    metadata_payload = as_dict(metadata)
    assert_no_private_keys(metadata_payload)

    race_public_id = f"ary-grs-001-race-{uuid.uuid4().hex[:8]}"
    now = utc_now()
    stored = PublicMetadataStored(
        **metadata_payload,
        race_public_id=race_public_id,
        created_at=now,
        updated_at=now,
    )
    ARY_METADATA_STORE[race_public_id] = as_dict(stored)

    print(f"[ARY] Created Race Public ID: {race_public_id}")
    print(
        "[ARY] Stored Public Metadata only. No Organizer private facts accepted."
    )
    return stored


@app.post("/ary/races/{race_public_id}/projection",
          response_model=PublicProjection)
def submit_public_projection(race_public_id: str,
                             projection: PublicProjection) -> PublicProjection:
    """
    Journey step 3:
    Organizer submits signed Public Projection. ARY validates Race Public ID,
    version shape, disclosure policy, and private-field absence.
    """
    if race_public_id not in ARY_METADATA_STORE:
        raise HTTPException(
            status_code=404,
            detail="Race Public ID not found in ARY metadata store.")
    if projection.race_public_id != race_public_id:
        raise HTTPException(
            status_code=400,
            detail="Projection race_public_id does not match URL.")
    if not projection.projection_version.startswith("v"):
        raise HTTPException(status_code=400,
                            detail="Projection version must start with 'v'.")

    projection_payload = as_dict(projection)
    assert_no_private_keys(projection_payload)

    policy = projection.disclosure_policy
    if (policy.contains_complete_race_data
            or policy.contains_participant_personal_data
            or policy.contains_execution_telemetry
            or policy.contains_review_or_retro_data):
        raise HTTPException(
            status_code=400,
            detail=
            "ARY rejected projection because disclosure policy is not public-safe."
        )

    ARY_PROJECTION_STORE[race_public_id] = projection_payload
    ARY_METADATA_STORE[race_public_id][
        "projection_version"] = projection.projection_version
    ARY_METADATA_STORE[race_public_id]["updated_at"] = utc_now()

    print(
        f"[ARY] Stored Public Projection {projection.projection_version} for {race_public_id}."
    )
    print(
        "[ARY] Projection is public display data; no complete Race data is persisted."
    )
    return projection


@app.get("/ary/races/{race_public_id}/page")
def render_public_race_page(race_public_id: str) -> Dict[str, Any]:
    """
    Journey step 4:
    Viewer/Agent reads only ARY's Public Metadata and Public Projection stores.
    This simulates the public page.
    """
    metadata = ARY_METADATA_STORE.get(race_public_id)
    if not metadata:
        raise HTTPException(status_code=404, detail="Public race not found.")

    projection = ARY_PROJECTION_STORE.get(race_public_id)
    print(f"[Viewer/Agent] Rendering public page for {race_public_id}.")
    print("[ARY] Read source: ARY_METADATA_STORE + ARY_PROJECTION_STORE only.")

    return {
        "page_type":
        "ary_public_race_page",
        "race_public_id":
        race_public_id,
        "metadata":
        metadata,
        "projection":
        projection,
        "notice":
        "This page is rendered only from Organizer-disclosed Public Metadata and Public Projection.",
    }


@app.get("/debug/ary-store")
def debug_ary_store() -> Dict[str, Any]:
    """
    Debug endpoint for PoC verification.
    It exposes only ARY's in-memory public stores so you can inspect that no
    Organizer fact fields were persisted.
    """
    return {
        "ARY_METADATA_STORE": deepcopy(ARY_METADATA_STORE),
        "ARY_PROJECTION_STORE": deepcopy(ARY_PROJECTION_STORE),
        "forbidden_private_keys": sorted(FORBIDDEN_ARY_KEYS),
    }


@app.get("/demo/run")
def run_demo_journey() -> Dict[str, Any]:
    """
    Runs the full PRD section 6 journey in one request:
    1. Organizer initializes private Race facts.
    2. Organizer submits Public Metadata to ARY.
    3. Organizer generates redacted Public Projection locally and submits it.
    4. Viewer/Agent renders the public page using only ARY stores.
    """
    print("\n========== ARY GRS 001 PoC Demo Start ==========")
    ARY_METADATA_STORE.clear()
    ARY_PROJECTION_STORE.clear()
    ORGANIZER_PRIVATE_RACE_STORE.clear()

    private_race = init_organizer_private_race()

    metadata = organizer_create_public_metadata(private_race)
    stored_metadata = create_public_race_object(metadata)
    race_public_id = stored_metadata.race_public_id

    projection = organizer_generate_public_projection(private_race,
                                                      race_public_id)
    submit_public_projection(race_public_id, projection)

    public_page = render_public_race_page(race_public_id)
    print("[Demo] ARY store keys:", list(ARY_METADATA_STORE.keys()),
          list(ARY_PROJECTION_STORE.keys()))
    print("[Demo] Organizer private store keys:",
          list(ORGANIZER_PRIVATE_RACE_STORE.keys()))
    print("========== ARY GRS 001 PoC Demo End ==========\n")

    return {
        "demo_status": "success",
        "race_public_id": race_public_id,
        "public_page": public_page,
        "privacy_check": {
            "ary_metadata_store_contains_private_keys":
            contains_forbidden_keys(ARY_METADATA_STORE),
            "ary_projection_store_contains_private_keys":
            contains_forbidden_keys(ARY_PROJECTION_STORE),
            "organizer_private_store_contains_complete_facts":
            True,
        },
    }


def contains_forbidden_keys(payload: Any) -> bool:
    if isinstance(payload, dict):
        return any(key in FORBIDDEN_ARY_KEYS or contains_forbidden_keys(value)
                   for key, value in payload.items())
    if isinstance(payload, list):
        return any(contains_forbidden_keys(item) for item in payload)
    return False


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
