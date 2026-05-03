---
name: eng_refactor_design
description: "Plan or execute a refactor that improves structure without losing behavior."
user-invocable: true
metadata: {"openclaw":{"emoji":"🛠️"}}
---

## Purpose
- Plan or execute a refactor that improves structure without losing behavior.

## Use when
- Use when the current code works poorly enough that maintenance speed, clarity, or correctness is suffering.

## Avoid when
- Do not use for cosmetic rewrites or speculative abstractions.

## Inputs to gather
- Current code structure: what exists and why is it hard to change?
- Target architecture: what should the code look like after refactoring?
- Change velocity: what changes are slow or risky because of the current structure?
- Test coverage: how much safety do existing tests provide during refactoring?
- Dependency map: what depends on the code being refactored?

## Operating rules
- Refactor around pressure points, not taste.
- Preserve behavior while changing structure.
- Break large refactors into reviewable slices.

- Read the code and the error before proposing a fix. Diagnose first, treat second.
- Prefer the minimal change that solves the problem. Every line added is a line that can break.
- Test the fix, test the surrounding area, test the edge cases. A fix that works for the happy path only is not a fix.
- Document why, not just what. Future engineers need to understand the reasoning, not just see the change.
- If the fix takes longer than 30 minutes, stop and reconsider the approach. Complex fixes usually indicate the wrong diagnosis.
## Claude Code tool pattern
- Use `Bash` to run diagnostic commands, read logs, and check system state.
- Use `Read` to inspect source files, configs, and error output directly.
- Use `Edit` for targeted code changes. Prefer `eng_minimal_patch` scope discipline.
- After changes, use `eng_test_strategy` to verify the fix works and nothing else broke.

## Expanded workflow
1. Identify the structural problem and desired end state.
2. Define safe boundaries and incremental stages.
3. Execute or describe the smallest high-value sequence.
4. Verify behavior stability after each stage.
## Output contract
- Structural problem
- Refactor target
- Incremental stages
- Verification plan or result
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid
- Rewriting instead of refactoring — a rewrite is a new system with new bugs; a refactor preserves behavior.
- No test coverage before refactoring — refactoring without tests is archaeology with dynamite.
- Big bang refactoring — changing too much at once makes rollback impossible.
- Refactoring without a clear target — 'make it better' is not a design.
- Ignoring the strangle fig pattern — incremental migration is safer than wholesale replacement.

## Handoff cues
- Refactoring plan: current state, target state, incremental steps.
- Test coverage assessment before starting.
- List of steps with verification at each stage.
- Any steps that require team coordination or feature flags.

## Example invocation
- Slash: `/eng_refactor_design <task>`
- Natural language: "Use refactor Design to plan or execute a refactor that improves structure without losing behavior."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar

- The refactoring has a clear target architecture.
- Existing tests cover the code before refactoring begins.
- Each refactoring step is small enough to verify independently.
- Behavior is preserved at every step — no functional changes mixed with structural changes.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`
