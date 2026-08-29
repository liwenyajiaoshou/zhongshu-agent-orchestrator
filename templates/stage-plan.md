# {{TASK_NAME}}｜施工方案

## 执行建议

- `task_class`: A / B / C
- `recommended_tool`:
- `recommended_model_tier`:
- `reasoning_level`:
- `multi_agent`: false / true
- `对话线程`: 继续 / 更换
- `Codex 线程`: 继续 / 更换
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
