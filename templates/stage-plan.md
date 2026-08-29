# {{TASK_NAME}}｜施工方案

## 执行建议

- `task_class`: A / B / C
- `recommended_tool`:
- `recommended_model_tier`:
- `reasoning_level`:
- `multi_agent`: false / true
- `对话线程`: 继续 / 更换
- `Codex 线程`: 继续 / 更换
- `Codex 模型动作`: 保持 / 升级 / 降级
- `推理等级动作`: 保持 / 提高 / 降低
- `模型切换方式`: 不适用 / 原线程低上下文切换 / 新 Codex 线程压缩交接
- `TUN`: on / off / unchanged
- `write_mode`: read-only / writable

## task_goal

{{GOAL}}

## workspace

`{{WORKSPACE}}`

## plan_path

`{{PLAN_PATH}}`

## allowed_scope

- 

## forbidden_scope

- 不超出本任务主目标；
- 不覆盖项目内最新且更严格治理规则；
- 未授权不 commit / push / PR / tag / release；
- 不执行 reset / clean / rebase / force；
- 未授权不真实联网、不下载依赖；
- 未授权不写正式数据或生产资产。

## required_tests

1. 开工先定位现有测试入口；
2. 先运行最小定向测试；
3. 再按风险决定回归范围；
4. 未执行测试必须明确记录。

## acceptance_criteria

- 

## boundaries

- `git_boundary`:
- `network_boundary`:
- `data_write_boundary`:
- `release_boundary`:

## stop_conditions

遇到以下情况停止并报告：
- 需要真实联网 / 外部 API；
- 需要联网下载依赖；
- 需要正式数据写入；
- 需要生产资产/生产业务语义变化；
- 需要不可逆 Git；
- 需要发布；
- 风险从当前等级明显升级；
- 需要 Owner 人工决策；
- 发现项目治理规则冲突；
- 工作区出现无法解释的新变化。

## low_risk_autonomy

在主目标和风险边界不变的前提下，允许 Agent 自主处理 fixture、helper、mock、临时目录、测试隔离、同目标测试补充和报告修正，不为这些事项另立方案。

## report_path

`{{REPORT_PATH}}`

报告保持精简，不回显完整 Diff 或完整测试日志。


## debug_escalation

仅复杂调试时填写：

```yaml
mode: NORMAL | REPEATED_FAILURE_REVIEW | BOUNDED_AUTONOMOUS_DEBUG
trigger_reasons: []
full_chain_audit_required: false
offline_first: true
validation_state: UNVERIFIED | OFFLINE_PASS | LIVE_VALIDATION_REQUIRED | LIVE_VALIDATION_PASS
```


## Codex 换挡判定

当推荐调整模型或推理等级时，必须说明：

```yaml
codex_context_quality: HIGH | MEDIUM | LOW
current_model_capability: SUFFICIENT | INSUFFICIENT | UNCERTAIN
reasoning_budget: SUFFICIENT | INSUFFICIENT | UNCERTAIN
decision:
  keep_thread: true | false
  keep_model: true | false
  change_reasoning: KEEP | INCREASE | DECREASE
  target_model_tier:
handoff_required: true | false
```

默认规则：
- 模型够 + 上下文高价值 → 原 Codex 线程，提高推理等级；
- 模型不够 + 已有实质上下文 → 新 Codex 线程，升级模型；
- 上下文污染 → 新 Codex 线程，模型重新按任务选择；
- 原线程直接换模型仅允许在线程极短且尚未实质施工时。
