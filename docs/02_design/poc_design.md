# ARY GRS 001 PoC 设计

## 1. 文档定位

本文将个人 PoC 理论设计对齐到小组基准 `group_ARY_week1/ary_grs_001_poc.py` 和 `group_ARY_week1/DEMO_VERIFICATION.md`。

P7 输出实现设计与任务清单；P8 冻结合约；P9 需要编写并运行实际 PoC 代码。

## 2. PoC 目标

证明 “Public Yard, Private Race Source” 成立：

- Organizer Server / DCR 控制域持有完整 Race Source Facts。
- ARY 只持久化 Organizer 主动披露的 Public Metadata / Public Projection。
- ARY Stateless Proxy 可转发报名请求，但不写报名事实。
- Organizer Server 是报名事实唯一写入位置。
- ARY 可显示 `Suspended`，但不推断赛事内部事实。
- 公开报名计数、公开 RiderID / nickname、公开参与摘要只有在 Organizer 主动披露为 Public Projection 后才能长期展示。

## 3. 最小运行组件

| 组件 | 最小职责 | 必须证明 |
| --- | --- | --- |
| Organizer Server | 保存完整 Race Source Facts；接收报名；生成公开披露 payload | 完整数据和报名事实只在 Organizer 侧落库 |
| DCR Boundary | 表示 Organizer 控制域内的执行核和投影辅助 | 输出不得含执行日志、判断链、私有代码或评审证据 |
| ARY Server | 保存 Public Metadata / Projection；渲染公开页；提供 debug 验证 | public stores 不含核心私有源事实 |
| ARY Stateless Proxy | 校验报名请求形状并转发到 Organizer Server | 无 `save()`、无 `commit()`、无本地报名表 |
| Demo Page | 展示 Public Metadata / Projection、报名入口和边界文案 | 页面不泄露 Race Source Facts |
| Verification Evidence | 汇总存储清单、字段溯源、拒绝演示、Suspended 演示 | 验收可复盘 |

## 4. 数据合约候选

### 4.1 Race Source Facts

必须留在 Organizer Server / DCR 控制域：

- `submission_code`
- `private_submissions`
- `riding_records`
- `execution_logs`
- `dcr_judgement_trace`
- `review_evidence`
- `retro_notes`
- `private_rulebook`
- `private_score_basis`
- `full_result_evidence`

### 4.2 Public Metadata

可由 ARY 持久化：

- `race_public_id`
- `series_id`
- `title`
- `public_summary`
- `organizer_public_profile`
- `public_status`
- `entry_mode`
- `organizer_endpoints`
- `time_window`
- `tags`
- `projection_version`
- `updated_at`

### 4.3 Public Projection

可由 ARY 持久化，但必须来自 Organizer 主动披露：

- `race_public_id`
- `projection_version`
- `projection_type`
- `title`
- `public_registration_count`
- `public_participant_aliases`
- `public_participation_status`
- `display_sections`
- `source.projection_hash`
- `source.signature`
- `published_at`

### 4.4 Registration Transit Payload

短暂经过 ARY Stateless Proxy，不由 ARY 持久化：

- `race_public_id`
- `rider_id`
- `client_request_id`

## 5. 接口草案

| 接口 | 所属组件 | 目的 | 禁止事项 |
| --- | --- | --- | --- |
| `POST /api/race/register` | Organizer Server | 写入报名事实并返回即时结果 | 要求 ARY 代存报名事实 |
| `POST /api/races/metadata` | ARY Server | 接收 Organizer 主动披露的 Public Metadata | 接收 Race Source Facts |
| `POST /api/races/{id}/projection` | ARY Server | 接收 Public Projection 并检查版本/hash/私有字段 | 接收执行日志、DCR 判断链、私有代码 |
| `POST /proxy/race/{id}/register` | ARY Stateless Proxy | 透传 Participant 报名意图 | `save()` / `commit()` / 本地报名表 |
| `GET /explore/race/{id}` | ARY Server | 展示公开页和 `Suspended` 状态 | 读取 Organizer 私有库 |
| `GET /debug/privacy-check` | ARY Server | 检查 public stores 是否泄露私有源事实 | 输出私有正文 |
| `GET /debug/rejection-demo` | ARY Server | 演示越界投影拒绝 | 将恶意投影写入 ARY store |

## 6. 失败用例

| 编号 | 失败用例 | 预期结果 |
| --- | --- | --- |
| F-01 | Public Metadata 包含 `private_rulebook` | ARY 拒绝 |
| F-02 | Public Projection 包含 `submission_code` 或 `local://dcr/.../full_trace.fit` | ARY 拒绝并报告路径 |
| F-03 | Projection 旧版本提交 | ARY 返回冲突 |
| F-04 | 同版本不同 hash 提交 | ARY 返回冲突 |
| F-05 | ARY Proxy 试图写本地报名表 | 验收失败 |
| F-06 | Organizer Server 不可达 | ARY 页面显示 `Suspended` |
| F-07 | 长期报名计数来自代理请求聚合 | 验收失败 |
| F-08 | 日志或 debug 输出包含参赛者代码、完整骑行记录、评审证据 | 验收失败 |

## 7. 实际 PoC 代码任务

| 编号 | 任务 | 输出 |
| --- | --- | --- |
| T-01 | 冻结 Pydantic schema 和 forbidden key/value marker | schema 与拒绝规则 |
| T-02 | 实现 Organizer Server 私有存储和报名接口 | `organizer_app` |
| T-03 | 实现 Organizer 生成 metadata/projection 并披露给 ARY | `/demo/disclose-to-ary` |
| T-04 | 实现 ARY public stores 和投影版本/hash 校验 | `ary_public_metadata_store`、`ary_public_projection_store` |
| T-05 | 实现 ARY Stateless Proxy | `/proxy/race/001/register` |
| T-06 | 实现公开页和表单 | `/explore/race/001` |
| T-07 | 实现 `Suspended` 检测 | Organizer offline demo |
| T-08 | 实现 privacy check / rejection demo / ary-store debug | 验证证据 API |
| T-09 | 编写 Demo 验收说明和运行命令 | 可复跑验收文档 |

## 8. 通过标准

- Organizer debug store 能看到完整 Race Source Facts。
- ARY debug store 只包含 Public Metadata、Public Projection、公开可达性状态。
- ARY public stores 的 forbidden key/value 检查为 false。
- 报名请求经 ARY Proxy 后，报名事实只进入 Organizer Server。
- 停止 Organizer Server 后，ARY 公开页显示 `Suspended`。
- 恶意投影被拒绝，且没有写入 ARY store。
- Demo 页面展示公开报名摘要时，来源是 Organizer 主动披露的 Public Projection。
