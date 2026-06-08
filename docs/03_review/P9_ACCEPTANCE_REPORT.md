# P9 实际 PoC 验收报告

## 1. 验收范围

本轮在现有 `group_ARY_week1/ary_grs_001_poc.py` 双 FastAPI app 上增量增强并运行验收。

未推倒现有实现，未拆分单文件 PoC。

## 2. 本轮代码与文档增强

| 类型 | 文件 | 内容 |
| --- | --- | --- |
| 代码 | `group_ARY_week1/ary_grs_001_poc.py` | 新增 `/debug/evidence-dashboard` JSON 证据入口 |
| 代码 | `group_ARY_week1/ary_grs_001_poc.py` | 新增 `/evidence-dashboard` HTML Evidence Dashboard 页面 |
| 代码 | `group_ARY_week1/ary_grs_001_poc.py` | 新增 `/debug/projection-version-hash-demo` 可复跑版本/hash 验证 |
| 代码 | `group_ARY_week1/ary_grs_001_poc.py` | 在公开页导航加入 Evidence 入口 |
| 文档 | `group_ARY_week1/DEMO_VERIFICATION.md` | 补全 debug 边界、Proxy 零落库、Evidence Dashboard、version/hash、Suspended、rejection-demo 步骤 |
| 文档 | `docs/03_review/P8_IMPLEMENTATION_CHECKLIST.md` | 标记 P9 代码与验收已完成 |

## 3. 运行环境

- Python venv: `.venv`
- 安装依赖：`fastapi`、`uvicorn`
- Organizer Server: `127.0.0.1:9001`
- ARY Server: `127.0.0.1:8000`

说明：本轮验收脚本在同一生命周期内启动两个真实 HTTP 服务，跑完后自动停止服务。

## 4. 验收结果

| 验收项 | 结果 | 关键证据 |
| --- | --- | --- |
| Organizer 服务启动 | 通过 | `/health` 返回 200 |
| ARY 服务启动 | 通过 | `/debug/privacy-check` 返回 200 |
| Organizer debug 边界 | 通过 | 本地 debug 可见私有字段名，报告只记录字段名 |
| Journey 1 创建与披露 | 通过 | `POST /demo/disclose-to-ary` 返回 `organizer_private_source_still_local=true` |
| Journey 2 公开旅程 | 通过 | metadata/projection 均存在，ARY privacy check 为 false |
| Proxy 零落库前置检查 | 通过 | `explicitly_absent` 包含 `ary_registration_store`、`ary_rider_db`、`ary_race_fact_db` |
| 报名代理 | 通过 | `ary_persistence=none`，报名事实写入 `local_organizer_db` |
| Proxy 零落库后置检查 | 通过 | ARY store 仍无报名事实库 |
| 公开页 | 通过 | 页面返回 200，包含“报名代理”和 Evidence 入口 |
| Evidence Dashboard 页面 | 通过 | 页面返回 200，包含 Dashboard 与 Values redacted 文案 |
| Privacy Check | 通过 | forbidden key/value paths 为空 |
| Rejection Demo | 通过 | `rejected=true`，`stored_in_ary=false` |
| Projection version/hash | 通过 | 旧版本拒绝、同版本同 hash 幂等、同版本不同 hash 冲突、新版本接受 |
| Evidence Dashboard JSON | 通过 | privacy=false、proxy absent、private values redacted |
| Suspended Demo | 通过 | Organizer 停止后页面、ARY store、Evidence Dashboard 均显示 `Suspended` |

## 5. 结论

P9 验收通过。

当前 PoC 能证明：

- ARY 只持久化 Organizer 主动披露的 Public Metadata / Public Projection。
- Race Source Facts 留在 Organizer / DCR 控制域。
- Registration Proxy 不生成 ARY 自有报名事实库。
- Projection version/hash 规则可复跑验证。
- Evidence Dashboard 提供统一证据入口，且不泄露私有正文。
- Organizer 不可达时，ARY 只展示 `Suspended` 公开可达性状态，不推断内部赛事事实。
