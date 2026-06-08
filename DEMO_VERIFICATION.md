# ARY GRS 001 PoC 验收说明

本文档用于验证 ARY GRS 001 PoC 是否满足 “Public Yard, Private Race Source” 架构边界。

权威 PoC 源码为 `ary_grs_001_poc.py`。`demo_page.html` 只是静态预览快照。

## 1. 启动命令

在第一个终端启动 Organizer Server：

```bash
uvicorn ary_grs_001_poc:organizer_app --port 9001
```

在第二个终端启动 ARY Server：

```bash
uvicorn ary_grs_001_poc:ary_app --port 8000
```

主流程验收默认使用：

- Organizer: `http://127.0.0.1:9001`
- ARY: `http://127.0.0.1:8000`

如果 Windows 提示 `WinError 10048` 或 `address already in use`，先检查是否已有服务运行：

```powershell
netstat -ano | findstr :9001
netstat -ano | findstr :8000
```

仅当 `9001` 被占用且无法结束占用进程时，才使用 `9002` 作为 Organizer fallback：

```powershell
$env:ORGANIZER_BASE_URL="http://127.0.0.1:9002"
uvicorn ary_grs_001_poc:organizer_app --port 9002
uvicorn ary_grs_001_poc:ary_app --port 8000
```

## 2. Debug 边界

| Endpoint | 所属边界 | 是否允许出现私有正文 | 用途 |
| --- | --- | --- | --- |
| `GET /debug/organizer-store` | Organizer local debug | 是，仅本地评审 | 证明完整 Race Source Facts 留在 Organizer 控制域 |
| `GET /debug/ary-store` | ARY public debug | 否 | 证明 ARY 只持久化 Public Metadata / Public Projection / connectivity |
| `GET /debug/privacy-check` | ARY public debug | 否 | 检查 ARY public stores 是否含 forbidden key/value |
| `GET /debug/evidence-dashboard` | ARY evidence | 否 | 汇总证据，Organizer 私有数据只显示字段名和存在性 |
| `GET /evidence-dashboard` | ARY evidence page | 否 | 可视化证据入口 |

注意：`/debug/organizer-store` 会返回完整 Organizer 本地数据，只能用于本地评审，不得嵌入 ARY 公开页或 Evidence Dashboard。

## 3. Journey 1：创建公开对象与披露投影

请求：

```text
POST http://127.0.0.1:9001/demo/disclose-to-ary
```

期望结果：

- Organizer 从本地完整 Race Source Facts 生成 Public Metadata 和 Public Projection。
- ARY 接收并写入 `ary_public_metadata_store` 与 `ary_public_projection_store`。
- 返回结果包含 `metadata_result`、`projection_result`、`organizer_private_source_still_local=true`。
- ARY 不接收 `private_rulebook`、`submission_code`、`riding_records`、`execution_logs`、`dcr_judgement_trace`、`review_evidence`、`retro_notes`。

## 4. Journey 2：公开旅程证据

请求：

```text
GET http://127.0.0.1:8000/debug/demo-journey
```

期望结果：

- `organizer_holds_complete_race_source_facts` 为 true。
- `ary_metadata_exists` 为 true。
- `ary_projection_exists` 为 true。
- `ary_privacy_check.contains_core_private_source_facts` 为 false。
- `public_registration_disclosure` 展示 Organizer 主动披露的公开报名摘要。

## 5. Journey 3：Proxy 零落库

报名之前先检查 ARY store：

```text
GET http://127.0.0.1:8000/debug/ary-store
```

期望：

- `explicitly_absent` 包含 `ary_registration_store`、`ary_rider_db`、`ary_race_fact_db`。

提交报名：

```text
POST http://127.0.0.1:8000/proxy/race/001/register
Content-Type: application/json

{
  "race_public_id": "race_001",
  "rider_id": "rider_demo_001",
  "client_request_id": "req_001"
}
```

期望：

- 返回 `boundary = Public Yard, Private Race Source`。
- 返回 `ary_persistence = none`。
- 返回 `ary_registration_store = does_not_exist`。
- `result_from_organizer.stored_in = local_organizer_db`。

报名之后再次检查：

```text
GET http://127.0.0.1:8000/debug/ary-store
GET http://127.0.0.1:8000/debug/evidence-dashboard
```

期望：

- ARY store 仍没有 `ary_registration_store`、`ary_rider_db`、`ary_race_fact_db`。
- Evidence Dashboard 中 `proxy_zero_persistence.ary_registration_store = absent`。
- 报名事实只反映为 Organizer registered rider count，不返回 ARY rider fact DB。

## 6. Journey 4：公开展示页与 Evidence Dashboard 页面

请求：

```text
GET http://127.0.0.1:8000/explore/race/001
GET http://127.0.0.1:8000/evidence-dashboard
```

期望：

- 公开页返回 HTMLResponse。
- 公开页展示 Public Metadata、Public Projection、公开状态和 Organizer 公开信息。
- 公开页包含“报名代理”表单，表单提交到 ARY proxy。
- 公开页说明公开报名摘要可以披露，但代码、完整骑行记录、执行日志、DCR 判断链、评审证据和复盘材料仍留在 Organizer / DCR。
- Evidence Dashboard 页面展示 privacy、proxy、projection、connectivity 和 debug boundary。
- Evidence Dashboard 只展示 Organizer 私有字段名和存在性，不展示私有正文。

## 7. Privacy Check：隐私边界检查

请求：

```text
GET http://127.0.0.1:8000/debug/privacy-check
```

期望：

- 返回 `forbidden_key_paths`。
- 返回 `suspicious_value_paths`。
- `ary_public_stores_contain_core_private_source_facts` 为 false。
- 说明 Organizer 持有完整 Source Facts，ARY 只持有公开披露数据。

## 8. Rejection Demo：泄露拒绝演示

请求：

```text
GET http://127.0.0.1:8000/debug/rejection-demo
GET http://127.0.0.1:8000/debug/ary-store
```

期望：

- `rejected` 为 true。
- 返回 `suspicious_value_paths`。
- 恶意投影中包含 `def private_agent_strategy` 或 `local://dcr/.../full_trace.fit` 等明显私有源事实标记。
- `stored_in_ary` 为 false。
- 后续 `debug/ary-store` 中没有恶意投影内容。

## 9. Projection Version / Hash Demo

请求：

```text
GET http://127.0.0.1:8000/debug/projection-version-hash-demo
```

期望：

- `cases.older_version_rejected.passed` 为 true。
- `cases.same_version_same_hash_idempotent.passed` 为 true。
- `cases.same_version_different_hash_rejected.passed` 为 true。
- `cases.newer_version_accepted.passed` 为 true。
- `private_source_facts_used` 为 false。

该 demo 使用独立公开 Race `race_projection_integrity_demo`，不会改变主线 `race_001` 的业务状态。

## 10. Suspended Demo：Organizer 离线挂起

步骤：

1. 停止 Organizer Server。
2. 保持 ARY Server 运行。
3. 访问：

```text
GET http://127.0.0.1:8000/explore/race/001
GET http://127.0.0.1:8000/debug/ary-store
GET http://127.0.0.1:8000/debug/evidence-dashboard
```

期望：

- 页面仍可由 ARY 的 Public Metadata / Public Projection 渲染。
- `public_status` 显示为 `Suspended`。
- `debug/ary-store.ary_public_connectivity_state.race_001.public_status = Suspended`。
- Evidence Dashboard 中 connectivity 显示 `Suspended`。
- `Suspended` 仅表示 Organizer Server 不可达，不代表 ARY 知道赛事执行状态、报名失败或内部事实。

恢复 Organizer Server 后，刷新公开页：

```text
GET http://127.0.0.1:8000/explore/race/001
```

期望：

- `public_status` 回到 `Open`。
- `organizer_connectivity` 回到 `online`。

## 11. 日志与 debug 输出约束

- ARY Proxy 不得记录完整请求体。
- ARY Proxy 不得记录 Organizer 返回的私有错误详情。
- 允许记录的最小日志字段：route、status、duration、client_request_id hash、connectivity。
- ARY debug endpoint 不得输出 `submission_code`、完整 `riding_records`、`execution_logs`、`dcr_judgement_trace`、`review_evidence`、`retro_notes` 正文。
- Evidence Dashboard 只能展示 Organizer 私有字段名和 `exists=true/false`。

## 12. 最终验收清单

以下清单已在 `docs/03_review/P9_ACCEPTANCE_REPORT.md` 中完成实际 HTTP 服务验收，并全部通过。

- [x] Organizer 持有完整 Race Source Facts。
- [x] ARY 只持久化 Organizer 主动披露的 Public Metadata / Public Projection。
- [x] ARY public stores 不含 forbidden key/value。
- [x] Registration Proxy 不产生 ARY 自有报名事实库。
- [x] 报名事实只写入 Organizer Server。
- [x] 公开报名摘要只有在 Organizer 主动披露为 Public Projection 时才长期展示。
- [x] Rejection Demo 证明恶意投影不会写入 ARY。
- [x] Projection version/hash demo 四项场景均通过。
- [x] Organizer 离线时 ARY 显示 `Suspended`，且不推断内部事实。
- [x] Evidence Dashboard 提供统一证据入口且不泄露私有正文。

## Final Acceptance Conclusion

ARY 可以通过 Organizer 主动披露的 Public Metadata 与 Public Projection 创建、披露、组织和渲染公开 Race 对象。

ARY 不会成为参赛者代码、完整骑行记录、执行日志、DCR 判断链、评审证据或复盘材料的中心化事实数据库。

报名摘要只有在 Organizer 主动披露为 Public Projection 时，才可以作为公开信息展示。

因此，该 PoC 证明了 “Public Yard, Private Race Source” 的架构边界。
