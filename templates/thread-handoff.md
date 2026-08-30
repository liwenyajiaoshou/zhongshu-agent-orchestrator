# {{PROJECT}}｜对话线程 / Codex 线程交接

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
