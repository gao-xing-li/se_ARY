# ARY GRS 001 最终 PoC/Demo 摘要

## 1. 当前最终方案

当前最终方案采用小组 PRD 基准：

> ARY 是 Public Yard，Organizer Server / DCR 是 Private Race Source。

核心含义：

- Organizer / DCR 控制域持有完整 Race Source Facts。
- ARY 只持久化 Organizer 主动披露的 Public Metadata / Public Projection。
- Participant 可从 ARY 公开页发起报名意图。
- ARY Stateless Proxy 只转发报名请求，不写报名事实。
- Organizer Server 是报名事实和完整 Race Source Facts 的写入位置。
- Organizer 主动披露的公开报名计数、公开 RiderID / nickname、公开参与摘要可以作为 Public Projection 长期展示。
- Organizer Server 不可达时，ARY 只显示 `Suspended` 公开可达性状态，不推断赛事内部事实。

## 2. PoC/Demo 已实现能力

| 能力 | 实现位置 | 说明 |
| --- | --- | --- |
| Organizer Server | `group_ARY_week1/ary_grs_001_poc.py` 的 `organizer_app` | 保存完整 Race Source Facts，接收报名并写入本地事实 |
| ARY Server | `group_ARY_week1/ary_grs_001_poc.py` 的 `ary_app` | 保存 Public Metadata / Public Projection，渲染公开页 |
| Public Metadata 披露 | `POST /api/races/metadata`、`POST /demo/disclose-to-ary` | Organizer 主动披露公开赛事对象 |
| Public Projection 披露 | `POST /api/races/{race_public_id}/projection` | ARY 校验并持久化公开投影 |
| Registration Proxy | `POST /proxy/race/001/register` | ARY 透传报名意图，Organizer Server 写入报名事实 |
| 公开页 | `GET /explore/race/001` | 展示公开披露、报名表单、Evidence 入口和边界文案 |
| Evidence Dashboard | `GET /evidence-dashboard`、`GET /debug/evidence-dashboard` | 汇总 privacy、proxy、projection、connectivity 证据 |
| Projection version/hash demo | `GET /debug/projection-version-hash-demo` | 验证旧版本拒绝、同版本幂等、同版本漂移拒绝、新版本接受 |
| Rejection Demo | `GET /debug/rejection-demo` | 证明含私有源事实标记的恶意投影不会写入 ARY |
| Suspended Demo | `GET /explore/race/001` + Organizer 离线 | Organizer 不可达时 ARY 显示 `Suspended` |

## 3. 如何证明 Public Yard / Private Race Source

### 3.1 数据留存

证明点：

- `GET /debug/organizer-store` 可在本地看到 Organizer 持有完整 Race Source Facts。
- `GET /debug/privacy-check` 证明 ARY public stores 不含 forbidden key/value。
- `GET /debug/evidence-dashboard` 只展示 Organizer 私有字段名和存在性，不展示私有正文。

结论：

完整 Race Source Facts 留在 Organizer / DCR 控制域。

### 3.2 ARY 公开持久化边界

证明点：

- `ary_public_metadata_store` 只保存 Public Metadata。
- `ary_public_projection_store` 只保存 Organizer 主动披露的 Public Projection。
- `GET /debug/ary-store` 明确缺失 `ary_registration_store`、`ary_rider_db`、`ary_race_fact_db`。

结论：

ARY 可持久化公开披露数据，但不是完整 Race 数据库。

### 3.3 Registration Proxy 零落库

证明点：

- 报名前后检查 `/debug/ary-store`，ARY 均不存在报名事实库。
- `POST /proxy/race/001/register` 返回 `ary_persistence = none`。
- Organizer 返回 `stored_in = local_organizer_db`。

结论：

报名请求可以经过 ARY，但报名事实只写 Organizer Server。

### 3.4 Public Projection 来源与完整性

证明点：

- Public Projection 来自 Organizer 主动披露。
- `/debug/projection-version-hash-demo` 证明版本/hash 规则可复跑：
  - 旧版本拒绝。
  - 同版本同 hash 幂等。
  - 同版本不同 hash 冲突。
  - 新版本接受。
- `/debug/rejection-demo` 证明含私有源事实标记的投影不会进入 ARY。

结论：

ARY 展示的是 Organizer 主动披露的公开投影，不是自行推断或补全的完整事实。

### 3.5 Suspended 状态

证明点：

- 停止 Organizer Server 后访问 ARY 公开页。
- 页面、`/debug/ary-store`、`/debug/evidence-dashboard` 均显示 `Suspended`。
- 文档明确 `Suspended` 只代表公开接入不可达。

结论：

ARY 能处理 Organizer 不可达，但不推断赛事内部执行状态或报名失败事实。

## 4. 演示顺序

推荐按以下顺序演示：

1. 启动 Organizer Server：`uvicorn ary_grs_001_poc:organizer_app --port 9001`。
2. 启动 ARY Server：`uvicorn ary_grs_001_poc:ary_app --port 8000`。
3. 本地查看 Organizer debug：`GET /debug/organizer-store`，说明该接口仅限本地评审。
4. 执行创建与披露：`POST /demo/disclose-to-ary`。
5. 查看公开旅程证据：`GET /debug/demo-journey`。
6. 查看 ARY store：`GET /debug/ary-store`，确认无报名事实库。
7. 访问公开页：`GET /explore/race/001`。
8. 提交报名代理：`POST /proxy/race/001/register`。
9. 再次查看 ARY store 和 Evidence Dashboard，确认 Proxy 零落库。
10. 访问 Evidence Dashboard：`GET /evidence-dashboard`。
11. 执行隐私检查：`GET /debug/privacy-check`。
12. 执行泄露拒绝：`GET /debug/rejection-demo`。
13. 执行 version/hash 验证：`GET /debug/projection-version-hash-demo`。
14. 停止 Organizer Server，刷新公开页并查看 `Suspended`。

完整请求与期望结果见 `group_ARY_week1/DEMO_VERIFICATION.md`。

## 5. 已知边界与非目标

当前 PoC/Demo 明确不做：

- 不引入生产级数据库。
- 不实现认证、权限、加密、端到端报名信封。
- 不支持多 Race、多 Organizer。
- 不实现完整赛事执行、骑行指导、成果评审、争议仲裁或复盘系统。
- 不实现生产级日志、APM、审计、监控或安全合规方案。
- 不把 Organizer debug 暴露为 ARY 公开页面。
- 不让 Evidence Dashboard 展示 Organizer 私有正文。

当前 PoC/Demo 的定位：

- 用最小实现证明架构边界。
- 用可复跑 endpoint 证明数据留存、公开持久化、Proxy 零落库、投影完整性、拒绝越界和 Suspended。
- 为后续真实产品设计提供边界依据，而不是生产系统。

## 6. 最终验收结论

最终验收依据：

- `group_ARY_week1/DEMO_VERIFICATION.md`
- `docs/03_review/P8_IMPLEMENTATION_CHECKLIST.md`
- `docs/03_review/P9_ACCEPTANCE_REPORT.md`

结论：

- P7 小组 PRD 对齐已完成。
- P8 实现检查与增强计划已完成。
- P9 实际 PoC/Demo 实现与 HTTP 验收已完成。
- 当前 PoC/Demo 能证明 Public Yard / Private Race Source 成立。
- ARY 不会成为参赛者代码、完整骑行记录、执行日志、DCR 判断链、评审证据、复盘材料或私有规则细节的中心化事实数据库。
- 报名摘要只有在 Organizer 主动披露为 Public Projection 时，才可以作为公开信息展示。
- 最终演示材料可进入 P10 冻结。

## 7. 提交材料边界

### 7.1 应提交材料

- `group_ARY_week1/ary_grs_001_poc.py`
- `group_ARY_week1/DEMO_VERIFICATION.md`
- `group_ARY_week1/demo_page.html`
- `group_ARY_week1/PRD-ARY-GRS-001.md`
- `group_ARY_week1/Riding Record.md`
- `docs/01_requirements/`
- `docs/02_design/`
- `docs/03_review/`
- `docs/04_submission/`
- `PLAN.md`
- `AGENTS.md`

### 7.2 不应提交材料

- `.venv/`
- `__pycache__/`
- `*.pyc`
- `*.log`
- `.pytest_cache/`
- 本地端口占用、进程号、临时启动输出。
- Organizer debug 返回的完整私有正文。

### 7.3 Debug 与证据边界

- `GET /debug/organizer-store` 仅用于本地评审，可能显示完整 Race Source Facts，不应截图或复制私有正文进入提交材料。
- `GET /debug/ary-store`、`GET /debug/privacy-check`、`GET /debug/evidence-dashboard` 可作为 ARY 侧边界证据，但不得包含私有正文。
- Evidence Dashboard 只允许展示 Organizer 私有字段名、存在性和 redacted 状态。
- P9 验收结论以 `docs/03_review/P9_ACCEPTANCE_REPORT.md` 为准，不提交运行日志作为证据。
