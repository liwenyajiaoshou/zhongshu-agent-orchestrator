# {{TASK_NAME}}｜施工报告

## status

PASS / REPAIR / PARTIAL / BLOCKED

## execution_context

```yaml
actual_model:
actual_reasoning_level:
codex_thread:
```

用于中枢审计实际施工质量；实际模型与方案推荐不同不自动视为问题。

## changes

- 实际修改摘要：

## tests

- `命令` → 结果
- 未执行项必须明确写“未执行”

## workspace

```yaml
worktree_state:
workspace_health:
pre_existing_changes:
task_created_changes:
unexplained_workspace_changes:
hygiene_recommendations:
milestone_snapshot_readiness:
```

若当前治理版本不提供某字段，写 `UNKNOWN`，不要伪造。

## boundaries

```yaml
network:
git_writes:
data_writes:
release_actions:
```

## execution_gate

```yaml
owner_action:
  required:
  reason:
  executed:
  machine_readable_artifacts:
  codex_post_action_readback:
```



### Owner Gate 异常证据（仅异常分支必填）

仅当：

```text
Owner 已报告执行
+
预期 machine-readable artifacts 缺失 / 不可读 / 不可访问
```

时填写：

```yaml
execution_gate_evidence:
  exact_owner_action:
  owner_reported_execution:
  execution_time_window:
  process_exit_status:
  stdout_stderr_evidence:
  expected_first_artifact:
  expected_artifact_path:
  post_action_directory_state:
  runner_started:
  external_request_started:
  artifact_writer_started:

blocker_attribution:
  category:
  confidence:
  evidence:

remaining_evidence_gap:
  - ...
```

规则：
- 无法确认写 `UNKNOWN`；
- 不猜测；
- 不因异常补证自动 retry；
- 不要求 Owner 默认搬运完整日志；
- 优先由 Codex 只读恢复本机已有 evidence。

## quality_observations

只记录可观察事实，不要求 Codex 自行给自己做“模型能力判定”：

- 是否多轮重复修同一目标：
- 是否出现根因反复推翻：
- 是否持续遗漏跨模块关系：
- 是否存在上下文重复调查：
- 其他明显施工质量问题：

## issues

- 

## next

- 


## review_diagnostic_hints

供中枢 REPORT_REVIEW 使用，不要求执行 Agent 自行归因：

```yaml
possible_review_causes:
  - PLAN_OR_CODE_DEFECT
  - MODEL_CAPABILITY_LIMIT
  - REASONING_LEVEL_INSUFFICIENT
  - CONTEXT_SATURATION
  - GOVERNANCE_FALSE_BLOCK
  - ENVIRONMENT_OR_TOOLING
  - REAL_EXTERNAL_BLOCKER
  - TEST_OR_DATA
  - TASK_SPEC_AMBIGUITY
  - UNKNOWN
```
