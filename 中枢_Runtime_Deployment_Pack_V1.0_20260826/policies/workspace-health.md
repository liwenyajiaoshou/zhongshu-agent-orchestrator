# Workspace Health｜项目级判断策略

## 两层状态

卫兵底层：
```yaml
worktree_state: CLEAN | ACCEPTED_DIRTY
```

中枢消费的派生信号：
```yaml
workspace_health:
  status: CLEAN | HEALTHY_DIRTY | NEEDS_CLOSURE | HIGH_RISK_DIRTY
  reason_codes: []
```

## 判断顺序

1. 变更能否归属；
2. 是否属于当前阶段；
3. 是否有恢复路径；
4. 是否触碰关键源码/正式数据资产；
5. 是否存在未知来源变化；
6. 是否跨阶段累计；
7. 是否属于可再生成产物；
8. 文件数量只做辅助。

## 动作

### CLEAN
继续。

### HEALTHY_DIRTY
允许继续当前阶段。
如果接近稳定里程碑，可提示安全快照，但不得自动 commit。

### NEEDS_CLOSURE
不直接开新的大阶段。
先完成：
- 归属确认；
- 临时/生成产物卫生处理建议；
- 必要测试；
- snapshot readiness 判断。

### HIGH_RISK_DIRTY
停止普通可写施工。
先做只读盘点/恢复方案。
禁止自动 reset / clean / checkout / rebase / force。

## Repository Hygiene

优先检查：
- `.gitignore`
- build / dist / cache
- test output
- log
- screenshot
- downloads
- local DB
- regenerable large data
- Agent 临时文件

已有目录规范优先复用。
不强制创建 `.agent-tmp/`。

## 核心原则

> No New Stage on Unexplained Dirty Workspace.
