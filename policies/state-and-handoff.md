# Current State 与 Handoff 收敛规则

## 目标

降低新对话线程 / Codex 线程恢复项目状态的成本，同时避免复制完整历史。

本规则是“恢复入口与交接方式”的方法约定，不建立项目状态数据库或新的 Context Manager。

## 1. Authoritative Current State

中枢优先寻找项目已有的单一当前状态入口，例如：

- `CURRENT_STATE`
- `LATEST_REPORT`
- 最新正式阶段报告
- 项目已有等价 authority

若现有入口已经能回答以下问题，不新建第二份状态文件：

```yaml
current_phase:
status:
active_task_contract:
last_verified_state:
known_blockers:
next_allowed_action:
authoritative_sources:
```

只有项目缺少等价入口时，才可使用 `templates/current-state.md` 作为轻量模板。

### 恢复顺序

```text
先读 Current State / 等价 authority
→ 只按 authoritative_sources 读取必要证据
→ 恢复当前阶段与下一步
```

禁止为了恢复状态而默认全文扫描完整项目历史。

## 2. Full Handoff / Delta Handoff

### FULL

仅在以下情况使用：

- 新项目；
- 大阶段切换；
- 当前 authority 已失效或不足；
- 重大架构变化；
- 旧基础上下文无法可靠恢复当前状态。

FULL 只保留恢复新上下文所需的完整 authority，不复制无关调试历史。

### DELTA

普通长线程切换默认使用 DELTA：

```yaml
base:
changes_since_base:
closed:
new_blockers:
current_next_action:
authoritative_sources:
```

原则：

> 已有稳定 base 时，只交接自 base 之后的变化。

## 3. 选择规则

```text
有稳定且仍有效的 base？
├─ 是 → DELTA
└─ 否 → FULL
```

若只是 Context Saturation、普通 blocker 闭环、普通 Codex 换线程，默认 DELTA。

## 4. 与现有线程治理的关系

继续复用：

- `Preserve Authority, Drop Debug History`
- `Finish Local Value, Then Compress`
- `Finish Local Dialogue Value, Then Compress`
- `Blocker Thread Split`

本规则不改变 Codex / 对话线程独立判断原则。

## 5. 非目标

不建立：

- Current State 数据库；
- 自动状态同步器；
- Context Manager；
- 自动跨线程复制历史。
