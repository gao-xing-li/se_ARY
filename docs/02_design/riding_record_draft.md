# ARY GRS 001 Riding Record 草稿

## 1. 记录定位

本文记录 ARY GRS 001 当前设计阶段的人机协作过程，重点说明输入、判断、约束、产出和后续代码 PoC 边界。

P7 当前阶段完成个人文档与小组 PRD 基准对齐；P8 冻结实现设计；P9 需要编写实际 PoC 代码并运行 Demo 验证。

## 2. 初始输入材料

| 类型 | 材料 | 作用 |
| --- | --- | --- |
| 原始任务材料 | `docs/00_sources/source_ARY_GRS_full_text.md`、`ARY_GRS.pdf` | 提供 Race 背景、核心冲突、PoC 证明对象和交付要求 |
| 项目约束 | `AGENTS.md` | 固化长期原则、事实来源、设计边界、Agent 执行规范 |
| 周计划 | `PLAN.md` | 管理 P0-P7 的阶段顺序、完成定义和非代码约束 |
| 需求基线 | `problem_definition.md`、`scope_boundary.md`、`acceptance_checklist.md` | 锁定问题、范围、角色边界和验收口径 |
| 小组基准 | `group_ARY_week1/PRD-ARY-GRS-001.md`、`DEMO_VERIFICATION.md`、`ary_grs_001_poc.py`、`demo_page.html`、`Riding Record.md` | 作为新的 PRD、PoC、Demo 和 Riding Record 对齐基准 |
| 设计产物 | `prd.md`、`poc_design.md`、`poc_validation_matrix.md`、`architecture.md`、`demo_plan.md` | 对齐小组基准后形成个人下游设计与实现任务 |
| 决策记录 | `decision_log.md` | 记录已确定和待验证的设计决策 |

## 3. 为什么先生成 AGENTS.md 和 PLAN.md

先生成 `AGENTS.md` 是为了把长期边界写清楚：

- Race 完整数据只留在 Organizer 侧。
- ARY 不持久化完整 Race 数据。
- 展示内容必须来自 Organizer 主动披露。
- 未完成实现设计前不跳过边界直接写代码；实现设计冻结后必须进入实际 PoC 代码。

先生成 `PLAN.md` 是为了把当前周目标拆成可验收步骤：

- P1 锁定问题与范围。
- P2 设计 PRD。
- P3 设计 PoC 理论方案。
- P4 设计架构与数据流。
- P5 设计 Demo。
- P6 维护 Riding Record。
- P7 做一致性评审与提交整理。

这个顺序避免 Agent 直接跳到实现或扩展功能。

## 4. 如何锁定问题定义和范围

P1 先从源材料中抽出核心冲突：

> Race 数据主权属于 Organizer，ARY 不做中心化持久化，但 ARY 仍要完成赛事创建、披露、组织与展示。

随后锁定四项 PoC 证明对象：

- 数据留存：完整 Race 数据仅留存在 Organizer 侧。
- 去中心化：ARY 不持久化完整 Race 数据仍可工作。
- 功能闭环：创建、披露、组织、展示可以闭合。
- 投影机制：ARY 展示完全来自公开元数据或 Public Projection。

范围控制方式：

- 将赛事指导、成果评审、骑行复盘排除在本阶段外。
- 将 DCR 部署、投影承载方式、公开字段集合保留为待确认或待验证。
- 将验收标准写成可检查条目，而不是泛泛描述。

## 5. 如何形成 PRD

P2 采用最小产品方案：

- Organizer 创建并维护权威 Race。
- Organizer 主动选择公开字段并发布 Public Projection。
- ARY 只登记公开入口和投影定位。
- 旧阶段采用“ARY 按需读取 Public Projection 并展示”的保守假设；P7 已由小组 PRD 基准替换为“ARY 可持久化 Organizer 主动披露的 Public Projection”。

PRD 重点回答：

- 产品目标：数据主权不转移，公开展示仍成立。
- 用户角色：Organizer、评审者或公开访问者。
- 系统角色：ARY、DCR、Public Projection。
- 产品闭环：创建、披露、组织、展示。
- 功能范围：Must / Should / Could 分级。
- 非目标：不做生产级平台、不做完整赛事执行系统、不写代码。

关键人类判断：

- 接受 Organizer-first 作为产品工作假设。
- 接受“ARY 只保存最小公开登记信息”的设计方向。
- 明确 Demo 和 PoC 都应服务于证明，而不是追求全栈完整度。

## 6. 如何形成 PoC 理论方案

P3 将 PoC 限定为单 Organizer、单 Race 的最小场景：

- Organizer 完整数据样例用于证明私有字段存在且留在 Organizer。
- ARY 最小登记信息样例用于证明 ARY 不需要完整数据。
- Public Projection 样例用于证明展示来源。

每项假设都定义了：

- 验证目标。
- 最小测试场景。
- 输入数据。
- 观测点。
- 通过标准。
- 失败条件。

PoC 不写代码，只形成后续代码 PoC 可执行的验证矩阵。

## 7. 如何形成架构与数据流

P4 将组件边界显式化：

- Organizer Local Store：持久化完整 Race 数据。
- Projection Publisher：从完整数据中生成公开投影。
- DCR：接触完整数据时必须位于 Organizer 授权域内。
- Public Projection：承载公开字段，不是完整数据源。
- ARY Registry：只持久化最小公开登记信息。
- ARY Display：临时读取和展示投影，不持久化完整数据。

数据流设计重点：

- 完整 Race 数据不进入 ARY。
- 公开登记信息从 Organizer 到 ARY Registry。
- Public Projection 从 Organizer 授权公开区到 ARY Display。
- 缓存只用于短期公开响应，不作为权威数据。

隐含复制检查关注：

- ARY Registry 字段是否膨胀。
- Public Projection 字段是否过宽。
- DCR 是否外传中间结果。
- 缓存是否变成事实持久化副本。

## 8. 如何形成 Demo 方案

P5 采用三页最小 Demo：

| 页面 | 证明内容 |
| --- | --- |
| Organizer 控制台 | 完整数据留在 Organizer；公开字段由 Organizer 主动选择 |
| ARY 公开页 | ARY 可通过 Public Projection 展示公开 Race |
| 验证证据页 | 对比 Organizer、ARY Registry、Public Projection 和展示字段 |

演示脚本按 8 步展开：

- 展示 Organizer 完整字段清单。
- 生成 Public Projection。
- 登记 ARY 公开入口。
- 打开 ARY 公开页。
- 展示字段溯源。
- 对比存储边界。
- 更新并撤回投影。
- 执行失败用例。

Demo 方向已确认：最小可证明方案，不实现全栈。

## 9. 人类做了哪些判断

- 指定当前阶段目标：PRD、PoC 理论、架构数据流、Demo、Riding Record。
- 明确 P7 不跳过实现设计直接写代码；P8 完成实现设计后，P9 必须编写实际 PoC 代码。
- 要求所有内容中文、关键、精炼。
- 要求先建约束与计划，再逐步推进。
- 明确每阶段产物、更新决策日志和输出下一步。
- 在 P5 后确认 Demo 是最小可证明方案，不实现全栈。

## 10. Agent 输出如何被约束

Agent 输出受到以下约束：

- 事实来源优先：以源材料和已生成文档为依据。
- 阶段边界：每次只完成 PLAN 中当前项。
- 范围约束：不扩展到非核心子系统。
- 数据边界：不设计完整数据进入 ARY 的路径。
- 决策约束：关键选择进入 `decision_log.md`。
- 验收约束：产物必须对照 `acceptance_checklist.md` 或阶段自检表。
- 文件约束：当前阶段只生成 Markdown 文档，不创建源码文件。

## 11. 留到下一阶段代码实现的内容

下一阶段如果进入代码 PoC，最小实现应包括：

- Organizer 本地完整数据存储样例。
- Public Projection 的生成、发布、更新、撤回。
- ARY Registry 的最小登记信息持久化。
- ARY 公开页展示 ARY 已持久化的 Organizer 主动披露 Public Projection，并保留字段溯源与撤回状态检查。
- 验证证据页展示字段清单、映射和失败用例。
- 自动或手动检查：
  - 私有字段不进入 ARY。
  - ARY 持久化内容不构成完整数据副本。
  - 展示字段均可追溯到 Public Projection。
  - 撤回后不展示旧有效正文。

仍不进入下一阶段的内容：

- 生产级权限系统。
- 多 Organizer、多 Race。
- 完整赛事执行、评审、复盘系统。
- 高可用、性能、安全合规的生产工程化。

## 12. 当前阶段复盘

当前设计链路成立：

```text
源材料
→ AGENTS / PLAN
→ 问题定义与范围
→ PRD
→ PoC 理论与验证矩阵
→ 架构与数据流
→ Demo 方案
→ Riding Record
```

当前最大风险不在产品方向，而在后续代码 PoC 是否严格执行边界：

- Public Projection 不能过宽。
- ARY Registry 不能膨胀。
- DCR 不能成为隐性复制通道。
- 缓存不能变成事实持久化副本。

## 13. P7 修订记录

根据一致性审查和修订计划，已完成以下设计文档修订：

- 同步阶段状态措辞，移除“留待 P4”“P4 前”等过期表达。
- 在 PRD 中更新 DCR 边界状态：P4 已形成 Organizer 授权域原则，真实部署和输出清单待代码 PoC 验证。
- 在 PoC 中增加 DCR 输出清单、最小 Public Projection 字段冻结、缓存撤回验证。
- 在架构与数据流中强化 DCR 输出边界、投影字段边界和缓存失效规则。
- 在 Demo 中增加 DCR 输出清单、投影字段冻结结果和缓存撤回检查的展示点。

本轮仍未编写实际 PoC 代码，所有新增内容均为后续代码 PoC 的验证前置条件。

## 14. Riding Record 自检

| 自检项 | 状态 |
| --- | --- |
| 记录初始输入材料 | 通过 |
| 说明 AGENTS.md 和 PLAN.md 的作用 | 通过 |
| 说明问题定义和范围如何锁定 | 通过 |
| 说明 PRD 形成路径 | 通过 |
| 说明 PoC 理论方案形成路径 | 通过 |
| 说明架构与数据流形成路径 | 通过 |
| 说明 Demo 方案形成路径 | 通过 |
| 记录人类判断 | 通过 |
| 记录 Agent 约束 | 通过 |
| 记录下一阶段代码实现边界 | 通过 |

## 15. P7 小组 PRD 对齐记录

本轮人类指令明确：以 `group_ARY_week1/PRD-ARY-GRS-001.md` 作为新的 PRD 基准，个人原 PRD 不再作为产品主线。

本轮关键对齐：

- 接受 ARY 可持久化 Public Metadata / Public Projection。
- 接受 Participant / Rider 作为用户角色。
- 接受 Registration Proxy 和 Organizer Server 进入产品主线。
- 接受报名请求可经过 ARY Stateless Proxy，但报名事实只能写入 Organizer Server。
- 接受公开报名计数、公开 RiderID / nickname、公开参与摘要可作为 Organizer 主动披露的 Public Projection 展示。
- 接受 `Suspended` 表示 Organizer Server 不可达或公开入口挂起。

本轮保留并下沉的个人原设计：

- Race Source Facts 不进入 ARY。
- 字段溯源、投影版本/hash、缓存撤回、DCR 输出边界、越界字段拒绝和验证证据页必须进入后续 PoC/Demo 验收。
- 日志、缓存、debug 输出和验证材料不得泄露参赛者代码、完整骑行记录、执行日志、DCR 判断链、评审证据、复盘材料和私有规则细节。

本轮纠偏：

- 旧口径“当前阶段不写实际 PoC 代码”调整为：P7 不跳过实现设计直接写代码；P8 完成实现设计与合约冻结；P9 必须编写实际 PoC 代码并运行 Demo 验证。

## 16. P8 实现检查与增强计划

P8 的任务不是继续扩展产品范围，而是检查现有小组 PoC 能否支撑 P9 验收，并冻结后续增强清单。

检查结论：

- 现有 `group_ARY_week1/ary_grs_001_poc.py` 已具备双 FastAPI app：`organizer_app` 作为 Private Race Source，`ary_app` 作为 Public Yard。
- 已具备 Public Metadata / Public Projection public stores。
- 已具备 Registration Proxy，报名事实写入 Organizer Server。
- 已具备公开页、privacy-check、rejection-demo、Suspended 基础能力。
- 主要缺口不在主链路，而在可复跑证据：projection version/hash 验证、统一 Evidence Dashboard、Demo 验收文档、debug 泄露边界。

P8 人类判断：

- 不推倒现有实现。
- 不引入数据库、认证、加密、多 Race、多 Organizer。
- 只在现有双 app 上补证据入口、验收步骤和边界说明。

P8 产出：

- 新增 `docs/03_review/P8_IMPLEMENTATION_CHECKLIST.md`。
- 明确 P9 代码修改清单：Evidence Dashboard、version/hash demo、Proxy 零落库证据、Suspended 与 rejection-demo 文档化、debug 边界说明。

## 17. P9 实际 PoC/Demo 实现与验收

P9 按 P8 清单执行，仍保持最小可证明方案。

实际增强：

- 在 `group_ARY_week1/ary_grs_001_poc.py` 中新增 `/debug/evidence-dashboard` JSON 证据入口。
- 新增 `/evidence-dashboard` HTML Evidence Dashboard 页面。
- 新增 `/debug/projection-version-hash-demo`，用于复跑投影版本/hash 验证。
- 在 ARY 公开页导航中增加 Evidence 入口。
- 更新 `group_ARY_week1/DEMO_VERIFICATION.md`，补全 debug 边界、Proxy 零落库、Evidence Dashboard、version/hash、Suspended、rejection-demo 的完整步骤。

验收方式：

- 使用 `.venv` 安装 `fastapi` 和 `uvicorn`。
- 在同一验收脚本生命周期内启动 Organizer Server 与 ARY Server。
- 通过真实 HTTP 请求逐项检查，不直接调用函数替代服务验收。
- 验收完成后自动停止服务。

验收结果：

- Organizer `/health` 和 ARY `/debug/privacy-check` 均可访问。
- `POST /demo/disclose-to-ary` 证明 Organizer 私有源事实仍在本地。
- `/debug/demo-journey` 证明 metadata/projection 存在，ARY privacy check 未发现核心私有源事实。
- 报名前后 `/debug/ary-store` 均证明 ARY 无 `ary_registration_store`、`ary_rider_db`、`ary_race_fact_db`。
- `POST /proxy/race/001/register` 证明报名事实写入 Organizer Server。
- `/explore/race/001` 返回公开页，包含 RIDE AGENT 与 Evidence 入口。
- `/evidence-dashboard` 返回可视化证据页，私有值被 redacted。
- `/debug/rejection-demo` 证明恶意投影不会写入 ARY。
- `/debug/projection-version-hash-demo` 四项场景通过：旧版本拒绝、同版本同 hash 幂等、同版本不同 hash 冲突、新版本接受。
- 停止 Organizer Server 后，公开页、ARY store、Evidence Dashboard 均显示 `Suspended`，且不推断内部事实。

P9 最终结论：

- P9 实际 HTTP 服务验收通过。
- 结论记录在 `docs/03_review/P9_ACCEPTANCE_REPORT.md`。
- 当前 PoC/Demo 已能证明 Public Yard / Private Race Source 的核心边界。

## 18. 最终提交整理结论

当前进入 P10：最终提交整理与演示材料冻结。

冻结范围：

- 小组 PRD 基准不再变更。
- PoC 保持现有双 FastAPI app 和单文件 Demo 结构。
- 演示材料以 `group_ARY_week1/DEMO_VERIFICATION.md`、`docs/03_review/P9_ACCEPTANCE_REPORT.md` 和 `docs/04_submission/final_poc_demo_summary.md` 为主。

明确不做：

- 不新增生产级数据库。
- 不新增认证、加密、权限系统。
- 不扩展多 Organizer、多 Race。
- 不实现完整赛事执行、成果评审、争议仲裁或复盘系统。
