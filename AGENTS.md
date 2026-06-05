你现在是一个面向智能体时代的资深产品经理与系统架构师。我们需要为 ARY GRS 001（智能体骑场创世骑行系列赛）编写一份产品定义与系统设计文档。

核心设计原则：
1. 明确去中心化数据主权：完整 Race 数据必须留存在 Organizer（赛事组织者）侧，ARY 绝对不做中心化的持久化存储。
2. 核心功能边界：ARY 仅通过 Organizer 主动披露的“公开元数据（Public Metadata）”或“公开投影（Public Projection）”，来实现赛事的【创建、披露、组织、展示】。
3. 排除范围：赛事的具体执行、指导骑行、成果评审和复盘不在本次设计范围内。

请帮我产出以下内容：
- 【产品定义】：详细描述在上述数据主权前提下，赛事的创建、披露、组织和展示的用户旅程与产品逻辑。
- 【系统设计】：清晰定义 Organizer、ARY（智能体骑场）、DCR（DevCompass Racing 执行核）以及公开投影（Public Projection）之间的关系和数据流向，并用 Markdown 表格或 Mermaid 架构图表示。

撰写POC:  

你现在是一名去中心化架构专家。请严格参考产品需求文档 `PRD-ARY-GRS-001.md`。

我们现在需要为 ARY GRS 001 实现一个关键技术 PoC，首先要定义组件之间的数据合约（Schema）。请严格遵守以下约束：
1. 完整 Race 数据（规则、具体参与者、执行明细）只能存在于 Organizer 控制域内。
2. ARY 侧的数据表/数据结构，绝对不允许包含任何完整 Race 数据的字段。

请为我设计并输出以下三个核心 JSON 数据结构，并对关键字段给出说明：
1. 【Organizer 内部事实库】：模拟存储在 Organizer 本地的完整 Race 数据结构（包含私密执行数据）。
2. 【Public Metadata Schema】：对应 PRD 第 9.1 节，提交给 ARY 的赛事基础公开元数据结构。
3. 【Public Projection Schema】：对应 PRD 第 9.2 节，由 Organizer 签名、处理后披露给 ARY 的公开投影结构。

在输出 JSON 之后，请从架构师的角度，用两句话向我解释：你是如何在数据结构设计上，确保 ARY 无法窥探到 Organizer 的私密数据的？


非常好，数据合约已对齐。现在请基于刚才的设计，使用 [Python 3.10+ / FastAPI] 编写一个最简、单文件可运行的 PoC 核心逻辑（你可以将所有逻辑写在一个文件或清晰的模块中）。

这个 PoC 必须完整模拟以下【用户旅程】（参考 `PRD-ARY-GRS-001.md` 第 6 节）：
1. 【模拟 Organizer 侧】：本地初始化一份完整的私密 Race 数据。
2. 【旅程一：创建公开对象】：Organizer 调用 ARY API 提交 `Public Metadata`，ARY 生成 `Race Public ID` 并持久化，返回成功。
3. 【旅程二：披露公开投影】：Organizer 本地运行一个函数，将私密 Race 数据脱敏并转换为 `Public Projection`，然后调用 ARY API 提交该投影。ARY 校验其版本并予以存储。
4. 【旅程四：展示公开页面】：提供一个 GET API（或简单的渲染函数），模拟 Viewer/Agent 访问 ARY，仅通过读取 ARY 存储的 Metadata 和 Projection，完整复现出赛事展示页。

代码要求：
- 不需要连接真实数据库，使用内存字典（In-memory dict）作为 Mock 存储即可。
- 代码必须包含清晰的 print 日志或注释，展示每一个动作发生时，数据到底在谁的手里。
- 严禁在 ARY 的存储字典中出现任何来自 Organizer 本地的事实库字段。

请直接输出完整、可运行的代码。