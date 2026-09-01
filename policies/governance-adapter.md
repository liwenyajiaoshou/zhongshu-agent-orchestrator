# Governance Adapter｜中枢—卫兵适配规则

## 目标

让中枢可以消费不同版本卫兵或其他既有治理框架的事实，而不把某个版本作为硬依赖。

## 三种能力状态

```yaml
interface_capability:
  rules: AVAILABLE | PARTIAL | UNKNOWN
  workspace_baseline: AVAILABLE | PARTIAL | UNKNOWN
  workspace_health: AVAILABLE | PARTIAL | UNKNOWN
  change_delta: AVAILABLE | PARTIAL | UNKNOWN
  hygiene: AVAILABLE | PARTIAL | UNKNOWN
  snapshot_readiness: AVAILABLE | PARTIAL | UNKNOWN
  multi_agent_isolation: AVAILABLE | PARTIAL | UNKNOWN
```

## 适配顺序

1. 检查项目内最新 `AGENTS.md`、规则索引和项目特定治理规则；
2. 检查是否存在卫兵或其他治理框架；
3. 读取现有施工报告中已经输出的治理事实；
4. 对缺失字段标 `PARTIAL/UNKNOWN`；
5. 只有当缺失字段实质阻塞重大决策时，才安排只读 Reality Check；
6. Reality Check 必须先确认“已有 / 只缺接线 / 只缺字段 / 真正缺失”；
7. 只有确认真缺口后才允许另立可写施工方案。

## 禁止

- 中枢新增 Workspace Baseline Engine；
- 中枢新增 ChangeTracker；
- 中枢新增 WorkspaceHistoryDB；
- 中枢新增 Stage Manager；
- 中枢新增 Multi-Agent Orchestrator；
- 因接口名不同而把已有卫兵能力重写一遍。

## 无卫兵项目

无卫兵不等于中枢停止工作。

中枢可以继续：
- Alignment；
- MVP / Stage；
- Routing；
- 生成治理部署方案；
- 生成只读检查方案。

但中枢不得临时扮演完整卫兵。

## Web GPT 可见性约束

如果网页版 GPT 当前不能读取真实本地仓库：
- 明确写“当前无法直接核验本机仓库”；
- 可以基于最新施工报告做项目级判断；
- 不得声称已验证当前 Git 状态或真实代码实现；
- 如确需机器事实，生成 Codex 只读 Reality Check。


## 中枢—卫兵最小语义接口

中枢只要求概念可映射，不要求卫兵使用完全相同字段名：

```yaml
project_phase:
execution_mode: RESEARCH | EXECUTION
task_class: A | B | C
task_contract_status: NONE | ACTIVE | CLOSED | SUPERSEDED
workspace_state:
risk_state:
closure_state:
next_allowed_action:
```

规则：

1. 已有同义字段优先复用；
2. 缺失但不阻塞当前决策时允许 `UNKNOWN`；
3. 不因为命名不同就新建第二套字段；
4. 如发现中枢与卫兵语义冲突，只记录冲突与最小兼容建议；
5. 不跨项目修改卫兵。
