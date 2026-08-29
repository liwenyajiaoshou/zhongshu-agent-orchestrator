# 自主调试换挡与上下文压缩策略

## 工作模式
仅保留：
- NORMAL
- REPEATED_FAILURE_REVIEW
- BOUNDED_AUTONOMOUS_DEBUG

结果状态继续使用：
- PASS
- REPAIR
- PARTIAL
- BLOCKED
- KNOWN_ISSUE

验证状态单独使用：
- UNVERIFIED
- OFFLINE_PASS
- LIVE_VALIDATION_REQUIRED
- LIVE_VALIDATION_PASS

## 重复失败触发
以下任一信号即可进入评估：
- 同一目标连续 2～3 轮修复仍未 PASS；
- 修复 A 后立即暴露 B/C；
- 同一测试链路在多个模块反复失败；
- 第一次失败已确认跨模块或跨契约；
- 人工往返明显超过普通实现任务。

2～3 次只是参考，不是硬阈值。

## 全链审计
复杂调试前，优先建立：
`REQUIREMENT → IMPLEMENTATION → CALLER → STATE → OBSERVABILITY → TEST`

项目已有更合适的契约矩阵时优先复用。

## 受约束自主调试
允许：
`READ → DIAGNOSE → MODIFY → TEST → INSPECT → REPEAT`

停止条件：
- hard boundary required；
- offline acceptance pass；
- root cause cannot be resolved in allowed scope。

## 硬边界
边界内可自主：
- 本地代码、测试、fixture、mock、helper；
- temp data / test DB；
- 日志和 audit 可观测性；
- 不改变冻结语义的局部重构。

必须停止：
- 冻结业务语义变化；
- 正式 schema / contract；
- Fail Closed 放宽；
- Gold expected answer；
- 治理权限；
- 正式数据或生产写入；
- 新真实 API / 付费调用；
- 下载依赖；
- Git 发布动作；
- 下一 Milestone；
- Owner 决策。

## 离线优先
`离线复现 → fixture/mock/temp data → 本地闭环 → 回归 → 最少次数真实验证`

## Codex 上下文饱和

本节只增强现有 Codex Thread Handoff；不建立新的 Token 监控平台、自动终止器或 Context Manager。

### 四条原则
1. **Cached Context Is Not Free Context**：缓存上下文可降低部分重复输入成本，但不能消除上下文污染、注意力竞争和 stale state 风险。
2. **Token Is a Signal, Not a Threshold**：Token 量级只作为辅助信号，不设置机械硬阈值。
3. **Finish Local Value, Then Compress**：当前高价值局部任务仍强依赖现有上下文时，优先完成该局部任务；一旦形成稳定 PASS / OFFLINE_PASS / 明确 blocker，立即评估压缩交接。
4. **Preserve Authority, Drop Debug History**：新 Codex 线程继承当前 authority、关闭事项、边界和测试基线，不继承完整调试历史。

### 价值 / 噪声判断
```yaml
codex_context:
  current_task_value: HIGH | MEDIUM | LOW
  historical_noise: HIGH | MEDIUM | LOW
```
```text
HIGH value + LOW/MEDIUM noise → 保持当前线程
HIGH value + HIGH noise → 完成当前局部任务 → 压缩交接 → 新 Codex 线程
LOW value + HIGH noise → 优先立即换线程
LOW value + LOW noise → 正常按任务规模判断
```

### Context Saturation Review 触发参考
以下信号用于评估，不自动切线程：跨越多个 blocker、大量 `RESOLVED / DO NOT REOPEN`、多轮根因推翻、同一模块多次修补、cached input 很高、non-cached input 进入高负载区、重复调查已关闭问题、当前任务只依赖最近一小段上下文、后续任务性质变化。

禁止“超过 X token 必须换线程”、因 cached input 高就无限延长线程、当前高价值修复未收口时仅因 Token 数字强行中断。

### 最佳切换点
`当前局部任务 → PASS / OFFLINE_PASS / 明确 blocker → machine evidence / report → 压缩成 authority → 新 Codex 线程`

### 换线程不等于换模型
```yaml
switch_reason:
  MODEL_CAPABILITY
  CONTEXT_SATURATION
  TASK_PHASE_CHANGE
  MODEL_DOWNGRADE
  OTHER
```
若 `switch_reason = CONTEXT_SATURATION` 且模型能力仍足够：新开 Codex 线程，但模型可以保持不变。

## Codex 模型 / 推理等级 / 线程联合路由

本节**只适用于 Codex 线程**。不对网页版对话线程的模型切换做规定。

### 三项联合判断

每次考虑“换挡”时，中枢同时判断：

```text
1. Codex 上下文质量
2. 当前模型能力
3. 当前推理等级
```

### 推荐决策

```text
任务复杂度上升
↓
上下文是否健康且具有高价值？
├─ 否
│   → 新开 Codex 线程
│   → 模型按当前任务重新选择
│
└─ 是
    ↓
    当前模型能力是否足够？
    ├─ 是
    │   → 保持当前 Codex 线程
    │   → 保持当前模型
    │   → 优先提高推理等级
    │
    └─ 否
        → 生成压缩交接
        → 新开 Codex 线程
        → 升级模型
        → 推理等级按新任务重新设置
```

### 推理等级不足

适合“原线程 + 原模型 + 提高推理等级”的信号：

- 当前模型总体理解正确；
- 根因方向稳定；
- 任务仍属于当前模型适用范围；
- 上下文有效且干净；
- 没有持续遗漏关键跨模块约束；
- 主要问题是需要更深入分析。

### 模型能力不足

适合“新 Codex 线程 + 升级模型”的信号：

- 较高推理等级后仍多轮无法收敛；
- 持续遗漏跨模块关系；
- 无法稳定维护复杂约束；
- 根因判断反复推翻；
- 任务已经明显超出当前模型推荐档位。

### 上下文污染

上下文污染严重时，即使模型本身没有变化，也应新开 Codex 线程。

### 模型降级

高档模型完成复杂分析后，如果后续任务已经变成边界清晰、机械施工：

```text
高档模型 Codex 线程
→ 压缩交接
→ 新的较低档模型 Codex 线程
```

不建议在原长线程中直接降级模型。

### 原线程直接换模型的例外

只有在线程极短、尚未实质施工时允许：

- 刚创建；
- 尚未修改代码；
- 工具调用很少；
- 尚未形成重要中间判断；
- 没有需要保留的高价值上下文。

否则：

> **Codex 模型变化默认伴随 Codex 线程变化。**



## 术语
任何换线程建议必须写：
- 对话线程：继续 / 更换
- Codex 线程：继续 / 更换

禁止只说“建议换线程”。
