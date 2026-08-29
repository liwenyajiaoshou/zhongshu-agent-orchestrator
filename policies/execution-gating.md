# Host 执行门与 Owner Gate 最小化策略

## 目标

减少没有治理收益的人工搬运步骤，把 Owner 注意力保留给真正的风险决策。

## 原则一：Execution Form Is Not Risk

PowerShell、Shell、Python、CLI 只是执行载体，不是风险类别。

判断执行主体时，必须看：

```text
真实副作用
+
治理授权边界
+
执行环境能力
```

而不是看命令长什么样。

## 原则二：Minimum Owner Gate

当任务触碰硬边界时，只把无法由 Codex 在现有权限/环境中安全完成的最小动作交给 Owner。

典型流程：

```text
Codex:
READ
→ DIAGNOSE
→ MODIFY
→ OFFLINE TEST
→ PREFLIGHT
→ 生成唯一 Owner Action

Owner:
执行唯一 hard-boundary action
→ 回复“已执行”

Codex:
读取 machine-readable artifacts
→ 判断 PASS / REPAIR / BLOCKED
→ 继续调试或收口
```

## 原则三：Machine-Readable Handoff After Owner Action

Owner Action 应尽量产出稳定文件，例如：

```text
result.json
audit.json
report.md
receipt.json
```

Owner 不承担日志搬运职责。

只有以下情况才要求额外人工证据：
- artifact 不存在；
- Codex 当前环境无法读取 Host artifact；
- 权限限制导致无法访问；
- 必须由人进行业务语义判断。

## 默认 Codex 可自主执行

在 allowed_scope 内：
- 本地只读；
- 文件读取；
- 状态读取；
- hash；
- compile；
- unit / integration tests；
- fixture / mock；
- temp / test data；
- 日志 / audit 读取；
- 只读 Git；
- 已授权范围内本地代码施工。

## 默认需要 Owner Gate 或既有治理授权

- 新真实联网；
- 外部 API；
- 付费调用；
- 联网下载依赖；
- 正式数据库写入；
- 生产数据 / 生产资产；
- 生产业务语义变化；
- Git publish；
- release；
- 不可逆 Git；
- 需要人工业务判断的语义变化。

## Host 与 Sandbox

需要判断：

```text
是否需要 Host-specific capability？
↓
否 → Codex 自主
是
↓
Codex 当前环境是否具备且已授权？
├─ 是 → Codex 执行
└─ 否 → Owner 只执行该 Host Action
```

Host-specific 不等于 Owner-only。

## 与自主调试结合

```text
BOUNDED_AUTONOMOUS_DEBUG
→ OFFLINE_PASS
→ 是否需要 hard-boundary validation？
├─ 否 → PASS
└─ 是
    → OWNER_ACTION_REQUIRED
    → Owner 执行唯一动作
    → Codex 自动读取 artifacts
    → LIVE_VALIDATION_PASS / REPAIR
```

## 非目标

不建立：
- Execution Manager；
- 第二套 Governance Runtime；
- Stage Manager；
- Host automation platform；
- 默认自动真实 API；
- 无限重试机制。
