# 组内沟通简报

## 1. 当前项目定位

本项目围绕 ARY GRS 001，回答一个核心问题：在完整 Race 数据只留存在 Organizer 侧、ARY 不中心化持久化完整 Race 数据的前提下，ARY 如何仍然完成赛事公开侧的创建、披露、组织与展示闭环。

当前成果不是普通赛事管理系统设计，也不是完整全栈 Demo，而是“最小可证明方案”的文档化设计。

## 2. 当前阶段目标

当前位于 P7：一致性评审与提交整理阶段。

本阶段目标是把个人文档体系对齐到小组 PRD 基准，并为后续实际 PoC 代码与 Demo 验证提供可执行任务说明。P7 不跳过实现设计直接写代码；P8 冻结合约后，P9 需要编写并运行实际 PoC。

## 3. 已完成成果清单

| 类别 | 已完成成果 | 作用 |
| --- | --- | --- |
| 项目约束 | `AGENTS.md`、`PLAN.md` | 明确数据边界、工作阶段、非代码约束 |
| 需求基线 | `problem_definition.md`、`scope_boundary.md`、`acceptance_checklist.md`、`open_questions.md` | 锁定核心冲突、范围、验收标准和待确认问题 |
| 产品设计 | `prd.md` | 定义 Organizer-first 的最小产品闭环 |
| PoC 理论 | `poc_design.md`、`poc_validation_matrix.md` | 定义四项核心证明的测试场景、观测点、通过标准和失败条件 |
| 架构设计 | `architecture.md`、`data_flow.md` | 明确组件职责、数据方向、所有者和持久化边界 |
| Demo 设计 | `demo_plan.md`、`demo_script.md` | 定义三页最小 Demo 和演示脚本 |
| 过程记录 | `decision_log.md`、`riding_record_draft.md` | 记录关键决策、人机协作过程和阶段复盘 |
| 评审材料 | `review_report.md`、`revision_plan.md` | 完成一致性审查，形成修订优先级 |

## 4. 核心方案一句话说明

Organizer 持有完整 Race 数据并主动披露 Public Projection，ARY 只登记最小公开入口并按需展示公开投影，从而在不持久化完整 Race 数据的情况下完成赛事公开闭环。

## 5. 核心问题与解决思路

| 核心问题 | 解决思路 |
| --- | --- |
| 完整 Race 数据不能进入 ARY，但 ARY 仍要展示 Race | 将完整数据留在 Organizer，ARY 只处理公开登记信息和 Public Projection |
| ARY 不能替 Organizer 决定公开内容 | 采用 Organizer-first 流程，由 Organizer 发布、更新、撤回公开投影 |
| Public Projection 可能过宽 | 设置最小字段集合、字段来源追溯和后续代码 PoC 冻结规则 |
| DCR 可能成为隐性复制通道 | 要求 DCR 接触完整数据时位于 Organizer 授权域，并在代码 PoC 检查输出清单 |
| 缓存可能继续展示旧内容 | 撤回、过期、不可用时只显示状态，不用旧缓存补全正文 |

## 6. PRD 结论摘要

PRD 已形成最小产品闭环：

- Organizer 创建并维护权威 Race。
- Organizer 主动选择公开字段并发布 Public Projection。
- ARY 保存最小公开登记信息，用于识别和组织公开 Race。
- ARY 持久化 Organizer 主动披露的 Public Metadata / Public Projection 并展示。
- Organizer 可更新或撤回披露，ARY 只能反映当前状态。

PRD 的 Must 范围只覆盖创建、披露、组织、展示和必要状态处理，不扩展到赛事指导、成果评审、骑行复盘或生产级平台能力。

## 7. PoC 理论设计摘要

PoC 理论设计围绕四项证明：

| 证明对象 | 要证明的结论 | 主要证据 |
| --- | --- | --- |
| 数据留存 | 完整 Race 数据只在 Organizer 侧 | Organizer 存储清单、ARY 登记清单、展示字段清单对比 |
| 去中心化 | ARY 不持久化完整数据仍可工作 | ARY 最小登记字段、投影读取记录、页面结果 |
| 功能闭环 | 创建、披露、组织、展示可顺序完成 | 四环节输入、输出、责任角色和状态变化 |
| 投影机制 | 展示内容来自 Organizer 主动披露 | 展示字段与 Public Projection 字段映射、撤回和失败用例 |

下一阶段代码 PoC 需要把这些理论证据变成可运行页面、存储快照、字段映射和失败用例结果。

## 8. 架构与数据流摘要

当前架构分为四个关键边界：

- Organizer 授权域：保存完整 Race 数据，生成公开投影。
- Organizer 授权公开区：承载 Public Projection。
- ARY 平台公开侧：保存 Public Metadata / Public Projection，提供公开页和无状态报名代理。
- 验证证据材料：只保存字段名、映射和结果，不保存私有正文。

关键数据流是：

```text
完整 Race 数据：只在 Organizer Local Store 内部流转
公开登记信息：Organizer / Projection Publisher → ARY Registry
Public Projection：Organizer → Public Projection → ARY Display → 访问者
运行时缓存：ARY Display 内部短期使用，不作为权威数据
```

当前设计未发现必须把完整 Race 数据复制到 ARY 的链路；主要风险留到代码 PoC 验证。

## 9. Demo 方案摘要

Demo 当前是展示方案和脚本，不是已实现的全栈系统。

最小 Demo 为三页：

| 页面 | 证明重点 |
| --- | --- |
| Organizer 控制台 | 完整数据留在 Organizer，公开字段由 Organizer 主动选择 |
| ARY 公开页 | ARY 通过 Public Projection 展示公开 Race |
| 验证证据页 | 对比 Organizer、ARY Registry、Public Projection 和展示字段，展示失败用例 |

演示主线为：展示完整字段清单 → 生成投影 → 登记公开入口 → ARY 展示 → 字段溯源 → 存储边界对比 → 更新/撤回 → 失败用例 → 缓存撤回与 DCR 输出检查。

## 10. 当前尚未完成事项

- 尚未进入实际代码 PoC。
- 尚未冻结完整 Race 数据最终分类。
- 尚未冻结 ARY 最小登记字段、用途和保留周期。
- 尚未冻结 Public Projection 最小字段集合、格式和承载方式。
- 尚未实现三页 Demo。
- 尚未实现发布、更新、撤回、缓存失效和失败用例的可运行验证。
- 尚未提供 DCR 真实部署位置、运行身份和输出清单验证。
- 尚未形成最终提交版 Riding Record。

## 11. 建议组内分工

| 角色 | 建议负责人 | 主要任务 |
| --- | --- | --- |
| 产品与需求负责人 | 1 人 | 维护 PRD 口径、Must 范围、待确认问题 |
| PoC 验证负责人 | 1 人 | 将验证矩阵转成代码 PoC 检查项和失败用例 |
| 架构与数据边界负责人 | 1 人 | 冻结数据分类、登记字段、投影字段、DCR 和缓存边界 |
| Demo 前端负责人 | 1 人 | 实现 Organizer 控制台、ARY 公开页、验证证据页 |
| Demo 数据与状态负责人 | 1 人 | 实现样例数据、投影发布/更新/撤回、状态流转 |
| 文档与汇报负责人 | 1 人 | 整理提交材料、Riding Record、组内讲解口径 |

如果人数较少，可合并为三组：产品文档组、代码 Demo 组、验证证据组。

## 12. 需要组内确认的问题

高优先级：

- “完整 Race 数据”最终包含哪些字段和数据类别？
- ARY 最小登记信息最终允许保存哪些字段，保留多久？
- Public Projection 最小字段集合、格式和承载位置是什么？
- DCR 在实际 Demo 中是否出现？如果出现，部署在哪里、输出什么？
- 撤回、过期、不可用、缓存命中时，ARY 页面具体显示什么？

文档状态待确认：

- `revision_plan.md` 写明当时“不直接修改正文、不进入提交材料最终整理”，但 `decision_log.md` 和 `riding_record_draft.md` 已记录 P7 修订执行结果；需确认 `revision_plan.md` 是否作为历史计划保留，还是需要补充“已执行”状态说明。

## 13. 下一步行动建议

1. 组内先确认数据分类、ARY 登记字段、Public Projection 字段、DCR 边界和缓存撤回语义。
2. 冻结代码 PoC 的最小实现范围：三页 Demo、单 Organizer、单 Race、固定字段集合。
3. 将 PoC 验证矩阵转为代码 Demo 验收清单。
4. 实现 Demo 页面和样例数据流，但不扩展成生产级系统。
5. 运行失败用例并生成验证证据页。
6. 整理最终提交材料和正式 Riding Record。
