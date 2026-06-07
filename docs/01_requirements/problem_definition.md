# ARY GRS 001 问题定义

## 文档定位

本文锁定 GRS 001 的问题基线与 PoC 证明目标。P7 起以 `group_ARY_week1/PRD-ARY-GRS-001.md` 为新的 PRD 基准；个人原 PRD 不再作为产品主线，只保留其数据边界、字段溯源、缓存撤回、DCR 输出边界和验证证据设计。

## 核心冲突

Race Source Facts 的主权与留存位置属于 Organizer / DCR 控制域，ARY 不得中心化持久化保存完整 Race 数据；但 ARY 仍需通过 Public Metadata、Public Projection、Registration Proxy 和公开展示能力完成赛事的创建、披露、组织、报名入口转发与展示。

因此，本作业要回答的核心问题是：

> 如何在完整 Race Source Facts 不离开 Organizer / DCR 控制域、ARY 不生成自己的完整 Race 或报名事实库的前提下，仅依靠 Organizer 主动披露的 Public Metadata / Public Projection 和无状态报名代理，形成可验证的赛事功能闭环？

## 问题拆解

| 维度 | 必须成立的条件 | 主要风险 |
| --- | --- | --- |
| 数据主权 | Organizer 控制完整数据及其披露 | 完整数据被复制、外传或越权使用 |
| 平台边界 | ARY 可持久化 Public Metadata / Public Projection，但不得持久化完整 Race Source Facts 或自有报名事实库 | 以缓存、日志、代理请求、debug 输出或索引名义形成隐性完整副本 |
| 产品能力 | ARY 仍可完成创建、披露、组织、展示和报名入口转发 | 去中心化约束导致业务链路或报名入口中断 |
| 展示来源 | 所有展示内容均可追溯到 Organizer 主动披露 | ARY 推断、补全或展示未披露数据 |

## 四项 PoC 核心证明对象

| 编号 | 证明对象 | 必须证明的结论 | 明确失败条件 |
| --- | --- | --- | --- |
| POC-01 | 数据留存 | Race 完整数据可以且仅留存在 Organizer 侧 | Organizer 之外出现完整数据副本，或 Organizer 失去披露控制权 |
| POC-02 | 去中心化 | ARY 仅持久化公开披露数据和公开可达性状态即可工作 | ARY 的核心能力依赖完整数据、报名事实库或私有执行数据的中心化持久化 |
| POC-03 | 功能闭环 | 在上述约束下，创建、披露、组织、报名入口转发、展示均可完成 | 任一环节必须访问未披露完整数据、ARY 必须写入报名事实，或链路无法闭合 |
| POC-04 | 投影机制 | ARY 展示内容完全来自 Organizer 主动披露的公开元数据或公开投影 | 展示字段无法追溯到披露来源，或出现未披露内容 |

## 工作定义

- **Race Source Facts**：参赛者代码、完整骑行记录、执行日志、DCR 判断链、评审证据、复盘材料、私有规则细节和其他支撑 Race 的完整事实数据。
- **Public Metadata**：Organizer 主动披露的赛事基础公开信息，可由 ARY 持久化、索引和展示。
- **Public Projection**：由 Organizer 主动生成并披露的公开投影，可由 ARY 持久化、索引和展示，但不得包含 Race Source Facts。
- **Registration Proxy**：ARY 的无状态报名请求转发层，只做请求形状校验、路由、超时和错误归一化，不 `save()` / `commit()` 报名事实。
- **Organizer Server**：Organizer 控制域内的 Private Race Source，负责报名事实写入和完整 Race 管理。
- **Suspended**：Organizer Server 不可达或 Organizer 主动挂起公开入口时的公开可达性状态，不代表 ARY 获得赛事内部事实。
- **功能闭环**：创建、披露、组织、报名入口转发、展示五项能力均有明确输入、责任角色、输出和可观察结果。

## P1 锁定结论

- 本作业围绕去中心化数据主权展开，不以普通赛事管理功能数量为目标。
- PoC 必须同时覆盖四项证明对象，不能以单一页面或单一接口替代完整证明；实现设计完成后需要编写实际 PoC 代码验证。
- 未明确披露的数据默认不可被 ARY、DCR 或 Public Projection 对外使用。
- 未决设计问题必须保留为待确认项，不得静默转化为需求。
