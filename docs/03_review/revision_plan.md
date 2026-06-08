# ARY GRS 001 修订计划

## 1. 计划定位

本文基于 `docs/03_review/review_report.md` 制定修订计划。当前步骤只制定计划，不直接修改 PRD、PoC、架构、数据流或 Demo 正文。

## 2. 修订分级

### Must Fix

| 编号 | 修订项 | 对应文件 | 原因 | 预期结果 |
| --- | --- | --- | --- | --- |
| MF-01 | 同步阶段状态措辞 | `docs/02_design/prd.md`、`docs/02_design/poc_validation_matrix.md` | 审查报告 R-003 指出个别状态表述滞后 | 消除“留待 P4”“P4 前”等阶段性过期表述 |

### Should Fix

| 编号 | 修订项 | 对应文件 | 原因 | 预期结果 |
| --- | --- | --- | --- | --- |
| SF-01 | 增加代码 PoC 阶段 DCR 输出清单检查 | `docs/02_design/poc_design.md`、`docs/02_design/poc_validation_matrix.md`、`docs/02_design/architecture.md`、`docs/02_design/data_flow.md` | 审查报告 R-001 指出 DCR 仍需实现阶段验证 | 后续代码 PoC 能检查 DCR 是否向 ARY 输出完整数据或中间结果 |
| SF-02 | 冻结最小 Public Projection 字段集合的前置计划 | `docs/02_design/poc_design.md`、`docs/02_design/poc_validation_matrix.md`、`docs/02_design/demo_plan.md`、`docs/01_requirements/open_questions.md` | 审查报告 R-002 指出投影字段过宽是主要风险 | 提交前明确“最小投影字段集合待代码 PoC 前冻结” |
| SF-03 | 强化缓存失效与撤回验证清单 | `docs/02_design/poc_validation_matrix.md`、`docs/02_design/data_flow.md`、`docs/02_design/demo_script.md` | 缓存可能形成事实副本或展示旧内容 | 后续验证明确撤回后不展示旧有效正文 |

### Could Fix

| 编号 | 修订项 | 对应文件 | 原因 | 预期结果 |
| --- | --- | --- | --- | --- |
| CF-01 | 增加一页式提交总览 | `docs/04_submission` | 方便评审快速理解最小可证明方案 | 提交材料更清晰 |
| CF-02 | 将 Demo “最小可证明方案，不实现全栈”放入提交摘要 | `docs/04_submission`、可引用 `demo_plan.md` | 避免评审误解为未完成全栈实现 | 明确当前阶段边界 |
| CF-03 | 将 Riding Record 草稿整理为提交版 | `docs/02_design/riding_record_draft.md`、`docs/04_submission` | 当前为草稿，提交时可更正式 | 提升协作过程展示质量 |

## 3. 修改顺序

| 顺序 | 动作 | 说明 |
| --- | --- | --- |
| 1 | 执行 MF-01 | 先消除阶段状态措辞不一致，避免后续引用混乱 |
| 2 | 执行 SF-01 | 补强 DCR 输出检查，保持架构和 PoC 验证一致 |
| 3 | 执行 SF-02 | 明确投影字段冻结计划，降低投影过宽风险 |
| 4 | 执行 SF-03 | 补强撤回、缓存、过期状态的验证口径 |
| 5 | 执行 CF-01 至 CF-03 | 进入提交整理，形成评审友好的摘要材料 |

## 4. 一致性保障方式

每次修订后按以下顺序检查：

1. **术语一致**：Organizer、ARY、DCR、Public Projection 的定义不变。
2. **数据边界一致**：完整 Race 数据仍只留在 Organizer；ARY 不持久化完整数据。
3. **流程一致**：PRD 的创建、披露、组织、展示闭环与 PoC、架构、Demo 保持一致。
4. **验证一致**：PoC 验证矩阵、架构隐性复制检查、Demo 失败用例指向同一组风险。
5. **阶段一致**：所有“待 P4”“下一阶段”等措辞应符合当前阶段状态。
6. **决策一致**：新增或改变关键判断必须同步 `docs/02_design/decision_log.md`。

## 5. 修订后检查清单

| 检查项 | 通过条件 |
| --- | --- |
| PRD 与 PoC 一致 | PRD 的产品闭环均能在 PoC 中找到验证项 |
| PoC 与架构一致 | PoC 的观测点能对应架构组件和数据流 |
| 架构与 Demo 一致 | Demo 页面能展示架构中的关键边界 |
| Demo 与评审维度一致 | Demo 能覆盖数据留存、去中心化、功能闭环、投影机制 |
| 无范围越界 | 不新增实际代码、不扩展全栈生产功能 |
| 无隐性复制 | 不引入完整数据进入 ARY 的链路 |

## 6. 本轮不执行的内容

- 不直接修改 `prd.md`、`poc_design.md`、`poc_validation_matrix.md`、`architecture.md`、`data_flow.md`、`demo_plan.md`、`demo_script.md`。
- 不创建实际 PoC 代码。
- 不创建页面文件。
- 不进入提交材料最终整理。

## 7. 修订计划结论

当前必须修复项较少，主要是阶段措辞同步。核心设计方向无需推翻。后续修订应集中在代码 PoC 验证前置条件：DCR 输出、投影字段、缓存失效、字段溯源。
