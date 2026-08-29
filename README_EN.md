<p align="right">
  <strong>Language:</strong>
  <a href="README.md">简体中文</a> · English
</p>

<h1 align="center">Zhongshu / 中枢</h1>

<p align="center">
  <strong>Keep long-running ChatGPT + Codex projects context-aware, verifiably complete, and always clear on what to do next.</strong>
</p>

<p align="center">
  A project orchestration and audit layer for long-running AI software development
</p>

<p align="center">
  <a href="../../releases/latest"><img src="https://img.shields.io/github/v/release/liwenyajiaoshou/zhongshu-agent-orchestrator?display_name=tag&label=release" alt="Latest release"></a>
  <a href="../../actions/workflows/repository-consistency.yml"><img src="https://github.com/liwenyajiaoshou/zhongshu-agent-orchestrator/actions/workflows/repository-consistency.yml/badge.svg" alt="Repository consistency"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
</p>

**[5-Minute Quick Start](#5-minute-quick-start)** · **[Latest Release](../../releases/latest)** · **[Full Docs](#more)**

<p align="center">
  <img
    src="assets/zhongshu-hero.png"
    alt="Zhongshu orchestration overview"
    width="100%"
  />
</p>

## What does Zhongshu solve?

### `01` Keep context across long-running projects

Projects span stages, threads, and agent runs. Zhongshu keeps the current state and handoff context so a new thread can continue instead of starting over.

### `02` Verify whether an agent actually finished

Zhongshu checks reports, tests, and machine-readable evidence to determine **PASS / REPAIR / BLOCKED**.

### `03` Know the next best step

Zhongshu uses the real project state to propose the smallest worthwhile next step instead of replanning the whole project every time.

## How it works

Zhongshu is a project-level orchestration layer: it judges stages, plans tasks, audits execution results, and hands over real risk boundaries to the optional Guardian governance layer.

```mermaid
flowchart TD
    U[Owner / User] --> P[ChatGPT Project]
    P --> Z[Zhongshu<br/>Stage Judgement · Task Planning · Model/Thread Routing · Audit]

    Z --> PLAN[Stage Plan]
    PLAN --> A[Codex / Antigravity]

    G[Guardian (Optional)<br/>Git · Network · Data · Release] -.Governance.-> A

    A --> E[Execution Report + Machine Evidence]
    E --> Z

    Z --> R{Audit Result}
    R -->|PASS| N[Next Stage]
    R -->|REPAIR| PLAN
    R -->|BLOCKED| U
```

### A typical workflow

After Codex finishes a run, you hand the report to Zhongshu:

> "Here is the latest execution report, please check if it is truly complete, and tell me the next step."

**Report → Tests / Evidence → PASS / REPAIR / BLOCKED → Next Step**

## 5-minute quick start

No Git, Python, GitHub CLI, or Guardian required. You only need a ChatGPT Project, and if local code execution is needed, attach Codex / Antigravity.

1. Download the **Latest Runtime Pack** (ZIP) from the [Latest Release](../../releases/latest).
2. Extract the ZIP file.
3. Open the `project-upload/` folder in the extracted directory.
4. Upload all files from `project-upload/` to your ChatGPT Project's Project Sources.
5. Open `PROJECT_INSTRUCTIONS.txt` and copy its entire content into the ChatGPT Project's Project Instructions.
6. Send the following self-check prompt.
7. Receiving `ZHONGSHU_RUNTIME_READY` means deployment is complete.

```text
Check whether Zhongshu is fully deployed.

Inspect only the Zhongshu Runtime available in the current Project:

1. Report the detected Runtime version.
2. Check whether all required Project Source files are present.
3. Check whether the Project Instructions are active.
4. If anything is missing, tell me exactly what is missing.
5. If everything is complete, reply with:

ZHONGSHU_RUNTIME_READY

Then tell me how to start a new project.
```

## Who is it for?

| Good fit | Probably not needed |
|---|---|
| ✓ Long-running software projects | ✗ Small scripts requiring a single prompt |
| ✓ Multi-stage / multi-thread agents | ✗ Simple single-file edits |
| ✓ Projects needing verified completions | ✗ No need for long contexts or agent audits |

## More

### Capabilities

Context Retention · Execution Audit · Minimum Next Step · Risk Boundaries

[View full capabilities (Chinese) →](README_部署与使用.md#12-详细能力矩阵)

### Zhongshu vs Guardian

Zhongshu decides "what to do now"; Guardian is an optional enhancement that restrains "how the agent can do it".

[View full explanation (Chinese) →](README_部署与使用.md#6-与卫兵的关系)

### Documentation

- [Full deployment & usage guide (Chinese)](README_部署与使用.md)
- [5-minute deployment (Chinese)](START_HERE.md)
- [Core Runtime (Chinese)](SKILL.md)
- [Release Governance (Chinese)](RELEASE_GOVERNANCE.md)
- [CHANGELOG (Chinese)](CHANGELOG.md)

<details>
<summary><strong>Scope / Design Principles</strong></summary>

**Scope:**
Zhongshu is not a Coding Agent, IDE, auto code generator, CI/CD platform, or Guardian replacement. It primarily orchestrates long-term software development for ChatGPT Project + Codex / Antigravity. Zhongshu can be used independently; Guardian is an optional field governance enhancement.

**Design Principles:**
- Minimum Sufficient Governance: Only add governance that truly reduces risk.
- Evidence over Claims: Completion needs verifiable evidence.
- Smallest Next Step: Only plan the most worthwhile next step.
- Finish Local Value, Then Compress: Finish local value before compressing threads.
- Execution Form Is Not Risk: Base boundaries on real side effects.
</details>

Licensed under the [MIT License](LICENSE).
