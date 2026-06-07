# ARY GRS 001 Agent Riding Record

## 1. Riding 目标

本次 Agent Riding 的目标，是围绕 ARY GRS 001 的核心命题，完成一套能够被产品定义、系统架构和 PoC 共同证明的方案：

> 在 Race 数据存留于 Organizer 侧、ARY 不持久化完整 Race 数据的前提下，ARY 仍然可以完成赛事的创建、披露、组织与展示。

我没有把 Agent 当成“一次性写稿工具”，而是把它当成工程协作者。我的主要任务是提出约束、判断方向、识别偏差、要求修正，并最终通过可运行 PoC 验证方案是否成立。

本记录中的对话片段是根据实际协作过程整理后的关键对话，重点呈现我如何引导 Agent 思考 Organizer 数据主权、公开投影、无状态代理和 PoC 验证。

---

## 2. Riding Plan

| 阶段 | 我的控制目标 | Agent 执行任务 | 验收方式 |
| --- | --- | --- | --- |
| 1. 明确核心命题 | 避免把 ARY 设计成中心化赛事平台 | 梳理 Organizer、ARY、Race、Public Projection 的关系 | 能说明完整 Race 数据为什么不进入 ARY |
| 2. 产品定义 | 把抽象命题转成可理解的产品场景 | 生成角色、用户旅程、功能边界和非目标 | 检查是否覆盖创建、披露、组织、展示 |
| 3. 架构与数据流 | 区分 Organizer Server、ARY Platform、Registration Proxy | 设计数据流、接口、状态和异常处理 | 检查 ARY 是否只保存公开数据和最小索引 |
| 4. 安全边界 | 找出隐性落库风险 | 补充代理日志、撤回、离线、缓存等风险 | 检查是否有 RiderID、报名事实或完整 Race 数据进入 ARY |
| 5. PoC 验证 | 不只写文档，要能运行证明 | 生成静态 Demo 和三服务真实 PoC | 跑通端到端链路和安全扫描 |
| 6. 展示优化 | 让评审知道每一步证明什么 | 增加页面说明、演示顺序和 README | 按演示路径检查是否讲得清楚 |

---

## 3. 关键对话与 Riding 过程

### 3.1 将任务从“写 PRD”校准为“证明数据主权”

**关键对话**

> 我：这次不能写成普通赛事管理平台。核心不是“ARY 怎么保存和管理所有 Race”，而是“Organizer 不交出完整 Race 数据，ARY 还能不能工作”。你先按这个约束重新定义产品边界。  
> Agent：明白。ARY 应该被定义为公开赛事对象的编排层，而不是 Race 原始数据仓库。完整 Race 数据留在 Organizer / DCR 侧，ARY 只处理 Organizer 主动披露的 Public Metadata 或 Public Projection。  
> 我：对。PRD 里要明确写出 ARY 做什么、不做什么。尤其是不能出现“上传完整规则、完整参赛者名单、完整成绩明细到 ARY”这种默认中心化设计。

**Riding 说明**

这一轮把任务从“生成一份 PRD”校准成“证明 Organizer 数据主权”。我要求 Agent 不要先堆功能，而是先回答：

- 完整 Race 数据包括什么；
- 哪些数据只属于 Organizer；
- 哪些数据可以被 ARY 保存；
- Public Metadata 和 Public Projection 如何区别；
- ARY 在创建、披露、组织、展示中到底承担什么角色。

最终形成的产品定位是：**ARY 是公共骑场，Organizer 掌握 Private Race Source，ARY 只展示被披露的数据与入口。**

---

### 3.2 拆分 Organizer 侧数据流

**关键对话**

> 我：只说“数据在 Organizer 侧”还不够，评审会问具体是什么数据、怎么流动、ARY 到底拿到了什么。你把 Organizer 侧数据流拆细。  
> Agent：可以拆成三层：完整 Race 数据、Public Metadata、Public Projection。完整 Race 数据包括规则、参与者、执行记录、成果和复盘；Public Metadata 是赛事公开身份；Public Projection 是 Organizer 主动从完整数据中生成的公开展示内容。  
> 我：还要强调投影不是原始数据。ARY 展示的内容必须来自 Organizer 处理后的投影，不能反向要求 Organizer 上传完整 Race 来校验。

**Riding 说明**

这一轮的结果，是把 Organizer 侧数据流明确成三层：

1. **完整 Race 数据**：完整规则、参赛者名单、执行记录、成果材料、评审依据、复盘材料，只在 Organizer / DCR 控制域。
2. **Public Metadata**：标题、公开简介、Organizer 公开身份、公开状态、时间窗口、标签和入口，可由 ARY 索引。
3. **Public Projection**：Organizer 主动生成的公开投影，例如公开规则摘要、公开进度状态、公开成果摘要，可由 ARY 展示。

这一步直接支撑最终版 PRD 中的原则：**投影优先于原始数据，公开披露最小化，可验证但不越权。**

---

### 3.3 识别 Registration Proxy 的隐性落库风险

**关键对话**

> 我：如果 Participant 从 ARY 页面报名，不能因为请求经过 ARY，就让 ARY 留下报名事实。这里很容易变成一个隐形的中心化报名数据库。  
> Agent：那可以设计成 Registration Proxy。ARY 只做请求形状校验、路由和错误归一化，报名事实写入 Organizer Server。  
> 我：还不够。要明确 Proxy 不能 `save()`、不能 `commit()`，不能存 RiderID、报名时间、报名状态。长期展示的报名计数也必须来自 Organizer 后续披露的 Public Projection。  
> Agent：我会把它写成“方案 B：前置代理与公开投影模式”，并在安全要求里加入代理零落库和日志最小化。

**Riding 说明**

这是本次 Riding 中最重要的人工干预之一。因为 Agent 很容易把“报名入口”自然写成平台表单，但这会破坏 ARY 的非持久化原则。

最终方案中，Participant 可以从 ARY 前端发起报名意图，但：

- 报名事实只写入 Organizer Server；
- ARY Stateless Proxy 不保存 RiderID；
- ARY 不保存报名状态、报名时间、资格校验结果；
- 报名成功后的长期展示数据必须由 Organizer 生成新的 Public Projection；
- Proxy 日志必须避免记录请求体、身份凭证和私密错误详情。

这一设计让 ARY 仍然可以提供公开入口，但不会变成报名数据库。

---

### 3.4 处理 Organizer 撤回与离线状态

**关键对话**

> 我：如果 Organizer 撤回投影，ARY 不能继续展示旧内容；如果 Organizer Server 离线，ARY 也不能推断赛事失败或报名失败。这个异常状态要单独设计。  
> Agent：可以区分 `Withdrawn` 和 `Suspended`。`Withdrawn` 表示 Organizer 主动撤回公开投影；`Suspended` 表示 Organizer 接入暂不可用。  
> 我：对，尤其是 Suspended 不能暗示 Organizer 内部 Race 事实。它只能说明公开接入暂时不可用，ARY 不能根据离线状态生成内部结论。

**Riding 说明**

这一轮解决的是异常状态下的数据边界。如果 Organizer 不可达，ARY 只能更新公开可达性状态，不能把它解释成：

- 赛事取消；
- 报名失败；
- Organizer 内部执行失败；
- 作品或评审状态异常。

因此最终版 PRD 增加了 Organizer 离线挂起数据流，并明确 `Suspended` 与 `Withdrawn` 的语义区别。

---

### 3.5 补充代理日志和可观测性风险

**关键对话**

> 我：即使 ARY 不写数据库，Web 访问日志、APM、错误追踪也可能记录 RiderID 或请求体。这个风险如果不写，评审可能会觉得我们只考虑了数据库，没有考虑真实系统。  
> Agent：我会在风险表里加入“代理日志泄露”，建议默认关闭请求体日志、RiderID 使用短期 token、日志字段白名单化。  
> 我：再补一个后续设计项，叫 Proxy Observability Policy，专门定义代理层允许记录什么、禁止记录什么。

**Riding 说明**

这一轮体现了对真实工程环境的考虑。数据安全不只发生在数据库，也可能发生在：

- HTTP access log；
- APM 采样；
- 错误追踪系统；
- 调试日志；
- 反向代理日志。

因此最终版 PRD 不仅写“ARY 不保存报名数据库”，还补充了代理日志泄露风险和 Proxy Observability Policy。

---

### 3.6 从静态 Demo 升级为三服务 PoC

**关键对话**

> 我：静态 Demo 能讲概念，但证明力不够。老师要看关键技术 PoC，我们最好让 Organizer、ARY、Team 真的作为不同服务运行，数据也真的放在不同目录。  
> Agent：可以做三服务 PoC：Organizer App、ARY Platform、Team Workspace。Organizer 保存完整 Race，ARY 只同步公开投影，Team 保存作品数据并只提交引用。  
> 我：对，而且要考虑 Organizer 不是技术人员，最好能双击启动。课堂上也可以一台电脑一个角色，演示数据流向和保存位置。

**Riding 说明**

这一轮把 PoC 从“展示型”升级成“验证型”。

最终生成的三服务 PoC：

```text
organizer-app   : http://localhost:4001
ary-platform    : http://localhost:4002
team-workspace  : http://localhost:4003
```

数据分别保存在不同服务目录：

- Organizer：`private_race_data.json`、`public_projection.json`、`grant.json`
- ARY：`ary_store.json`
- Team：`private_artifacts.json`、`submission_reference.json`、`showcase_summary.json`

这个结构能直接演示：完整 Race 数据和 Team 原始作品数据并不在 ARY Store 中。

---

### 3.7 要求端到端验收，而不是只看生成结果

**关键对话**

> 我：代码生成出来还不算完成。你要跑一遍关键链路，确认不是只有页面能打开。  
> Agent：我会检查三个服务语法，然后模拟 ARY 同步 Organizer 公开投影、Team 提交引用、Reviewer 访问控制、Coach 授权访问和安全扫描。  
> 我：验收结果要能对应老师评分点。尤其要证明未分配 Reviewer 访问会失败，敏感字段没有进入 ARY。

**Riding 说明**

最终端到端验证结果为：

```text
sync=True
sub=True
show=True
grant=True
reviewOk=True
reviewDenied=403
coach=True
scanFailures=0
```

对应含义：

- ARY 成功同步 Organizer 公开投影；
- Team 成功提交作品引用和公开摘要；
- Coach 授权访问成功；
- Reviewer 访问被分配作品成功；
- Reviewer 访问未分配作品被拒绝，返回 403；
- 安全扫描未发现敏感字段进入 ARY Store。

这一轮体现了 Riding 的验收环节：Agent 生成内容后，必须通过运行结果证明关键假设。

---

### 3.8 优化演示可理解性

**关键对话**

> 我：现在页面功能是有了，但评审第一次打开不一定知道先点哪里，也不知道每一步证明什么。Demo 要能被讲出来。  
> Agent：我会在 ARY Platform 增加推荐演示顺序，在 Organizer App 和 Team Workspace 增加操作说明。  
> 我：重点不是让页面更花，而是让评审能顺着“完整数据在哪里、公开投影怎么流动、ARY 保存了什么、敏感数据为什么搜不到”这条线看。

**Riding 说明**

最终三个页面都加入了演示引导：

- Organizer App：说明完整 Race 数据和 Public Projection 的区别；
- ARY Platform：说明推荐演示顺序；
- Team Workspace：说明提交引用、公开摘要、Coach 授权分别对应什么数据流。

这一步让 PoC 不只是可运行，也更适合课堂展示。

---

## 4. 人机分工说明

### 4.1 我的主要判断和干预

1. 明确 ARY 不能被设计成中心化 Race 数据库。
2. 要求完整 Race 数据、Public Metadata、Public Projection 分开定义。
3. 要求 Registration Proxy 保持无状态，避免报名事实落入 ARY。
4. 指出代理日志、错误追踪、缓存也可能造成隐性持久化风险。
5. 要求补充 Organizer 撤回和离线挂起状态。
6. 判断静态 Demo 证明力不足，要求升级为三服务真实 PoC。
7. 要求做端到端验证，而不是只相信生成代码。
8. 从评审视角检查页面是否容易演示，并要求增加操作说明。

### 4.2 Agent 主要完成的工作

1. 根据约束整理 PRD 结构和数据边界。
2. 补充用户旅程、数据流图、接口样例和安全要求。
3. 生成静态 PoC Demo。
4. 生成三服务真实 PoC，包括 Organizer App、ARY Platform 和 Team Workspace。
5. 编写启动脚本、JSON 数据样例、HTTP API 和页面。
6. 执行语法检查和端到端接口验证。
7. 根据反馈优化演示说明和 README。

---

## 5. 关键修正记录

| 问题 | 初始风险 | 我的干预 | 最终修正 |
| --- | --- | --- | --- |
| ARY 被设计成普通赛事平台 | 可能默认持有完整 Race 数据 | 要求区分 Public Metadata、Public Projection 和完整 Race 数据 | ARY 只做公开赛事对象编排层 |
| 报名入口导致事实落库 | RiderID 和报名状态可能进入 ARY | 要求 Registration Proxy 无状态 | 报名事实只写入 Organizer Server |
| 代理日志泄露 | 请求体、RiderID、错误信息可能被日志记录 | 要求补充 Proxy Observability Policy | 日志字段白名单化，避免记录私密请求体 |
| Organizer 离线语义不清 | ARY 可能推断赛事失败或取消 | 要求区分 Suspended / Withdrawn | 离线只表示公开接入暂不可用 |
| PoC 过于展示化 | 静态页面难以证明数据真的分离 | 要求三服务真实 PoC | Organizer、ARY、Team 分服务运行，各自持有数据 |
| Demo 不易讲解 | 页面能跑但评审不一定看懂 | 要求增加演示顺序 | 三个页面均加入操作说明 |

---

## 6. PoC 验证结果

最终 PoC 验证了以下核心结论：

1. Organizer 可以本地保存完整 Race 数据。
2. Organizer 可以生成 Public Projection，并通过授权接口披露给 ARY。
3. ARY 可以同步公开投影并生成公开展示页。
4. ARY Store 中不出现完整 Race brief、内部评分规则、手机号、邮箱或 secret notes。
5. Team 作品数据可以留在 Team 侧，ARY 只保存引用和公开摘要。
6. Reviewer 只能访问被分配的 submission，访问未分配 submission 返回 403。
7. Coach 只有在 Team 授权后才能访问指定指导材料。
8. Audit Log 能记录同步、提交、授权、拒绝访问和安全扫描。
9. 安全扫描结果 `scanFailures=0`，说明敏感字段没有进入 ARY 持久化数据。

---

## 7. 与最终版 PRD 的关系

本次 Riding 中探索过 Team / Rider、Reviewer、Coach、Auditor 等更完整的角色边界。这些探索帮助我确认了一个更一般的原则：

> 谁拥有数据主权，完整数据就应该留在谁的控制域；ARY 只处理公开披露、引用、授权和审计所需的最小数据。

团队最终版 PRD 做了合理收束，把 GRS 001 的主线聚焦在：

1. Organizer 持有完整 Race 数据。
2. ARY 只保存 Public Metadata / Public Projection。
3. Participant 报名可以经过 ARY Stateless Proxy，但报名事实只写入 Organizer Server。
4. DCR 或 Organizer 侧系统承载执行、评审、复盘等私有数据处理。
5. ARY 对 Organizer 离线、投影撤回、代理日志等情况保持最小化处理，不推断内部 Race 事实。

因此，Riding 过程中的扩展讨论不是偏题，而是帮助我们把最终版 PRD 的核心边界收得更稳。

---

## 8. 我的 Agent Riding Skill 复盘

这次协作里，我最大的收获是：Agent 很擅长快速生成结构，但它需要被持续约束在正确的问题上。

如果我只让 Agent 写“一个 ARY 比赛平台”，它很可能会自然生成中心化数据库、报名表、评审表、排行榜等传统平台功能。但 GRS 001 的关键恰恰是不能这么做。我的主要 Riding 动作就是不断把 Agent 拉回核心命题：

- 数据在哪里？
- 谁拥有数据主权？
- ARY 到底保存了什么？
- 哪些字段绝对不能进入 ARY？
- 如果 Organizer 撤回或离线，ARY 能不能继续展示？
- 如果报名经过 ARY，ARY 会不会在日志里留下报名事实？
- PoC 能不能实际证明，而不是只画图？

这次 Riding 不是让 Agent 多写，而是让我持续通过提问、约束、修正和验收，让 Agent 的产出逼近正确的产品边界。

---

## 9. 下一步改进

如果继续迭代，我会优先做三件事：

1. 把 Organizer App 做成更适合非技术 Organizer 的桌面启动包，让发起方不需要理解 Node.js 或端口。
2. 补充 Encrypted Registration Envelope，让 Participant 用 Organizer 公钥加密报名载荷，ARY Proxy 只转发密文。
3. 完善 Proxy Observability Policy，明确代理层允许记录哪些指标，禁止记录哪些字段。

---

## 10. 一句话总结

本次 Agent Riding 的核心不是让 Agent 替我写完作业，而是我持续用产品命题、数据边界和 PoC 验收牵引 Agent：让 ARY 从一个容易滑向中心化的平台方案，收束为一个尊重 Organizer 数据主权、只处理公开投影和无状态入口的可验证产品定义。

