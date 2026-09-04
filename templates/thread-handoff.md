# {{PROJECT}}｜对话线程 / Codex 线程交接

## 交接模式

```yaml
handoff_mode: FULL | DELTA
base:
```

- 普通长线程切换默认 `DELTA`；
- 新项目、大阶段切换、authority 失效、重大架构变化或 base 不足时才用 `FULL`。

### DELTA 必填

```yaml
changes_since_base:
closed:
new_blockers:
current_next_action:
authoritative_sources:
```

## 项目

{{PROJECT_SUMMARY}}

## 已完成

- 

## 当前权威文件

- 

## 当前治理入口

- `AGENTS.md`：
- 规则索引：
- 最新施工报告：

## Owner 已冻结决策

- 

## 当前阶段

- 

## 当前状态

- PASS / REPAIR / PARTIAL / BLOCKED
- Workspace Health：
- 外部阻塞：

## 禁止重新讨论 / 重复建设

- 

## 下一步

- 

## 新线程启动要求

先读取上述权威文件，先定位后读取；不要要求 Owner 重复完整历史；若当前设备无法访问真实仓库，明确能力边界，不伪造 Reality Check。


## 线程建议

```text
对话线程：继续 / 更换
Codex 线程：继续 / 更换
```

如更换 Codex 线程，明确是“Codex 施工线程”还是“Codex 调试线程”。



## CURRENT AUTHORITATIVE STATE

```yaml
current_phase:
status:
active_task_contract:
last_verified_state:
known_blockers:
current_next_action:
authoritative_sources:
```

## 新对话线程启动提示词

```text
你现在接管「{{PROJECT}}」项目统筹。

请先到 ChatGPT 文件库检索并读取：
<THIS_HANDOFF_FILENAME>

读取后：
1. 以文档中的 CURRENT AUTHORITATIVE STATE 为当前权威状态；
2. 只按 authoritative_sources 读取必要证据；
3. 不回扫完整历史；
4. 不重新打开 RESOLVED / DO NOT REOPEN；
5. 按 current_next_action 直接接管推进。

如果文件库找不到该交接文档，明确报告“未找到指定交接文档”，不要凭历史猜测项目状态。
```

## Codex 上下文压缩（仅换 Codex 线程时）

```text
CURRENT AUTHORITATIVE STATE

RESOLVED / DO NOT REOPEN

CURRENT BLOCKER

ALLOWED SCOPE

FORBIDDEN SCOPE

STOP CONDITIONS

LATEST TEST BASELINE
```

## Codex 上下文饱和判断（仅 Codex 换线程时）
```yaml
codex_context:
  current_task_value: HIGH | MEDIUM | LOW
  historical_noise: HIGH | MEDIUM | LOW
  switch_reason: MODEL_CAPABILITY | CONTEXT_SATURATION | TASK_PHASE_CHANGE | MODEL_DOWNGRADE | OTHER
  recommendation: KEEP | FINISH_THEN_SWITCH | SWITCH_NOW
```
规则：不设置 Token 硬阈值；Token 只作辅助信号；当前高价值局部任务未收口时不因 Token 大而强行切换；到 PASS / OFFLINE_PASS / 明确 blocker 后优先压缩；`CONTEXT_SATURATION` 不自动意味着换模型。

## 压缩原则
只保留当前 authority，不复制完整调试历史。优先保留当前阶段与状态、最新有效 contract/schema/data authority、最新 offline/live evidence、已关闭根因与禁止重查项、当前 blocker、允许/禁止范围和最新测试基线。删除或省略旧失败日志、旧 prompt、被推翻假设过程、重复命令输出及与下一任务无关的历史实现细节。


## 新 Codex 线程模型重新定级

```yaml
task_minimum_model_tier:
previous_codex_model:
previous_model_is_authority: false
model_rebaseline_required: true
switch_reason:
```

新 Codex 线程不得仅因上一线程使用 high tier 就自动继承 high tier。


## 子统筹线程启动（仅主统筹 → 子统筹时使用）

```yaml
thread_name:
target_direction:
current_stage:
allowed_scope:
forbidden_scope:
authoritative_sources:
current_next_action:
```

### 子线程第一步

```text
先做 Scope Match Check：
比较当前收到的任务/文档与 target_direction、current_stage、allowed_scope、authoritative_sources。

若 MISMATCH：
- 不吸收为 authority；
- 不施工；
- 提示“当前指令与本线程方向不匹配，可能发送到了错误线程”。

若 AMBIGUOUS：
- 只请求最小澄清；
- 不擅自扩 scope。

只有 PASS 后再按 authoritative_sources 读取必要证据并推进。
```

### 命名

`thread_name` 优先使用 Owner 常用语言，保持短、直观，不默认英语、内部术语或缩写堆叠。
