# ARY GRS 001 设计决策记录

## 使用规则

- 仅记录会影响产品逻辑、PoC 证明、架构边界或 Demo 表达的具体决策。
- 决策变更时新增记录并标明替代关系，不直接抹除历史。
- 状态使用：`已确定`、`待验证`、`已替代`。

## 当前决策

| 编号 | 状态 | 决策 | 依据与影响 |
| --- | --- | --- | --- |
| D-001 | 已确定 | Race 完整数据仅留存在 Organizer 侧 | 数据主权属于 Organizer；后续设计不得要求完整数据外传 |
| D-002 | 已确定 | ARY 不持久化保存完整 Race 数据 | 架构与 PoC 必须排除中心化完整数据副本 |
| D-003 | 已确定 | ARY 展示内容仅来自 Organizer 主动披露的公开元数据或公开投影 | 展示链路必须可追溯到 Organizer 的披露动作 |
| D-004 | 已确定 | GRS 001 的 PoC 聚焦四项核心假设 | 仅验证数据留存、去中心化、功能闭环、投影机制 |
| D-005 | 已确定 | 赛事指导、成果评审、骑行复盘子系统不属于本次核心设计范围 | 防止方案偏离数据安全与去中心化命题 |
| D-006 | 已确定 | 架构说明必须显式区分 Organizer、ARY、DCR、Public Projection | 用于检查职责、权限、交互和持久化边界 |
| D-007 | 已替代 | 当前阶段只完成设计文档，不编写实际 PoC 代码 | 已由 D-044 替代：P8 冻结实现设计后，P9 必须编写实际 PoC 代码 |
| D-008 | 已确定 | 未被 Organizer 明确披露的数据默认按非公开数据处理 | 防止 ARY、DCR 或 Public Projection 静默扩大数据可见范围 |
| D-009 | 已确定 | Public Projection 是 Organizer 授权公开的有限派生视图，不是完整 Race 数据源 | 投影不转移数据主权，也不得被用于重建完整数据 |
| D-010 | 已确定 | 功能闭环按创建、披露、组织、展示四项可观察能力验收 | 每项能力必须有输入、责任角色、输出和可观察结果 |
| D-011 | 已确定 | P1 只锁定来源支持的角色边界，未知部署与技术形式保留为待确认问题 | 避免将 DCR 部署、投影承载方式等推测写成架构事实 |
| D-012 | 已确定 | 创建赛事的最低边界是不要求 ARY 创建或保存完整 Race 数据 | 具体发起流程由 D-013 作为待验证设计推进 |
| D-013 | 待验证 | 采用 Organizer-first 产品闭环：Organizer 创建权威 Race，ARY 创建公开入口 | 最直接维护数据主权；需在 P3/P4 验证流程与架构可行性 |
| D-014 | 已替代 | ARY 仅持久化最小公开登记信息，Public Projection 按需读取 | 已由 D-038 替代：ARY 可持久化 Organizer 主动披露的 Public Metadata / Public Projection |
| D-015 | 待验证 | 最小公开登记信息包含公开 Race 标识、Organizer 公开标识、投影定位、状态与版本或更新时间 | 支撑识别、组织、追溯与状态判断；最终字段待验证 |
| D-016 | 待验证 | Organizer 主动控制 Public Projection 的发布、更新与撤回 | 保证披露控制权完整；时效、缓存和历史处理规则待验证 |
| D-017 | 已确定 | Public Projection 不可用、过期或已撤回时，ARY 应明确显示状态而非补全内容 | 防止使用未授权历史数据或制造来源不明展示 |
| D-018 | 已确定 | P2 的 Must 功能仅覆盖创建、披露、组织、展示及必要的状态处理 | 保持最小可证明产品范围，避免扩展到完整赛事执行系统 |
| D-019 | 待验证 | P3 理论 PoC 采用单 Organizer、单 Race 的最小场景 | 足以覆盖四项核心证明；多 Organizer、多 Race 留到后续扩展 |
| D-020 | 待验证 | PoC 数据分为 Organizer 完整数据、ARY 最小登记信息、Public Projection 三类 | 用字段清单对比证明数据留存、去中心化和投影边界 |
| D-021 | 待验证 | PoC 观测证据包括存储清单、投影读取记录、展示字段映射和失败用例结果 | 为后续代码 PoC 提供可执行验收依据 |
| D-022 | 待验证 | 撤回、过期、不可用状态均按“不展示旧有效内容，只展示状态”处理 | 防止缓存或历史内容破坏 Organizer 披露控制 |
| D-023 | 待验证 | DCR 接触完整 Race 数据时必须位于 Organizer 授权域内 | 防止 DCR 成为完整数据向 ARY 复制的隐性通道 |
| D-024 | 待验证 | ARY Registry 可持久化的内容限定为最小公开登记信息 | 字段包括公开 Race 标识、Organizer 公开标识、投影定位、状态、版本或更新时间 |
| D-025 | 已替代 | ARY Display 可临时处理 Public Projection，但不将投影正文作为权威持久化数据 | 已由 D-038 替代；保留“不持久化完整 Race Source Facts”和“撤回后不补正文”的约束 |
| D-026 | 已确定 | 验证证据只保存字段名、清单、映射和结果，不保存私有内容正文 | 防止评审材料或报告成为数据泄露路径 |
| D-027 | 待验证 | 当前架构不存在必须复制完整 Race 数据到 ARY 的链路 | 仍需在代码 PoC 阶段检查投影字段过宽、登记字段膨胀和缓存失效 |
| D-028 | 已确定 | Demo 采用三页最小结构：Organizer 控制台、ARY 公开页、验证证据页 | 三页足以覆盖数据留存、去中心化、功能闭环和投影机制 |
| D-029 | 已确定 | Demo 不展示私有字段正文，只展示字段名、位置和边界标签 | 避免演示材料本身泄露完整 Race 数据 |
| D-030 | 已确定 | Demo 必须包含失败用例展示 | 用越界登记、误投影和未披露字段请求证明边界可验收 |
| D-031 | 待验证 | 下一阶段代码 Demo 的最小页面为三页加可选导航页 | 保持实现范围最小，同时支撑评审叙事 |
| D-032 | 已确定 | Riding Record 按 P0-P6 的阶段链路记录，而不是复述全部文档正文 | 保持过程可复盘且内容精炼 |
| D-033 | 已确定 | Riding Record 必须区分人类判断、Agent 约束和待进入代码 PoC 的内容 | 支撑评审维度中的协作过程可追踪、可解释、可复盘 |
| D-034 | 已确定 | P7 一致性审查结论为理论设计基本通过，提交整理阶段需同步少量状态措辞 | 当前未发现必须复制完整 Race 数据到 ARY 的设计链路，主要风险留待代码 PoC 验证 |
| D-035 | 已确定 | P7 修订计划将阶段状态措辞同步列为 Must Fix，DCR 输出检查和投影字段冻结列为 Should Fix | 先消除直接一致性问题，再补强代码 PoC 前置验证，不在本轮直接修改正文 |
| D-036 | 已确定 | P7 第三部分已执行 MF-01、SF-01、SF-02、SF-03 的设计文档修订 | 已同步阶段状态措辞，并强化 DCR 输出、最小投影字段、缓存撤回和 Demo 证明映射 |
| D-037 | 已确定 | P7 起以 `group_ARY_week1/PRD-ARY-GRS-001.md` 作为新的 PRD 基准 | 个人原 PRD 不再作为产品主线；其严谨边界下沉到 PoC、架构、数据流、Demo 与验收 |
| D-038 | 已确定 | ARY 可持久化 Organizer 主动披露的 Public Metadata / Public Projection | 替代 D-014 中“Public Projection 按需读取”的主线；仍禁止持久化完整 Race Source Facts |
| D-039 | 已确定 | 引入 Participant / Rider、Registration Proxy、Organizer Server 作为产品主线角色 | 报名入口转发成为功能闭环的一部分，报名事实只写 Organizer Server |
| D-040 | 已确定 | ARY Stateless Proxy 不得 `save()` / `commit()`，不得从代理请求生成报名事实库 | Proxy 只做请求形状校验、路由、超时控制和错误归一化 |
| D-041 | 已确定 | 公开报名计数、公开 RiderID / nickname、公开参与摘要可作为 Organizer 主动披露的 Public Projection 展示 | 长期展示必须以 Organizer Projection 为来源，不能由 ARY 从代理请求聚合 |
| D-042 | 已确定 | `Suspended` 表示 Organizer Server 不可达或公开入口挂起 | 该状态只描述公开可达性，不代表 ARY 知道赛事内部执行或报名事实 |
| D-043 | 已确定 | 参赛者代码、完整骑行记录、执行日志、DCR 判断链、评审证据、复盘材料和私有规则细节不得进入 ARY 持久化、日志、缓存、debug 或验证材料 | 将核心保护对象从“所有报名相关信息”校正为 Race Source Facts |
| D-044 | 已确定 | 实现设计完成后需要编写实际 PoC 代码并运行 Demo 验证 | P7 只做文档对齐；P8 冻结合约；P9 进入实际代码与验收闭环 |
| D-045 | 已确定 | P9 在现有双 FastAPI app 上增量增强，不推倒现有 PoC | 保持单文件 PoC、Organizer Server 与 ARY Server 架构；不引入数据库、认证、加密、多 Race、多 Organizer |
| D-046 | 已确定 | 新增 Evidence Dashboard 作为统一证据入口 | `/debug/evidence-dashboard` 汇总 public stores、privacy、proxy、projection、connectivity；`/evidence-dashboard` 提供可视化页面；Organizer 私有数据只显示字段名和存在性 |
| D-047 | 已确定 | 新增 projection version/hash 可复跑验证 | `/debug/projection-version-hash-demo` 覆盖旧版本拒绝、同版本同 hash 幂等、同版本不同 hash 冲突、新版本接受，且不使用私有源事实 |
| D-048 | 已确定 | 明确 Organizer debug 与 ARY debug 的泄露边界 | Organizer debug 可作为本地评审接口查看完整私有数据；ARY debug 与 Evidence Dashboard 不得输出私有正文 |
| D-049 | 已确定 | P9 实际 HTTP 服务验收已通过 | `docs/03_review/P9_ACCEPTANCE_REPORT.md` 记录 Organizer/ARY 启动、创建披露、Proxy 零落库、公开页、Evidence Dashboard、privacy-check、rejection-demo、version/hash、Suspended 全部通过 |
| D-050 | 已确定 | P10 进入最终提交整理与演示材料冻结 | 冻结最终摘要、验收依据、演示顺序、边界与非目标，不继续扩展生产级功能 |

## 待形成决策

待形成决策统一维护在 `docs/01_requirements/open_questions.md`。
