# P8 实现检查与增强清单

## 1. 文档定位

本文用于 P8：在不推倒现有 `group_ARY_week1/ary_grs_001_poc.py` 双 FastAPI app 的前提下，检查现有代码已覆盖哪些 P9 验收项，并冻结后续代码与 Demo 增强任务。

原则：

- 不重写系统，不拆分现有单文件 PoC。
- 只在现有 `organizer_app` 与 `ary_app` 上增量增强。
- 优先补强可复跑验证、统一证据入口、Demo 文档和 debug 泄露边界。
- 所有增强仍必须遵守 Public Yard / Private Race Source：ARY 只持久化 Organizer 主动披露的 Public Metadata / Public Projection，不持久化 Race Source Facts 或报名事实库。

## 2. 现有代码覆盖情况

| P9 验收项 | 当前覆盖 | 证据位置 | 结论 |
| --- | --- | --- | --- |
| P9-01 Organizer Server | 已覆盖 | `organizer_app`、`local_organizer_db`、`POST /api/race/register`、`GET /debug/organizer-store` | Organizer 持有完整 Race Source Facts，并写入报名事实 |
| P9-02 ARY public stores | 已覆盖 | `ary_public_metadata_store`、`ary_public_projection_store`、`POST /api/races/metadata`、`POST /api/races/{race_public_id}/projection` | ARY 持久化 Public Metadata / Public Projection |
| P9-03 Registration Proxy | 基本覆盖 | `POST /proxy/race/001/register`、`POST /proxy/race/001/register-form`、`GET /debug/ary-store` | Proxy 透传报名请求，返回 `ary_registration_store = does_not_exist` |
| P9-04 Public Page | 已覆盖 | `GET /explore/race/001`、`demo_page.html` | 页面展示公开披露、报名表单和边界文案 |
| P9-05 Suspended Demo | 基本覆盖 | `organizer_is_online()`、`GET /explore/race/001`、Proxy 异常分支 | Organizer 不可达时写入 connectivity state 并展示 `Suspended` |
| P9-06 验证证据接口 | 部分覆盖 | `GET /debug/privacy-check`、`GET /debug/ary-store`、`GET /debug/demo-journey`、`GET /debug/rejection-demo` | 证据分散，缺少统一 Evidence Dashboard |
| P9-07 Demo Verification | 部分覆盖 | `group_ARY_week1/DEMO_VERIFICATION.md` | 已覆盖主旅程、Proxy、Suspended、privacy、rejection；缺少版本/hash 可复跑步骤和 debug 边界说明 |

## 3. 关键缺口

| 缺口 | 当前状态 | 风险 | P8 处理 |
| --- | --- | --- | --- |
| Projection version/hash 可复跑验证 | 代码已有旧版本拒绝、同版本同 hash 幂等、同版本不同 hash 冲突逻辑，但没有独立验收步骤或样例 payload | 评审只能读代码，不能稳定复现 | 补充请求样例；必要时增加 `/debug/projection-version-hash-demo` |
| Evidence Dashboard | 现有证据分散在多个 debug endpoint | Demo 时需要多次切换接口，容易漏验 | 增加统一证据入口 `/debug/evidence-dashboard`，聚合 stores、privacy、proxy、projection、connectivity 结果 |
| DEMO_VERIFICATION.md 不完整 | 现有文档覆盖主旅程，但版本/hash、Proxy 零落库、debug 边界不够细 | 后续代码验收缺少固定脚本 | 补全版本/hash、Proxy 零落库、Suspended、rejection-demo、debug 边界完整步骤 |
| Organizer debug 与 ARY debug 泄露边界 | `GET /debug/organizer-store` 会返回完整私有数据；ARY debug 只应返回公开数据、字段路径、布尔结果 | 若把 Organizer debug 当公开证据页展示，会泄露私有正文 | 明确 Organizer debug 仅限本地评审；ARY debug 不得输出私有正文 |
| Proxy 零落库证明 | Proxy 返回 `ary_registration_store = does_not_exist`，ARY store 有 `explicitly_absent`，但 DEMO 文档未要求报名前后对比 | 不能清楚证明 ARY 未沉淀报名事实 | 增加报名前后 `/debug/ary-store` 对比步骤 |
| 日志边界 | 现有代码使用 `print()`，没有统一日志白名单说明 | 未来增强时可能把请求体或私有错误详情打进日志 | 明确只允许 route、status、duration、client_request_id hash、connectivity，不记录请求体 |

## 4. P8 增强计划

### E-01 Projection version/hash 可复跑验证

目标：让评审能用固定请求复现三类结果。

必须覆盖：

- 旧版本提交返回 `409`。
- 同版本同 `projection_hash` 返回 `idempotent = true`。
- 同版本不同 `projection_hash` 返回 `409`。
- 新版本更高且 hash 不同可以写入。

实现选项：

- 最小方案：只补充 `DEMO_VERIFICATION.md` 的 curl / HTTP payload。
- 推荐方案：新增 `GET /debug/projection-version-hash-demo`，内部构造三类提交并返回结构化结果，便于一键验收。

验收：

- 输出包含 `older_version_rejected`、`same_version_same_hash_idempotent`、`same_version_different_hash_rejected`、`newer_version_accepted`。
- 验证过程不得写入私有源事实。

### E-02 Evidence Dashboard 或统一证据入口

目标：把分散证据聚合到一个 endpoint，降低 Demo 操作复杂度。

推荐新增：

```text
GET /debug/evidence-dashboard
```

返回建议：

- `boundary`: `Public Yard, Private Race Source`
- `organizer_private_source_summary`: 只返回私有字段名、是否存在、存储位置，不返回私有正文。
- `ary_public_store_summary`: metadata/projection/connectivity keys。
- `ary_privacy_check`: forbidden key/value paths 与布尔结果。
- `proxy_zero_persistence`: `ary_registration_store`、`ary_rider_db`、`ary_race_fact_db` 均 absent。
- `projection_integrity`: 当前版本、hash、签名、最近验证结果。
- `registration_boundary`: Organizer registered rider count；ARY 不返回 rider 明细库。
- `connectivity`: Open / Suspended、checked_at。
- `rejection_demo`: 最近或即时的恶意投影拒绝结果。

边界：

- 不在 dashboard 中返回 `submission_code`、完整 `riding_records`、`execution_logs`、`dcr_judgement_trace`、`review_evidence`、`retro_notes` 正文。
- 如需证明 Organizer 持有完整数据，只返回字段名和 `exists = true`。

### E-03 DEMO_VERIFICATION.md 补全

必须新增或扩展以下章节：

- `Projection Version / Hash Demo`
  - 旧版本拒绝。
  - 同版本同 hash 幂等。
  - 同版本不同 hash 冲突。
  - 新版本接受。
- `Proxy Zero Persistence`
  - 报名前访问 `/debug/ary-store`。
  - 提交 `/proxy/race/001/register`。
  - 报名后再次访问 `/debug/ary-store`。
  - 验证 `explicitly_absent` 仍包含 `ary_registration_store`、`ary_rider_db`、`ary_race_fact_db`。
- `Evidence Dashboard`
  - 访问 `/debug/evidence-dashboard`。
  - 核对 public stores、privacy、proxy、projection、connectivity。
- `Suspended Demo`
  - 保留停止 Organizer Server 的手动步骤。
  - 增加访问 `/debug/ary-store` 检查 `ary_public_connectivity_state` 的步骤。
- `Rejection Demo`
  - 明确恶意投影不得进入 `ary_public_projection_store`。
- `Debug Boundary`
  - `GET /debug/organizer-store` 是 Organizer 本地验证接口，可显示私有数据，仅用于本地评审。
  - `GET /debug/ary-store` 是 ARY 公开侧调试接口，只能显示公开披露和公开可达性状态。
  - `GET /debug/privacy-check` 与 `/debug/evidence-dashboard` 不得输出私有正文。

### E-04 Organizer Debug 与 ARY Debug 边界

当前判断：

- `GET /debug/organizer-store` 返回 `local_organizer_db`，包含完整私有源事实。它只能作为 Organizer 控制域本地调试接口，不应作为 ARY 公开页面或公开证据页内容。
- `GET /debug/ary-store` 返回 ARY public stores，并调用 `assert_ary_public_stores_are_clean()`，可作为 ARY 侧边界证据。
- `GET /debug/demo-journey` 因单进程 PoC 能读取 `local_organizer_db`，但当前只返回私有源事实存在性和 Organizer rider count，不返回私有正文；后续增强必须保持该边界。
- `GET /debug/privacy-check` 当前只检查 ARY public stores 并返回布尔值、路径和说明，符合 ARY debug 边界。

P8 要求：

- 在代码注释或 Demo 文档中标注 Organizer debug 与 ARY debug 的可见范围。
- Evidence Dashboard 只能输出 Organizer 私有字段名和存在性，不输出私有正文。
- 所有 ARY debug endpoint 均不得返回 Organizer 私有源事实正文。

## 5. P9 代码修改清单

| 编号 | 修改项 | 文件 | 验收 |
| --- | --- | --- | --- |
| C-01 | 新增 `/debug/evidence-dashboard` | `group_ARY_week1/ary_grs_001_poc.py` | 一次请求返回核心证据，且不泄露私有正文 |
| C-02 | 新增或文档化 projection version/hash demo | `ary_grs_001_poc.py` 或 `DEMO_VERIFICATION.md` | 四类版本/hash 场景可复跑 |
| C-03 | 强化 Proxy 零落库证据 | `ary_grs_001_poc.py`、`DEMO_VERIFICATION.md` | 报名前后 ARY store 均无报名事实库 |
| C-04 | 明确 Organizer debug / ARY debug 边界 | `DEMO_VERIFICATION.md`、必要代码注释 | 文档写明哪些 endpoint 可显示私有内容，哪些绝不允许 |
| C-05 | 补全 Suspended 验证 | `DEMO_VERIFICATION.md` | 页面与 `ary_public_connectivity_state` 均显示 Suspended |
| C-06 | 补全 rejection-demo 验证 | `DEMO_VERIFICATION.md` | 恶意投影 rejected，且 projection store 未被污染 |
| C-07 | 日志白名单说明 | `DEMO_VERIFICATION.md` 或代码注释 | 禁止请求体、私有错误详情、Race Source Facts 进入日志 |

## 6. 后续执行顺序

1. 先补 `DEMO_VERIFICATION.md`，把已有能力变成可复跑验收步骤。
2. 再新增 `/debug/evidence-dashboard`，只聚合已有证据，不改变业务流。
3. 再决定 version/hash 使用文档 payload 还是新增一键 debug endpoint。
4. 最后运行完整 Demo，按 `DEMO_VERIFICATION.md` 记录结果。

## 7. P8 完成标准

- [x] 已确认现有代码覆盖哪些 P9 验收项。
- [x] 已列出 Projection version/hash、Evidence Dashboard、DEMO_VERIFICATION.md、debug 泄露边界缺口。
- [x] 已明确不推倒现有实现，只在双 FastAPI app 上增强。
- [x] 已给出后续代码修改清单。
- [x] P9 按本清单完成代码与 Demo 文档修改。
- [x] P9 运行完整验收并记录结果。
