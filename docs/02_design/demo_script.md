# ARY GRS 001 Demo 演示脚本

## 1. 演示目标

用一条可运行 PoC 旅程证明：ARY 可创建、披露、组织和展示公开 Race 对象，并支持报名入口代理；但完整 Race Source Facts 和报名事实仍只在 Organizer Server / DCR 控制域内。

## 2. 演示准备

| 准备项 | 内容 |
| --- | --- |
| Organizer Server | `uvicorn ary_grs_001_poc:organizer_app --port 9001` |
| ARY Server | `uvicorn ary_grs_001_poc:ary_app --port 8000` |
| Race Public ID | `race_001` |
| Participant | `rider_demo_001` |
| 私有源事实 | `submission_code`、`riding_records`、`execution_logs`、`dcr_judgement_trace`、`review_evidence`、`retro_notes`、`private_rulebook` |
| 公开披露数据 | Public Metadata、Public Projection、公开报名计数、公开 alias、公开参与状态 |

## 3. 演示步骤

### S1 展示 Organizer 持有完整源事实

- **请求**：`GET http://127.0.0.1:9001/debug/organizer-store`
- **展示**：完整 Race Source Facts 位于 Organizer Server / DCR 控制域。
- **证明**：数据留存。
- **讲解**：这些字段不会进入 ARY public stores。

### S2 创建公开对象并披露投影

- **请求**：`POST http://127.0.0.1:9001/demo/disclose-to-ary`
- **展示**：Organizer 从本地源事实生成 Public Metadata / Projection 并提交给 ARY。
- **证明**：创建、披露、公开持久化边界。
- **讲解**：ARY 存储的是公开披露数据，不是完整 Race。

### S3 查看 ARY public stores

- **请求**：`GET http://127.0.0.1:8000/debug/ary-store`
- **展示**：`ary_public_metadata_store`、`ary_public_projection_store`、`ary_public_connectivity_state`，并明确缺失 `ary_registration_store`。
- **证明**：去中心化、代理零落库。
- **讲解**：Public Projection 可持久化，但报名事实库不可在 ARY 出现。

### S4 打开公开页

- **请求**：`GET http://127.0.0.1:8000/explore/race/001`
- **展示**：Public Metadata、Public Projection、公开报名摘要、报名表单、边界说明。
- **证明**：组织、展示、投影机制。
- **讲解**：页面展示的长期报名摘要来自 Organizer 主动披露的 Public Projection。

### S5 提交报名代理

- **请求**：

```text
POST http://127.0.0.1:8000/proxy/race/001/register
Content-Type: application/json

{
  "race_public_id": "race_001",
  "rider_id": "rider_demo_001",
  "client_request_id": "req_001"
}
```

- **展示**：ARY Proxy 返回 Organizer 结果；Organizer Server 报名计数增加。
- **证明**：报名事实只写 Organizer Server。
- **讲解**：ARY Proxy 只有转发能力，没有 `save()`、`commit()` 或本地报名表。

### S6 执行隐私检查

- **请求**：`GET http://127.0.0.1:8000/debug/privacy-check`
- **展示**：`ary_public_stores_contain_core_private_source_facts=false`。
- **证明**：Race Source Facts 未进入 ARY public stores。
- **讲解**：验证材料只输出字段路径和布尔结果，不展示私有正文。

### S7 执行泄露拒绝演示

- **请求**：`GET http://127.0.0.1:8000/debug/rejection-demo`
- **展示**：恶意投影被拒绝，`stored_in_ary=false`。
- **证明**：投影机制有负向验收。
- **讲解**：字段名和敏感 value marker 都要检查。

### S8 演示 Organizer 离线挂起

- **操作**：停止 Organizer Server，保持 ARY Server 运行。
- **请求**：`GET http://127.0.0.1:8000/explore/race/001`
- **展示**：公开页显示 `Suspended`。
- **证明**：公开可达性状态独立于内部赛事事实。
- **讲解**：`Suspended` 不代表 ARY 知道赛事执行失败或报名失败。

### S9 展示投影版本/hash 规则

- **操作**：提交旧版本、同版本同 hash、同版本不同 hash 三类投影。
- **展示**：旧版本拒绝，同版本同 hash 幂等，同版本不同 hash 冲突。
- **证明**：公开投影不会发生不可追溯内容漂移。
- **讲解**：版本/hash 是公开披露的最小完整性控制。

## 4. 演示口径

- 不说“ARY 拥有 Race 数据”，只说“ARY 持有公开披露数据”。
- 不说“ARY 完成报名”，只说“ARY 代理报名意图，Organizer Server 写报名事实”。
- 不说“报名计数由 ARY 统计”，只说“长期报名摘要来自 Organizer 主动披露的 Public Projection”。
- 不说“Suspended 是赛事状态”，只说“Suspended 是 Organizer Server 公开接入不可达或挂起状态”。
- 不展示私有字段正文，只展示字段名、路径、布尔结果和边界标签。

## 5. 最终验收口径

Demo 通过条件：

- ARY 可以通过 Public Metadata / Projection 完成公开 Race 展示。
- Participant 可以通过 ARY 发起报名意图。
- Organizer Server 写入报名事实。
- ARY public stores 不含完整 Race Source Facts。
- ARY 不存在报名事实库。
- 恶意投影被拒绝。
- Organizer 离线时展示 `Suspended`。
- 验证材料、日志、debug 输出不泄露核心私有源事实。
