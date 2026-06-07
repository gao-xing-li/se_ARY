# PRD 对齐与 PoC/Demo 迭代任务说明

## 1. 差异分析

| 维度 | 个人原文档 | 小组 PRD 基准 | 对齐结论 |
| --- | --- | --- | --- |
| PRD 主线 | Organizer-first，ARY 仅最小登记，Public Projection 倾向按需读取 | Public Yard / Private Race Source；ARY 可持久化 Public Metadata / Projection | 采用小组 PRD，个人 PRD 降为下游约束来源 |
| ARY 持久化 | 公开登记信息最小化，Projection 不作为长期主线 | Public Metadata / Public Projection 可由 ARY 存储、索引、展示 | 改为“公开披露可持久化，Race Source Facts 不可持久化” |
| 用户角色 | Organizer、评审者/访问者 | Organizer、Rider / Participant、Viewer、Agent | 补入 Participant / Rider 与 Agent 访问边界 |
| 报名链路 | 未进入核心闭环 | ARY Stateless Proxy 转发报名，Organizer Server 写入事实 | 报名入口转发进入功能闭环 |
| 报名数据 | 偏保守，报名摘要未明确可展示 | 公开报名计数、公开 RiderID / nickname 可由 Organizer 披露为 Projection | 长期展示必须来自 Organizer 主动披露 |
| 可用性状态 | `unavailable` / `revoked` 为主 | 引入 `Suspended` | `Suspended` 表示公开接入不可达，不表示内部事实 |
| 代码阶段 | 当前周不写实际 PoC 代码 | 小组已有可运行 PoC | 改为 P8 冻结实现设计，P9 必须编写实际 PoC 代码 |
| 个人严谨设计 | 字段溯源、缓存撤回、DCR 输出、验证证据页 | 小组 PoC 已有 privacy check / rejection demo / demo verification | 保留并迁移为后续迭代验收项 |

## 2. 文档修改计划

| 文件 | 修改方向 | 状态 |
| --- | --- | --- |
| `PLAN.md` | 增加 P8 实现设计、P9 实际 PoC 代码阶段 | 已完成 |
| `problem_definition.md` | 将核心问题改为 Public Yard / Private Race Source | 已完成 |
| `scope_boundary.md` | 加入 Participant、Registration Proxy、Organizer Server、Suspended | 已完成 |
| `acceptance_checklist.md` | 加入 Proxy 零落库、公开持久化、代码 PoC 验收 | 已完成 |
| `open_questions.md` | 将已由小组 PRD 确认的项降级为实现待冻结，新增凭证、日志、端点信任问题 | 已完成 |
| `prd.md` | 改为 PRD 对齐说明，不再作为产品主线 | 已完成 |
| `poc_design.md` | 改为实际 PoC 设计与代码任务入口 | 已完成 |
| `poc_validation_matrix.md` | 增加 Proxy、Suspended、公开持久化和版本/hash 验证 | 已完成 |
| `architecture.md` | 改为 Public Yard / Private Race Source 架构 | 已完成 |
| `data_flow.md` | 增加报名代理、公开报名摘要、Suspended 数据流 | 已完成 |
| `demo_plan.md`、`demo_script.md` | 改为可运行 PoC 验收脚本 | 已完成 |
| `decision_log.md` | 新增 D-037 至 D-044 | 已完成 |
| `riding_record_draft.md` | 记录小组基准对齐和代码阶段纠偏 | 已完成 |

## 3. PoC/Demo 迭代任务清单

| 阶段 | 任务 | 产出 | 验证 |
| --- | --- | --- | --- |
| P8-01 | 冻结 Public Metadata schema | 字段表、Pydantic model | 私有源事实字段无法通过 |
| P8-02 | 冻结 Public Projection schema | 字段表、版本/hash 规则 | 旧版本拒绝，同版本同 hash 幂等，同版本不同 hash 冲突 |
| P8-03 | 冻结 forbidden key/value marker | forbidden 清单 | key-level 和 value-level 泄露均可识别 |
| P8-04 | 冻结 Proxy 日志白名单 | 日志字段规则 | 请求体、私有错误详情不落日志 |
| P9-01 | 实现或迭代 Organizer Server | `organizer_app` | 完整 Race Source Facts 和报名事实只在 Organizer |
| P9-02 | 实现或迭代 ARY public stores | `ary_app` | 只存 Public Metadata / Projection / connectivity |
| P9-03 | 实现或迭代 Registration Proxy | `/proxy/race/001/register` | 无 `save()`、无 `commit()`、无报名库 |
| P9-04 | 实现或迭代 Public Page | `/explore/race/001` | 展示公开数据、表单、边界文案 |
| P9-05 | 实现 Suspended Demo | health check + 离线页面 | Organizer 离线时只展示公开可达性状态 |
| P9-06 | 实现验证证据页或 debug endpoints | privacy-check、ary-store、rejection-demo、demo-journey | 验收证据可复跑 |
| P9-07 | 更新 Demo Verification | 启动命令、请求、预期结果 | 组员可按文档复现 |

## 4. 本轮验收清单

- [x] `group_ARY_week1/PRD-ARY-GRS-001.md` 被明确设为 PRD 基准。
- [x] 个人 PRD 中旧的“Public Projection 仅按需读取”不再作为当前主线。
- [x] 文档承认 ARY 可持久化 Public Metadata / Public Projection。
- [x] 文档承认 Participant / Rider、Registration Proxy、Organizer Server。
- [x] 报名事实只写 Organizer Server。
- [x] ARY Proxy 不 `save()` / `commit()`，不生成报名事实库。
- [x] 公开报名计数、公开 RiderID / nickname、公开参与摘要长期展示时来自 Organizer Public Projection。
- [x] `Suspended` 只表示 Organizer Server 不可达或入口挂起。
- [x] Race Source Facts 不进入 ARY 持久化、日志、缓存、debug 输出或验证材料。
- [x] 字段溯源、缓存撤回、DCR 输出清单、越界拒绝和验证证据页进入 PoC/Demo 任务。

## 5. 后续验收清单

- [ ] P8 完成实现设计与合约冻结。
- [ ] P9 编写实际 PoC 代码并运行 Demo 验证。
