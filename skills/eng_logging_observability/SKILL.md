---
name: eng_logging_observability
description: "Improve logs, metrics, and traces so failures become diagnosable without drowning operators in noise."
user-invocable: true
---

## Purpose
- Improve logs, metrics, and traces so failures become diagnosable without drowning operators in noise.

## Use when
- Use when the system is hard to debug because signals are missing, noisy, or not tied to user impact.

## Avoid when
- Do not add logging that leaks secrets or creates alert spam.

## Inputs to gather

- System architecture: services, data flows, and integration points.
- Current observability: what's logged, what's traced, what's metric'd?
- Failure modes: what breaks, and what would you need to see to diagnose it?
- Alert requirements: what conditions need immediate notification?
- Cost and performance constraints: log volume budgets, sampling strategies.

## Operating rules
- Instrument for decisions, not vanity.
- Prefer structured signals that connect cause, scope, and user impact.
- Every new signal should have an intended operator use.

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
1. Find the blind spots in the current signals.
2. Define the questions operators need answered.
3. Recommend logs, metrics, or traces tied to those questions.
4. Verify that the new signals will be usable and safe.
## Output contract
- Observability gaps
- Recommended signals
- Operator use cases
- Risks and safeguards
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid

- Logging everything and finding nothing — volume without structure is noise.
- Missing correlation IDs — can't trace requests across service boundaries.
- No structured logging — grepping unstructured logs at scale is unreliable.
- Alert fatigue — too many alerts means nobody responds to the important ones.
- Logging PII — sensitive data in logs is a security and compliance issue.

## Handoff cues

- Observability plan: what to log, trace, and metric.
- Alert definitions with thresholds and owners.
- Correlation ID implementation requirements.
- PII exclusion rules for logs.
- Sampling strategy for high-volume services.

## Example invocation
- Slash: `/eng_logging_observability <task>`
- Natural language: "Use logging and Observability to improve logs, metrics, and traces so failures become diagnosable without drowning operators in noise."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- Better observability means faster diagnosis with less guesswork and less noise.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`
