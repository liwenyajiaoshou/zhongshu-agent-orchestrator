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


## 6. 统筹对话线程主动交接

当统筹对话线程达到适合切换的自然节点，中枢应主动交付交接材料，而不是只给建议。

### 触发后默认动作

除非 Owner 明确要求暂不更换：

```text
生成交接文档
→ 给出文件名 / 链接
→ 生成新线程启动提示词
```

交接文档至少包含：

```text
CURRENT AUTHORITATIVE STATE
RESOLVED / DO NOT REOPEN
CURRENT BLOCKER
CURRENT STAGE / SUBSTAGE
ALLOWED / FORBIDDEN SCOPE
LATEST TEST / REPORT BASELINE
current_next_action
authoritative_sources
```

### 新线程启动提示词

必须明确写：

```text
请先到文件库检索：
<指定交接文档文件名>

读取后，以其中 CURRENT AUTHORITATIVE STATE 为当前状态；
只按 authoritative_sources 读取必要证据，不回扫完整历史；
按 current_next_action 接管推进。
```

如果文件库检索不到指定文档：
- 不猜测历史；
- 明确报告未找到；
- 再请求最小必要定位信息。

本规则不建立交接管理器，只规范现有 Full / Delta Handoff 的交付方式。


## 7. 主统筹 → 子统筹线程的安全启动

主统筹向子统筹线程交付任务时，应明确：

```yaml
thread_name:
target_direction:
current_stage:
allowed_scope:
forbidden_scope:
authoritative_sources:
current_next_action:
```

子统筹线程收到后，第一步必须做：

```yaml
scope_match:
  status: PASS | MISMATCH | AMBIGUOUS
  conflicts: []
```

### MISMATCH

如果指令 / 文档明显属于其他 Track、阶段、题材、子项目或超出本线程方向：

- 不吸收为本线程 authority；
- 不进入施工；
- 明确提示可能发送到了错误线程；
- 有可靠依据时指出更可能的目标方向。

### AMBIGUOUS

只做最小澄清，不擅自把 scope 扩大为“都处理”。

### 命名

主统筹建议的子线程名称应跟随 Owner 常用语言，保持简短，不默认英语或内部开发术语。

本规则只增加输入防误投，不建立 Thread Router 或 Handoff Manager。
