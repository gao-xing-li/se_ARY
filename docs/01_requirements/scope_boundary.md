# ARY GRS 001 范围与边界

## 范围内

- 定义数据主权、披露边界和四项 PoC 证明目标。
- 定义 Organizer、ARY、DCR、Public Metadata、Public Projection、Participant / Rider、Registration Proxy、Organizer Server 的职责与禁止事项。
- 设计创建、披露、组织、报名入口转发、展示的最小功能闭环。
- 设计 PoC 理论验证、系统架构与数据流、Demo 展示方案。
- 记录关键决策、Agent 协作过程与评审依据。

## 角色边界

| 角色 | 核心职责 | 可处理的数据 | 不得承担的职责 |
| --- | --- | --- | --- |
| Organizer | 拥有并留存完整 Race Source Facts；决定公开内容；主动披露 Public Metadata / Public Projection | 完整 Race Source Facts、Public Metadata、Public Projection | 不得把完整数据主权默认转移给 ARY |
| Organizer Server | Organizer 控制域内的 Private Race Source；接收报名并写入报名事实 | 完整 Race 数据、报名事实、执行数据、评审与复盘数据 | 不得要求 ARY 代存报名事实 |
| ARY | 创建公开 Race Shell；存储、索引、展示 Organizer 主动披露的 Public Metadata / Public Projection | Public Metadata、Public Projection、公开状态、公开可达性状态 | 不得持久化完整 Race Source Facts；不得从代理请求生成报名事实库 |
| ARY Stateless Proxy | 转发 Participant 到 Organizer Server 的报名请求 | 短暂处理 `race_public_id`、`rider_id`、`client_request_id` 等 transit payload | 不得执行 `save()` / `commit()`；不得聚合报名事实、计数或名单 |
| Participant / Rider | 浏览公开赛事并发起报名意图 | 公开页面、公开入口、Organizer 返回的即时响应 | 不得通过 ARY 访问私密 Race Source Facts |
| DCR | Organizer 侧执行核，可处理规则、过程编排、投影生成辅助 | Organizer 授权范围内的完整数据 | 不得成为向 ARY 隐性复制完整数据的通道；不得外传中间判断链 |
| Public Projection | 承载 Organizer 主动披露的有限公开视图，供 ARY 持久化、索引和展示 | Organizer 明确批准公开的数据 | 不得被视为完整 Race 数据源；不得包含未披露数据 |

## 数据边界

| 数据类别 | 所有者或控制者 | 可见范围 | 当前边界 |
| --- | --- | --- | --- |
| Race Source Facts | Organizer / DCR | Organizer 授权域内 | 仅留存在 Organizer Server / DCR 控制域 |
| Public Metadata | Organizer 决定披露 | 公开侧、ARY | ARY 可持久化、索引和展示 |
| Public Projection | Organizer 决定内容与授权 | 公开侧、ARY | ARY 可持久化、索引和展示；必须来自 Organizer 主动披露 |
| Registration Transit Payload | Participant 发起，Organizer Server 处理 | 传输中短暂经过 ARY Proxy | ARY 不持久化；日志不得记录核心私有源事实 |
| Public Registration Summary | Organizer 主动披露 | 公开侧、ARY | 可作为 Public Projection 长期展示 |
| Organizer Connectivity State | ARY 健康检查或 Organizer 主动状态 | 公开侧、ARY | ARY 可保存 `Suspended` 等公开可达性状态 |

默认规则：任何未被 Organizer 明确标记为公开的数据，均不得进入 ARY 展示链路。

## 功能边界

以下为 P1 工作口径，具体交互方式仍待后续确认：

| 能力 | 最小含义 | 边界 |
| --- | --- | --- |
| 创建 | 形成可被识别和访问的赛事公开入口 | 不要求 ARY 创建或保存完整 Race 数据 |
| 披露 | Organizer 主动决定并发布公开元数据或 Public Projection | ARY 不得代替 Organizer 决定公开内容 |
| 组织 | ARY 基于公开信息支持赛事公开侧的组织与呈现 | 不依赖未披露完整数据 |
| 报名入口转发 | ARY Stateless Proxy 将报名意图透传给 Organizer Server | ARY 不写入报名事实，不生成自有报名库 |
| 展示 | ARY 向评审或公众呈现已披露内容 | 每个展示字段必须可追溯到披露来源 |

## 设计阶段非目标

- P1 阶段不编写 PRD 正文；进入 P2 后按已锁定边界开展 PRD 设计。
- 不编写、生成或伪装实现实际 PoC 代码。
- 实现设计完成前不实现生产级平台或完整赛事管理系统；实现设计完成后允许编写最小实际 PoC 代码和 Demo 页面。
- 不实现指导骑行、成果评审、骑行复盘等赛事执行子系统。
- 不确定公开字段、通信协议、部署拓扑或技术选型的最终方案。
- 不扩展到与四项 PoC 证明无直接关系的功能。

## 越界判定

出现以下任一情况即视为方案越界：

- Organizer 之外持久化了完整 Race 数据。
- ARY 展示了无法追溯到 Organizer 主动披露的数据。
- DCR 绕过 Organizer 的授权或披露控制。
- 为完成闭环而引入非必要的完整赛事执行子系统。
- P7 文档对齐阶段跳过实现设计直接产出扩展代码。
- ARY Registration Proxy 从请求中沉淀报名事实、计数或名单。
- 参赛者代码、完整骑行记录、执行日志、DCR 判断链、评审证据、复盘材料或私有规则细节进入 ARY 持久化存储、日志、缓存、debug 输出或验证材料。
