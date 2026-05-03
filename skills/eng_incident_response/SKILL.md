---
name: eng_incident_response
description: "Stabilize a service issue with fast diagnosis, containment, user-impact framing, and clear next actions."
user-invocable: true
---

## Purpose
- Stabilize a service issue with fast diagnosis, containment, user-impact framing, and clear next actions.

## Use when
- Use during an outage, degraded service, severe bug, or urgent production issue.

## Avoid when
- Do not mix long-term cleanup with the first containment pass.

## Inputs to gather

- Incident signal: alert, user report, or monitoring anomaly.
- Current impact: how many users, what functionality is affected?
- Timeline: when did the issue start? When was it detected?
- System state: recent deployments, config changes, known ongoing issues.
- Communication chain: who needs to be informed and when?

## Operating rules
- Contain first, explain second, optimize later.
- Prefer explicit status, ownership, and checkpoints over improvisation.
- Track user impact separately from technical root cause.

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
1. State the incident and user impact.
2. Contain or reduce the blast radius.
3. Identify the likely cause surface and next checks.
4. Document status, owner, and next update.
## Output contract
- Incident summary
- Impact
- Containment steps
- Next checks
- Status note
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid

- Debugging before mitigating — stop the bleeding first, then find the root cause.
- No incident commander — without a single decision-maker, the response fragments.
- Poor communication — stakeholders learn about the incident from Twitter.
- No timeline capture — you can't do a postmortem if nobody recorded what happened when.
- Declaring resolution before verifying — the symptom stopped but the root cause might recur.

## Handoff cues

- Incident summary: impact, timeline, mitigation, root cause.
- Postmortem scheduled and assigned.
- Follow-up actions to prevent recurrence.
- Communication log: who was informed, when, and what they were told.

## Example invocation
- Slash: `/eng_incident_response <task>`
- Natural language: "Use incident Response to stabilize a service issue with fast diagnosis, containment, user-impact framing, and clear next actions."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- An incident pass is good when users are protected quickly and the team regains control.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`
