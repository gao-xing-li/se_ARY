# ARY GRS 001 PoC 验证矩阵

## 1. 矩阵用途

本矩阵把小组 PRD 基准映射到实际 PoC 验证项。P9 代码 PoC 必须按本矩阵产出可观察证据。

## 2. 核心验证矩阵

| 编号 | 证明对象 | 验证目标 | 最小场景 | 观测点 | 通过标准 | 失败条件 |
| --- | --- | --- | --- | --- | --- | --- |
| VM-01 | 数据留存 | 完整 Race Source Facts 留在 Organizer / DCR 控制域 | Organizer Server 持有私有规则、代码、骑行记录、执行日志、评审证据 | `/debug/organizer-store`、`/debug/privacy-check` | ARY public stores 不含 forbidden key/value | ARY store、页面、日志或 debug 输出出现核心私有源事实 |
| VM-02 | 公开持久化边界 | ARY 只持久化 Organizer 主动披露的 Public Metadata / Projection | Organizer 提交 metadata 和 projection | `/debug/ary-store`、投影版本/hash 响应 | ARY 持久化公开字段，且不构成完整数据副本 | ARY 要求上传完整 Race 或投影字段过宽 |
| VM-03 | 功能闭环 | 创建、披露、组织、报名入口转发、展示成立 | `/demo/disclose-to-ary` 后访问公开页并提交报名 | demo journey、公开页、Organizer 报名计数 | 每环节有输出，报名事实在 Organizer Server | 任一环节必须读取未披露数据，或 ARY 写报名事实 |
| VM-04 | 投影机制 | 展示字段来自 Organizer 主动披露的 Public Projection | 页面展示公开摘要、报名计数、公开 alias | 页面字段、projection source、hash、version | 长期报名摘要来自 Public Projection | ARY 从代理请求自行聚合长期报名摘要 |
| VM-05 | Registration Proxy | ARY Proxy 无状态透传 | Participant POST 报名请求 | proxy 响应、Organizer store、ARY store | ARY 无 `ary_registration_store`，无 `save()` / `commit()` | ARY 生成本地报名表、名单或计数 |
| VM-06 | Suspended | Organizer 不可达时仅展示公开可达性状态 | 停止 Organizer Server 后访问 ARY 公开页 | 页面状态、connectivity state | 显示 `Suspended`，不推断内部事实 | 将 Suspended 解释为赛事失败、报名失败或内部事实 |
| VM-07 | 拒绝演示 | 越界投影不会写入 ARY | malicious projection 含私有代码或 DCR 路径 | `/debug/rejection-demo` | rejected=true，stored_in_ary=false | 恶意投影写入 public store |

## 3. 数据分类检查矩阵

| 数据类别 | Organizer Server / DCR | ARY Metadata Store | ARY Projection Store | ARY Proxy | ARY Display |
| --- | --- | --- | --- | --- | --- |
| Race Source Facts | 必须存在 | 禁止 | 禁止 | 禁止持久化 | 禁止展示 |
| Public Metadata | 可生成 | 可持久化 | 可引用 | 可读取路由信息 | 可展示 |
| Public Projection | 可生成 | 记录版本 | 可持久化 | 不从代理请求生成 | 可展示 |
| Registration Transit Payload | 接收并写入事实 | 禁止持久化 | 禁止沉淀 | 短暂处理并转发 | 即时结果可临时展示 |
| Public Registration Summary | 可主动披露 | 可记录版本 | 可持久化 | 不可聚合生成 | 可展示 |
| Organizer Connectivity State | 提供 health | 可保存公开状态 | 不涉及 | 可更新 `Suspended` | 可展示 `Suspended` |

## 4. 状态验证矩阵

| 状态 | 含义 | ARY 行为 | 验证重点 |
| --- | --- | --- | --- |
| Draft | 公开对象未正式披露 | 仅保存或限制展示公开草稿 | 草稿不得包含完整 Race |
| Open | 公开开放 | 展示公开入口和报名按钮 | 报名事实仍写 Organizer Server |
| Active | 公开进行中 | 展示公开进度投影 | 不接收执行数据 |
| Completed | 公开完成 | 展示 Organizer 披露的成果摘要 | 不做评审裁决 |
| Archived | 归档 | 保留公开历史展示 | 历史内容仍是公开披露 |
| Withdrawn | Organizer 撤回 | 停止展示被撤回投影 | 不用旧缓存补正文 |
| Suspended | Organizer Server 不可达或入口挂起 | 暂停入口或代理转发 | 不代表内部赛事事实 |

## 5. P9 代码验收证据

| 编号 | 证据 | 期望 |
| --- | --- | --- |
| EV-01 | Organizer store 快照 | 包含完整 Race Source Facts |
| EV-02 | ARY store 快照 | 只含 Public Metadata / Projection / connectivity |
| EV-03 | privacy-check | `ary_public_stores_contain_core_private_source_facts=false` |
| EV-04 | rejection-demo | 恶意投影被拒绝，不写入 ARY |
| EV-05 | proxy registration | Organizer rider count 增加，ARY 无报名库 |
| EV-06 | Suspended demo | Organizer 离线时页面显示 `Suspended` |
| EV-07 | projection version/hash | 旧版本拒绝，同版本同 hash 幂等，同版本不同 hash 冲突 |
| EV-08 | demo page | 展示公开字段、边界文案、报名表单 |
