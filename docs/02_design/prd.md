# ARY GRS 001 PRD 对齐说明

## 1. 文档定位

本文不再作为独立产品主线。P7 起，新的 PRD 基准为 `group_ARY_week1/PRD-ARY-GRS-001.md`。

本文用于说明个人原 PRD 如何吸收小组基准，并把原有严谨设计迁移到 PoC、架构、数据流、Demo 和验收任务中。

## 2. 新 PRD 基准

小组 PRD 的一句话产品定义为：

> ARY GRS 001 让 Organizer 能够在不交出完整 Race 数据主权的前提下，把一场赛事创建为可识别、可披露、可组织、可展示的公开对象。

个人文档后续均采用以下主线：

- ARY 是 Public Yard，负责公开赛事对象、公开披露、组织协同、公开展示和报名入口转发。
- Organizer Server 是 Private Race Source，负责完整 Race Source Facts 和报名事实写入。
- DCR 位于 Organizer / DCR 控制域，可处理完整 Race 数据和投影生成辅助。
- ARY 可持久化 Organizer 主动披露的 Public Metadata 和 Public Projection。
- ARY 不得持久化完整 Race Source Facts，不得从代理请求生成自己的报名事实库。

## 3. 必须吸收的新设计

| 新设计 | 对个人文档的影响 |
| --- | --- |
| Public Metadata 可由 ARY 持久化 | 旧“最小公开登记信息”升级为 Public Metadata，允许存储、索引和展示 |
| Public Projection 可由 ARY 持久化 | 旧“按需读取投影”不再作为唯一主线；改为“可持久化，但必须来自 Organizer 主动披露” |
| 引入 Participant / Rider | 用户角色从 Organizer / Viewer 扩展到可发起报名意图的参与者 |
| 引入 Registration Proxy | 产品闭环加入报名入口转发，但 ARY Proxy 必须无状态 |
| 引入 Organizer Server | 明确报名事实和完整 Race Source Facts 的唯一写入位置 |
| 报名请求可经过 ARY Stateless Proxy | ARY 可校验形状、路由、超时和错误归一化，不得 `save()` / `commit()` |
| 公开报名摘要可展示 | 报名计数、公开 RiderID / nickname、公开参与摘要可作为 Organizer 主动披露的 Public Projection |
| 引入 `Suspended` | Organizer Server 不可达时，ARY 可展示公开可达性挂起状态，不得推断内部事实 |

## 4. 保留并下沉的个人严谨设计

| 原设计资产 | 下沉位置 |
| --- | --- |
| 数据留存证明 | PoC 验证矩阵、隐私检查、存储清单 |
| 去中心化证明 | ARY public stores 检查、代理零落库检查 |
| 投影字段溯源 | Public Projection schema、页面字段映射、验证证据页 |
| 缓存撤回规则 | Demo 验收和 Suspended / Withdrawn 状态检查 |
| DCR 输出边界 | 架构与数据流、DCR 输出清单、禁止中间判断链外传 |
| 越界字段拒绝 | `FORBIDDEN_ARY_KEYS`、value marker 检查、rejection demo |
| 验证证据页 | PoC/Demo 后续任务中的必做模块 |
| 日志与 debug 防泄露 | PoC 任务和验收清单中的日志字段白名单 |

## 5. 产品闭环

```text
Organizer / DCR 创建完整 Race Source Facts
  -> Organizer 在 ARY 创建 Race Shell / Public Metadata
  -> Organizer 主动披露 Public Projection
  -> ARY 存储、索引和展示公开披露数据
  -> Participant 从 ARY 公开页发起报名意图
  -> ARY Stateless Proxy 透传至 Organizer Server
  -> Organizer Server 写入报名事实
  -> Organizer 后续披露公开报名摘要为 Public Projection
  -> ARY 展示公开摘要、版本、来源和状态
```

## 6. Must 范围

| 编号 | 功能要求 | 验收要点 |
| --- | --- | --- |
| M-01 | Organizer / DCR 持有完整 Race Source Facts | ARY public stores 不含私有源事实 |
| M-02 | ARY 创建并持久化 Public Metadata | 字段均为 Organizer 明确公开内容 |
| M-03 | Organizer 主动提交 Public Projection | 投影可持久化，但不得包含私有源事实 |
| M-04 | ARY 公开页展示 Public Metadata / Projection | 展示字段可追溯到公开披露来源 |
| M-05 | Participant 可通过 ARY 发起报名意图 | ARY Proxy 只透传，不沉淀报名事实 |
| M-06 | Organizer Server 写入报名事实 | `rider_id`、报名事实只在 Organizer 控制域持久化 |
| M-07 | Organizer 主动披露公开报名摘要 | 长期报名计数、公开 RiderID / nickname 来自 Public Projection |
| M-08 | Organizer 不可达时显示 `Suspended` | 只表示公开接入不可用，不表示赛事内部事实 |
| M-09 | 实现设计完成后编写实际 PoC 代码 | PoC 可运行并产出验收证据 |

## 7. 明确禁止

- ARY 持久化完整规则、参赛者代码、完整骑行记录、执行日志、DCR 判断链、评审证据、复盘材料、私有规则细节。
- ARY Proxy 从报名请求中生成本地报名表、报名名单、报名计数或聚合事实。
- ARY Proxy 执行 `save()` / `commit()` 来沉淀报名事实。
- ARY 从即时代理响应中生成长期报名摘要；长期展示必须来自 Organizer 主动披露的 Public Projection。
- 日志、缓存、APM、debug 输出、验证材料泄露核心私有源事实。

## 8. 后续实现设计入口

后续 P8/P9 不再重新定义产品主线，只围绕小组 PRD 基准完成：

- schema 冻结。
- Organizer Server / ARY Server 接口边界。
- Stateless Proxy 零落库证明。
- Suspended、Withdrawn、rejection demo、privacy check。
- 验证证据页与 Demo 脚本。
