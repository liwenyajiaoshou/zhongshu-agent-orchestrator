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


## Research Contract Must Precede Research Mode

在选择普通联网研究或 Deep Research 前，先冻结最小 Research Contract：

```yaml
research_contract:
  decision_question:
  entities:
  entity_disambiguation:
  cutoff:
  required_evidence:
  evidence_schema:
  forbidden_inference:
  stop_condition:
  final_decision_format:
```

简单任务可以简写，但不得先选研究模式、后猜研究目标。

核心顺序：

```text
Question
→ Evidence Requirement
→ Entity / Cutoff / Evidence Schema
→ Search Difficulty
→ Mode Selection
→ Research
→ Independent Audit
→ Decision
→ Stop
```

---

## Deep Research Is a Retrieval Multiplier, Not a Quality Guarantee

Deep Research 只代表更强的检索、来源覆盖与跨来源探索能力，不代表研究质量自动更高。

禁止隐式映射：

```text
任务重要 → Deep Research
任务复杂 → Deep Research
要求高质量 → Deep Research
```

研究质量仍由以下因素决定：

- entity 是否正确；
- cutoff 是否遵守；
- evidence schema 是否服从；
- primary source 是否足够；
- event / historical chain 是否真正建立；
- decision-critical evidence gap 是否减少；
- stop condition 是否真的满足。

---

## Normal Research First, Deep on Explicit Gaps

默认：

```yaml
research_routing:
  mode: NORMAL
```

普通联网研究完成结构化 Evidence 后，执行 Gap Review。

只有存在明确、会影响 Decision 的 evidence gap 时，才升级：

```yaml
research_routing:
  mode: TARGETED_DEEP
  decision_critical_evidence_gap:
  deep_trigger_reason:
```

推荐 `deep_trigger_reason`：

```text
EARLIEST_ANCHOR_GAP
FRAGMENTED_PRIMARY_SOURCES
CROSS_SOURCE_CONFLICT
MULTI_LANGUAGE_EVIDENCE
EXHAUSTIVE_RECALL_GAP
ORDINARY_RESEARCH_BLOCKED
```

Deep Research 应针对已知 gap，不接受模糊的“再研究深一点”。

---

## Research Depth Is Evidence Depth, Not Search Volume

Research depth 不以以下指标为主要判断：

```text
source_count
report_length
search_volume
```

优先看：

```yaml
depth_evidence:
  event_chain_depth:
  earliest_verified_anchor_quality:
  primary_source_quality:
  contradiction_handling:
  evidence_gap_resolution:
```

如果新增搜索没有改变 Decision、Evidence sufficiency、Historical relation、Case classification 或 blocker 判断，则其边际收益可能已经很低，应考虑停止。

---

## Independent Research Audit

普通联网研究与 Targeted Deep Research 使用同一质量门槛。

至少检查：

```yaml
research_quality:
  entity_integrity:
  cutoff_integrity:
  primary_source_quality:
  evidence_traceability:
  historical_chain_depth:
  semantic_contract_fidelity:
  evidence_gap_honesty:
  stop_condition_fidelity:
  unsupported_conclusion_risk:
```

重要规则：

```text
Deep Research 完成
!=
Research PASS
```

如果 mode 已完成但 Decision evidence 不足：

```text
RESEARCH_INCOMPLETE
```

不得因使用高级研究模式而默认 PASS。

---

## Small-Sample Mode Validation

昂贵、长时间或高范围 Research 在扩大前优先做小样本：

```text
1 个主题
+
1 条关键 evidence chain
+
2～3 个 representative cases
```

先检查：

- entity 是否稳定；
- evidence schema 是否服从；
- cutoff 是否稳定；
- evidence trace 是否可用；
- 当前 Research Mode 是否真的带来增益。

如果样本阶段出现明显 semantic drift：

```text
STOP
→ 修正 Research Contract
→ 重新评估 mode
```

不得继续扩大错误方向。

---

## A/B Research Contamination

仅当任务明确比较：

```text
Deep Research vs Normal Research
Model A vs Model B
Agent vs Single Thread
```

时启用。

至少记录：

```yaml
ab_research_integrity:
  same_prompt:
  same_cutoff:
  same_evidence_schema:
  same_stop_condition:
  no_cross_group_final_output:
  file_library_contamination:
  shared_project_context_contamination:
  retrieved_snippet_contamination:
```

如果存在 File Library / shared project context / retrieved snippet contamination：

> 可以形成 practical workflow conclusion，但不得宣称严格 blind superiority。

---

## Research Mode Independence

必须保持：

```text
Research Mode
!= Model Tier
!= Agent Count
!= Task Class
```

分别判断：

```yaml
research_mode:
  由外部 evidence retrieval 难度决定

model_tier:
  由推理复杂度与已观察能力决定

agent_count:
  由并行独立性与上下文污染风险决定

task_class:
  由范围、风险与副作用决定
```

Deep Research 不自动意味着 high model、more agents 或 C 类任务。
