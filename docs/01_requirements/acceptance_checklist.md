# ARY GRS 001 验收清单

## 使用说明

- P1 完成检查用于确认本轮问题基线是否锁定。
- 后续方案验收项在对应设计与验证完成后逐项勾选。
- 任一核心项不通过，不能认定 GRS 001 方案成立。

## P1 完成检查

- [x] 已用一句话明确数据主权与平台能力之间的核心冲突。
- [x] 已分别定义数据留存、去中心化、功能闭环、投影机制四项证明对象。
- [x] 已为四项证明对象写明必须证明的结论和失败条件。
- [x] 已明确 Organizer、ARY、DCR、Public Projection 的职责与禁止事项。
- [x] 已明确当前阶段非目标与越界判定。
- [x] 已将无法从来源确定的事项写入待确认问题。
- [x] 本轮未编写 PRD 正文或实际 PoC 代码。

## 四项 PoC 核心验收

### AC-01 数据留存

- [ ] 完整 Race 数据的范围和存储位置已明确。
- [ ] 数据流说明中不存在 Organizer 之外的完整数据副本。
- [ ] 验证方案能够检查完整数据是否仅留存在 Organizer 侧。
- [ ] Organizer 能控制哪些数据被公开。

通过条件：以上条目全部满足，且未发现完整数据外传或隐性复制。

### AC-02 去中心化

- [ ] ARY 可持久化的 Public Metadata、Public Projection、公开可达性状态范围、用途和保留周期已明确。
- [ ] ARY 的持久化内容不构成完整 Race Source Facts 或报名事实库副本。
- [ ] 创建、披露、组织、报名入口转发、展示不依赖 ARY 持久化完整 Race 数据。
- [ ] 验证方案能够检查 ARY 的持久化边界。

通过条件：ARY 在不持久化完整 Race 数据时仍可完成目标能力。

### AC-03 功能闭环

- [ ] 创建环节有明确输入、责任角色、输出和可观察结果。
- [ ] 披露环节由 Organizer 主动控制。
- [ ] 组织环节仅使用允许访问的数据。
- [ ] 报名入口可经过 ARY Stateless Proxy，但报名事实只写入 Organizer Server。
- [ ] 展示环节仅使用公开元数据或 Public Projection。
- [ ] Organizer Server 不可达时，ARY 公开页显示 `Suspended`，且不暗示赛事内部事实。
- [ ] 五个环节可按明确顺序形成闭环。

通过条件：四个环节全部可完成，且任一环节均不要求访问未披露完整数据。

### AC-04 投影机制

- [ ] Public Projection 的内容边界已定义，且明确 ARY 可持久化 Organizer 主动披露的公开投影。
- [ ] 每个 ARY 展示字段均可追溯到 Organizer 的披露来源。
- [ ] 未披露字段不会出现在 ARY 展示结果中。
- [ ] 更新、撤回与过期数据的处理规则已定义。
- [ ] 长期展示的报名计数、公开 RiderID / nickname、公开参与摘要来自 Organizer 主动披露的 Public Projection。
- [ ] 验证方案能够识别越权展示或来源不明字段。

通过条件：ARY 展示内容完全由 Organizer 主动披露决定。

## 角色与架构验收

- [ ] Organizer 始终是完整 Race 数据的所有者和披露控制者。
- [ ] ARY 的职责不包含完整 Race 数据的中心化持久化。
- [ ] ARY Registration Proxy 不包含 `save()`、`commit()` 或本地报名数据表写入逻辑。
- [ ] Organizer Server 是报名事实和完整 Race Source Facts 的写入位置。
- [ ] DCR 的部署位置、授权范围和数据访问边界已明确。
- [ ] DCR 不会成为完整数据向 ARY 复制的隐性通道。
- [ ] Public Projection 不被视为完整 Race 数据源。
- [ ] 架构图和数据流图标明所有权、数据方向与持久化位置。

## 范围与一致性验收

- [ ] 方案未扩展到指导骑行、成果评审、骑行复盘等非核心子系统。
- [ ] PRD、PoC 理论、架构、数据流和 Demo 方案使用一致的角色与数据边界。
- [ ] 所有关键设计决策均记录在 `docs/02_design/decision_log.md`。
- [ ] 所有未决事项均记录在 `docs/01_requirements/open_questions.md`。
- [ ] P7 文档对齐后已冻结 P8 实现设计任务。
- [ ] P9 实际 PoC 代码能运行 Organizer Server、ARY Server、公开页、报名代理、隐私检查、拒绝演示和 Suspended Demo。
