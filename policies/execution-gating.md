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


## Machine-Readable Handoff Failure｜异常证据恢复

正常路径保持不变：

```text
Owner 执行唯一 hard-boundary action
→ 回复“已执行”
→ Codex 自动读取 machine-readable artifacts
→ 继续判断
```

当同时满足：

```yaml
owner_action.executed: true | OWNER_REPORTED
machine_readable_artifacts: MISSING | UNREADABLE | INACCESSIBLE
```

自动进入异常证据恢复分支：

```text
STOP
→ NO RETRY
→ NO SECOND LIVE
→ READ-ONLY EXECUTION EVIDENCE RECOVERY
→ MINIMAL BLOCKER ATTRIBUTION
```

规则：

1. **Owner 报告“已执行”不等于 runner 已启动。**
2. 不得自动推断外部 API 已发起。
3. 不得自动推断 artifact writer 已启动。
4. 不得因 artifact 缺失自动进入代码修复或允许第二次真实调用。
5. 优先从当前机器已有事实恢复证据：
   - receipt / result / audit；
   - runtime log；
   - 目录与文件时间戳；
   - shell history（若可安全读取）；
   - 进程退出状态；
   - runner 自身稳定日志；
   - 预期 artifact 路径及目录变化。
6. Codex 无法获得机器事实时，才向 Owner 请求**最小必要证据**，不得默认要求完整 stdout/stderr 或截图。

### 最小 decision-critical evidence

异常分支至少尝试形成：

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
```

无法确认的字段必须写：

```text
UNKNOWN
```

不得猜测。

同时形成：

```yaml
blocker_attribution:
  category:
    - OWNER_EXECUTION_UNVERIFIED
    - RUNNER_START_FAILURE
    - ENVIRONMENT_OR_TOOLING
    - ARTIFACT_PERSISTENCE_FAILURE
    - PERMISSION_OR_PATH
    - UNKNOWN
  confidence:
  evidence:

remaining_evidence_gap:
  - ...
```

这只是既有 Owner Gate 的异常恢复分支，不是新的 Execution Manager 或 Owner Gate 状态机。


## Host Action Must Be Irreducible

`Minimum Owner Gate` 的进一步要求是：

> 在把动作交给 Owner 前，Codex 必须先耗尽当前环境内所有可安全执行的非 hard-boundary 诊断、修复、终端测试、DryRun 与 preflight。

Owner 不承担：
- 首次发现脚本语法错误；
- 首次发现路径 / 编码 / quoting 问题；
- native command exit-code 调试；
- manifest / staged state / branch-worktree collision 只读检查；
- 普通 Host runtime compatibility 调试；
- DryRun 首次验证。

进入 Owner Gate 前建议形成：

```yaml
owner_action_preflight:
  autonomous_debug_exhausted: true | false
  all_non_hard_boundary_steps_exhausted: true | false
  codex_terminal_self_tested: true | false
  artifact_generated: true | false
  artifact_parse_validated: true | false
  dry_run_available: true | false
  dry_run_passed: true | false
  workspace_or_repo_sanity: PASS | FAIL | UNKNOWN
  input_manifest_validation: PASS | FAIL | UNKNOWN
  collision_check: PASS | FAIL | UNKNOWN
  forbidden_action_check: PASS | FAIL | UNKNOWN
  host_runtime_simulated_or_invoked: true | false
  common_prewrite_path_tested: true | false
  ordinary_failures_remaining:
  remaining_owner_action_is_irreducible: true | false
  expected_owner_commands:
```

默认只有：

```yaml
autonomous_debug_exhausted: true
ordinary_failures_remaining: 0
remaining_owner_action_is_irreducible: true
expected_owner_commands: 1
```

才进入最终 Owner handoff。

如果同一 hard boundary 下连续要求 Owner 手工执行多轮普通测试，应视为：

```text
OWNER_HANDOFF_NOT_MINIMIZED
```

并退回 Codex 自主调试。

---

## Common Prewrite Path

当 Owner Action 依赖脚本或 runner：

```text
COMMON INITIALIZATION
→ workspace/repo discovery
→ path normalization
→ sanity checks
→ pre-existing state
→ manifest/input validation
→ collision checks
→ all pre-write preparation
→ PREWRITE_BOUNDARY
→ if preflight: emit machine-readable result + exit
→ if execute: first real side effect
→ post-action readback
```

原则：

> preflight 与 execute 必须尽量共享相同的 pre-write 路径；分叉点应尽量晚到第一条真实副作用之前。

不得用一套简化 DryRun 代替正式执行路径的关键初始化和检查。

---

## Complex Host Automation Language Routing

执行语言只按任务形态选择，不改变治理边界：

```yaml
host_execution_routing:
  codex_direct: PREFERRED_IF_CAPABLE
  complex_local_automation: PYTHON_RUNNER
  windows_system_administration: POWERSHELL_7
  powershell_5_1: THIN_WRAPPER_OR_LEGACY_FALLBACK
```

### Python runner 适合

当任务同时包含多项：
- Unicode / 非 ASCII 路径；
- Git subprocess orchestration；
- exact manifest；
- staged equality；
- branch/worktree lifecycle；
- machine-readable preflight；
- 多阶段本地安全检查。

推荐任务级薄 runner：

```text
python <task_runner.py> --preflight
python <task_runner.py> --execute
```

Codex 负责 build / self-test / preflight / repair；Owner 默认只执行最终一次 `--execute`。

### PowerShell

- Windows Registry / Service / OS policy / 系统管理：优先 PowerShell 7；
- Windows PowerShell 5.1：只用于短命令、薄 wrapper 或 legacy fallback；
- 若复杂 `.ps1` 连续出现 encoding / Provider / native command / path / runtime compatibility 问题，应评估语言换挡，而不是无限修补。

> 换执行语言不能绕过 Owner Gate，也不能扩大 Git / API / production side-effect 授权。
