# Changelog


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



