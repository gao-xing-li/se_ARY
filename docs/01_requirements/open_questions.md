# ARY GRS 001 待确认问题

## 处理原则

- 未确认问题不得静默写成既定需求或架构事实。
- 未明确公开的数据默认按非公开数据处理。
- 高优先级问题应在 PRD 与 PoC 理论设计定稿前解决，或形成明确假设与备选方案。

## 高优先级

| 编号 | 待确认问题 | 影响 |
| --- | --- | --- |
| Q-001 | “完整 Race 数据”具体包含哪些数据类别？ | 决定数据留存证明和越界判定 |
| Q-002 | ARY 可持久化哪些公开数据、状态、索引、缓存或日志？保留多久？ | 小组 PRD 已确认 Public Metadata / Public Projection 可持久化；仍需实现设计冻结字段与保留周期 |
| Q-003 | “创建赛事”是由 Organizer 本地创建后向 ARY 登记，还是由 ARY 发起并在 Organizer 侧落地？ | 小组 PRD 已确认 ARY 创建 Race Shell / Public Metadata，完整 Race 在 Organizer 侧 |
| Q-004 | Public Projection 的最小字段集合、数据格式与承载位置是什么？ | 小组 PRD 已给出示例；仍需代码 PoC 冻结 schema 与拒绝规则 |
| Q-005 | Organizer 如何更新、撤回或使 Public Projection 失效？ARY 如何处理旧数据？ | 决定披露控制是否完整成立 |
| Q-006 | DCR 部署在哪里，代表谁执行，能够访问哪些数据？ | 决定 DCR 是否可能造成数据越权或隐性复制 |
| Q-007 | 用什么可观察证据证明 Organizer 之外没有完整数据副本、ARY 没有持久化完整数据？ | 决定 PoC 的证明力度与验收方法 |

## 中优先级

| 编号 | 待确认问题 | 影响 |
| --- | --- | --- |
| Q-008 | Organizer 的披露动作如何被授权、鉴别并证明来源可信？ | 决定投影真实性与越权防护 |
| Q-009 | Organizer 或 Public Projection 暂时不可用时，ARY 应展示什么？ | 决定可用性与缓存边界 |
| Q-010 | “组织赛事”在本次 PoC 中必须覆盖哪些最小能力？ | 决定功能闭环范围 |
| Q-011 | PoC 是否只验证单个 Organizer 和单场 Race，还是需要覆盖多 Organizer、多 Race？ | 决定验证场景复杂度 |
| Q-012 | Demo 必须面向哪些角色，需展示哪些关键操作和失败场景？ | 决定展示脚本与评审证据 |
| Q-013 | Participant 报名凭证、RiderID 防伪造、防重复机制如何设计？ | 决定报名代理从 Demo 走向真实产品的可信边界 |
| Q-014 | Organizer Server endpoint 如何注册、签名、轮换和撤销？ | 决定 ARY Proxy 路由可信度与攻击面 |
| Q-015 | 报名代理日志、APM、错误追踪允许记录哪些字段？ | 防止日志、debug 输出泄露核心私有源事实 |
| Q-016 | 是否需要端到端加密报名信封？ | 降低 ARY Proxy 在传输中看到敏感载荷的风险 |

## 当前默认处理

- 对 Q-001：未被明确披露的数据均视为完整数据边界内的受保护数据。
- 对 Q-002：ARY 可持久化 Organizer 主动披露的 Public Metadata / Public Projection 与公开可达性状态；不得持久化 Race Source Facts 或自有报名事实库。
- 对 Q-004：以小组 PRD 的 Public Projection 示例为基准，代码 PoC 前冻结 schema、版本/hash 规则和越界字段拒绝规则。
- 对 Q-006：DCR 暂作为抽象执行核处理，不预设部署位置。
- 对其他问题：在后续设计中提供最小方案和必要备选，不提前扩展范围。

## P2 工作假设

- 对 Q-003：采用小组 PRD 的 Public Yard / Private Race Source 流程：ARY 创建 Race Shell 与公开对象，完整 Race 与报名事实留在 Organizer Server。
- 对 Q-004：ARY 可持久化 Organizer 主动披露的 Public Projection；字段溯源、版本/hash、撤回与越界拒绝规则进入代码 PoC 验证。
- 对 Q-005：Organizer 主动发布、更新、暂停与撤回；ARY 停止展示被撤回内容，长期报名摘要必须来自 Organizer 新投影。

## P4 工作假设

- 对 Q-002：ARY Registry 可持久化最小公开登记信息；ARY Display 只临时处理公开投影。
- 对 Q-006：DCR 接触完整数据时位于 Organizer 授权域内；ARY 侧只处理公开登记信息和投影。
- 对 Q-009：投影不可用、过期或撤回时，ARY 不使用旧正文补全展示，只显示状态。

## P7 对齐结论

- 新 PRD 基准为 `group_ARY_week1/PRD-ARY-GRS-001.md`。
- 个人原 PRD 的严格设计保留为下游验证约束：字段溯源、缓存撤回、DCR 输出清单、越界字段拒绝、验证证据页。
- 实现设计完成后需要编写实际 PoC 代码，不再停留在理论文档。
