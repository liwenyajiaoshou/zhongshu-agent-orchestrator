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
出现大量旧失败路径、失效假设、重复补丁或重复调查已关闭问题时，优先新开 Codex 调试线程。

压缩交接只保留：
- CURRENT AUTHORITATIVE STATE
- RESOLVED / DO NOT REOPEN
- CURRENT BLOCKER
- ALLOWED SCOPE
- FORBIDDEN SCOPE
- STOP CONDITIONS
- LATEST TEST BASELINE

## 模型动态升级
`普通失败 → 当前线程低风险自主修正 → 重复失败复核 → 检查上下文污染 → 必要时先换 Codex 线程 → 仍需复杂跨层推理时再升级模型`

## 术语
任何换线程建议必须写：
- 对话线程：继续 / 更换
- Codex 线程：继续 / 更换

禁止只说“建议换线程”。
