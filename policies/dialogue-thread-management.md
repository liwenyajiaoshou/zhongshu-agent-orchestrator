# 网页对话线程治理｜Dialogue Thread Management

## 目标

规范网页版 GPT 的阶段对话线程何时继续、何时分流 blocker、何时因上下文膨胀更换线程。

本策略只作用于“对话线程”，不替代 Codex Thread Handoff。

---

## 1. Blocker Thread Split

子阶段施工过程中出现新的 blocker 时，不默认开启独立对话线程。

### 继续当前阶段对话线程

满足多数条件时继续当前线程：
- blocker 仍属于当前子阶段主链路；
- 强依赖当前线程已有上下文；
- 预计少量轮次即可闭环；
- 解决后可以直接恢复当前施工；
- 不需要形成独立研究/修复 authority。

### 新开“问题处理对话线程”

满足以下任一强信号时建议分流：
- blocker 已形成相对独立的研究/修复单元；
- 预计需要较长处理；
- 需要大量新资料、新分析或独立验证；
- 会显著污染当前阶段主线程；
- 需要独立形成方案、证据或结论后再回填主阶段；
- 当前阶段主线已经被 blocker 讨论长期挤占。

推荐流程：

```text
阶段对话线程
→ 发现独立 blocker
→ 问题处理对话线程
→ blocker 闭环
→ 压缩结论 / authority
→ 回到阶段对话线程继续
```

原则：

> 新问题独立，不等于必须新开线程；只有当分流能明显提高主阶段上下文质量和推进效率时才分流。

---

## 2. Dialogue Context Saturation Review

网页对话线程也需要轻量上下文饱和判断，但不设置机械轮次阈值。

50～100 次对话可视为强信号，但不是硬规则。

### 触发参考

满足以下任一情况时应评估：
- 经常重新解释已确认事实；
- 已关闭 blocker 与当前 blocker 混杂；
- 已解决问题被反复重新讨论；
- 很难快速说清当前 authoritative state；
- 当前任务只依赖最近几轮，但历史占比很大；
- 已跨越多个 blocker / 子任务；
- 每次下一步都要重新梳理大量旧背景；
- 用户需要频繁提醒“我们现在做到哪了”；
- 对话轮次已经非常长，例如 50～100 次以上。

### 不设置硬阈值

禁止：

```text
超过 50 次必须换线程
超过 100 次自动换线程
```

轮次只作为辅助信号。

真正判断依据：

```text
当前有效上下文价值
vs
历史噪声 / 失效上下文
```

---

## 3. 最佳切换点

不要在当前高价值局部任务进行到一半时仅因线程很长强行切换。

推荐：

```text
当前局部任务仍在处理
→ 先完成

达到 PASS / 明确 blocker / 稳定语义边界
→ 压缩交接
→ 新阶段对话线程
```

原则：

> Finish Local Dialogue Value, Then Compress.

---

## 4. 对话线程压缩交接

新阶段对话线程只继承：

- CURRENT AUTHORITATIVE STATE
- RESOLVED / DO NOT REOPEN
- CURRENT BLOCKER
- CURRENT STAGE / SUBSTAGE
- ALLOWED / FORBIDDEN SCOPE
- LATEST TEST / REPORT BASELINE
- NEXT ACTION

不要复制：
- 完整历史对话；
- 详细失败过程；
- 已被推翻的猜测；
- 重复命令和测试日志；
- 与下一步无关的旧分析。

---

## 5. 与 Codex 线程分开

必须明确：

```text
对话线程：网页版 GPT 上下文
Codex 线程：Codex CLI / Client 上下文
```

两者可以独立判断：

```text
对话线程：更换
Codex 线程：继续
```

或：

```text
对话线程：继续
Codex 线程：更换
```

不得把两类线程绑定。

---

## 6. 首次项目部署的交互视角

统筹对话线程第一次在项目中部署/接管时，如果 Owner 尚未明确表达偏好，应主动询问：

```text
用户视角
开发者视角
```

- 用户视角：后续网页回复优先说明功能、问题、实际影响和 Owner 是否需要操作，尽量不用术语；
- 开发者视角：可保留工程状态、治理边界、测试、线程、模型和实现细节。

该偏好只控制网页表达层，不改变底层治理和 evidence 标准。

---

## 7. 子统筹线程启动校验

### 主统筹发布指令

主统筹新开子统筹线程时，启动提示词至少提供：

```yaml
thread_name:
target_direction:
current_stage:
allowed_scope:
forbidden_scope:
authoritative_sources:
```

### 子统筹第一步：Scope Match Check

在大量读取、吸收新 authority 或进入施工前，先判断：

```text
当前收到的任务 / 文档
是否与
本线程 target_direction / current_stage / allowed_scope / authority
匹配
```

结果：

```yaml
scope_match:
  status: PASS | MISMATCH | AMBIGUOUS
  conflicts: []
```

- `PASS`：继续；
- `MISMATCH`：停止吸收和施工，提示可能发错线程；
- `AMBIGUOUS`：做最小澄清，不擅自扩 scope。

若有足够依据，可提示更可能对应的线程/方向；无依据时不要猜。

此检查优先于全文历史扫描和写操作。

### 子线程命名

名称必须：
- 跟随用户常用语言；
- 短、自然、易识别；
- 优先“对象 + 任务 / 阶段”；
- 不默认英语、内部开发术语或缩写串。

---

## 8. 非目标

不建立：
- Dialogue Context Manager；
- 自动轮次计数器；
- 自动终止线程；
- Token / message 数量硬阈值；
- 自动跨线程复制完整历史。

目标只是：
> 在网页对话长期施工中，及时分流独立 blocker，并在主线程历史噪声过高时选择合适的语义边界进行压缩换线程。
