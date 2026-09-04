# {{TASK_NAME}}｜施工方案

## 执行建议

- `execution_mode`: RESEARCH / EXECUTION
- `task_class`: A / B / C
- `inference_complexity`: LOW / MEDIUM / HIGH
- `recommended_tool`:
- `task_minimum_model_tier`: low / medium / high
- `current_codex_model`:
- `codex_model_action`: KEEP / UPGRADE / DOWNGRADE / NOT_APPLICABLE
- `reasoning_level`:
- `reasoning_action`: KEEP / INCREASE / DECREASE
- `model_routing_reason`: 
- `model_rebaseline_required`: true / false
- `multi_agent`: false / true
- `对话线程`: 继续 / 更换
- `Codex 线程`: 继续 / 更换
- `TUN`: on / off / unchanged
- `write_mode`: read-only / writable

注意：
- A/B/C 主要描述范围/风险，不与模型 tier 一一绑定；
- 新 Codex 线程必须重新按当前任务定级；
- 当前高价值线程模型可保持，但 reasoning 可升降；
- high tier 到 PASS / OFFLINE_PASS / 明确 blocker / 新任务边界时重新评估。

## research_contract

仅 `execution_mode = RESEARCH` 时填写：

```yaml
decision_question:
required_evidence: []
stop_condition:
```

达到 `stop_condition` 后停止继续扩展研究并输出 Decision。

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

## execution_gate

```yaml
execution_gate:
  local_read: CODEX_ALLOWED
  offline_test: CODEX_ALLOWED
  temp_write: CODEX_ALLOWED_WITHIN_SCOPE
  external_api: OWNER_GATE | GOVERNANCE_AUTHORIZED | NOT_APPLICABLE
  production_write: OWNER_GATE | GOVERNANCE_AUTHORIZED | NOT_APPLICABLE
  git_publish: OWNER_GATE | GOVERNANCE_AUTHORIZED | NOT_APPLICABLE
  release: OWNER_GATE | GOVERNANCE_AUTHORIZED | NOT_APPLICABLE

owner_action:
  required: true | false
  reason:
  exact_command:
  max_calls:
  post_action_artifacts: []

owner_action_preflight:
  autonomous_debug_exhausted: true | false | NOT_APPLICABLE
  codex_terminal_self_tested: true | false | NOT_APPLICABLE
  artifact_parse_validated: PASS | FAIL | NOT_APPLICABLE
  dry_run_passed: PASS | FAIL | NOT_APPLICABLE
  workspace_or_repo_sanity: PASS | FAIL | UNKNOWN | NOT_APPLICABLE
  input_manifest_validation: PASS | FAIL | UNKNOWN | NOT_APPLICABLE
  collision_check: PASS | FAIL | UNKNOWN | NOT_APPLICABLE
  host_runtime_simulated_or_invoked: true | false | NOT_APPLICABLE
  common_prewrite_path_tested: true | false | NOT_APPLICABLE
  ordinary_failures_remaining: 0
  remaining_owner_action_is_irreducible: true | false | NOT_APPLICABLE
  expected_owner_commands: 0 | 1
```

PowerShell / Shell / Python / CLI 不作为 Owner Gate 判据。
复杂本地 Host orchestration 默认优先任务级 Python runner；PowerShell 5.1 仅作短命令/薄 wrapper/legacy fallback。

## debug_escalation

仅复杂调试时填写：

```yaml
mode: NORMAL | REPEATED_FAILURE_REVIEW | BOUNDED_AUTONOMOUS_DEBUG
trigger_reasons: []
full_chain_audit_required: false
offline_first: true
validation_state: UNVERIFIED | OFFLINE_PASS | LIVE_VALIDATION_REQUIRED | LIVE_VALIDATION_PASS
```

## stop_conditions

遇到以下情况停止并报告：
- 需要超出当前授权的真实联网 / 外部 API；
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
