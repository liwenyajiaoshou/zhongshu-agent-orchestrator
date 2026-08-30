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
