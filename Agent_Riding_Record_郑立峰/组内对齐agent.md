# 对齐PRD与文档体系

> 你是本项目的“PRD 对齐、PoC/Demo 迭代设计 Agent”。
>
> 当前任务不是自由扩展功能，也不是重写一个新系统，而是在小组已选定的 PRD 基准上，完成我的个人文档体系对齐，并为后续 PoC/Demo 迭代提供清晰、可执行的工程任务说明。
>
> 请严格遵守：
>
> 1. 先阅读项目根目录：
>    - AGENTS.md
>    - PLAN.md
>
> 2. 再阅读我原有设计文档：
>    - docs/01_requirements/problem_definition.md
>    - docs/01_requirements/scope_boundary.md
>    - docs/01_requirements/acceptance_checklist.md
>    - docs/01_requirements/open_questions.md
>    - docs/02_design/prd.md
>    - docs/02_design/poc_design.md
>    - docs/02_design/poc_validation_matrix.md
>    - docs/02_design/architecture.md
>    - docs/02_design/data_flow.md
>    - docs/02_design/demo_plan.md
>    - docs/02_design/demo_script.md
>    - docs/02_design/decision_log.md
>    - docs/02_design/riding_record_draft.md
>
> 3. 再阅读小组基准材料：
>    - group_ARY_week1/PRD-ARY-GRS-001.md
>    - group_ARY_week1/DEMO_VERIFICATION.md
>    - group_ARY_week1/ary_grs_001_poc.py
>    - group_ARY_week1/demo_page.html
>    - group_ARY_week1/Riding Record.md
>
> 4. 以 group_ARY_week1/PRD-ARY-GRS-001.md 作为新的 PRD 基准。
>    我的原 PRD 不再作为产品主线，但其中关于数据留存、去中心化、投影机制、字段溯源、缓存撤回、DCR 输出边界、验证证据页的严谨设计，需要被保留并迁移到下游文档中。
>
> 5. 必须承认并吸收小组 PRD 中的新设计：
>    - Public Metadata 可由 ARY 持久化；
>    - Public Projection 可由 ARY 持久化，但必须来自 Organizer 主动披露；
>    - 引入 Participant / Rider 用户；
>    - 引入 Registration Proxy；
>    - 引入 Organizer Server；
>    - 报名请求可经过 ARY Stateless Proxy；
>    - 报名事实只能写入 Organizer Server；
>    - 公开报名计数、公开 RiderID / nickname、公开参与摘要可作为 Organizer 主动披露的 Public Projection 展示；
>    - 引入 Suspended 状态表示 Organizer Server 不可达。
>
> 6. 必须保留不可突破边界：
>    - 完整 Race Source Facts 留在 Organizer / DCR 控制域；
>    - ARY 不得持久化完整 Race 数据；
>    - ARY 不得从代理请求中生成自己的报名事实库；
>    - ARY Proxy 不得 save / commit 报名事实；
>    - 参赛者代码、完整骑行记录、执行日志、DCR 判断链、评审证据、复盘材料、私有规则细节不得进入 ARY 持久化存储；
>    - ARY 展示的长期报名摘要必须来自 Organizer 主动披露的 Public Projection；
>    - 日志、缓存、debug 输出、验证材料也不得泄露核心私有源事实。
>
> 7. 工作顺序必须是：
>    A. 先做差异分析；
>    B. 再提出文档修改计划；
>    C. 再修改文档；
>    D. 再给出 PoC/Demo 迭代任务清单；
>    E. 最后给出验收清单。

<details><summary>32 previous messages</summary>

> Stream error
>
> Reconnecting 5/5
> stream disconnected before completion: 远程主机强迫关闭了一个现有的连接。 (os error 10054)
>
> 我会按你指定的顺序先读根目录约束和计划，再读个人文档与小组基准。之后我会先做差异分析和修改计划，再动手改文档，避免把 PRD 主线和下游约束混在一起。
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `Get-Content -Raw -Encoding UTF8 PLAN.md`
> - Ran `Get-Content -Raw -Encoding UTF8 AGENTS.md`
>
> </details>
>
> 根目录约束确认：当前阶段仍强调“不编写实际 PoC 代码”，但这次任务要求对齐小组已存在的 PoC/Demo 基准，因此我会只输出后续迭代任务说明，不修改或新增实现代码。接下来读个人文档；并做一次轻量记忆检索，确认是否有此前 ARY 相关决策需要避免遗漏。
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `Select-String -Path C:\Users\Administrator\.codex\memories\MEMORY.md -Pattern 'ARY','SE_experiment','PLAN.md','prd.md' | Select-Object Path,LineNumber,Line`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\01_requirements\problem_definition.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\01_requirements\acceptance_checklist.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\01_requirements\open_questions.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\01_requirements\scope_boundary.md`
>
> </details>
>
> 个人需求文档显示旧基线偏严格：ARY 对 Public Projection 多处按“按需读取/不长期保存”处理，DCR 仍偏抽象。这正是需要迁移的重点：保留边界证明力度，但接受小组 PRD 对可持久化公开数据、报名链路和 Suspended 状态的新增定义。
>
> 修改：在实现设计后需要编写实际 PoC 代码
>
> <details><summary>Ran 9 commands</summary>
>
> - Ran `Get-Content -Raw -Encoding UTF8 docs\02_design\poc_design.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\02_design\demo_script.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\02_design\prd.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\02_design\decision_log.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\02_design\demo_plan.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\02_design\riding_record_draft.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\02_design\poc_validation_matrix.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\02_design\data_flow.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\02_design\architecture.md`
>
> </details>
>
> 收到。这个修改会覆盖旧文档里“当前阶段不写实际 PoC 代码”的绝对表述：我会把它调整为“先完成实现设计与边界冻结，再进入实际 PoC 代码编写”，并在任务清单里明确代码实现步骤和验收证据。现在继续读取小组基准材料。
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `Get-Content -Raw -Encoding UTF8 group_ARY_week1\PRD-ARY-GRS-001.md`
> - Ran `Get-Content -Raw -Encoding UTF8 group_ARY_week1\ary_grs_001_poc.py`
> - Ran `Get-Content -Raw -Encoding UTF8 "group_ARY_week1\Riding Record.md"`
> - Ran `Get-Content -Raw -Encoding UTF8 group_ARY_week1\demo_page.html`
> - Ran `Get-Content -Raw -Encoding UTF8 group_ARY_week1\DEMO_VERIFICATION.md`
>
> </details>
>
> 小组基准已经读完。关键变化很明确：小组 PRD 不只是放宽“公开投影可持久化”，还把报名旅程、Organizer Server、ARY Stateless Proxy、公开报名摘要和 `Suspended` 纳入产品主线；个人文档要从“按需读取投影的理论设计”调整为“Public Yard, Private Race Source 的可实现 PoC 设计”。
>
> 差异分析先给出可执行结论：旧个人文档的严谨边界要保留，但“ARY 不持久化 Public Projection”“不写实际 PoC 代码”“只有 Organizer/ARY/DCR/访问者角色”这三类表述需要替换或降级。修改计划是：先改计划与范围口径，再改 PRD/PoC/架构/数据流/Demo 的角色、存储和报名链路，最后把代码 PoC 任务和验收项落到文档里。
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `rg -n "^def |^class |@.*\.(get|post)|FORBIDDEN_ARY_KEYS|ary_public_.*store|organizer_app|ary_app" group_ARY_week1\ary_grs_001_poc.py`
> - Ran `git status --short`
> - Ran `rg -n "不写实际|不编写实际|按需读取|Public Projection 按需|Participant|Rider|Registration Proxy|Organizer Server|Stateless Proxy|Suspended|Public Metadata" .`
>
> </details>
>
> 我将开始修改文档。假设是：这次不直接扩展小组 PoC 的实现代码，而是把个人文档改成“实现设计完成后必须进入实际 PoC 代码”的路线；如果下一步你要求我继续执行代码实现，我会基于这些任务清单落到 `group_ARY_week1/ary_grs_001_poc.py` 或新的个人 PoC 文件上。
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./PLAN.md` (+9 -4)
>
> </details>
>
> `PLAN.md` 已先改掉旧的绝对禁写代码口径：现在阶段顺序是 P7 对齐、小组基准吸收，P8 冻结实现设计，P9 编写并验证实际 PoC。接下来改需求边界与验收文档，让后续 PRD/PoC/架构修改有统一口径。
>
> <details><summary>Edited 4 files</summary>
>
> - Wrote `./docs/01_requirements/acceptance_checklist.md` (+12 -6)
> - Wrote `./docs/01_requirements/open_questions.md` (+18 -8)
> - Wrote `./docs/01_requirements/problem_definition.md` (+15 -12)
> - Wrote `./docs/01_requirements/scope_boundary.md` (+20 -12)
>
> </details>
>
> 需求层已对齐：Public Metadata / Projection 可由 ARY 持久化，报名代理和 `Suspended` 已进入边界与验收。接下来改设计层文档，把旧的“按需读取投影”主线替换为小组 PRD 的“ARY 存储公开披露数据，但不存 Race Source Facts”。
>
> <details><summary>Created 2 files</summary>
>
> - Wrote `./docs/02_design/poc_design.md` (+136 -0)
> - Wrote `./docs/02_design/prd.md` (+93 -0)
>
> </details>
>
> PRD 与 PoC 设计已改成“以小组 PRD/PoC 为基准”的对齐文件，原来的字段溯源、DCR 输出、缓存撤回和拒绝规则被迁移成 PoC 任务与验收项。现在继续改验证矩阵、架构和数据流，确保代理报名和 `Suspended` 不再是旁支。
>
> <details><summary>Created 3 files</summary>
>
> - Wrote `./docs/02_design/architecture.md` (+98 -0)
> - Wrote `./docs/02_design/data_flow.md` (+116 -0)
> - Wrote `./docs/02_design/poc_validation_matrix.md` (+53 -0)
>
> </details>
>
> 验证矩阵、架构、数据流已完成主线切换：现在验收对象包含 public stores、Proxy 零落库、Organizer Server 报名写入、公开报名摘要来源和 `Suspended`。接下来改 Demo 方案与脚本，让演示能直接指导后续实际 PoC。
>
> <details><summary>Created 2 files</summary>
>
> - Wrote `./docs/02_design/demo_plan.md` (+79 -0)
> - Wrote `./docs/02_design/demo_script.md` (+115 -0)
>
> </details>
>
> Demo 方案与脚本已改成可运行 PoC 的验收路径，包含启动端口、公开页、报名代理、隐私检查、泄露拒绝和离线挂起。接下来更新决策日志、Riding Record，并新增一份集中对齐与迭代任务文档，承接你要求的差异分析、修改计划、代码任务和验收清单。
>
> <details><summary>Created 1 file, edited 2 files, ran 3 commands</summary>
>
> - Wrote `./docs/02_design/decision_log.md` (+8 -0)
> - Wrote `./docs/02_design/riding_record_draft.md` (+27 -3)
> - Wrote `./docs/03_review/prd_alignment_and_poc_iteration.md` (+63 -0)
> - Ran `rg -n "不写实际|不编写实际|按需读取|Public Projection 按需|当前阶段不存在实际 PoC|当前仍不编写实际 PoC|只完成文档设计" PLAN.md docs\01_requirements docs\02_design docs\03_review docs\04_submission`
> - Ran `rg -n "Registration Proxy|Organizer Server|Suspended|Public Metadata|Public Projection|save\(\)|commit\(\)" docs\01_requirements docs\02_design docs\03_review\prd_alignment_and_poc_iteration.md`
> - Ran `Get-ChildItem -Recurse -File docs | Select-Object FullName,Length`
>
> </details>
>
> 一次全文检查发现还有三处旧材料会误导：`review_report.md`、`team_communication_brief.md` 和 Riding Record 的历史段落仍写着“按需读取/不写代码”。我会把它们改成带时间边界的旧阶段描述或新的 P8/P9 口径，避免提交材料互相冲突。
>
> <details><summary>Edited 4 files, ran 3 commands</summary>
>
> - Wrote `./docs/02_design/decision_log.md` (+3 -3)
> - Wrote `./docs/02_design/riding_record_draft.md` (+3 -3)
> - Wrote `./docs/03_review/review_report.md` (+1 -1)
> - Wrote `./docs/04_submission/team_communication_brief.md` (+3 -3)
> - Ran `rg -n "不写实际|不编写实际|当前仍不编写实际 PoC|按需读取 Public Projection|Public Projection 按需读取|当前阶段不存在实际 PoC|只完成文档设计" PLAN.md docs\01_requirements docs\02_design docs\03_review docs\04_submission`
> - Ran `rg -n "D-037|D-038|D-039|D-040|D-041|D-042|D-043|D-044" docs\02_design\decision_log.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\03_review\prd_alignment_and_poc_iteration.md`
>
> </details>
>
> 检查结果里剩下的“按需读取/不写代码”都已经是历史或已替代记录，不再作为当前主线。最后我会把集中任务文档里的验收清单拆成“本轮已完成”和“后续待完成”，再做一次一致性核对。
>
> <details><summary>Edited 1 file, ran 3 commands</summary>
>
> - Wrote `./docs/03_review/prd_alignment_and_poc_iteration.md` (+14 -11)
> - Ran `rg -n "group_ARY_week1/PRD-ARY-GRS-001.md|Public Yard|Private Race Source|Registration Proxy|Organizer Server|Suspended|P9" PLAN.md docs\01_requirements docs\02_design docs\03_review\prd_alignment_and_poc_iteration.md docs\04_submission\team_communication_brief.md`
> - Ran `Get-Content -Head 30 -Encoding UTF8 docs\02_design\prd.md`
> - Ran `Get-Content -Tail 30 -Encoding UTF8 docs\03_review\prd_alignment_and_poc_iteration.md`
>
> </details>
>
> 一致性核对完成：当前主线已经覆盖小组 PRD 的新增设计，并保留了个人原文档中的严谨验证项。没有改动小组 PoC 代码；本轮产出停在 P7 文档对齐和 P8/P9 任务冻结说明。
>
> 已完成 P7 文档体系对齐，并按你的修改把路线改为：实现设计冻结后必须进入实际 PoC 代码编写。
>
> 主要改动：
> - 更新 [PLAN.md](./PLAN.md)，新增 P8 实现设计冻结、P9 实际 PoC 代码与 Demo 验证阶段。
> - 将个人 PRD 改为对齐说明：[docs/02_design/prd.md](./docs/02_design/prd.md)。
> - 重写 PoC、验证矩阵、架构、数据流、Demo 方案和脚本，使主线对齐小组 PRD 的 Public Yard / Private Race Source。
> - 更新需求边界、待确认问题、验收清单、决策日志和 Riding Record。
> - 新增集中任务文档：[docs/03_review/prd_alignment_and_poc_iteration.md](./docs/03_review/prd_alignment_and_poc_iteration.md)，包含差异分析、修改计划、P8/P9 任务清单和验收清单。
>
> 保留并下沉了原设计中的严谨项：字段溯源、缓存撤回、DCR 输出边界、越界字段拒绝、验证证据页、日志/debug 防泄露。未修改小组 PoC 代码；本轮只完成文档对齐与后续代码任务定义。
>
> 验证：已用 `rg` 检查新主线关键词和旧口径替代记录，确认当前文档明确承认 Public Metadata / Projection 可由 ARY 持久化、Registration Proxy 无状态、报名事实只写 Organizer Server、`Suspended` 仅表示公开可达性状态。
>
> <details><summary>Plan</summary>
>
> - [x] 读取小组 PRD、Demo 验证、PoC 代码与 Riding Record 基准
> - [x] 完成个人文档与小组基准差异分析
> - [x] 提出并执行文档修改计划
> - [x] 补充 PoC/Demo 代码迭代任务清单
> - [x] 按验收清单核对修改结果
>
> </details>
</details>

已完成 P7 文档体系对齐，并按你的修改把路线改为：实现设计冻结后必须进入实际 PoC 代码编写。

主要改动：
- 更新 [PLAN.md](./PLAN.md)，新增 P8 实现设计冻结、P9 实际 PoC 代码与 Demo 验证阶段。
- 将个人 PRD 改为对齐说明：[docs/02_design/prd.md](./docs/02_design/prd.md)。
- 重写 PoC、验证矩阵、架构、数据流、Demo 方案和脚本，使主线对齐小组 PRD 的 Public Yard / Private Race Source。
- 更新需求边界、待确认问题、验收清单、决策日志和 Riding Record。
- 新增集中任务文档：[docs/03_review/prd_alignment_and_poc_iteration.md](./docs/03_review/prd_alignment_and_poc_iteration.md)，包含差异分析、修改计划、P8/P9 任务清单和验收清单。

保留并下沉了原设计中的严谨项：字段溯源、缓存撤回、DCR 输出边界、越界字段拒绝、验证证据页、日志/debug 防泄露。未修改小组 PoC 代码；本轮只完成文档对齐与后续代码任务定义。

验证：已用 `rg` 检查新主线关键词和旧口径替代记录，确认当前文档明确承认 Public Metadata / Projection 可由 ARY 持久化、Registration Proxy 无状态、报名事实只写 Organizer Server、`Suspended` 仅表示公开可达性状态。

> 做 P8 检查与增强计划：
>
> 1. 确认现有代码已覆盖哪些 P9 验收项；
> 2. 列出缺口，重点包括：
>    - Projection version/hash 的可复跑验证；
>    - Evidence Dashboard 或统一证据入口；
>    - DEMO_VERIFICATION.md 补全版本/hash、Proxy 零落库、Suspended、rejection-demo 的完整步骤；
>    - 明确 Organizer debug 与 ARY debug 的泄露边界；
> 3. 不推倒现有实现，只在现有 FastAPI 双 app 上增强；
> 4. 输出一个 P8_IMPLEMENTATION_CHECKLIST.md，作为后续实际修改代码和 Demo 的执行清单。

<details><summary>10 previous messages</summary>

> 我会先核对现有双 FastAPI app 和 Demo 验收文档，而不是重写实现。重点看实际已有 endpoint、存储边界、版本/hash 逻辑、debug 证据入口和 `DEMO_VERIFICATION.md` 覆盖情况，然后新增一个 P8 执行清单文档。
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `Select-String -Path C:\Users\Administrator\.codex\memories\MEMORY.md -Pattern 'ARY','P8','P9','PoC','DEMO_VERIFICATION' | Select-Object Path,LineNumber,Line`
> - Ran `Get-Content -Raw -Encoding UTF8 group_ARY_week1\DEMO_VERIFICATION.md`
> - Ran `rg -n "@.*\.(get|post)|def |ary_public_.*store|local_organizer_db|parse_projection_version|projection_hash|rejection-demo|privacy-check|debug/ary-store|debug/organizer-store|Suspended|No save|No commit|ary_registration_store" group_ARY_week1\ary_grs_001_poc.py`
> - Ran `rg -n "P8|P9|version/hash|Evidence|Dashboard|DEMO_VERIFICATION|Proxy 零落库|Suspended|rejection-demo|debug" docs group_ARY_week1\README.md`
>
> </details>
>
> 现有代码已经有不少 P9 能力：双 app、public stores、Proxy、privacy-check、rejection-demo、Suspended、版本/hash 判断都在。明显缺口是“可复跑脚本化验证”和“统一证据入口”还不够完整，`DEMO_VERIFICATION.md` 也没有把版本/hash 和 debug 泄露边界写成可执行步骤。
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `Get-Content -Encoding UTF8 group_ARY_week1\ary_grs_001_poc.py | Select-Object -Skip 430 -First 60`
> - Ran `Get-Content -Encoding UTF8 group_ARY_week1\ary_grs_001_poc.py | Select-Object -Skip 900 -First 95`
> - Ran `Get-Content -Encoding UTF8 group_ARY_week1\ary_grs_001_poc.py | Select-Object -Skip 980 -First 120`
> - Ran `Get-Content -Encoding UTF8 group_ARY_week1\ary_grs_001_poc.py | Select-Object -Skip 620 -First 55`
>
> </details>
>
> 我会把 P8 清单放在 `docs/03_review/P8_IMPLEMENTATION_CHECKLIST.md`，因为它是实现前检查与增强计划，不是代码或提交说明。内容会明确“已覆盖、缺口、增强任务、验收步骤”，并约束只在现有双 app 上增量增强。
>
> <details><summary>Created 1 file</summary>
>
> - Wrote `./docs/03_review/P8_IMPLEMENTATION_CHECKLIST.md` (+155 -0)
>
> </details>
>
> `P8_IMPLEMENTATION_CHECKLIST.md` 已新增。现在我做最后一次核对，确认它包含你点名的四类缺口，并且没有提出推倒现有实现的方案。
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `rg -n "Projection version/hash|Evidence Dashboard|DEMO_VERIFICATION|Proxy 零落库|Suspended|rejection-demo|Organizer debug|ARY debug|不推倒|双 FastAPI|P9 验收项" docs\03_review\P8_IMPLEMENTATION_CHECKLIST.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\03_review\P8_IMPLEMENTATION_CHECKLIST.md`
>
> </details>
>
> 已完成 P8 检查与增强计划，新增文件：
>
> [docs/03_review/P8_IMPLEMENTATION_CHECKLIST.md](./docs/03_review/P8_IMPLEMENTATION_CHECKLIST.md)
>
> 内容覆盖了你要求的四点：
>
> - 确认现有代码已覆盖的 P9 项：Organizer Server、ARY public stores、Registration Proxy、Public Page、Suspended、privacy/rejection/debug endpoints。
> - 列出缺口：version/hash 可复跑验证、统一 Evidence Dashboard、`DEMO_VERIFICATION.md` 补全、Organizer debug 与 ARY debug 泄露边界。
> - 明确不推倒现有实现：只在现有 `organizer_app` / `ary_app` 双 FastAPI app 上增量增强。
> - 给出后续代码和 Demo 修改清单：新增 `/debug/evidence-dashboard`、补 version/hash demo、强化 Proxy 零落库、补全 Suspended / rejection-demo / debug boundary 步骤。
>
> 本轮未改代码，也未改 `DEMO_VERIFICATION.md`，只完成 P8 检查与后续执行清单。
>
> <details><summary>Plan</summary>
>
> - [x] 核对现有 FastAPI PoC 覆盖的 P9 验收项
> - [x] 识别 P8 缺口与增强边界
> - [x] 新增 P8_IMPLEMENTATION_CHECKLIST.md
> - [x] 复核文档内容与后续执行清单
>
> </details>
</details>

已完成 P8 检查与增强计划，新增文件：

[docs/03_review/P8_IMPLEMENTATION_CHECKLIST.md](./docs/03_review/P8_IMPLEMENTATION_CHECKLIST.md)

内容覆盖了你要求的四点：

- 确认现有代码已覆盖的 P9 项：Organizer Server、ARY public stores、Registration Proxy、Public Page、Suspended、privacy/rejection/debug endpoints。
- 列出缺口：version/hash 可复跑验证、统一 Evidence Dashboard、`DEMO_VERIFICATION.md` 补全、Organizer debug 与 ARY debug 泄露边界。
- 明确不推倒现有实现：只在现有 `organizer_app` / `ary_app` 双 FastAPI app 上增量增强。
- 给出后续代码和 Demo 修改清单：新增 `/debug/evidence-dashboard`、补 version/hash demo、强化 Proxy 零落库、补全 Suspended / rejection-demo / debug boundary 步骤。

本轮未改代码，也未改 `DEMO_VERIFICATION.md`，只完成 P8 检查与后续执行清单。

> 进入 P9：启动服务，逐条跑验收，补页面和文档。

<details><summary>56 previous messages</summary>

> 我会按 P9 执行：先快速核对当前代码和运行环境，然后增量补现有双 FastAPI app 的证据入口与 version/hash 验证，再启动两个服务逐条跑验收，最后同步 `DEMO_VERIFICATION.md`。不会重写现有实现。
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `Select-String -Path C:\Users\Administrator\.codex\memories\MEMORY.md -Pattern 'ARY','P9','FastAPI','DEMO_VERIFICATION' | Select-Object Path,LineNumber,Line`
> - Ran `rg -n "evidence|projection-version|debug|explore|tailwind|demo_page" group_ARY_week1\ary_grs_001_poc.py group_ARY_week1\DEMO_VERIFICATION.md`
> - Ran `Get-Content -Encoding UTF8 group_ARY_week1\ary_grs_001_poc.py | Select-Object -First 120`
> - Ran `Get-Command python,uvicorn -ErrorAction SilentlyContinue | Select-Object Name,Source`
>
> </details>
>
> 我会补两个最小代码点：一个 JSON 统一证据入口，一个可打开的 Evidence Dashboard 页面；再加一个 version/hash 一键验证 endpoint。它们只聚合或验证已有公开数据，不改变主业务链路，也不把 Organizer 私有正文放进 ARY debug 输出。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `Get-Content -Encoding UTF8 group_ARY_week1\ary_grs_001_poc.py | Select-Object -Skip 520 -First 90`
>
> </details>
>
> 现在补代码。改动集中在 `group_ARY_week1/ary_grs_001_poc.py`：新增 Evidence Dashboard JSON/HTML 和 version/hash demo，不碰 Organizer 私有存储、Proxy 主流程或公开页的既有逻辑。
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./group_ARY_week1/ary_grs_001_poc.py` (+94 -10)
>
> </details>
>
> 我注意到私有字段存在性摘要需要递归检查嵌套 dict/list，避免漏掉 `private_score_basis` 这类嵌套字段；会先补这个小工具再继续加 endpoint。
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./group_ARY_week1/ary_grs_001_poc.py` (+9 -5)
>
> </details>
>
> 接下来加三个 endpoint：`/debug/evidence-dashboard` JSON、`/evidence-dashboard` HTML 页面、`/debug/projection-version-hash-demo` 一键验证。Version/hash demo 会使用独立的公开 demo race，不污染核心 `race_001` 验收状态。
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./group_ARY_week1/ary_grs_001_poc.py` (+256 -11)
>
> </details>
>
> 页面端我再加一个轻量入口链接，让公开页能直接跳到 Evidence Dashboard。保持现有样式和布局，不改业务展示。
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./group_ARY_week1/ary_grs_001_poc.py` (+7 -7)
>
> </details>
>
> 代码增强点已经补上。下一步先做语法检查，然后补 `DEMO_VERIFICATION.md`，把新增证据入口和 version/hash 验证写成可复跑步骤。
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `python -m py_compile group_ARY_week1\ary_grs_001_poc.py`
> - Ran `Get-Content -Raw -Encoding UTF8 group_ARY_week1\DEMO_VERIFICATION.md`
>
> </details>
>
> 语法检查通过。现在补全 `DEMO_VERIFICATION.md`，把新增 endpoint、Proxy 前后对比、Suspended 的 connectivity state、debug 可见边界都写进去，方便后续复跑。
>
> <details><summary>Created 1 file</summary>
>
> - Wrote `./group_ARY_week1/DEMO_VERIFICATION.md` (+259 -0)
>
> </details>
>
> 文档已补全。现在我会启动两个服务并按文档跑验收；如果 `uvicorn` 不在 PATH，就用 `python -m uvicorn`。若缺依赖，会先确认本机环境再处理。
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `python -m py_compile group_ARY_week1\ary_grs_001_poc.py`
> - Ran `python -c "import fastapi, uvicorn; print('fastapi', fastapi.__version__); print('uvicorn', uvicorn.__version__)"`
> - Ran `rg -n "evidence-dashboard|projection-version-hash-demo|Debug 边界|Proxy 零落库|Projection Version|Suspended Demo" group_ARY_week1\DEMO_VERIFICATION.md group_ARY_week1\ary_grs_001_poc.py`
>
> </details>
>
> 系统 Python 没装 FastAPI/uvicorn。先不联网安装，我会检查 Codex 工作区自带运行时，优先使用已有依赖来启动服务。
>
> 我找到 bundled Python。接下来用它检查 FastAPI/uvicorn；如果可用，就用这个 Python 启动两个服务。
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `& "C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -c "import fastapi, uvicorn; print('fastapi', fastapi.__version__); print('uvicorn', uvicorn.__version__)"`
> - Ran `netstat -ano | findstr ":9001"`
> - Ran `netstat -ano | findstr ":8000"`
>
> </details>
>
> 两个 Python 都缺 FastAPI/uvicorn，端口也空着。为了实际启动服务，需要在工作区建一个本地虚拟环境并安装 `fastapi`、`uvicorn`；我先尝试普通沙箱安装，若因为网络受限失败会按规则请求提升权限。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `python -m venv .venv`
>
> </details>
>
> 虚拟环境已创建在工作区。现在安装运行依赖。
>
> <details><summary>Approved 1 request, ran 2 commands</summary>
>
> - Ran `.\.venv\Scripts\python.exe -m pip install fastapi uvicorn`
>
> - Ran `.\.venv\Scripts\python.exe -m pip install fastapi uvicorn`
>
> Auto-review
>
> Status: approved
> Risk: medium
> Rationale: Installing FastAPI and Uvicorn into a project-local virtual environment is a bounded, reversible dependency setup step needed to run the user-requested PoC acceptance checks, and it does not export workspace data or secrets to an untrusted destination.
>
> </details>
>
> 依赖已装入工作区 `.venv`。我现在用这个虚拟环境启动 Organizer 和 ARY，并把日志写到 `group_ARY_week1/*.log`，便于验收失败时定位。
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `$p = Start-Process -FilePath "C:\Users\Administrator\Desktop\SE_experiment\ARY\.venv\Scripts\python.exe" -ArgumentList "-m uvicorn ary_grs_001_poc:organizer_app --host 127.0.0.1 --port 9001" -WorkingDirectory "C:\Users\Administrator\Desktop\SE_experiment\ARY\group_ARY_week1" -RedirectStandardOutput "C:\Users\Administrator\Desktop\SE_experiment\ARY\group_ARY_week1\organizer_server.log" -RedirectStandardError "C:\Users\Administrator\Desktop\SE_experiment\ARY\group_ARY_week1\organizer_server.err.log" -WindowStyle Hidden -PassThru; $p.Id`
> - Ran `$p = Start-Process -FilePath "C:\Users\Administrator\Desktop\SE_experiment\ARY\.venv\Scripts\python.exe" -ArgumentList "-m uvicorn ary_grs_001_poc:ary_app --host 127.0.0.1 --port 8000" -WorkingDirectory "C:\Users\Administrator\Desktop\SE_experiment\ARY\group_ARY_week1" -RedirectStandardOutput "C:\Users\Administrator\Desktop\SE_experiment\ARY\group_ARY_week1\ary_server.log" -RedirectStandardError "C:\Users\Administrator\Desktop\SE_experiment\ARY\group_ARY_week1\ary_server.err.log" -WindowStyle Hidden -PassThru; $p.Id`
>
> </details>
>
> `Start-Process` 被当前环境里的 `Path/PATH` 重复键绊住了。我会用 `-UseNewEnvironment` 重新启动，仍然隐藏窗口并写日志。
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `$p = Start-Process -FilePath "C:\Users\Administrator\Desktop\SE_experiment\ARY\.venv\Scripts\python.exe" -ArgumentList "-m uvicorn ary_grs_001_poc:organizer_app --host 127.0.0.1 --port 9001" -WorkingDirectory "C:\Users\Administrator\Desktop\SE_experiment\ARY\group_ARY_week1" -RedirectStandardOutput "C:\Users\Administrator\Desktop\SE_experiment\ARY\group_ARY_week1\organizer_server.log" -RedirectStandardError "C:\Users\Administrator\Desktop\SE_experiment\ARY\group_ARY_week1\organizer_server.err.log" -WindowStyle Hidden -UseNewEnvironment -PassThru; $p.Id`
> - Ran `$p = Start-Process -FilePath "C:\Users\Administrator\Desktop\SE_experiment\ARY\.venv\Scripts\python.exe" -ArgumentList "-m uvicorn ary_grs_001_poc:ary_app --host 127.0.0.1 --port 8000" -WorkingDirectory "C:\Users\Administrator\Desktop\SE_experiment\ARY\group_ARY_week1" -RedirectStandardOutput "C:\Users\Administrator\Desktop\SE_experiment\ARY\group_ARY_week1\ary_server.log" -RedirectStandardError "C:\Users\Administrator\Desktop\SE_experiment\ARY\group_ARY_week1\ary_server.err.log" -WindowStyle Hidden -UseNewEnvironment -PassThru; $p.Id`
>
> </details>
>
> PowerShell 的 `Start-Process` 在这个会话环境里仍然失败。改用 `cmd /c start /b` 后台启动，仍写日志到工作区。
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `cmd /c start "organizer" /b "C:\Users\Administrator\Desktop\SE_experiment\ARY\.venv\Scripts\python.exe" -m uvicorn ary_grs_001_poc:organizer_app --host 127.0.0.1 --port 9001 ^> organizer_server.log 2^> organizer_server.err.log`
> - Ran `cmd /c start "ary" /b "C:\Users\Administrator\Desktop\SE_experiment\ARY\.venv\Scripts\python.exe" -m uvicorn ary_grs_001_poc:ary_app --host 127.0.0.1 --port 8000 ^> ary_server.log 2^> ary_server.err.log`
>
> </details>
>
> `cmd /c start /b` 超时了，可能进程仍已启动或被当前 shell 挂住。我先检查端口和日志，再决定是否换成临时前台验收方式。
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `netstat -ano | findstr ":9001"`
> - Ran `Get-Content -Tail 20 -Encoding UTF8 group_ARY_week1\organizer_server.err.log`
> - Ran `netstat -ano | findstr ":8000"`
> - Ran `Get-Content -Tail 20 -Encoding UTF8 group_ARY_week1\ary_server.err.log`
>
> </details>
>
> 端口没起来，日志也空。现在用 Python 的 `subprocess.Popen` detached 模式启动两个服务，这比 PowerShell 启动器更可控，并继续写入同一组日志文件。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `.\.venv\Scripts\python.exe -c "import subprocess, os; root=r'C:\Users\Administrator\Desktop\SE_experiment\ARY\group_ARY_week1'; py=r'C:\Users\Administrator\Desktop\SE_experiment\ARY\.venv\Scripts\python.exe'; flags=0x00000008|0x00000200; specs=[('organizer',['-m','uvicorn','ary_grs_001_poc:organizer_app','--host','127.0.0.1','--port','9001']),('ary',['-m','uvicorn','ary_grs_001_poc:ary_app','--host','127.0.0.1','--port','8000'])]; pids=[]; [pids.append(subprocess.Popen([py]+args,cwd=root,stdout=open(os.path.join(root,name+'_server.log'),'ab'),stderr=open(os.path.join(root,name+'_server.err.log'),'ab'),creationflags=flags).pid) for name,args in specs]; print(pids)"`
>
> </details>
>
> 两个服务进程已启动。给它们几秒初始化后开始按验收接口逐条跑。
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `Start-Sleep -Seconds 2; netstat -ano | findstr ":9001"`
> - Ran `Start-Sleep -Seconds 2; netstat -ano | findstr ":8000"`
> - Ran `Start-Sleep -Seconds 2; Get-Content -Tail 20 -Encoding UTF8 group_ARY_week1\organizer_server.err.log`
> - Ran `Start-Sleep -Seconds 2; Get-Content -Tail 20 -Encoding UTF8 group_ARY_week1\ary_server.err.log`
>
> </details>
>
> 进程很快退出了，但 stderr 为空。我检查 stdout 日志和进程状态，定位启动失败原因。
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `Get-Content -Tail 50 -Encoding UTF8 group_ARY_week1\organizer_server.log`
> - Ran `Get-Content -Tail 50 -Encoding UTF8 group_ARY_week1\ary_server.log`
> - Ran `Get-Process -Id 23528,28996 -ErrorAction SilentlyContinue | Select-Object Id,ProcessName,HasExited`
> - Ran `.\.venv\Scripts\python.exe -m uvicorn --version`
>
> </details>
>
> `uvicorn` 本身可用。Detached 启动方式没有留下错误信息，我用短时间前台启动 Organizer 验证导入和绑定；如果能保持运行到超时，就说明服务可用，问题只在后台启动方式。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `.\.venv\Scripts\python.exe -m uvicorn ary_grs_001_poc:organizer_app --host 127.0.0.1 --port 9001`
>
> </details>
>
> 刚才前台命令在 `group_ARY_week1` 目录里用了相对 `.venv`，路径不对。改用绝对路径再试。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `"C:\Users\Administrator\Desktop\SE_experiment\ARY\.venv\Scripts\python.exe" -m uvicorn ary_grs_001_poc:organizer_app --host 127.0.0.1 --port 9001`
>
> </details>
>
> PowerShell 运行带空格/引号的可执行文件需要 `&` 调用符。继续用绝对路径验证。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `& "C:\Users\Administrator\Desktop\SE_experiment\ARY\.venv\Scripts\python.exe" -m uvicorn ary_grs_001_poc:organizer_app --host 127.0.0.1 --port 9001`
>
> </details>
>
> 前台启动能正常跑，说明代码和依赖没问题。后台失败是启动方式问题。我改用普通 `Popen` 后台子进程，不用 detached flags；这通常能在父进程退出后继续监听端口。
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `.\.venv\Scripts\python.exe -c "import subprocess, os; root=r'C:\Users\Administrator\Desktop\SE_experiment\ARY\group_ARY_week1'; py=r'C:\Users\Administrator\Desktop\SE_experiment\ARY\.venv\Scripts\python.exe'; specs=[('organizer',['-m','uvicorn','ary_grs_001_poc:organizer_app','--host','127.0.0.1','--port','9001']),('ary',['-m','uvicorn','ary_grs_001_poc:ary_app','--host','127.0.0.1','--port','8000'])]; pids=[]; [pids.append(subprocess.Popen([py]+args,cwd=root,stdin=subprocess.DEVNULL,stdout=open(os.path.join(root,name+'_server.log'),'ab'),stderr=open(os.path.join(root,name+'_server.err.log'),'ab'),close_fds=True).pid) for name,args in specs]; print(pids)"`
> - Ran `Start-Sleep -Seconds 2; netstat -ano | findstr ":9001"`
> - Ran `Start-Sleep -Seconds 2; netstat -ano | findstr ":8000"`
> - Ran `Start-Sleep -Seconds 2; Get-Content -Tail 20 -Encoding UTF8 group_ARY_week1\organizer_server.log`
> - Ran `Start-Sleep -Seconds 2; Get-Content -Tail 20 -Encoding UTF8 group_ARY_week1\ary_server.log`
>
> </details>
>
> 后台进程会被当前执行环境回收，所以我改用一个验收脚本在同一个进程生命周期里启动两个服务、逐条请求、执行 Suspended 场景，然后自动停止服务。这仍然是真实 HTTP 服务验收，不是直接调用函数。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `@'
> import json
> import subprocess
> import time
> import urllib.error
> import urllib.request
> from pathlib import Path
>
> ROOT = Path(r"C:\Users\Administrator\Desktop\SE_experiment\ARY")
> APP = ROOT / "group_ARY_week1"
> PY = ROOT / ".venv" / "Scripts" / "python.exe"
>
> procs = []
> results = []
>
>
> def request(method, url, payload=None, timeout=8):
>     data = None
>     headers = {}
>     if payload is not None:
>         data = json.dumps(payload).encode("utf-8")
>         headers["Content-Type"] = "application/json"
>     req = urllib.request.Request(url, data=data, method=method, headers=headers)
>     try:
>         with urllib.request.urlopen(req, timeout=timeout) as resp:
>             body = resp.read()
>             text = body.decode("utf-8", errors="replace")
>             content_type = resp.headers.get("content-type", "")
>             parsed = None
>             if "application/json" in content_type:
>                 parsed = json.loads(text)
>             return {"ok": True, "status": resp.status, "text": text, "json": parsed}
>     except urllib.error.HTTPError as exc:
>         text = exc.read().decode("utf-8", errors="replace")
>         parsed = None
>         try:
>             parsed = json.loads(text)
>         except json.JSONDecodeError:
>             pass
>         return {"ok": False, "status": exc.code, "text": text, "json": parsed}
>     except Exception as exc:
>         return {"ok": False, "status": None, "error": repr(exc), "text": "", "json": None}
>
>
> def wait_for(name, url, seconds=20):
>     deadline = time.time() + seconds
>     last = None
>     while time.time() < deadline:
>         last = request("GET", url, timeout=2)
>         if last["ok"]:
>             results.append({"step": f"wait_{name}", "passed": True, "status": last["status"]})
>             return True
>         time.sleep(0.5)
>     results.append({"step": f"wait_{name}", "passed": False, "last": last})
>     return False
>
>
> def record(step, passed, evidence=None):
>     results.append({"step": step, "passed": bool(passed), "evidence": evidence or {}})
>
>
> def start_service(name, app_ref, port):
>     log = APP / f"p9_{name}.log"
>     err = APP / f"p9_{name}.err.log"
>     p = subprocess.Popen(
>         [str(PY), "-m", "uvicorn", app_ref, "--host", "127.0.0.1", "--port", str(port)],
>         cwd=str(APP),
>         stdout=log.open("wb"),
>         stderr=err.open("wb"),
>     )
>     procs.append(p)
>     return p
>
> try:
>     organizer = start_service("organizer", "ary_grs_001_poc:organizer_app", 9001)
>     ary = start_service("ary", "ary_grs_001_poc:ary_app", 8000)
>
>     wait_for("organizer", "http://127.0.0.1:9001/health")
>     wait_for("ary", "http://127.0.0.1:8000/debug/privacy-check")
>
>     organizer_debug = request("GET", "http://127.0.0.1:9001/debug/organizer-store")
>     organizer_keys = sorted((organizer_debug["json"] or {}).get("local_organizer_db", {}).get("private_race_source", {}).keys())
>     record("organizer_debug_boundary", organizer_debug["ok"] and "private_submissions" in organizer_keys, {"private_source_keys_only_reported": organizer_keys})
>
>     disclose = request("POST", "http://127.0.0.1:9001/demo/disclose-to-ary")
>     dj = disclose["json"] or {}
>     record("journey_1_disclose_to_ary", disclose["ok"] and dj.get("organizer_private_source_still_local") is True, {"status": disclose["status"], "keys": sorted(dj.keys())})
>
>     demo = request("GET", "http://127.0.0.1:8000/debug/demo-journey")
>     demo_json = demo["json"] or {}
>     journey = demo_json.get("journey", {})
>     privacy = demo_json.get("ary_privacy_check", {})
>     record("journey_2_demo_journey", demo["ok"] and journey.get("organizer_holds_complete_race_source_facts") is True and journey.get("ary_metadata_exists") is True and journey.get("ary_projection_exists") is True and privacy.get("contains_core_private_source_facts") is False, {"journey": journey, "privacy": privacy})
>
>     ary_before = request("GET", "http://127.0.0.1:8000/debug/ary-store")
>     absent_before = set((ary_before["json"] or {}).get("explicitly_absent", []))
>     record("proxy_zero_persistence_before", {"ary_registration_store", "ary_rider_db", "ary_race_fact_db"}.issubset(absent_before), {"explicitly_absent": sorted(absent_before)})
>
>     registration = request("POST", "http://127.0.0.1:8000/proxy/race/001/register", {
>         "race_public_id": "race_001",
>         "rider_id": "rider_demo_001",
>         "client_request_id": "req_001",
>     })
>     reg_json = registration["json"] or {}
>     record("journey_3_registration_proxy", registration["ok"] and reg_json.get("ary_persistence") == "none" and reg_json.get("ary_registration_store") == "does_not_exist" and reg_json.get("result_from_organizer", {}).get("stored_in") == "local_organizer_db", {"response": reg_json})
>
>     ary_after = request("GET", "http://127.0.0.1:8000/debug/ary-store")
>     absent_after = set((ary_after["json"] or {}).get("explicitly_absent", []))
>     record("proxy_zero_persistence_after", {"ary_registration_store", "ary_rider_db", "ary_race_fact_db"}.issubset(absent_after), {"explicitly_absent": sorted(absent_after)})
>
>     public_page = request("GET", "http://127.0.0.1:8000/explore/race/001")
>     record("journey_4_public_page", public_page["ok"] and "RIDE AGENT" in public_page["text"] and "Evidence" in public_page["text"], {"status": public_page["status"], "contains_ride_agent": "RIDE AGENT" in public_page["text"], "contains_evidence_link": "Evidence" in public_page["text"]})
>
>     evidence_page = request("GET", "http://127.0.0.1:8000/evidence-dashboard")
>     record("evidence_dashboard_page", evidence_page["ok"] and "Evidence Dashboard" in evidence_page["text"] and "Values redacted" in evidence_page["text"], {"status": evidence_page["status"]})
>
>     privacy_check = request("GET", "http://127.0.0.1:8000/debug/privacy-check")
>     pc = privacy_check["json"] or {}
>     record("privacy_check", privacy_check["ok"] and pc.get("ary_public_stores_contain_core_private_source_facts") is False, {"forbidden_key_paths": pc.get("forbidden_key_paths"), "suspicious_value_paths": pc.get("suspicious_value_paths")})
>
>     rejection = request("GET", "http://127.0.0.1:8000/debug/rejection-demo")
>     rj = rejection["json"] or {}
>     record("rejection_demo", rejection["ok"] and rj.get("rejected") is True and rj.get("stored_in_ary") is False, {"response": rj})
>
>     version_hash = request("GET", "http://127.0.0.1:8000/debug/projection-version-hash-demo")
>     vh = version_hash["json"] or {}
>     cases = vh.get("cases", {})
>     vh_passed = all(cases.get(name, {}).get("passed") is True for name in ["older_version_rejected", "same_version_same_hash_idempotent", "same_version_different_hash_rejected", "newer_version_accepted"])
>     record("projection_version_hash_demo", version_hash["ok"] and vh_passed and vh.get("private_source_facts_used") is False, {"cases": {k: v.get("passed") for k, v in cases.items() if isinstance(v, dict)}, "current_projection_version": vh.get("current_projection_version")})
>
>     evidence = request("GET", "http://127.0.0.1:8000/debug/evidence-dashboard")
>     ev = evidence["json"] or {}
>     ev_privacy = ev.get("ary_privacy_check", {})
>     ev_proxy = ev.get("proxy_zero_persistence", {})
>     ev_private = ev.get("organizer_private_source_summary", {})
>     record("evidence_dashboard_json", evidence["ok"] and ev_privacy.get("ary_public_stores_contain_core_private_source_facts") is False and ev_proxy.get("ary_registration_store") == "absent" and ev_private.get("values_redacted") is True, {"privacy": ev_privacy, "proxy": ev_proxy, "private_values_redacted": ev_private.get("values_redacted")})
>
>     organizer.terminate()
>     try:
>         organizer.wait(timeout=5)
>     except subprocess.TimeoutExpired:
>         organizer.kill()
>         organizer.wait(timeout=5)
>     time.sleep(1.0)
>
>     suspended_page = request("GET", "http://127.0.0.1:8000/explore/race/001")
>     suspended_store = request("GET", "http://127.0.0.1:8000/debug/ary-store")
>     suspended_evidence = request("GET", "http://127.0.0.1:8000/debug/evidence-dashboard")
>     conn_store = (suspended_store["json"] or {}).get("ary_public_connectivity_state", {}).get("race_001", {})
>     conn_ev = (suspended_evidence["json"] or {}).get("connectivity", {}).get("race_001", {})
>     record("suspended_demo", suspended_page["ok"] and "Suspended" in suspended_page["text"] and conn_store.get("public_status") == "Suspended" and conn_ev.get("public_status") == "Suspended", {"page_contains_suspended": "Suspended" in suspended_page["text"], "store_connectivity": conn_store, "evidence_connectivity": conn_ev})
>
> finally:
>     for p in procs:
>         if p.poll() is None:
>             p.terminate()
>             try:
>                 p.wait(timeout=5)
>             except subprocess.TimeoutExpired:
>                 p.kill()
>
> summary = {"passed": all(item.get("passed") for item in results), "results": results}
> print(json.dumps(summary, ensure_ascii=False, indent=2))
> '@ | .\.venv\Scripts\python.exe -`
>
> </details>
>
> 验收脚本全部通过。因为我新增了 Evidence Dashboard 页面，还需要做一次本地页面打开/查看。服务在验收脚本结束时已清理，我会临时再启动一次用于浏览器检查。
>
> 验收全部通过。由于这个环境没有可用的 in-app Browser 控制工具，我用真实 HTTP 服务检查了公开页和 Evidence Dashboard 页面内容；页面返回 200，包含 `RIDE AGENT`、Evidence 链接和 Dashboard 文案。接下来写入 P9 验收报告并更新执行清单状态。
>
> <details><summary>Created 1 file, edited 1 file</summary>
>
> - Wrote `./docs/03_review/P8_IMPLEMENTATION_CHECKLIST.md` (+2 -2)
> - Wrote `./docs/03_review/P9_ACCEPTANCE_REPORT.md` (+60 -0)
>
> </details>
>
> P9 验收报告已写入。最后做一次轻量复核：语法检查、关键 endpoint/doc 关键字和验收报告是否齐全。
>
> <details><summary>Ran 7 commands</summary>
>
> - Ran `python -m py_compile group_ARY_week1\ary_grs_001_poc.py`
> - Ran `rg -n "evidence-dashboard|projection-version-hash-demo|P9 验收通过|Proxy 零落库|Debug 边界|Suspended" group_ARY_week1\ary_grs_001_poc.py group_ARY_week1\DEMO_VERIFICATION.md docs\03_review\P9_ACCEPTANCE_REPORT.md docs\03_review\P8_IMPLEMENTATION_CHECKLIST.md`
> - Ran `Get-ChildItem group_ARY_week1 -Filter "p9_*.log" | Select-Object Name,Length`
> - Ran `Get-Content -Tail 30 -Encoding UTF8 group_ARY_week1\p9_ary.err.log`
> - Ran `Get-Content -Tail 30 -Encoding UTF8 group_ARY_week1\p9_organizer.err.log`
> - Ran `netstat -ano | findstr ":9001"`
> - Ran `netstat -ano | findstr ":8000"`
>
> </details>
>
> P9 已完成：服务启动、逐条 HTTP 验收、页面增强和文档补全都做完了。
>
> 改动文件：
> - [ary_grs_001_poc.py](./group_ARY_week1/ary_grs_001_poc.py): 新增 `/debug/evidence-dashboard`、`/evidence-dashboard`、`/debug/projection-version-hash-demo`，并在公开页加 Evidence 入口。
> - [DEMO_VERIFICATION.md](./group_ARY_week1/DEMO_VERIFICATION.md): 补全 version/hash、Proxy 零落库、Suspended、rejection-demo、debug 边界和 Evidence Dashboard 验收步骤。
> - [P8_IMPLEMENTATION_CHECKLIST.md](./docs/03_review/P8_IMPLEMENTATION_CHECKLIST.md): 标记 P9 已完成。
> - [P9_ACCEPTANCE_REPORT.md](./docs/03_review/P9_ACCEPTANCE_REPORT.md): 新增实际验收报告。
>
> 验收结果：全部通过。覆盖 Organizer/ARY 服务启动、创建披露、Proxy 零落库、公开页、Evidence Dashboard、privacy-check、rejection-demo、projection version/hash、Suspended。服务是在验收脚本生命周期内启动并自动停止的；`.venv` 中已安装 `fastapi` 和 `uvicorn`，后续可按 `DEMO_VERIFICATION.md` 直接复跑。
>
> <details><summary>Plan</summary>
>
> - [ ] 核对运行环境与现有 PoC 入口
> - [ ] 增量补 Evidence Dashboard、version/hash demo 和页面入口
> - [ ] 补全 DEMO_VERIFICATION.md 验收步骤
> - [ ] 启动 Organizer 与 ARY 服务
> - [ ] 逐条运行 P9 验收并修正问题
> - [ ] 汇总验收结果与服务地址
>
> </details>
</details>

P9 已完成：服务启动、逐条 HTTP 验收、页面增强和文档补全都做完了。

改动文件：
- [ary_grs_001_poc.py](./group_ARY_week1/ary_grs_001_poc.py): 新增 `/debug/evidence-dashboard`、`/evidence-dashboard`、`/debug/projection-version-hash-demo`，并在公开页加 Evidence 入口。
- [DEMO_VERIFICATION.md](./group_ARY_week1/DEMO_VERIFICATION.md): 补全 version/hash、Proxy 零落库、Suspended、rejection-demo、debug 边界和 Evidence Dashboard 验收步骤。
- [P8_IMPLEMENTATION_CHECKLIST.md](./docs/03_review/P8_IMPLEMENTATION_CHECKLIST.md): 标记 P9 已完成。
- [P9_ACCEPTANCE_REPORT.md](./docs/03_review/P9_ACCEPTANCE_REPORT.md): 新增实际验收报告。

验收结果：全部通过。覆盖 Organizer/ARY 服务启动、创建披露、Proxy 零落库、公开页、Evidence Dashboard、privacy-check、rejection-demo、projection version/hash、Suspended。服务是在验收脚本生命周期内启动并自动停止的；`.venv` 中已安装 `fastapi` 和 `uvicorn`，后续可按 `DEMO_VERIFICATION.md` 直接复跑。

> 请执行最终提交整理：
>
> 1. 更新 PLAN.md：
>    - P7、P8、P9 标记为已完成；
>    - 新增 P10：最终提交整理与演示材料冻结。
>
> 2. 更新 group_ARY_week1/DEMO_VERIFICATION.md：
>    - 将最终验收清单同步为已通过，或明确引用 P9_ACCEPTANCE_REPORT.md 作为通过依据。
>
> 3. 更新 docs/02_design/decision_log.md：
>    - 增加 P9 相关决策，例如 Evidence Dashboard、projection version/hash demo、debug 边界、P9 验收通过。
>
> 4. 更新 docs/02_design/riding_record_draft.md：
>    - 补充 P8/P9 阶段：从文档对齐到实际 PoC/Demo 实现、验收、纠偏和最终结论。
>
> 5. 新建 docs/04_submission/final_poc_demo_summary.md：
>    - 当前最终方案是什么；
>    - PoC/Demo 实现了哪些能力；
>    - 如何证明 Public Yard / Private Race Source；
>    - 演示顺序；
>    - 已知边界与非目标；
>    - 最终验收结论。
>
> 6. 不要新增生产级功能，不要引入数据库、认证、加密、多 Race、多 Organizer。

<details><summary>17 previous messages</summary>

> 我会只做最终提交整理的文档更新，不再改 PoC 代码或引入新功能。先核对当前 P7/P8/P9 文档状态，再按你列的 6 项逐个落文件。
>
> <details><summary>Ran 6 commands</summary>
>
> - Ran `Select-String -Path C:\Users\Administrator\.codex\memories\MEMORY.md -Pattern 'ARY','P9','P10','final_poc_demo_summary' | Select-Object Path,LineNumber,Line`
> - Ran `Get-Content -Raw -Encoding UTF8 PLAN.md`
> - Ran `Get-Content -Raw -Encoding UTF8 group_ARY_week1\DEMO_VERIFICATION.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\02_design\decision_log.md`
> - Ran `Get-Content -Tail 90 -Encoding UTF8 docs\02_design\riding_record_draft.md`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\03_review\P9_ACCEPTANCE_REPORT.md`
>
> </details>
>
> 我已核对当前 P9 报告和验收文档。接下来会做纯文档提交整理：阶段状态、最终验收口径、决策记录、Riding Record 和最终摘要，不触碰 PoC 代码。
>
> 先更新 `PLAN.md` 和小组验收文档：把 P7/P8/P9 标成已完成，加入 P10；Demo 的最终清单改为已通过，并明确依据 P9 验收报告。
>
> <details><summary>Edited 2 files</summary>
>
> - Wrote `./PLAN.md` (+4 -3)
> - Wrote `./group_ARY_week1/DEMO_VERIFICATION.md` (+12 -10)
>
> </details>
>
> 阶段计划和 Demo 验收清单已同步。接下来更新决策日志，补齐 Evidence Dashboard、version/hash demo、debug 边界和 P9 验收通过这些 P9 决策。
>
> 现在更新 `decision_log.md` 和 Riding Record。Riding Record 会补 P8/P9 的实际过程和最终结论，但不会把它写成新增生产能力。
>
> <details><summary>Edited 2 files</summary>
>
> - Wrote `./docs/02_design/decision_log.md` (+6 -0)
> - Wrote `./docs/02_design/riding_record_draft.md` (+78 -0)
>
> </details>
>
> 决策日志和 Riding Record 已补 P8/P9/P10。接下来新增最终提交摘要，面向评审和演示使用，集中说明最终方案、能力、证明链路、演示顺序、边界和验收结论。
>
> 我会新建 `docs/04_submission/final_poc_demo_summary.md`。内容只总结当前最终方案和演示证据，不提出新的系统功能。
>
> <details><summary>Created 1 file</summary>
>
> - Wrote `./docs/04_submission/final_poc_demo_summary.md` (+155 -0)
>
> </details>
>
> 最终摘要已新增。最后做一致性复核：确认 P7/P8/P9/P10 状态、最终清单已勾选、P9 决策存在、摘要存在，并检查没有引入你禁止的生产级扩展措辞。
>
> 我会跑几条文本检查，确认提交整理文件互相引用正确，且没有把数据库、认证、加密、多 Race、多 Organizer 写成新增实现项。
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `rg -n "P7 \| 已完成|P8 \| 已完成|P9 \| 已完成|P10 \| 下一步" PLAN.md`
> - Ran `rg -n "P9_ACCEPTANCE_REPORT|\[x\]|Final Acceptance Conclusion" group_ARY_week1\DEMO_VERIFICATION.md`
> - Ran `rg -n "D-045|D-046|D-047|D-048|D-049|D-050" docs\02_design\decision_log.md`
> - Ran `rg -n "P8 实现检查|P9 实际 PoC|最终提交整理|不引入生产级数据库|不新增认证|不扩展多 Organizer" docs\02_design\riding_record_draft.md docs\04_submission\final_poc_demo_summary.md`
> - Ran `rg -n "引入生产级数据库|实现认证|实现.*加密|支持多 Race|支持多 Organizer|生产级功能" docs\04_submission\final_poc_demo_summary.md docs\02_design\riding_record_draft.md PLAN.md group_ARY_week1\DEMO_VERIFICATION.md`
>
> </details>
>
> 复核通过：状态、验收引用、决策、Riding Record 和最终摘要都已到位；生产级数据库/认证/加密/多 Race/多 Organizer 只作为非目标出现。
>
> 最终提交整理已完成。
>
> 更新内容：
> - [PLAN.md](./PLAN.md): P7/P8/P9 标记为已完成，新增 P10“最终提交整理与演示材料冻结”。
> - [DEMO_VERIFICATION.md](./group_ARY_week1/DEMO_VERIFICATION.md): 最终验收清单已勾选通过，并引用 [P9_ACCEPTANCE_REPORT.md](./docs/03_review/P9_ACCEPTANCE_REPORT.md) 作为依据。
> - [decision_log.md](./docs/02_design/decision_log.md): 新增 D-045 至 D-050，记录 Evidence Dashboard、version/hash demo、debug 边界、P9 验收通过和 P10 冻结决策。
> - [riding_record_draft.md](./docs/02_design/riding_record_draft.md): 补充 P8/P9 阶段过程、验收、纠偏与最终结论。
> - 新增 [final_poc_demo_summary.md](./docs/04_submission/final_poc_demo_summary.md): 汇总最终方案、PoC/Demo 能力、证明链路、演示顺序、边界与验收结论。
>
> 复核结果：没有新增生产级功能；数据库、认证、加密、多 Race、多 Organizer 只作为非目标出现。
>
> <details><summary>Plan</summary>
>
> - [x] 核对 PLAN、验收文档、决策日志和 Riding Record 当前状态
> - [x] 更新 PLAN 和 DEMO_VERIFICATION 最终验收口径
> - [x] 更新 decision_log 与 riding_record_draft
> - [x] 新增 final_poc_demo_summary.md
> - [x] 复核无生产级功能扩展和提交材料一致性
>
> </details>
</details>

最终提交整理已完成。

更新内容：
- [PLAN.md](./PLAN.md): P7/P8/P9 标记为已完成，新增 P10“最终提交整理与演示材料冻结”。
- [DEMO_VERIFICATION.md](./group_ARY_week1/DEMO_VERIFICATION.md): 最终验收清单已勾选通过，并引用 [P9_ACCEPTANCE_REPORT.md](./docs/03_review/P9_ACCEPTANCE_REPORT.md) 作为依据。
- [decision_log.md](./docs/02_design/decision_log.md): 新增 D-045 至 D-050，记录 Evidence Dashboard、version/hash demo、debug 边界、P9 验收通过和 P10 冻结决策。
- [riding_record_draft.md](./docs/02_design/riding_record_draft.md): 补充 P8/P9 阶段过程、验收、纠偏与最终结论。
- 新增 [final_poc_demo_summary.md](./docs/04_submission/final_poc_demo_summary.md): 汇总最终方案、PoC/Demo 能力、证明链路、演示顺序、边界与验收结论。

复核结果：没有新增生产级功能；数据库、认证、加密、多 Race、多 Organizer 只作为非目标出现。

> 清理缓存、日志和提交材料边界

<details><summary>13 previous messages</summary>

> 我会按保守口径处理：清理我在 P9 运行中产生的日志和 Python 缓存，不删除 `.venv`，因为它是复跑 PoC 所需的本地运行环境。提交材料边界我会写进最终提交摘要，明确哪些文件可提交、哪些只作本地运行/调试材料。
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `Get-ChildItem -Force group_ARY_week1 | Select-Object Name,Mode,Length,LastWriteTime`
> - Ran `Get-ChildItem -Recurse -Force -Directory | Where-Object { $_.Name -eq '__pycache__' -or $_.Name -eq '.pytest_cache' } | Select-Object FullName`
> - Ran `Get-ChildItem -Recurse -Force -File | Where-Object { $_.Name -match '\.log$|\.pyc$|\.pyo$' } | Select-Object FullName,Length`
> - Ran `Get-Content -Raw -Encoding UTF8 docs\04_submission\final_poc_demo_summary.md`
>
> </details>
>
> 盘点结果：需要清理的是 `group_ARY_week1` 下 P9 运行日志和 `__pycache__`；`.venv` 里也有大量依赖缓存，但它属于本地复跑环境，我不会删除。接下来先删除项目运行产物，再补提交边界说明。
>
> <details><summary>Approved 1 request, ran 1 command</summary>
>
> - Ran `$root = (Resolve-Path .).Path; $targets = @('group_ARY_week1\ary_server.err.log','group_ARY_week1\ary_server.log','group_ARY_week1\organizer_server.err.log','group_ARY_week1\organizer_server.log','group_ARY_week1\p9_ary.err.log','group_ARY_week1\p9_ary.log','group_ARY_week1\p9_organizer.err.log','group_ARY_week1\p9_organizer.log','group_ARY_week1\__pycache__'); foreach ($t in $targets) { $p = Join-Path $root $t; if (Test-Path -LiteralPath $p) { $rp = (Resolve-Path -LiteralPath $p).Path; if (-not $rp.StartsWith($root, [System.StringComparison]::OrdinalIgnoreCase)) { throw "Refusing to delete outside workspace: $rp" }; Remove-Item -LiteralPath $rp -Recurse -Force } }; "cleaned=$($targets.Count)"`
>
> Auto-review
>
> Status: approved
> Risk: low
> Rationale: Auto-review returned a low-risk allow decision.
>
> </details>
>
> 运行日志和项目级 `__pycache__` 已清理。现在我会补提交材料边界，明确哪些是交付材料、哪些是本地运行产物、哪些 debug 输出不得提交。
>
> 我会把边界写进最终提交摘要，并补一个 `.gitignore`，防止 `.venv`、日志、缓存这类本地运行产物混入后续提交。
>
> <details><summary>Created 1 file, edited 1 file</summary>
>
> - Wrote `./.gitignore` (+6 -0)
> - Wrote `./docs/04_submission/final_poc_demo_summary.md` (+33 -0)
>
> </details>
>
> 注意到 `group_ARY_week1` 自身有 `.git` 目录，所以根目录 `.gitignore` 不会约束它的内部仓库。我会再给 `group_ARY_week1` 增加同样的忽略规则，确保日志和缓存不会混入小组材料。
>
> <details><summary>Created 1 file</summary>
>
> - Wrote `./group_ARY_week1/.gitignore` (+5 -0)
>
> </details>
>
> `.gitignore` 已分别补在根目录和 `group_ARY_week1`。现在做最终复核：确认日志/缓存已清掉，提交边界说明存在，小组内部 git 状态不再包含运行日志。
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `Get-ChildItem -Force group_ARY_week1 | Select-Object Name,Mode,Length`
> - Ran `Get-ChildItem -Recurse -Force -File group_ARY_week1 | Where-Object { $_.Name -match '\.log$|\.pyc$|\.pyo$' } | Select-Object FullName,Length`
> - Ran `Get-ChildItem -Recurse -Force -Directory group_ARY_week1 | Where-Object { $_.Name -eq '__pycache__' -or $_.Name -eq '.pytest_cache' } | Select-Object FullName`
> - Ran `rg -n "提交材料边界|应提交材料|不应提交材料|Organizer debug|P9 验收结论" docs\04_submission\final_poc_demo_summary.md .gitignore group_ARY_week1\.gitignore`
> - Ran `git -C group_ARY_week1 status --short`
>
> </details>
>
> 已完成清理和边界整理。
>
> 清理内容：
> - 删除了 `group_ARY_week1` 下的运行日志：`*.log`。
> - 删除了 `group_ARY_week1/__pycache__`。
> - 保留 `.venv/`，因为它是复跑 PoC 所需的本地环境，不作为提交材料。
>
> 新增/更新：
> - 新增 [.gitignore](./.gitignore)
> - 新增 [group_ARY_week1/.gitignore](./group_ARY_week1/.gitignore)
> - 更新 [final_poc_demo_summary.md](./docs/04_submission/final_poc_demo_summary.md)，新增“提交材料边界”，明确应提交、不应提交、debug/证据边界。
>
> 复核结果：
> - `group_ARY_week1` 下已无 `*.log`、`*.pyc`、`__pycache__`。
> - 提交材料边界已明确：不提交 `.venv/`、缓存、日志、本地进程信息、Organizer debug 私有正文。
> - `git -C group_ARY_week1 status` 因 Windows ownership/safe.directory 限制未执行成功；我没有修改全局 git 配置。
>
> <details><summary>Plan</summary>
>
> - [x] 盘点缓存、日志和提交材料相关文件
> - [x] 清理可安全删除的运行日志与 Python 缓存
> - [x] 补充提交材料边界说明
> - [x] 复核清理结果与文档边界
>
> </details>
</details>

已完成清理和边界整理。

清理内容：
- 删除了 `group_ARY_week1` 下的运行日志：`*.log`。
- 删除了 `group_ARY_week1/__pycache__`。
- 保留 `.venv/`，因为它是复跑 PoC 所需的本地环境，不作为提交材料。

新增/更新：
- 新增 [.gitignore](./.gitignore)
- 新增 [group_ARY_week1/.gitignore](./group_ARY_week1/.gitignore)
- 更新 [final_poc_demo_summary.md](./docs/04_submission/final_poc_demo_summary.md)，新增“提交材料边界”，明确应提交、不应提交、debug/证据边界。

复核结果：
- `group_ARY_week1` 下已无 `*.log`、`*.pyc`、`__pycache__`。
- 提交材料边界已明确：不提交 `.venv/`、缓存、日志、本地进程信息、Organizer debug 私有正文。
- `git -C group_ARY_week1 status` 因 Windows ownership/safe.directory 限制未执行成功；我没有修改全局 git 配置。

> 将公开页中的主要展示文字修改为中文

<details><summary>46 previous messages</summary>

> Stream error
>
> Reconnecting 5/5
> stream disconnected before completion: 远程主机强迫关闭了一个现有的连接。 (os error 10054)
>
> 我会把 ARY 公开页的用户可见主文案改成中文，同时保留接口名、字段名和边界证明用的英文标识不动。会同步动态 FastAPI 页面和 `demo_page.html` 静态预览，避免两处展示不一致。
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `rg -n "Genesis Ride|Organizer-disclosed|Organizer-approved|Use the ARY|Public registration|Public participant|Projection Version|Last Update|Series Tags|Public Summary|Organizer Link|RIDE AGENT|Public Rider ID|Submit via ARY Proxy|Boundary|ARY renders|This Race follows|Overview|Public Logs|Insights|Evidence|Summary|Public Entry|Public Status|Public Registration Count|Public Participant Aliases|No public" group_ARY_week1\ary_grs_001_poc.py group_ARY_week1\demo_page.html`
> - Ran `Select-String -Path C:\Users\Administrator\.codex\memories\MEMORY.md -Pattern 'ARY','公开页','demo_page','ary_grs_001_poc' | Select-Object Path,LineNumber,Line`
>
> </details>
>
> 我找到两类文字：公开页数据源里的英文展示内容，以及 HTML 模板里的标签/按钮/边界说明。现在会同时改 `ary_grs_001_poc.py` 和静态 `demo_page.html`。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `Get-Content -Encoding UTF8 group_ARY_week1\ary_grs_001_poc.py | Select-Object -Skip 770 -First 45`
>
> </details>
>
> 我会顺手把状态和 section 标题也做中文映射，这样页面上不会继续显示 `Open`、`Public Entry` 这类英文主标题；底层 API 字段仍保持原样。
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./group_ARY_week1/ary_grs_001_poc.py` (+13 -13)
> - Wrote `./group_ARY_week1/ary_grs_001_poc.py` (+66 -41)
>
> </details>
>
> 动态页面已改成中文。接下来同步静态 `demo_page.html`，并把验收文档里对页面文案的描述从 `RIDE AGENT` 改为“报名代理”。
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./group_ARY_week1/demo_page.html` (+30 -30)
>
> </details>
>
> Context compaction
>
> Source: automatic
> Status: completed
>
> 我会继续把静态预览页也改成中文。刚才 `apply_patch` 无法读取它的原始编码，我会用 PowerShell 按系统默认编码读取并写回 UTF-8，只替换页面展示文字，不动功能逻辑。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `$path = 'group_ARY_week1\demo_page.html'
> $resolved = (Resolve-Path $path).Path
> $encoding = [System.Text.Encoding]::Default
> $text = [System.IO.File]::ReadAllText($resolved, $encoding)
> $replacements = [ordered]@{
>   'ARY GRS 001 Genesis Ride · ARY GRS 001' = 'ARY GRS 001 创世骑行 · ARY GRS 001'
>   'ARY GRS 001 Genesis Ride' = 'ARY GRS 001 创世骑行'
>   'Organizer-disclosed public race page.' = '由 Organizer 主动披露的公开赛事页面。'
>   'Organizer-approved public summary for ARY display.' = 'Organizer 批准披露、供 ARY 展示的公开摘要。'
>   'Use the ARY public entry button. Registration is proxied, then stored only by Organizer Server.' = '通过 ARY 公开入口发起报名；请求经 ARY 代理转发，报名事实只由 Organizer Server 保存。'
>   'Public registration is open while Organizer Server is reachable.' = 'Organizer Server 可达时，公开报名入口保持开放。'
>   'Public registration count disclosed by Organizer: 2.' = 'Organizer 主动披露的公开报名计数：2。'
>   'Public participant aliases: Neon Alpha, rider_demo_001' = '公开参与者昵称：Neon Alpha, rider_demo_001'
>   'Open disclosed link' = '打开披露链接'
>   'Overview' = '概览'
>   'Public Logs' = '公开记录'
>   'Insights' = '证据'
>   'Projection Version' = '投影版本'
>   'Last Update' = '最近更新'
>   'Series Tags' = '系列标签'
>   'Public Summary' = '公开摘要'
>   'Public Entry' = '公开报名入口'
>   'Public Status' = '公开状态'
>   'Public Registration Count' = '公开报名计数'
>   'Public Participant Aliases' = '公开参与者昵称'
>   'Organizer Link' = 'Organizer 连接状态'
>   'online' = '在线'
>   'RIDE AGENT' = '报名代理'
>   'Public Rider ID / nickname' = '公开 Rider ID / 昵称'
>   'Submit via ARY Proxy' = '通过 ARY Proxy 提交'
>   'Boundary' = '边界'
>   'ARY renders only Organizer-disclosed public metadata/projection. Complete Race Source Facts, DCR reasoning, rider code, logs, and review evidence stay outside ARY persistent storage.' = 'ARY 只展示 Organizer 主动披露的公开元数据与公开投影。完整 Race Source Facts、DCR 判断链、参赛者代码、日志和评审证据都不进入 ARY 持久化存储。'
>   'This Race follows decentralized data sovereignty. ARY is the public yard, not the source of truth.' = '本赛事遵循去中心化数据主权原则。ARY 是公开展示场，不是事实源。'
> }
> foreach ($entry in $replacements.GetEnumerator()) {
>   $text = $text.Replace($entry.Key, $entry.Value)
> }
> [System.IO.File]::WriteAllText($resolved, $text, [System.Text.UTF8Encoding]::new($false))
> Get-Item $path | Select-Object FullName,Length`
>
> </details>
>
> 静态页已完成编码转换和展示文案替换。接下来我会检查是否还有明显英文主文案残留，并同步更新依赖页面文字的验收说明。
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `rg -n "Genesis Ride|Organizer-disclosed|Organizer-approved|Use the ARY|Public registration|Public participant|Projection Version|Last Update|Series Tags|Public Summary|Organizer Link|RIDE AGENT|Public Rider ID|Submit via ARY Proxy|Boundary|ARY renders|This Race follows|Overview|Public Logs|Insights|Public Entry|Public Status|Public Registration Count|Public Participant Aliases" group_ARY_week1\ary_grs_001_poc.py group_ARY_week1\demo_page.html group_ARY_week1\DEMO_VERIFICATION.md docs\03_review\P9_ACCEPTANCE_REPORT.md`
> - Ran `rg -n "RIDE AGENT|报名代理|Public Rider ID|公开 Rider ID|Evidence|证据入口|explore/race" group_ARY_week1\DEMO_VERIFICATION.md docs\03_review\P9_ACCEPTANCE_REPORT.md`
> - Ran `Get-Content -Encoding UTF8 group_ARY_week1\demo_page.html | Select-Object -Skip 212 -First 26`
> - Ran `Get-Content -Encoding UTF8 group_ARY_week1\DEMO_VERIFICATION.md | Select-Object -Skip 136 -First 12`
> - Ran `Get-Content -Encoding UTF8 docs\03_review\P9_ACCEPTANCE_REPORT.md | Select-Object -Skip 36 -First 8`
>
> </details>
>
> 检查结果显示还剩静态页页脚/边界说明和两处验收文本引用了旧英文文案。我会把这些收口，避免后续验收脚本或人工检查仍按旧文案判断。
>
> <details><summary>Edited 3 files</summary>
>
> - Wrote `./docs/03_review/P9_ACCEPTANCE_REPORT.md` (+1 -1)
> - Wrote `./group_ARY_week1/DEMO_VERIFICATION.md` (+1 -1)
> - Wrote `./group_ARY_week1/demo_page.html` (+2 -2)
>
> </details>
>
> 页面和验收说明已经统一到中文主文案。现在我会跑静态检查和一个轻量服务检查，确认动态公开页返回的主要文字已经是中文且 Python 文件仍可编译。
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `rg -n "Genesis Ride|Organizer-disclosed|Organizer-approved|Use the ARY|Public registration|Public participant|Projection Version|Last Update|Series Tags|Public Summary|Organizer Link|RIDE AGENT|Public Rider ID|Submit via ARY Proxy|ARY renders|This Race follows|Overview|Public Logs|Insights|Public Entry|Public Status|Public Registration Count|Public Participant Aliases" group_ARY_week1\ary_grs_001_poc.py group_ARY_week1\demo_page.html group_ARY_week1\DEMO_VERIFICATION.md docs\03_review\P9_ACCEPTANCE_REPORT.md`
> - Ran `.\.venv\Scripts\python.exe -m py_compile group_ARY_week1\ary_grs_001_poc.py`
> - Ran `git diff -- group_ARY_week1\ary_grs_001_poc.py group_ARY_week1\demo_page.html group_ARY_week1\DEMO_VERIFICATION.md docs\03_review\P9_ACCEPTANCE_REPORT.md`
>
> </details>
>
> 静态检查只剩内部 JSON/debug 字段里的英文边界字符串，公开页面的主要可见文案已经清掉旧英文。`py_compile` 也通过了；我继续做一次本地 HTTP 页面检查。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `rg -n "if __name__|uvicorn|organizer_app|ary_app|FastAPI" group_ARY_week1\ary_grs_001_poc.py`
>
> </details>
>
> 为了避免依赖已存在的后台进程，我会用一个临时脚本启动 Organizer 和 ARY，再请求公开页并检查中文关键文案，脚本结束时会清理进程。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `@'
> import subprocess
> import sys
> import time
> import urllib.request
> import urllib.error
> from pathlib import Path
>
> root = Path.cwd()
> python = root / '.venv' / 'Scripts' / 'python.exe'
> workdir = root / 'group_ARY_week1'
> procs = []
>
> def start(args):
>     p = subprocess.Popen(
>         [str(python), '-m', 'uvicorn', *args],
>         cwd=str(workdir),
>         stdout=subprocess.PIPE,
>         stderr=subprocess.STDOUT,
>         text=True,
>     )
>     procs.append(p)
>     return p
>
> def wait_url(url, timeout=20):
>     deadline = time.time() + timeout
>     last_error = None
>     while time.time() < deadline:
>         try:
>             with urllib.request.urlopen(url, timeout=2) as response:
>                 return response.read().decode('utf-8', errors='replace')
>         except Exception as exc:
>             last_error = exc
>             time.sleep(0.5)
>     raise RuntimeError(f'timeout waiting for {url}: {last_error}')
>
> try:
>     start(['ary_grs_001_poc:organizer_app', '--host', '127.0.0.1', '--port', '9001'])
>     start(['ary_grs_001_poc:ary_app', '--host', '127.0.0.1', '--port', '8000'])
>     wait_url('http://127.0.0.1:9001/health')
>     page = wait_url('http://127.0.0.1:8000/explore/race/001')
>     expected = ['ARY GRS 001 创世骑行', '公开摘要', '投影版本', '最近更新', '报名代理', '公开 Rider ID / 昵称', '边界', '证据']
>     missing = [item for item in expected if item not in page]
>     if missing:
>         raise AssertionError('missing public page text: ' + ', '.join(missing))
>     forbidden = ['RIDE AGENT', 'Projection Version', 'Last Update', 'Public Summary', 'Submit via ARY Proxy']
>     leaked = [item for item in forbidden if item in page]
>     if leaked:
>         raise AssertionError('old English public page text still present: ' + ', '.join(leaked))
>     static = (workdir / 'demo_page.html').read_text(encoding='utf-8')
>     static_missing = [item for item in expected if item not in static]
>     if static_missing:
>         raise AssertionError('missing static page text: ' + ', '.join(static_missing))
>     print('public page Chinese text check passed')
> finally:
>     for p in procs:
>         if p.poll() is None:
>             p.terminate()
>     for p in procs:
>         try:
>             p.wait(timeout=5)
>         except subprocess.TimeoutExpired:
>             p.kill()
> '@ | .\.venv\Scripts\python.exe -`
>
> </details>
>
> 第一次 HTTP 检查失败是测试脚本里的中文字符串被 PowerShell 管道编码成了问号，不是页面断言本身。我要用 Unicode 转义重跑同一项检查，避免控制台编码影响。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `@'
> import subprocess
> import time
> import urllib.request
> from pathlib import Path
>
> root = Path.cwd()
> python = root / '.venv' / 'Scripts' / 'python.exe'
> workdir = root / 'group_ARY_week1'
> procs = []
>
> def start(args):
>     p = subprocess.Popen(
>         [str(python), '-m', 'uvicorn', *args],
>         cwd=str(workdir),
>         stdout=subprocess.PIPE,
>         stderr=subprocess.STDOUT,
>         text=True,
>     )
>     procs.append(p)
>     return p
>
> def wait_url(url, timeout=20):
>     deadline = time.time() + timeout
>     last_error = None
>     while time.time() < deadline:
>         try:
>             with urllib.request.urlopen(url, timeout=2) as response:
>                 return response.read().decode('utf-8', errors='replace')
>         except Exception as exc:
>             last_error = exc
>             time.sleep(0.5)
>     raise RuntimeError(f'timeout waiting for {url}: {last_error}')
>
> try:
>     start(['ary_grs_001_poc:organizer_app', '--host', '127.0.0.1', '--port', '9001'])
>     start(['ary_grs_001_poc:ary_app', '--host', '127.0.0.1', '--port', '8000'])
>     wait_url('http://127.0.0.1:9001/health')
>     page = wait_url('http://127.0.0.1:8000/explore/race/001')
>     expected = [
>         'ARY GRS 001 \u521b\u4e16\u9a91\u884c',
>         '\u516c\u5f00\u6458\u8981',
>         '\u6295\u5f71\u7248\u672c',
>         '\u6700\u8fd1\u66f4\u65b0',
>         '\u62a5\u540d\u4ee3\u7406',
>         '\u516c\u5f00 Rider ID / \u6635\u79f0',
>         '\u8fb9\u754c',
>         '\u8bc1\u636e',
>     ]
>     missing = [item for item in expected if item not in page]
>     if missing:
>         raise AssertionError('missing public page text: ' + repr(missing))
>     forbidden = ['RIDE AGENT', 'Projection Version', 'Last Update', 'Public Summary', 'Submit via ARY Proxy']
>     leaked = [item for item in forbidden if item in page]
>     if leaked:
>         raise AssertionError('old English public page text still present: ' + repr(leaked))
>     static = (workdir / 'demo_page.html').read_text(encoding='utf-8')
>     static_missing = [item for item in expected if item not in static]
>     if static_missing:
>         raise AssertionError('missing static page text: ' + repr(static_missing))
>     print('public page Chinese text check passed')
> finally:
>     for p in procs:
>         if p.poll() is None:
>             p.terminate()
>     for p in procs:
>         try:
>             p.wait(timeout=5)
>         except subprocess.TimeoutExpired:
>             p.kill()
> '@ | .\.venv\Scripts\python.exe -`
>
> </details>
>
> 第二次检查说明请求到的服务状态不是预期公开页内容，很可能端口上已有旧进程或当前内存未披露 Race。现在我会先看实际返回片段，再决定是否调用披露接口后复测。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `@'
> import subprocess
> import time
> import urllib.request
> from pathlib import Path
>
> root = Path.cwd()
> python = root / '.venv' / 'Scripts' / 'python.exe'
> workdir = root / 'group_ARY_week1'
> procs = []
>
> def start(args):
>     p = subprocess.Popen([str(python), '-m', 'uvicorn', *args], cwd=str(workdir), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
>     procs.append(p)
>     return p
>
> def wait_url(url, timeout=8):
>     deadline = time.time() + timeout
>     last_error = None
>     while time.time() < deadline:
>         try:
>             with urllib.request.urlopen(url, timeout=2) as response:
>                 return response.read().decode('utf-8', errors='replace')
>         except Exception as exc:
>             last_error = exc
>             time.sleep(0.5)
>     raise RuntimeError(f'timeout waiting for {url}: {last_error}')
>
> try:
>     start(['ary_grs_001_poc:organizer_app', '--host', '127.0.0.1', '--port', '9001'])
>     start(['ary_grs_001_poc:ary_app', '--host', '127.0.0.1', '--port', '8000'])
>     time.sleep(1)
>     for p in procs:
>         if p.poll() is not None:
>             print('process exited')
>             print((p.stdout.read() if p.stdout else '')[:800])
>     page = wait_url('http://127.0.0.1:8000/explore/race/001')
>     print(page[:1200].encode('unicode_escape').decode())
> finally:
>     for p in procs:
>         if p.poll() is None:
>             p.terminate()
>     for p in procs:
>         try:
>             p.wait(timeout=5)
>         except subprocess.TimeoutExpired:
>             p.kill()
> '@ | .\.venv\Scripts\python.exe -`
>
> </details>
>
> 端口 8000/9001 上已有服务，所以刚才请求命中了旧进程，不能作为本次变更依据。我会改用 FastAPI `TestClient` 直接加载当前文件做页面断言，这样验证的是工作区里的最新代码。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `@'
> from pathlib import Path
> from fastapi.testclient import TestClient
> import ary_grs_001_poc
>
> client = TestClient(ary_grs_001_poc.ary_app)
> response = client.get('/explore/race/001')
> assert response.status_code == 200, response.status_code
> page = response.text
> expected = [
>     'ARY GRS 001 \u521b\u4e16\u9a91\u884c',
>     '\u516c\u5f00\u6458\u8981',
>     '\u6295\u5f71\u7248\u672c',
>     '\u6700\u8fd1\u66f4\u65b0',
>     '\u62a5\u540d\u4ee3\u7406',
>     '\u516c\u5f00 Rider ID / \u6635\u79f0',
>     '\u8fb9\u754c',
>     '\u8bc1\u636e',
> ]
> missing = [item for item in expected if item not in page]
> if missing:
>     raise AssertionError('missing public page text: ' + repr(missing))
> forbidden = ['RIDE AGENT', 'Projection Version', 'Last Update', 'Public Summary', 'Submit via ARY Proxy']
> leaked = [item for item in forbidden if item in page]
> if leaked:
>     raise AssertionError('old English public page text still present: ' + repr(leaked))
> static = Path('demo_page.html').read_text(encoding='utf-8')
> static_missing = [item for item in expected if item not in static]
> if static_missing:
>     raise AssertionError('missing static page text: ' + repr(static_missing))
> print('current-code public page Chinese text check passed')
> '@ | ..\.venv\Scripts\python.exe -`
>
> </details>
>
> `TestClient` 需要缺失的 `httpx/httpx2`，我不安装新依赖。公开页函数本身是无参 FastAPI handler，我会直接在进程内调用 handler，验证返回 HTML 内容。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `@'
> import asyncio
> from pathlib import Path
> import ary_grs_001_poc
>
> result = asyncio.run(ary_grs_001_poc.explore_race_001())
> body = result.body.decode('utf-8') if hasattr(result, 'body') else str(result)
> expected = [
>     'ARY GRS 001 \u521b\u4e16\u9a91\u884c',
>     '\u516c\u5f00\u6458\u8981',
>     '\u6295\u5f71\u7248\u672c',
>     '\u6700\u8fd1\u66f4\u65b0',
>     '\u62a5\u540d\u4ee3\u7406',
>     '\u516c\u5f00 Rider ID / \u6635\u79f0',
>     '\u8fb9\u754c',
>     '\u8bc1\u636e',
> ]
> missing = [item for item in expected if item not in body]
> if missing:
>     raise AssertionError('missing public page text: ' + repr(missing))
> forbidden = ['RIDE AGENT', 'Projection Version', 'Last Update', 'Public Summary', 'Submit via ARY Proxy']
> leaked = [item for item in forbidden if item in body]
> if leaked:
>     raise AssertionError('old English public page text still present: ' + repr(leaked))
> static = Path('demo_page.html').read_text(encoding='utf-8')
> static_missing = [item for item in expected if item not in static]
> if static_missing:
>     raise AssertionError('missing static page text: ' + repr(static_missing))
> print('current-code public page Chinese text check passed')
> '@ | ..\.venv\Scripts\python.exe -`
>
> </details>
>
> handler 是同步返回 `HTMLResponse`，我会去掉 coroutine 包装后再跑同一个断言。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `@'
> from pathlib import Path
> import ary_grs_001_poc
>
> result = ary_grs_001_poc.explore_race_001()
> body = result.body.decode('utf-8') if hasattr(result, 'body') else str(result)
> expected = [
>     'ARY GRS 001 \u521b\u4e16\u9a91\u884c',
>     '\u516c\u5f00\u6458\u8981',
>     '\u6295\u5f71\u7248\u672c',
>     '\u6700\u8fd1\u66f4\u65b0',
>     '\u62a5\u540d\u4ee3\u7406',
>     '\u516c\u5f00 Rider ID / \u6635\u79f0',
>     '\u8fb9\u754c',
>     '\u8bc1\u636e',
> ]
> missing = [item for item in expected if item not in body]
> if missing:
>     raise AssertionError('missing public page text: ' + repr(missing))
> forbidden = ['RIDE AGENT', 'Projection Version', 'Last Update', 'Public Summary', 'Submit via ARY Proxy']
> leaked = [item for item in forbidden if item in body]
> if leaked:
>     raise AssertionError('old English public page text still present: ' + repr(leaked))
> static = Path('demo_page.html').read_text(encoding='utf-8')
> static_missing = [item for item in expected if item not in static]
> if static_missing:
>     raise AssertionError('missing static page text: ' + repr(static_missing))
> print('current-code public page Chinese text check passed')
> '@ | ..\.venv\Scripts\python.exe -`
>
> </details>
>
> 当前代码路径的公开页断言已通过，动态页和静态页都包含中文主文案，也没有检测到几处旧英文主标签。最后我看一眼变更文件列表，确保没有额外文件被误改。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `git status --short`
>
> </details>
>
> `git status` 显示当前目录没有可用 Git 仓库，所以我无法用 Git 汇总差异；我会用文件级检查收尾。
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `Get-ChildItem -Force | Select-Object Name,Mode,Length`
> - Ran `Select-String -Path group_ARY_week1\ary_grs_001_poc.py,group_ARY_week1\demo_page.html,group_ARY_week1\DEMO_VERIFICATION.md,docs\03_review\P9_ACCEPTANCE_REPORT.md -Pattern '报名代理','公开摘要','投影版本','最近更新','ARY GRS 001 创世骑行' | Select-Object Path,LineNumber,Line`
>
> </details>
>
> 文件级检查确认中文文案已落在动态页、静态页和验收说明中。还有一个非展示但相关的细节：公开页 HTML 语言标记仍是 `en`，我会顺手改为 `zh-CN`，这属于页面中文化的直接配套。
>
> <details><summary>Edited 4 files, ran 2 commands</summary>
>
> - Wrote `./group_ARY_week1/ary_grs_001_poc.py` (+2 -2)
> - Wrote `./group_ARY_week1/demo_page.html` (+1 -1)
> - Ran `rg -n "<html lang" group_ARY_week1\ary_grs_001_poc.py group_ARY_week1\demo_page.html`
> - Ran `Get-Content -Encoding UTF8 group_ARY_week1\ary_grs_001_poc.py | Select-Object -Skip 724 -First 12`
> - Wrote `./group_ARY_week1/ary_grs_001_poc.py` (+1 -1)
> - Wrote `./group_ARY_week1/demo_page.html` (+1 -1)
>
> </details>
>
> `lang` 标记已改到公开页和静态页。现在重跑编译和中文断言作为最终验证。
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `rg -n "<html lang|RIDE AGENT|Projection Version|Last Update|Public Summary|Submit via ARY Proxy|ARY GRS 001 创世骑行|报名代理" group_ARY_week1\ary_grs_001_poc.py group_ARY_week1\demo_page.html group_ARY_week1\DEMO_VERIFICATION.md docs\03_review\P9_ACCEPTANCE_REPORT.md`
> - Ran `.\.venv\Scripts\python.exe -m py_compile group_ARY_week1\ary_grs_001_poc.py`
>
> </details>
>
> 检查发现我刚才把 `zh-CN` 改到了 Evidence Dashboard 模板，公开页模板仍是 `en`。我会修正这个定位问题：公开页改为 `zh-CN`，Evidence Dashboard 保持原样。
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `Get-Content -Encoding UTF8 group_ARY_week1\ary_grs_001_poc.py | Select-Object -Skip 1371 -First 10`
> - Ran `Get-Content -Encoding UTF8 group_ARY_week1\ary_grs_001_poc.py | Select-Object -Skip 834 -First 10`
>
> </details>
>
> 我已确认两个模板位置，下面只做这两行修正。
>
> <details><summary>Edited 1 file, ran 2 commands</summary>
>
> - Wrote `./group_ARY_week1/ary_grs_001_poc.py` (+3 -3)
> - Ran `.\.venv\Scripts\python.exe -m py_compile group_ARY_week1\ary_grs_001_poc.py`
> - Ran `rg -n "<html lang|RIDE AGENT|Projection Version|Last Update|Public Summary|Submit via ARY Proxy|ARY GRS 001 创世骑行|报名代理" group_ARY_week1\ary_grs_001_poc.py group_ARY_week1\demo_page.html group_ARY_week1\DEMO_VERIFICATION.md docs\03_review\P9_ACCEPTANCE_REPORT.md`
>
> </details>
>
> 编译通过，公开页模板现在是 `zh-CN`，Evidence Dashboard 仍保持原语言标记。最后重跑当前代码的页面断言。
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `@'
> from pathlib import Path
> import ary_grs_001_poc
>
> result = ary_grs_001_poc.explore_race_001()
> body = result.body.decode('utf-8') if hasattr(result, 'body') else str(result)
> expected = [
>     '<html lang="zh-CN">',
>     'ARY GRS 001 \u521b\u4e16\u9a91\u884c',
>     '\u516c\u5f00\u6458\u8981',
>     '\u6295\u5f71\u7248\u672c',
>     '\u6700\u8fd1\u66f4\u65b0',
>     '\u62a5\u540d\u4ee3\u7406',
>     '\u516c\u5f00 Rider ID / \u6635\u79f0',
>     '\u8fb9\u754c',
>     '\u8bc1\u636e',
> ]
> missing = [item for item in expected if item not in body]
> if missing:
>     raise AssertionError('missing public page text: ' + repr(missing))
> forbidden = ['RIDE AGENT', 'Projection Version', 'Last Update', 'Public Summary', 'Submit via ARY Proxy']
> leaked = [item for item in forbidden if item in body]
> if leaked:
>     raise AssertionError('old English public page text still present: ' + repr(leaked))
> static = Path('demo_page.html').read_text(encoding='utf-8')
> static_missing = [item for item in expected if item not in static]
> if static_missing:
>     raise AssertionError('missing static page text: ' + repr(static_missing))
> print('current-code public page Chinese text check passed')
> '@ | ..\.venv\Scripts\python.exe -`
>
> </details>
</details>

已完成公开页主要展示文字中文化。

改动范围：
- [ary_grs_001_poc.py](./group_ARY_week1/ary_grs_001_poc.py:250)：动态公开页的赛事标题、摘要、导航、状态、报名代理、边界说明等主文案改为中文，并将公开页 `lang` 改为 `zh-CN`。
- [demo_page.html](./group_ARY_week1/demo_page.html:2)：静态公开页同步中文化；该文件原编码无法被 `apply_patch` 读取，已转换为 UTF-8。
- [DEMO_VERIFICATION.md](./group_ARY_week1/DEMO_VERIFICATION.md:142) 和 [P9_ACCEPTANCE_REPORT.md](./docs/03_review/P9_ACCEPTANCE_REPORT.md:41)：把验收描述中的旧 `RIDE AGENT` 文案同步为“报名代理”。

验证已跑：
- `python -m py_compile group_ARY_week1\ary_grs_001_poc.py` 通过。
- 直接调用当前代码的公开页 handler，确认动态页和静态页包含中文关键文案，并且不再包含旧的 `RIDE AGENT`、`Projection Version`、`Last Update`、`Public Summary`、`Submit via ARY Proxy`。
- 当前目录不是 Git 仓库，`git status` 无法使用。
