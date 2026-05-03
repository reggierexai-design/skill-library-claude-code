---
name: eng_feature_flag_rollout
description: "Design a staged feature-flag rollout with targeting, monitoring, and rollback criteria."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udea9"}}
---

## Purpose
- Design a staged feature-flag rollout with targeting, monitoring, and rollback criteria.

## Use when
- Use when a change should ship gradually or only to part of the audience first.

## Avoid when
- Do not use when the change cannot be safely isolated behind a flag.

## Inputs to gather
- Feature flag definition: name, type (boolean, percentage, variant), targeting rules.
- Rollout plan: percentage increments, duration at each stage, success criteria.
- Kill switch: how to instantly disable if something goes wrong?
- Metrics to monitor: which signals indicate the feature is working or broken?
- Cleanup plan: when and how will the flag be removed after full rollout?

## Operating rules
- Every feature flag needs a kill switch tested before rollout begins.
- Rollout in increments: 5% then 25% then 50% then 100%. Never go straight to 100%.
- Monitor during rollout. You need to know the feature is broken before users tell you.
- Flag cleanup is non-negotiable. Schedule the removal ticket before the rollout starts.
- Flag naming must be unique and descriptive: 'payments-v2-checkout' not 'new-thing'.

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
1. Define the flag: name, type, targeting rules, default state.
2. Implement the kill switch and test it before any rollout.
3. Set up monitoring: the metrics that indicate success or failure.
4. Roll out incrementally: 5% then 25% then 50% then 100%.
5. Verify at each stage: are the metrics healthy?
6. After 100% stable for 1+ weeks, schedule flag removal.
7. Remove the flag and clean up the code paths.

## Output contract
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid
- No kill switch â€” if the feature causes problems, the only option is a full rollback.
- Rolling out to 100% immediately â€” skip incremental rollout and you skip the safety net.
- No monitoring during rollout â€” you don't know the feature is broken until users complain.
- Permanent flags â€” flags that never get removed become technical debt and configuration complexity.
- Flag name collision or unclear naming â€” 'new_dashboard' in 3 different services is a mess.

## Handoff cues
- Feature flag spec: name, type, targeting, rollout plan.
- Kill switch instructions.
- Monitoring dashboard or alert thresholds.
- Flag cleanup ticket with target date.

## Example invocation
- Slash: `/eng_feature_flag_rollout <task>`
- Natural language: "Use engineering Feature Flag Rollout to design a staged feature-flag rollout with targeting, monitoring, and rollback criteria."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
## Related workflows
- Debug chain: `eng_bug_triage` â†’ `eng_debug_systematically` â†’ `eng_minimal_patch` â†’ `eng_test_strategy`
- Release safety: `eng_release_readiness` â†’ `eng_code_review_pass` â†’ `eng_feature_flag_rollout`
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.