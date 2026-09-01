# Research / Execution 分流与停止条件

## 目标

避免研究任务被套入完整工程施工治理，也避免“再多查一点”导致无限研究。

## 1. 先判断任务模式

```text
RESEARCH
EXECUTION
```

### RESEARCH

用于：

- 机制研究；
- 技术路线比较；
- GitHub / 开源复用审计；
- 架构研究；
- 外部资料研究；
- 方案可行性判断。

最小流程：

```text
Question → Evidence → Decision → Stop
```

RESEARCH 默认不创建完整 Execution TaskContract；但真实联网、外部账户动作、付费调用等仍遵守项目既有授权边界。

### EXECUTION

用于：

- 写代码；
- 修 Bug；
- 重构；
- 测试；
- 数据迁移；
- 工程实施。

EXECUTION 才进入项目既有卫兵 / TaskContract 治理。

## 2. Research Stop Condition

研究开始时尽量定义：

```yaml
decision_question:
required_evidence:
stop_condition:
```

当 required evidence 足以回答 decision question，且 stop condition 已满足：

> 停止继续扩展检索，输出 Decision。

只有发现会实质改变决策的新证据缺口时，才继续研究。

## 3. 研究转施工

当 Research 已形成足够 Decision，后续需要写代码或工程实施：

```text
RESEARCH CLOSED
→ 形成最小 authority
→ 重新评估当前任务
→ EXECUTION
→ 进入既有 TaskContract / 卫兵流程
```

禁止把 Research 阶段的临时假设直接当成 Execution authority。

## 4. 非目标

不建立 Research Manager、知识库数据库、自动检索循环或新的治理 Runtime。
