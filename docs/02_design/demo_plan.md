# ARY GRS 001 Demo 展示方案

## 1. 文档定位

本文对齐小组 Demo 基准 `group_ARY_week1/DEMO_VERIFICATION.md` 和 `demo_page.html`。P9 需要实现或迭代实际 PoC 页面与验收路径，而不是只停留在理论页面草案。

## 2. Demo 核心叙事

一句话叙事：

> ARY 是 Public Yard，只持久化 Organizer 主动披露的 Public Metadata / Public Projection；Organizer Server 是 Private Race Source，完整 Race Source Facts 和报名事实只在那里落库。

## 3. Demo 页面与接口清单

| 展示对象 | 面向对象 | 展示内容 | 证明重点 |
| --- | --- | --- | --- |
| Organizer Server debug | 评审者 | 完整 Race Source Facts、报名事实位置 | 数据留存 |
| ARY 公开页 | Viewer / Participant / Agent | Public Metadata、Public Projection、报名表单、边界文案、`Suspended` | 功能闭环、投影机制 |
| ARY store debug | 评审者 | Public Metadata Store、Public Projection Store、connectivity state、明确缺失报名库 | 去中心化 |
| Privacy Check | 评审者 | forbidden key/value 检查结果 | 数据留存、日志/debug 边界 |
| Rejection Demo | 评审者 | 恶意投影拒绝结果 | 投影机制、越界拒绝 |
| Demo Verification 文档 | 小组和评审 | 启动命令、请求路径、期望结果 | 可复跑验收 |

## 4. 必须展示的产品能力

| 能力 | Demo 方式 | 通过标准 |
| --- | --- | --- |
| 创建公开对象 | `POST /demo/disclose-to-ary` 或 metadata API | ARY 写入 Public Metadata，不接收 Source Facts |
| 披露公开投影 | projection API | ARY 写入 Public Projection，版本/hash 规则有效 |
| 公开展示 | `GET /explore/race/001` | 页面展示公开字段、来源、状态和边界文案 |
| 报名代理 | `POST /proxy/race/001/register` 或表单 | Organizer Server 写报名事实，ARY 无报名库 |
| 公开报名摘要 | Organizer 主动更新 Projection | 页面长期展示来源于 Public Projection |
| Organizer 离线 | 停止 Organizer Server 后刷新公开页 | 页面显示 `Suspended` |
| 隐私检查 | `GET /debug/privacy-check` | ARY public stores 不含核心私有源事实 |
| 泄露拒绝 | `GET /debug/rejection-demo` | 恶意投影 rejected=true，stored_in_ary=false |

## 5. 验证证据页设计

个人原设计中的“验证证据页”保留为后续 Demo 增强模块，最小内容：

- Organizer private source 字段清单，只显示字段名和存储位置。
- ARY public stores 字段清单。
- Public Projection 字段与页面展示字段映射。
- Proxy 零落库证据：不存在 `ary_registration_store`、`ary_rider_db`、`ary_race_fact_db`。
- Projection 版本/hash 验证结果。
- Forbidden key/value marker 检查结果。
- `Suspended` 状态说明。
- 日志/debug 输出白名单说明。

## 6. Demo 非目标

- 不实现生产级身份认证、反作弊、权限系统或高可用。
- 不实现完整骑行执行、成果评审、争议仲裁或复盘系统。
- 不让 ARY 保存参赛者代码、完整骑行记录、执行日志、DCR 判断链、评审证据、复盘材料或私有规则细节。
- 不让 ARY 从代理请求中生成长期报名统计。

## 7. 下一阶段代码迭代清单

| 优先级 | 任务 | 验证 |
| --- | --- | --- |
| Must | 保持双 FastAPI app：Organizer Server 与 ARY Server | 两个端口可启动 |
| Must | 补齐 Public Metadata / Projection schema 检查 | 越界字段被拒绝 |
| Must | 保持 Registration Proxy 无状态 | ARY store 中无报名库 |
| Must | 补齐 `Suspended` 页面状态 | Organizer 离线时页面可见 |
| Must | 增强验证证据页或 debug endpoint | 验收证据一页/一组接口可复盘 |
| Should | 日志字段白名单化 | 日志不含请求体和私有源事实 |
| Should | 投影字段映射可视化 | 页面字段可追溯 |
| Should | Demo 页面中明确公开报名摘要来源 | 避免误认为 ARY 聚合 |

## 8. Demo 自检

| 自检项 | 状态 |
| --- | --- |
| 吸收小组 Demo 的 API 旅程 | 通过 |
| 覆盖 Public Metadata / Projection 可持久化 | 通过 |
| 覆盖 Registration Proxy 与 Organizer Server | 通过 |
| 覆盖公开报名摘要来源 | 通过 |
| 覆盖 Suspended | 通过 |
| 保留验证证据页、字段溯源、DCR 输出和缓存撤回要求 | 通过 |
