# ARY GRS 001 PoC 验收说明

本文档用于验证 ARY GRS 001 PoC 是否满足“Public Yard, Private Race Source”的架构边界。

## 启动命令

在第一个终端启动 Organizer Server：

```bash
uvicorn ary_grs_001_poc:organizer_app --port 9001
```

在第二个终端启动 ARY Server：

```bash
uvicorn ary_grs_001_poc:ary_app --port 8000
```

如果 Windows 提示 `WinError 10048` 或 `address already in use`，说明该端口已经被占用。优先检查是否已经有一个 Organizer Server 在运行；如果有，直接复用该服务，不需要重复启动。

Windows 查看占用：

```powershell
netstat -ano | findstr :9001
```

结束占用进程：

```powershell
taskkill /PID <PID> /F
```

默认 Organizer 端口是 `9001`。仅当 `9001` 被占用且无法结束占用进程时，才使用 `9002` 作为 fallback：

```bash
uvicorn ary_grs_001_poc:organizer_app --port 9002
```

如果使用 `9002`，必须在启动 ARY Server 时同步设置 `ORGANIZER_BASE_URL`，否则 ARY 仍会按默认配置访问 `9001`。

PowerShell：

```powershell
$env:ORGANIZER_BASE_URL="http://127.0.0.1:9002"
uvicorn ary_grs_001_poc:ary_app --port 8000
```

主流程验收默认仍使用：

- Organizer：`http://127.0.0.1:9001`
- ARY：`http://127.0.0.1:8000`

`demo_page.html` is a static preview snapshot; the authoritative PoC source remains `ary_grs_001_poc.py`.

cmd：

```bat
set ORGANIZER_BASE_URL=http://127.0.0.1:9002
uvicorn ary_grs_001_poc:ary_app --port 8000
```

## Journey 1：创建公开对象

请求：

```text
POST http://127.0.0.1:9001/demo/disclose-to-ary
```

期望结果：

- Organizer 从本地完整 Race Source Facts 生成 Public Metadata。
- ARY 接收并写入 `ary_public_metadata_store`。
- 返回结果包含 `race_public_id`、`stored_in`、`boundary`。
- ARY 不接收 `private_rulebook`、`submission_code`、`riding_records`、`execution_logs` 等源事实字段。

## Journey 2：披露公开投影

请求：

```text
GET http://127.0.0.1:8000/debug/demo-journey
```

期望结果：

- `organizer_holds_complete_race_source_facts` 为 true。
- `ary_metadata_exists` 为 true。
- `ary_projection_exists` 为 true。
- `ary_privacy_check.contains_core_private_source_fact_keys` 为 false。
- `public_registration_disclosure` 展示 Organizer 主动披露的公开报名摘要。

## Journey 3：报名代理

请求：

```text
POST http://127.0.0.1:8000/proxy/race/001/register
Content-Type: application/json

{
  "race_public_id": "race_001",
  "rider_id": "rider_demo_001",
  "client_request_id": "req_001"
}
```

期望结果：

- ARY Stateless Proxy 只做转发，不生成 ARY 自有 Race Source Facts 数据库。
- Organizer Server 接收报名请求，并在 Organizer 控制域内处理。
- 报名计数或公开 RiderID / nickname 可以后续由 Organizer 主动披露为 Public Projection。

## Journey 4：公开展示页

请求：

```text
GET http://127.0.0.1:8000/explore/race/001
```

期望结果：

- 返回 HTMLResponse 页面。
- 页面展示 Public Metadata、Public Projection、公开状态和 Organizer 公开信息。
- 页面包含 RIDE AGENT 表单，表单提交到 ARY proxy。
- 页面说明公开报名摘要可以披露，但代码、完整骑行记录和评审证据仍留在 Organizer / DCR。

## Privacy Check：隐私边界检查

请求：

```text
GET http://127.0.0.1:8000/debug/privacy-check
```

期望结果：

- 返回 `forbidden_key_paths`。
- 返回 `suspicious_value_paths`。
- `ary_public_stores_contain_core_private_source_facts` 为 false。
- 说明 Organizer 持有完整 Source Facts，ARY 只持有公开披露数据。

## Rejection Demo：泄露拒绝演示

请求：

```text
GET http://127.0.0.1:8000/debug/rejection-demo
```

期望结果：

- `rejected` 为 true。
- 返回 `suspicious_value_paths`。
- 恶意投影中包含 `def private_agent_strategy` 或 `local://dcr/.../full_trace.fit` 等明显私有源事实标记。
- 恶意投影不会写入 ARY store。

## Suspended Demo：Organizer 离线挂起

步骤：

1. 停止 Organizer Server。
2. 保持 ARY Server 运行。
3. 访问：

```text
GET http://127.0.0.1:8000/explore/race/001
```

期望结果：

- 页面仍可由 ARY 的 Public Metadata / Public Projection 渲染。
- `public_status` 显示为 `Suspended`。
- `Suspended` 仅表示 Organizer Server 不可达，不代表 ARY 知道赛事执行状态或内部事实。

## 验收结论

ARY 只持久化 Organizer 主动披露的 Public Metadata / Public Projection。Race Source Facts，包括参赛者代码、完整骑行记录、执行日志、DCR 判断链、评审证据、复盘材料和私有规则细节，仍然留在 Organizer / DCR 控制域。

## Final Acceptance Conclusion（最终验收结论）

ARY 可以通过 Organizer 主动披露的 Public Metadata 与 Public Projection 创建、披露、组织和渲染公开 Race 对象。

ARY 不会成为参赛者代码、完整骑行记录、执行日志、DCR 判断链、评审证据或复盘材料的中心化事实数据库。

报名摘要只有在 Organizer 主动披露为 Public Projection 时，才可以作为公开信息展示。

因此，该 PoC 证明了“Public Yard, Private Race Source（公开骑场，私有赛事源）”的架构边界。
