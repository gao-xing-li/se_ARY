# 初始化项目约束

> 你是本项目的单 Agent 工作助手。请基于当前项目目录中的材料，初始化项目工作约束。
>
> 当前已有文件：
>
> /docs/00_sources/
>   ARY_GRS.pdf
>   source_ARY_GRS_full_text.md
>
> 当前阶段目标：
>
> 1. 完成 ARY GRS 001 的 PRD 文档设计；
> 2. 完成 PoC 理论设计；
> 3. 完成系统架构与数据流说明；
> 4. 完成 Demo 展示方案；
> 5. 完成 Riding Record；
> 6. 当前阶段不写实际 PoC 代码。
>
> 请完成以下任务：
>
> 1. 阅读 `/docs/00_sources/source_ARY_GRS_full_text.md`；
> 2. 必要时参考 `/docs/00_sources/ARY_GRS.pdf`；
> 3. 在项目根目录创建 `AGENTS.md`；
> 4. 在项目根目录创建 `PLAN.md`；
> 5. 创建目录：
>    - `/docs/01_requirements`
>    - `/docs/02_design`
>    - `/docs/03_review`
>    - `/docs/04_submission`
> 6. 创建 `/docs/02_design/decision_log.md`。
>
> 文档要求：
>
> 1. 所有生成内容必须使用中文；
> 2. 内容要关键、精炼，不要写成长篇说明；
> 3. `AGENTS.md` 管长期原则；
> 4. `PLAN.md` 管当前周目标；
> 5. `decision_log.md` 管过程中形成的具体设计决策；
> 6. 当前阶段不要写 PRD 正文，不要写 PoC 代码。
>
> 请生成文件后，输出：
> 1. 创建了哪些文件；
> 2. 每个文件的作用；
> 3. 下一步应执行 PLAN.md 中的哪一项。

<details><summary>7 previous messages</summary>

> 我先读取现有需求材料和目录状态，提炼长期约束、当前周计划与决策记录的最小结构；随后只创建你指定的目录和三个文档，不展开 PRD 正文或 PoC 代码。
>
> 源材料已确认覆盖任务核心：数据完整留在 Organizer，ARY 不持久化完整 Race 数据，通过公开元数据或公开投影完成创建、披露、组织与展示闭环。当前根目录已有一个空的 `AGENTS.md`，且目录不是 Git 仓库；我会覆盖该空文件，并按“本阶段只做文档设计、不写 PoC 代码”的边界制定计划。
>
> MCP tool call
>
> node_repl.js
>
> ```json
> {
>   "title": "读取 UTF-8 源材料",
>   "code": "var fs = await import('node:fs/promises'); var path = await import('node:path'); var cwd = nodeRepl.cwd; var sourceText = await fs.readFile(path.join(cwd,'docs','00_sources','source_ARY_GRS_full_text.md'),'utf8'); nodeRepl.write(sourceText);"
> }
> ```
>
> ````text
> # ARY Genesis Race Series (创世骑行系列赛) —— 课程作业设计与挑战指南
>
> ---
>
> ## 一、 项目背景与核心理念
>
> ### 1.1 什么是 ARY？
>
> * 
> **核心定义**：ARY 全称为 **Agent Racing Yard（智能体骑场）**，是智能体时代的软件开发训练场与竞技场 。
>
>
> * 
> **运转模式**：学生通过一次次 Race（比赛）骑行智能体，在完成真实项目、获得真实挑战与过程指导的同时，沉淀作品资产并展示自己的 **Agent Riding Skill（智能体骑行能力）** 。
>
>
> * **双重定位**：
> * 
> **训练场**：练习如何与 AI Agent 协同，共同完成真实项目 。
>
>
> * 
> **竞技场**：提供一个让开发过程、最终作品以及个人能力被清晰看见的平台 。
>
>
>
>
> * 
> **首发规模**：本次为课堂级首发实验，面向约 100 名学生骑手，旨在验证第一套赛事机制、打磨课堂训练方法，并产出第一批可展示的智能体骑行作品 。
>
>
>
> ### 1.2 从软件工程师到“智能体工程师”的转变
>
> ARY 提出核心角色演进：从 **Coder（软件工程师）** 走向 **Rider（智能体工程师）** 。
>
> | 维度 | 传统软件工程师 (Coder) × 
>
>  | 智能体工程师 (Rider) √ 
>
>  |
> | --- | --- | --- |
> | **关注核心** | • 写了多少行代码 
>
> <br>
>
> <br>• 做了多少个页面 
>
> <br>
>
> <br>• 单点产出的速度快慢 
>
>  | • 能否把终极目标讲清楚 
>
> <br>
>
> <br>• 能否把复杂任务拆解清楚 
>
>  |
> | **行动模式** | • 亲自手动编写逻辑、堆砌代码与页面 
>
>  | • 驾驭并让 Agent 正确行动 
>
> <br>
>
> <br>• 进行全程的观察、判断、干预与验收 
>
> <br>
>
> <br>• 将开发过程复盘并沉淀为自身能力 
>
>  |
>
> > 
> > **核心寄语**：智能体工程师，就是指能够骑行智能体、完成真实创造的人 。本次 Race 的价值不只在最后的作品，更在于让大家学到下一次怎么做得更好 。
> > 
> > 
>
> ---
>
> ## 二、 本次 Race 任务：ARY GRS 001 (Product Definition)
>
> 当前阶段的核心任务是**完成产品的定义（PRD 文档编写）与关键技术的验证（PoC 测试）** 。
>
> ### 2.1 攻关命题：数据安全的 Race
>
> * 
> **核心冲突**：在 Race 数据主权属于 Organizer（组织者）侧、**ARY 平台不进行中心化持久化存储**的前提下，ARY 平台该如何顺利完成赛事的创建、披露、组织与展示 ？
>
>
>
> ### 2.2 PoC 核心证明对象 (验证范围)
>
> 本次关键技术 PoC **必须证明** 以下四个核心假设成立 ：
>
> * 
> **数据留存**：Race 的完整数据可以且仅存留在 Organizer（组织者）侧 。
>
>
> * 
> **去中心化**：证明 ARY 平台不需要持久化保存完整的 Race 数据 。
>
>
> * 
> **功能闭环**：在此前提下，ARY 平台依然有能力实现赛事的**创建、披露、组织与展示** 。
>
>
> * 
> **投影机制**：ARY 平台的展示内容，必须完全来自 Organizer 主动披露的公开元数据或公开投影 。
>
>
>
> > ⚠️ **不在本次 PoC 范围内的内容**：
> > 赛事的具体执行（如指导骑行、成果评审、骑行复盘等子系统的实现细节）不属于本次 GRS 001 的核心证明对象 。重点不是写一份平庸的普通 PRD，而是围绕去中心化数据主权，**提出一个能够被代码验证的关键技术 PoC** 。
> > 
> > 
>
> ---
>
> ## 三、 参赛流程与生命周期 (Race Flow)
>
> 比赛不仅看重最终的答案，更看重整个骑行协同的过程 。完整赛程包含以下 8 个标准节点 ：
>
> ```
> [1. Race Brief] ➔ [2. Team Build] ➔ [3. Agent Setup] ➔ [4. Riding Plan]
>                                                                ➔
> [8. Review & Replay] ⮪ [7. Submission] ⮪ [6. Checkpoint] ⮪ [5. Co-Riding]
>
> ```
>
> * 1. Race Brief（理解挑战）：深入理解本次数据安全与去中心化 PoC 的攻关核心 。
>
>
> * 2. Team Build（完成组队）：标准战队配置为 **1 名 Coach（教练） + 4~5 名 Riders（骑手）** 。
>
>
> * 3. Agent Setup（智能体环境配置）：安装配置 Codex / Claude 等大模型，并安装 **DevCompass Racing（即 ARY 执行核）** 。
>
>
> * 4. Riding Plan（制定骑行计划）：明确分工，规划如何拆解并逐步落地 PoC 验证步骤 。
>
>
> * 5. Co-Riding（智能体协同）：与 Agent 深度协同，共同攻克并编写产品定义方案与验证代码 。
>
>
> * 6. Checkpoint（中途检查）：接受中途进度检查，获取导师或系统的专业反馈指导 。
>
>
> * 7. Submission（成果交付）：将最终作品、说明文档以及全过程记录提交至指定的 **GitHub Classroom** 。
>
>
> * 8. Review & Replay（评审复盘）：下周一进行公开评审、过程复盘与成果展示，总结改进方向 。
>
>
>
> ---
>
> ## 四、 作业阶段交付物 (Race Deliverables)
>
> 团队最终需要交付以下 5 项核心沉淀资产 ：
>
> * 01. 产品定义说明书 (PRD)：团队对 ARY/GRS 001 数据安全与赛事管理方案的深度理解与产品逻辑设计 。
>
>
> * 02. 系统架构设计：清晰梳理并画出 Organizer（组织者）、ARY（平台）、DCR（执行核）以及公开投影（Public Projection）之间的拓扑与交互关系 。
>
>
> * 03. 技术 PoC 源码：能够实际运行的代码，核心用于证明在数据不出 Organizer 本地侧的前提下，ARY 仍能通过无状态或轻量化的方式完成赛事看板的创建与数据披露 。
>
>
> * 04. 展示页面或 Demo：前端交互界面，向评审和他人直观、形象地展示你们的去中心化数据方案是如何顺畅工作的 。
>
>
> * 05. Riding Record（骑行协同记录）：人机协作的过程记录 。这不仅是作业的一部分，更是评估你们 **Agent Riding Skill** 的核心依据 。
>
>
>
> ---
>
> ## 五、 作品评估与评审维度
>
> 优秀的作品不仅看重“最后生成了什么文件”，更看重“你是如何骑行智能体把它做出来的” 。官方将通过 7 个硬性维度进行综合评估 ：
>
> * 
> **维度 1：问题定义** ➔ 团队对数据主权与赛事系统矛盾的拆解和定义是否足够清晰 。
>
>
> * 
> **维度 2：产品逻辑** ➔ 业务闭环、元数据披露与公开投影的逻辑设计是否能够完全成立 。
>
>
> * 
> **维度 3：去中心化数据主权** ➔ 是否真正理解了“数据归 Organizer 所有，ARY 不做持久化”的技术边界 。
>
>
> * 
> **维度 4：PoC 证明力度** ➔ 编写的代码是否切实有效地证明了核心的技术解法与技术假设 。
>
>
> * 
> **维度 5：架构边界** ➔ 各系统组件（Organizer、DCR、ARY）的分工与职责边界是否合理、清晰、无越权 。
>
>
> * 
> **维度 6：展示效果** ➔ 页面或 Demo 是否能够让人一眼看懂，其界面体验与传递效率是否优秀 。
>
>
> * 
> **维度 7：协作过程（重中之重）** ➔ 与 Agent 的多轮对话、任务编排、Prompt 工程等协作过程是否**可追踪、可解释、可复盘** 。
> ````
>
> 现在开始落盘：`AGENTS.md` 只写长期协作与设计约束；`PLAN.md` 把本周工作拆成可验收步骤，并明确第一项待办；`decision_log.md` 记录从 GRS 材料中已经锁定的设计决策。不会创建 PRD 正文、架构正文或任何代码。
>
> <details><summary>Created 2 files, edited 1 file</summary>
>
> - Wrote `./AGENTS.md` (+46 -0)
> - Wrote `./PLAN.md` (+39 -0)
> - Wrote `./docs/02_design/decision_log.md` (+27 -0)
>
> </details>
>
> 首轮文件已创建。核对时我发现根目录 `AGENTS.md` 还应合并你提供的四项通用 Agent 行为准则；我会补充一段精炼的长期执行规范，然后检查目录、文件内容及“未生成 PRD 正文/PoC 代码”的边界。
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./AGENTS.md` (+9 -2)
>
> </details>
</details>

已完成项目工作约束初始化，未编写 PRD 正文或 PoC 代码。

**创建文件**
- [AGENTS.md](./AGENTS.md)：管理长期设计边界、Agent 执行原则、文档规范与完成标准。
- [PLAN.md](./PLAN.md)：管理当前周目标、执行顺序与验收标准。
- [decision_log.md](./docs/02_design/decision_log.md)：记录已确定设计决策及待决策事项。

**创建目录**
- `docs/01_requirements`
- `docs/02_design`
- `docs/03_review`
- `docs/04_submission`

**下一步**
执行 `PLAN.md` 中的 **P1：锁定问题定义、范围与验收口径**。

> 现在执行 P1：锁定问题定义、范围与验收口径。
>
> 请基于：
>
> 1. `docs/00_sources/source_ARY_GRS_full_text.md`
> 2. `docs/00_sources/ARY_GRS.pdf`
> 3. `AGENTS.md`
> 4. `PLAN.md`
>
> 生成：
>
> 1. `docs/01_requirements/problem_definition.md`
> 2. `docs/01_requirements/scope_boundary.md`
> 3. `docs/01_requirements/acceptance_checklist.md`
> 4. `docs/01_requirements/open_questions.md`
>
> 要求：
>
> 1. 明确本作业的核心冲突；
> 2. 明确四项 PoC 核心证明对象：数据留存、去中心化、功能闭环、投影机制；
> 3. 明确 Organizer、ARY、DCR、Public Projection 的角色边界；
> 4. 明确当前阶段非目标；
> 5. 把验收标准写成可检查条目；
> 6. 不写 PRD 正文；
> 7. 不写实际 PoC 代码；
> 8. 完成后更新 `docs/02_design/decision_log.md`。
>
> 最后输出本轮产物、关键决策、待确认问题和下一步。

<details><summary>7 previous messages</summary>

> 我将执行 P1：先复核四个指定来源并检查现有决策记录，再生成四份需求基线文档，最后把本轮形成的边界决策写入 `decision_log.md`，并将 `PLAN.md` 的 P1 状态更新为已完成。PDF 只用于核对 Markdown 是否遗漏关键信息。
>
> Markdown 来源已完整覆盖核心命题、交付物和评审维度。当前仍有几项不能在 P1 中擅自定死：公开字段集合、披露撤回语义、ARY 可保存的轻量数据边界、DCR 部署位置；我会把它们列为阻塞后续设计的待确认问题，同时用 PDF 核对是否存在补充说明。
>
> P1 基线已明确：问题不是“如何把完整 Race 数据放进 ARY”，而是“如何在 Organizer 保持完整数据主权时，让 ARY 仅依靠主动披露的信息完成可观察的赛事闭环”。接下来我会落盘四份文档；角色中只锁定来源可支持的边界，DCR 部署、公开投影承载方式等未决项会明确保留，不会被写成既定架构。
>
> <details><summary>Created 4 files, edited 2 files</summary>
>
> - Wrote `./PLAN.md` (+2 -2)
> - Wrote `./docs/01_requirements/acceptance_checklist.md` (+74 -0)
> - Wrote `./docs/01_requirements/open_questions.md` (+37 -0)
> - Wrote `./docs/01_requirements/problem_definition.md` (+45 -0)
> - Wrote `./docs/01_requirements/scope_boundary.md` (+59 -0)
> - Wrote `./docs/02_design/decision_log.md` (+6 -5)
>
> </details>
>
> 四份需求基线与决策记录已落盘。现在进行一致性检查：重点确认四项证明对象在各文档中的口径一致、角色边界没有把待确认事项写死、P1 已完成且 P2 成为下一步，同时确认没有新增 PRD 正文或代码文件。
>
> 一致性检查通过，未发现角色口径冲突或额外代码文件。仅发现 `PLAN.md` 中仍保留“当前初始化任务不写 PRD 正文”的旧措辞；我会把它改为明确的阶段规则，避免 P1 完成后与下一步 P2 产生歧义。
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./PLAN.md` (+1 -1)
>
> </details>
</details>

P1 已完成，`PLAN.md` 已将 P2 标记为下一步。未编写 PRD 正文或实际 PoC 代码。

**本轮产物**
- [problem_definition.md](./docs/01_requirements/problem_definition.md)：核心冲突、问题拆解、四项 PoC 证明对象。
- [scope_boundary.md](./docs/01_requirements/scope_boundary.md)：角色、数据、功能边界及非目标。
- [acceptance_checklist.md](./docs/01_requirements/acceptance_checklist.md)：可检查的 P1 与后续方案验收条目。
- [open_questions.md](./docs/01_requirements/open_questions.md)：高、中优先级待确认问题。
- 更新 [decision_log.md](./docs/02_design/decision_log.md)：新增 D-008 至 D-012。
- 更新 [PLAN.md](./PLAN.md)：P1 已完成，P2 为下一步。

**关键决策**
- 未明确披露的数据默认按非公开数据处理。
- Public Projection 是有限公开派生视图，不是完整 Race 数据源。
- 功能闭环按创建、披露、组织、展示四项可观察能力验收。
- 不将 DCR 部署位置、投影承载方式等未知事项写成架构事实。

**主要待确认问题**
- 完整 Race 数据的具体分类。
- ARY 可持久化的轻量数据范围与保留周期。
- 创建赛事由 Organizer 还是 ARY 发起。
- Public Projection 的字段、承载、更新与撤回机制。
- DCR 部署位置及数据访问权限。
- PoC 如何提供“无完整数据副本”的可观察证据。

**下一步**
执行 P2：设计 PRD。

> 现在执行 P2：设计 PRD。
>
> 请基于：
>
> 1. `docs/01_requirements/problem_definition.md`
> 2. `docs/01_requirements/scope_boundary.md`
> 3. `docs/01_requirements/acceptance_checklist.md`
> 4. `docs/01_requirements/open_questions.md`
>
> 生成：
>
> 1. `docs/02_design/prd.md`
>
> 要求：
>
> 1. 明确 ARY GRS 001 的产品目标；
> 2. 明确用户角色与使用场景；
> 3. 说明 Race 创建、披露、组织、展示的产品闭环；
> 4. 说明 Organizer 数据主权；
> 5. 说明 ARY 不持久化完整 Race 数据时，产品流程如何仍然成立；
> 6. 说明 Public Projection 的产品意义；
> 7. 功能范围使用 Must / Should / Could 分级；
> 8. 明确非目标；
> 9. 文末加入 PRD 自检表，对照 `acceptance_checklist.md`；
> 10. 不写实际 PoC 代码；
> 11. 完成后更新 `docs/02_design/decision_log.md`。
>
> 最后输出本轮产物、关键决策、待确认问题和下一步。

<details><summary>8 previous messages</summary>

> 我将执行 P2：先复核 P1 四份基线和当前决策记录，选择一套最小、可验证且不越权的产品闭环；随后生成 `prd.md`，把新形成的产品决策写入决策日志，并更新 `PLAN.md` 状态。不会写任何实际 PoC 代码。
>
> P1 中保留的若干问题必须在 PRD 中形成产品级工作假设，否则闭环无法被描述。我将采用最小方案：Organizer 侧创建权威 Race；ARY 仅登记最小公开入口；Public Projection 按需读取且不作为完整数据副本；更新、撤回由 Organizer 主动控制。这些会标为“待验证设计决策”，供 P3/P4 验证，而不是冒充来源事实。
>
> 开始写入 PRD。内容会区分“已锁定边界”和“P2 工作假设”：前者不可突破，后者用于让产品流程可描述，并将在 P3/P4 中验证或修订。功能仅围绕四项核心证明对象分级，不扩展到完整赛事执行系统。
>
> <details><summary>Created 1 file, edited 2 files</summary>
>
> - Wrote `./PLAN.md` (+2 -2)
> - Wrote `./docs/02_design/decision_log.md` (+6 -0)
> - Wrote `./docs/02_design/prd.md` (+192 -0)
>
> </details>
>
> PRD 已生成，并形成了六项产品决策。复核时发现 P1 的 `scope_boundary.md` 仍把“PRD 正文”写为当前阶段越界项；由于项目已经正式进入 P2，这会造成文档冲突。我会做最小修正，将该限制明确为 P1 阶段历史约束，并在待确认问题中标注 P2 已采用但仍待验证的工作假设。
>
> <details><summary>Edited 2 files</summary>
>
> - Wrote `./docs/01_requirements/open_questions.md` (+6 -0)
> - Wrote `./docs/01_requirements/scope_boundary.md` (+3 -3)
>
> </details>
>
> 自检结果显示 PRD 已覆盖全部要求，但有两项必须保持“待验证”而不能宣称完全通过：ARY 最小登记信息的最终持久化规则，以及 DCR 的部署与访问边界。我会在 PRD 中补充设计状态说明，并消除决策日志中 P1“待选择发起方”与 P2 Organizer-first 工作假设之间的表述歧义。
>
> <details><summary>Edited 2 files</summary>
>
> - Wrote `./docs/02_design/decision_log.md` (+1 -1)
> - Wrote `./docs/02_design/prd.md` (+5 -0)
>
> </details>
</details>

P2 已完成，未生成实际 PoC 代码。

**本轮产物**
- [prd.md](./docs/02_design/prd.md)：包含产品目标、角色、场景、产品闭环、数据主权、Public Projection、Must/Should/Could、非目标及自检表。
- 更新 [decision_log.md](./docs/02_design/decision_log.md)：新增 D-013 至 D-018。
- 更新 [open_questions.md](./docs/01_requirements/open_questions.md)：记录 P2 工作假设。
- 更新 [scope_boundary.md](./docs/01_requirements/scope_boundary.md)：解除 P1 阶段的 PRD 限制。
- 更新 [PLAN.md](./PLAN.md)：P2 已完成，P3 为下一步。

**关键决策**
- 采用 Organizer-first 流程：Organizer 创建权威 Race，ARY 创建公开入口。
- ARY 仅持久化最小公开登记信息，Public Projection 按需读取。
- Organizer 主动控制投影发布、更新和撤回。
- 投影无效、过期或撤回时，ARY 显示明确状态，不补全内容。
- Must 范围仅覆盖最小产品闭环及必要状态处理。

**待确认问题**
- 完整 Race 数据的具体分类。
- ARY 最小登记信息的最终字段与保留周期。
- Public Projection 的格式、承载位置和授权证明。
- 缓存、断连、过期及撤回的精确语义。
- DCR 部署与数据访问边界。

**下一步**
执行 P3：设计 PoC 理论方案与验证矩阵。

> 现在执行 P3：设计 PoC 理论方案。
>
> 请基于：
>
> 1. `docs/02_design/prd.md`
> 2. `docs/01_requirements/acceptance_checklist.md`
> 3. `docs/01_requirements/scope_boundary.md`
>
> 生成：
>
> 1. `docs/02_design/poc_design.md`
> 2. `docs/02_design/poc_validation_matrix.md`
>
> 要求：
>
> 1. 当前阶段只做理论设计，不写实际代码；
> 2. 围绕四项核心证明对象设计 PoC：
>    - 数据留存；
>    - 去中心化；
>    - 功能闭环；
>    - 投影机制。
> 3. 每项假设都要包含：
>    - 验证目标；
>    - 最小测试场景；
>    - 输入数据；
>    - 观测点；
>    - 通过标准；
>    - 失败条件。
> 4. 可以写 JSON 样例、API 草案、页面草案；
> 5. 不创建源码文件；
> 6. 明确哪些内容留到下一阶段代码 PoC；
> 7. 文末加入 PoC 自检表；
> 8. 完成后更新 `docs/02_design/decision_log.md`。
>
> 最后输出本轮产物、关键决策、待确认问题和下一步。

<details><summary>5 previous messages</summary>

> 我将执行 P3：先复核 PRD、验收清单和范围边界，然后把四项证明对象拆成理论 PoC 场景与验证矩阵。会使用 JSON/API/页面草案表达可验证思路，但只写 Markdown 文档，不创建任何源码文件。
>
> 已复核三份输入文档。P3 将采用“单 Organizer、单 Race、最小公开投影”的理论场景，因为它足以覆盖四项核心证明；多 Organizer、多 Race、生产级认证和真实网络部署都保留到后续阶段，不进入本轮理论 PoC 范围。
>
> 现在落盘两份 PoC 理论文档。`poc_design.md` 说明验证方案、样例数据、API/页面草案和下一阶段代码 PoC 边界；`poc_validation_matrix.md` 用矩阵把每项假设的目标、场景、输入、观测点、通过标准和失败条件对齐。
>
> <details><summary>Created 2 files, edited 2 files</summary>
>
> - Wrote `./PLAN.md` (+2 -2)
> - Wrote `./docs/02_design/decision_log.md` (+4 -0)
> - Wrote `./docs/02_design/poc_design.md` (+195 -0)
> - Wrote `./docs/02_design/poc_validation_matrix.md` (+64 -0)
>
> </details>
>
> P3 文档和决策日志已写入。现在做收尾检查：确认两个 PoC 文档都覆盖四项核心证明与六类验证要素，`PLAN.md` 已切到 P4，且没有新增任何非 Markdown/PDF 文件。
</details>

P3 已完成，未创建任何源码文件；当前项目仍只有 Markdown 和 PDF 文档。

**本轮产物**
- [poc_design.md](./docs/02_design/poc_design.md)：PoC 理论设计，包含 JSON 样例、API 草案、页面草案、四项证明对象、失败用例和自检表。
- [poc_validation_matrix.md](./docs/02_design/poc_validation_matrix.md)：四项核心证明对象的验证矩阵。
- 更新 [decision_log.md](./docs/02_design/decision_log.md)：新增 D-019 至 D-022。
- 更新 [PLAN.md](./PLAN.md)：P3 已完成，P4 为下一步。

**关键决策**
- P3 理论 PoC 采用单 Organizer、单 Race 的最小场景。
- PoC 数据分为三类：Organizer 完整数据、ARY 最小登记信息、Public Projection。
- 观测证据包括存储清单、投影读取记录、展示字段映射和失败用例结果。
- 撤回、过期、不可用状态统一按“不展示旧有效内容，只展示状态”处理。

**待确认问题**
- 完整 Race 数据的最终字段分类。
- ARY 最小登记字段和保留周期。
- Public Projection 的真实承载方式。
- DCR 部署位置与数据访问边界。
- 下一阶段代码 PoC 的实际存储、接口、页面和自动化验证方式。

**下一步**
执行 P4：设计系统架构与数据流。

> 现在执行 P4：设计系统架构与数据流。
>
> 请基于：
>
> 1. `docs/02_design/prd.md`
> 2. `docs/02_design/poc_design.md`
> 3. `docs/02_design/poc_validation_matrix.md`
> 4. `docs/01_requirements/scope_boundary.md`
>
> 生成：
>
> 1. `docs/02_design/architecture.md`
> 2. `docs/02_design/data_flow.md`
>
> 要求：
>
> 1. 明确 Organizer、ARY、DCR、Public Projection 的组件职责；
> 2. 标明数据方向、数据所有者、数据权限和持久化位置；
> 3. 说明哪些数据：
>    - 留在 Organizer；
>    - 可公开披露；
>    - 可被 ARY 临时处理；
>    - 可缓存；
>    - 禁止由 ARY 持久化。
> 4. 包含 Mermaid 架构图；
> 5. 包含 Mermaid 关键时序图；
> 6. 包含数据分类与持久化边界表；
> 7. 检查是否存在隐含的完整数据复制；
> 8. 完成后更新 `docs/02_design/decision_log.md`。
>
> 最后输出本轮产物、关键决策、待确认问题和下一步。

<details><summary>5 previous messages</summary>

> 我将执行 P4：先复核 PRD、PoC 理论、验证矩阵和范围边界，然后生成架构与数据流文档。重点会把所有权、权限、方向、持久化位置写清楚，并专门检查是否存在隐含完整数据复制。
>
> 输入复核完成。P4 需要把一个此前悬而未决的问题落成架构假设：DCR 不作为完整数据向 ARY 传输的桥；凡是接触完整 Race 数据的执行能力必须位于 Organizer 授权边界内，ARY 侧只接触公开登记信息和 Public Projection。该假设会进入决策日志，并在后续代码 PoC 中验证。
>
> 现在写入 `architecture.md` 和 `data_flow.md`。两份文档都会把所有权、权限、数据方向和持久化位置作为主线；其中架构文档放 Mermaid 组件图，数据流文档放关键时序图和隐含复制检查。
>
> <details><summary>Created 2 files, edited 3 files</summary>
>
> - Wrote `./PLAN.md` (+2 -2)
> - Wrote `./docs/01_requirements/open_questions.md` (+6 -0)
> - Wrote `./docs/02_design/architecture.md` (+114 -0)
> - Wrote `./docs/02_design/data_flow.md` (+123 -0)
> - Wrote `./docs/02_design/decision_log.md` (+5 -0)
>
> </details>
>
> 架构与数据流文档已生成。现在做一致性检查：确认 Mermaid 图、时序图、数据分类表、缓存规则和隐含复制检查都存在；同时确认 P4 已完成、P5 已成为下一步，并且仍未新增任何源码文件。
</details>

P4 已完成，未创建任何源码文件。

**本轮产物**
- [architecture.md](./docs/02_design/architecture.md)：组件职责、Mermaid 架构图、数据分类与持久化边界、DCR 边界、隐含完整数据复制检查。
- [data_flow.md](./docs/02_design/data_flow.md)：关键数据流、Mermaid 时序图、数据方向、权限规则、缓存规则、复制风险检查。
- 更新 [decision_log.md](./docs/02_design/decision_log.md)：新增 D-023 至 D-027。
- 更新 [open_questions.md](./docs/01_requirements/open_questions.md)：记录 P4 工作假设。
- 更新 [PLAN.md](./PLAN.md)：P4 已完成，P5 为下一步。

**关键决策**
- DCR 接触完整 Race 数据时必须位于 Organizer 授权域内。
- ARY Registry 只持久化最小公开登记信息。
- ARY Display 可临时处理 Public Projection，但不把投影正文作为权威持久化数据。
- 验证证据只保存字段名、清单、映射和结果，不保存私有内容正文。
- 当前架构不存在必须复制完整 Race 数据到 ARY 的链路。

**待确认问题**
- Public Projection 字段是否过宽，需要代码 PoC 验证。
- ARY 最小登记字段是否会膨胀为可重建完整数据的集合。
- 缓存失效、过期和撤回的实际实现细节。
- DCR 在真实部署中的具体位置与运行边界。

**下一步**
执行 P5：设计 Demo 展示方案。

> 现在执行 P5：设计 Demo 展示方案。
>
> 请基于：
>
> 1. `docs/02_design/prd.md`
> 2. `docs/02_design/poc_design.md`
> 3. `docs/02_design/poc_validation_matrix.md`
> 4. `docs/02_design/architecture.md`
> 5. `docs/02_design/data_flow.md`
>
> 生成：
>
> 1. `docs/02_design/demo_plan.md`
> 2. `docs/02_design/demo_script.md`
>
> 要求：
>
> 1. 当前阶段不写代码；
> 2. 说明 Demo 页面清单；
> 3. 说明每个页面展示什么；
> 4. 说明演示步骤；
> 5. 说明每一步证明哪项核心假设；
> 6. 明确如何展示 Organizer 持有完整数据；
> 7. 明确如何展示 Public Projection；
> 8. 明确如何证明 ARY 没有持久化完整 Race 数据；
> 9. 明确下一阶段代码实现时需要实现的最小页面；
> 10. 完成后更新 `docs/02_design/decision_log.md`。
>
> 最后输出本轮产物、关键决策、待确认问题和下一步。

<details><summary>5 previous messages</summary>

> 我将执行 P5：先复核 PRD、PoC、架构与数据流文档，然后把 Demo 拆成页面清单和逐步演示脚本。当前仍只写设计文档，不创建任何页面代码或源码文件。
>
> 输入复核完成。Demo 会采用三页最小组合：Organizer 控制台、ARY 公开页、验证证据页；这比做完整前端更小，但能同时证明完整数据留存、公开投影、ARY 最小持久化和功能闭环。
>
> 现在写入 Demo 方案和演示脚本。方案会明确每个页面展示内容、下一阶段最小页面实现；脚本会逐步说明“展示什么”和“证明哪项核心假设”。
>
> <details><summary>Created 2 files, edited 2 files</summary>
>
> - Wrote `./PLAN.md` (+2 -2)
> - Wrote `./docs/02_design/decision_log.md` (+4 -0)
> - Wrote `./docs/02_design/demo_plan.md` (+144 -0)
> - Wrote `./docs/02_design/demo_script.md` (+126 -0)
>
> </details>
>
> Demo 方案和脚本已落盘。现在做最后核对：检查页面清单、展示内容、演示步骤、假设映射、下一阶段最小页面，以及确认没有新增任何代码文件。
</details>

P5 已完成，未创建任何代码或页面文件。

**本轮产物**
- [demo_plan.md](./docs/02_design/demo_plan.md)：Demo 页面清单、页面展示内容、证明映射、演示步骤总览、下一阶段最小页面。
- [demo_script.md](./docs/02_design/demo_script.md)：8 步演示脚本，每步包含页面、操作、展示内容和证明假设。
- 更新 [decision_log.md](./docs/02_design/decision_log.md)：新增 D-028 至 D-031。
- 更新 [PLAN.md](./PLAN.md)：P5 已完成，P6 为下一步。

**关键决策**
- Demo 采用三页最小结构：Organizer 控制台、ARY 公开页、验证证据页。
- Demo 不展示私有字段正文，只展示字段名、位置和边界标签。
- Demo 必须包含失败用例：越界登记、误投影、未披露字段请求。
- 下一阶段代码 Demo 最小页面为三页，可选增加导航页。

**待确认问题**
- 下一阶段页面是否需要真实交互，还是静态模拟即可。
- Public Projection 的真实承载方式和字段格式。
- 失败用例是自动检测还是手动展示证据。
- 是否需要为评审准备一页式总览页。

**下一步**
执行 P6：维护 Riding Record。

> 在下一步前，简要确认：Demo设计方向是最小可证明方案，不实现全栈

确认：Demo 设计方向是**最小可证明方案**，不实现全栈。

当前 Demo 只要求用最小页面证明四件事：完整数据留在 Organizer、ARY 不持久化完整 Race 数据、Public Projection 可支撑展示、创建/披露/组织/展示闭环成立。生产级权限、后端服务、数据库、真实部署、多 Organizer/多 Race 都不在当前 Demo 范围内。

> 现在执行 P6：维护 Riding Record。
>
> 请基于当前已有文档：
>
> 1. `AGENTS.md`
> 2. `PLAN.md`
> 3. `docs/01_requirements/problem_definition.md`
> 4. `docs/01_requirements/scope_boundary.md`
> 5. `docs/01_requirements/acceptance_checklist.md`
> 6. `docs/02_design/prd.md`
> 7. `docs/02_design/poc_design.md`
> 8. `docs/02_design/poc_validation_matrix.md`
> 9. `docs/02_design/architecture.md`
> 10. `docs/02_design/demo_plan.md`
> 11. `docs/02_design/decision_log.md`
>
> 生成或更新：
>
> 1. `docs/02_design/riding_record_draft.md`
>
> 要求记录：
>
> 1. 初始输入材料；
> 2. 为什么先生成 AGENTS.md 和 PLAN.md；
> 3. 如何锁定问题定义和范围；
> 4. 如何形成 PRD；
> 5. 如何形成 PoC 理论方案；
> 6. 如何形成架构与数据流；
> 7. 如何形成 Demo 方案；
> 8. 人类做了哪些判断；
> 9. Agent 输出如何被约束；
> 10. 哪些内容留到下一阶段代码实现。
>
> 内容中文、精炼、可复盘。
> 完成后更新 `docs/02_design/decision_log.md`。

<details><summary>6 previous messages</summary>

> 我将执行 P6：先复核你列出的现有文档和当前计划，再生成一份精炼的 Riding Record 草稿，记录从初始化到 Demo 设计的关键输入、判断、约束和阶段边界；最后更新决策日志和 `PLAN.md`。
>
> P6 只维护过程记录，不改变前面设计口径。我会把“人类判断”和“Agent 约束”分开写，避免把设计结论写成流水账。
>
> 材料复核完成。接下来我会生成 `riding_record_draft.md`，结构上按 P0 到 P5 的工作推进记录，最后列出人类判断、Agent 约束和下一阶段代码实现边界。
>
> 现在写入过程记录和决策日志。Riding Record 不会复述所有文档正文，只记录关键输入、判断路径、约束方式和可复盘结论。
>
> <details><summary>Created 1 file, edited 2 files</summary>
>
> - Wrote `./PLAN.md` (+2 -2)
> - Wrote `./docs/02_design/decision_log.md` (+2 -0)
> - Wrote `./docs/02_design/riding_record_draft.md` (+229 -0)
>
> </details>
>
> Riding Record 草稿已生成，决策日志和计划已更新。现在做收尾检查：确认记录覆盖十项要求，P6 已完成、P7 成为下一步，并且没有新增源码文件。
</details>

P6 已完成，未创建任何源码文件。

**本轮产物**
- [riding_record_draft.md](./docs/02_design/riding_record_draft.md)：记录初始输入、P0-P5 形成路径、人类判断、Agent 约束、下一阶段代码实现边界。
- 更新 [decision_log.md](./docs/02_design/decision_log.md)：新增 D-032、D-033。
- 更新 [PLAN.md](./PLAN.md)：P6 已完成，P7 为下一步。

**关键决策**
- Riding Record 按 P0-P6 阶段链路记录，不复述全部文档正文。
- Riding Record 明确区分人类判断、Agent 输出约束、下一阶段代码 PoC 内容。

**待确认问题**
- 代码 PoC 阶段是否需要把 Riding Record 扩展为逐轮对话记录。
- 是否需要在提交前补一版更正式的 `Riding Record` 到 `docs/04_submission`。

**下一步**
执行 P7：一致性评审与提交整理。

> 现在执行 P7 的第一部分：一致性评审。
>
> 请审查以下文件：
>
> 1. `docs/01_requirements/acceptance_checklist.md`
> 2. `docs/02_design/prd.md`
> 3. `docs/02_design/poc_design.md`
> 4. `docs/02_design/poc_validation_matrix.md`
> 5. `docs/02_design/architecture.md`
> 6. `docs/02_design/data_flow.md`
> 7. `docs/02_design/demo_plan.md`
> 8. `docs/02_design/demo_script.md`
>
> 生成：
>
> 1. `docs/03_review/review_report.md`
>
> 要求重点检查：
>
> 1. 是否满足七项评审维度；
> 2. 是否写成普通 PRD；
> 3. 是否真正证明数据安全与去中心化；
> 4. 是否存在 ARY 隐性持久化完整 Race 数据；
> 5. Organizer、ARY、DCR、Public Projection 的职责是否冲突；
> 6. PRD、PoC、架构、Demo 是否一致；
> 7. 是否存在超出当前阶段范围的内容；
> 8. 是否存在待确认但未标记的问题。
>
> 只生成审查报告，不修改正文。
> 完成后更新 `docs/02_design/decision_log.md`。

<details><summary>7 previous messages</summary>

> 我将按代码评审式的严谨口径执行 P7 第一部分：只审查并生成报告，不改 PRD、PoC、架构或 Demo 正文。会重点找冲突、越界、隐性持久化风险和未标记问题，然后只更新决策日志记录本次审查结论。
>
> 开始读取全部被审查文件。审查时我会把“设计中已标注待验证”的内容和“未标记的缺口”区分开，避免把合理的阶段性假设误判为错误。
>
> 审查材料已经读完。初步结论：方案整体不是普通 PRD，主线围绕数据主权与去中心化证明展开；主要风险集中在少数待验证项的状态同步和后续代码 PoC 的边界执行，而不是当前文档方向错误。
>
> 现在生成 `review_report.md`，并只在 `decision_log.md` 追加本次审查决策记录。不会修改被审查的正文文件。
>
> <details><summary>Created 1 file, edited 1 file</summary>
>
> - Wrote `./docs/02_design/decision_log.md` (+1 -0)
> - Wrote `./docs/03_review/review_report.md` (+148 -0)
>
> </details>
>
> 审查报告已生成。现在我会核对只新增了报告并更新了决策日志，没有修改被审查正文，同时确认报告覆盖八项检查要求。
>
> 核对通过：本轮只新增审查报告并更新决策日志，没有新增非文档文件，也没有改动被审查正文。
</details>

P7 第一部分一致性审查已完成，未修改被审查正文。

**本轮产物**
- [review_report.md](./docs/03_review/review_report.md)：一致性审查报告。
- 更新 [decision_log.md](./docs/02_design/decision_log.md)：新增 D-034。

**审查结论**
- 当前设计整体通过一致性审查。
- 方案不是普通 PRD，主线仍是数据安全与去中心化证明。
- 未发现必须把完整 Race 数据复制到 ARY 的设计链路。
- Organizer、ARY、DCR、Public Projection 职责未发现直接冲突。
- PRD、PoC、架构、数据流、Demo 基本一致。

**主要风险**
- DCR 边界需要在代码 PoC 阶段验证。
- Public Projection 字段过宽仍是主要待验证风险。
- 少量阶段状态措辞需要在提交整理阶段统一修正。

**下一步**
执行 P7 第二部分：提交整理。

> 现在执行 P7 的第二部分：制定修订计划。
>
> 请基于：
>
> 1. `docs/03_review/review_report.md`
>
> 生成：
>
> 1. `docs/03_review/revision_plan.md`
>
> 要求：
>
> 1. 按 Must Fix / Should Fix / Could Fix 分类；
> 2. 说明每项修改对应哪些文件；
> 3. 说明修改顺序；
> 4. 说明修改后如何保证 PRD、PoC、架构、Demo 一致；
> 5. 不直接修改正文；
> 6. 完成后更新 `docs/02_design/decision_log.md`。
>
> 最后输出本轮产物、关键决策、待确认问题和下一步。

<details><summary>7 previous messages</summary>

> 我将基于审查报告制定修订计划，只新增 `revision_plan.md` 并更新决策日志；不会直接修改 PRD、PoC、架构、Demo 等正文文件。计划会把必须修、应该修、可选修分开，并标明文件、顺序和一致性保障方式。
>
> 先读取审查报告和决策日志，确认修订项只来自已发现的问题和风险，不额外扩大范围。
>
> 审查报告只提出三个修订来源：DCR 验证、投影字段冻结、阶段状态措辞同步。我会把“状态措辞同步”列为 Must Fix，因为它是提交前的直接一致性问题；另外两个是 Should Fix，因为需要为代码 PoC 建立清单和前置规则，但不应在本轮直接改正文。
>
> 现在写入修订计划。它会说明修改顺序和一致性保障方法，但不会对正文文件执行任何实际修订。
>
> <details><summary>Created 1 file, edited 1 file</summary>
>
> - Wrote `./docs/02_design/decision_log.md` (+1 -0)
> - Wrote `./docs/03_review/revision_plan.md` (+72 -0)
>
> </details>
>
> 修订计划已生成。现在我会核对它包含 Must/Should/Could、文件映射、修改顺序和一致性保障，并确认未修改任何正文文件、未新增代码。
>
> 核对通过：本轮只新增修订计划并更新决策日志，没有修改正文文件，也没有新增非文档文件。
</details>

P7 第二部分修订计划已完成，未修改任何正文文件。

**本轮产物**
- [revision_plan.md](./docs/03_review/revision_plan.md)：按 Must Fix / Should Fix / Could Fix 分类的修订计划。
- 更新 [decision_log.md](./docs/02_design/decision_log.md)：新增 D-035。

**关键决策**
- Must Fix：先同步阶段状态措辞。
- Should Fix：补强 DCR 输出检查、冻结最小 Public Projection 字段集合、强化缓存失效与撤回验证。
- Could Fix：提交总览、最小可证明方案摘要、Riding Record 提交版。
- 本轮只制定计划，不直接修改正文。

**待确认问题**
- 是否现在执行 Must Fix 和 Should Fix。
- 提交材料是否需要一页式总览。
- Riding Record 是否需要整理成提交版。

**下一步**
按 `revision_plan.md` 执行修订项，建议先处理 `MF-01`。

> 现在执行 P7 的第三部分：根据修订计划修改设计文档。
>
> 请基于：
>
> 1. `docs/03_review/revision_plan.md`
>
> 修订：
>
> 1. `docs/02_design/prd.md`
> 2. `docs/02_design/poc_design.md`
> 3. `docs/02_design/poc_validation_matrix.md`
> 4. `docs/02_design/architecture.md`
> 5. `docs/02_design/data_flow.md`
> 6. `docs/02_design/demo_plan.md`
> 7. `docs/02_design/demo_script.md`
>
> 要求：
>
> 1. 优先修复 Must Fix；
> 2. 保持术语一致；
> 3. 保持数据边界一致；
> 4. 删除超出当前阶段的内容；
> 5. 强化四项 PoC 核心证明；
> 6. 不写实际 PoC 代码；
> 7. 完成后更新 `docs/02_design/decision_log.md` 和 `docs/02_design/riding_record_draft.md`。
>
> 最后输出修改摘要、剩余问题和下一步。

<details><summary>8 previous messages</summary>

> 我将按 `revision_plan.md` 执行 P7 第三部分：先处理 Must Fix 的阶段状态措辞，再补强 DCR 输出检查、投影字段冻结、缓存撤回验证。会只修改设计文档、决策日志和 Riding Record，不写任何 PoC 代码。
>
> 先读取修订计划和七个目标文档，定位需要改的具体段落。重点检查过期措辞、DCR 输出清单、最小投影字段和缓存撤回规则。
>
> 我已定位需要修订的点：主要是阶段措辞、DCR 输出验证、Public Projection 最小字段冻结、缓存撤回验证。接下来会用最小补丁改目标文档，保持现有结构和术语，不引入实现细节或代码。
>
> <details><summary>Edited 7 files</summary>
>
> - Wrote `./docs/02_design/architecture.md` (+16 -4)
> - Wrote `./docs/02_design/data_flow.md` (+5 -2)
> - Wrote `./docs/02_design/demo_plan.md` (+6 -0)
> - Wrote `./docs/02_design/demo_script.md` (+12 -0)
> - Wrote `./docs/02_design/poc_design.md` (+25 -0)
> - Wrote `./docs/02_design/poc_validation_matrix.md` (+7 -4)
> - Wrote `./docs/02_design/prd.md` (+5 -5)
>
> </details>
>
> 第一轮修订已完成。接下来我会检查是否还残留“待 P4 / P4 前 / 留待 P4”等过期措辞，并同步更新决策日志与 Riding Record 记录本次修订。
>
> 检查发现一个小口径不一致：`demo_plan.md` 的 S8 证明对象少写了“投影机制”，而 `demo_script.md` 已包含。这个属于本轮一致性修订范围，我会一并修正，并在 PoC 自检中补充 DCR、投影字段和缓存验证项。
>
> <details><summary>Edited 4 files</summary>
>
> - Wrote `./docs/02_design/decision_log.md` (+1 -0)
> - Wrote `./docs/02_design/demo_plan.md` (+1 -1)
> - Wrote `./docs/02_design/poc_design.md` (+3 -0)
> - Wrote `./docs/02_design/riding_record_draft.md` (+13 -1)
>
> </details>
>
> 修订和记录更新已完成。现在做最终一致性检查：确认没有残留过期 P4 表述、没有新增源码文件，且四项 PoC、DCR、投影字段、缓存撤回相关内容已覆盖。
</details>

已执行 P7 第三部分修订，未写实际 PoC 代码，未新增源码文件。

**修改摘要**
- 修订 [prd.md](./docs/02_design/prd.md)：同步 P4 后的 DCR 边界状态，移除过期阶段措辞。
- 修订 [poc_design.md](./docs/02_design/poc_design.md)：增加 DCR 输出清单、最小 Public Projection 字段冻结规则、缓存撤回失败用例。
- 修订 [poc_validation_matrix.md](./docs/02_design/poc_validation_matrix.md)：增加 DCR 输出、投影字段冻结、缓存失效的代码 PoC 验证项。
- 修订 [architecture.md](./docs/02_design/architecture.md)：补充 DCR 输出边界和 Public Projection 最小字段边界。
- 修订 [data_flow.md](./docs/02_design/data_flow.md)：补充 DCR 输出检查和缓存撤回验证规则。
- 修订 [demo_plan.md](./docs/02_design/demo_plan.md)、[demo_script.md](./docs/02_design/demo_script.md)：增加 DCR 输出清单、投影字段冻结、缓存撤回检查展示步骤。
- 更新 [decision_log.md](./docs/02_design/decision_log.md)：新增 D-036。
- 更新 [riding_record_draft.md](./docs/02_design/riding_record_draft.md)：记录 P7 修订过程。

**剩余问题**
- 完整 Race 数据分类仍需在代码 PoC 前冻结。
- 最小 Public Projection 字段集合仍需在实现前最终确认。
- DCR 真实部署、运行身份和输出清单需要代码 PoC 验证。
- 缓存失效、撤回、过期的实际实现仍待代码阶段验证。

**下一步**
执行 P7 后续提交整理：生成 `docs/04_submission` 下的提交总览与最终材料清单。
