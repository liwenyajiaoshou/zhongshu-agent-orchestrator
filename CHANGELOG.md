# Changelog


## v1.11.0 - 2026-09-04

- Added "Owner Is Not a Debug Terminal" principle: Forced autonomous debugging for ordinary script errors, pathing, and environment mismatches before reaching the Owner Gate.
- Introduced "Child Thread Scope Match": Child threads must now actively verify task alignment (Scope Match Check) before absorbing authority, preventing silent cross-contamination from misrouted inputs.
- Implemented User/Developer interactive perspective choice upon first deployment to align reporting styles to Owner preferences.
- Streamlined Host automation priority, explicitly favoring Python runners and PowerShell 7 for complex orchestration while relegating PS 5.1 to legacy fallbacks.

## v1.10.0 - 2026-09-03

- Enshrined "Deep Research Is a Retrieval Multiplier, Not a Quality Guarantee" principle in project instructions, separating Research Mode from Model Tier, Agent Count, and Task Class routing.
- Mandated "Normal Research First": Targeted Deep Research is only triggered when there are clear, decision-critical evidence gaps in normal research results.
- Formalized "Research Contract Must Precede Research Mode": Decision Questions, Entity disambiguation, cutoff constraints, and Evidence Schemas must be frozen before determining the research mode.

## v1.9.0 - 2026-09-02

- Introduced formal Handoff Deliverables requirements: Zhongshu must actively generate handoff documents and startup prompts instead of passively suggesting a switch.
- Added Execution Gate Evidence Recovery to policies/execution-gating.md: Enforces a STOP and read-only recovery fallback when an Owner reports execution but machine-readable artifacts are missing or inaccessible.
- Strengthened 	emplates/stage-report.md compression rules: Report compression must not omit decision-critical evidence that affects next actions or blocker attribution.

## v1.8.0 - 2026-09-01

- Added policies/research-execution.md to distinguish Research from Execution tasks, ensuring research stops effectively without unneeded governance overhead.
- Added policies/state-and-handoff.md and 	emplates/current-state.md to support Delta/Full Handoffs and authoritative state recovery, avoiding full historical scans when possible.
- Added policies/taskcontract-lifecycle.md to define Zhongshu's role in TaskContract lifecycle management (CONTINUE/SUPERSEDE/STOP_AND_REPLAN).
- Expanded REPORT_REVIEW to detect Governance False Block, Real External Blocker, and Environment/Tooling blockers.

## v1.7.0 - 2026-08-31

- Added policies/dialogue-thread-management.md to define splitting logic for Blocker Threads and handle Dialogue Context Saturation in web workflows.
- Prevented automatic opening of new threads for every minor issue or blocker, ensuring thread coherence and proper context closure.

## v1.6.1 - 2026-08-31

- Added constraints for web dialog output (policies/web-dialog-output.md) to prioritize Owner-facing summaries over verbose engineering analysis.
- Added a structured review response template (	emplates/web-review-response.md) for web dialogue.
- Cancelled the mandatory "Model Capability" assessment display in normal scenarios, triggering it only upon verified quality issues.
- Integrated all relevant template and policy updates from the S2.5.1 revision.

## v1.5.0 - 2026-08-30

- Refocused public documentation on core user problems and practical value.
- Simplified README visual hierarchy and compressed verbose matrix tables.
- Added comprehensive English translation (`README_EN.md`) with language switcher.
- Strengthened Markdown rendering compatibility.

## v1.4.0 - 2026-08-29

- Added Host execution gating and minimum Owner Gate (S2.3).
- Added Codex long thread context cost and optimal handoff timing (S2.2, previously planned for V1.3).
- Updated manifest and policies for execution gating.

v1.3.0 was not published; the local source package was not retained.

## v1.2.0 - 2026-08-29

- Added Codex model, reasoning, and thread joint routing (S2.1).
- Updated policies for debug escalation and model routing.
- Updated stage plan templates.
## v1.1.0 - 2026-08-29

- Restored V1.1 policy and template files to their canonical `policies/` and `templates/` paths.
- Added constrained autonomous debugging, repeated-failure escalation, and Codex context-handoff guidance.
- Updated deployment documentation to identify the current Runtime as V1.1.
- Added the V1.1 runtime manifest metadata.

## v1.0.0

- Initial public release of Zhongshu.
- Added core orchestration skill.
- Added policies and templates.
- Added deployment and project instructions.






