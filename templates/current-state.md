# {{PROJECT}}｜Current State

> 仅当项目缺少已有 `CURRENT_STATE` / `LATEST_REPORT` / 等价 authority 时使用。若已有稳定入口，不重复创建。

```yaml
current_phase:
status:
active_task_contract:
last_verified_state:
known_blockers: []
next_allowed_action:
authoritative_sources: []
```

## 说明

- `last_verified_state` 只写有证据支持的最新状态；
- `known_blockers` 只保留仍有效 blocker；
- `authoritative_sources` 指向必要证据，不复制其全文；
- 状态变化后更新当前入口，不在 Skill 内保存项目实时状态。
