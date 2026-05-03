---
name: safe_high_impact_changes
description: "Add extra caution before actions that could affect production, money, users, or public trust."
user-invocable: false
metadata: {"openclaw":{"emoji":"\ud83d\udea6"}}
---

## Purpose
- Add extra caution before actions that could affect production, money, users, or public trust.
- This is a **safety specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before high-impact edits, launches, migrations, account actions, or external publishing.

## Avoid when
- Do not treat low-risk drafting like a production incident.

## Inputs to gather
- What sensitive asset, account, production system, or public claim is in scope.
- Who could be impacted if the action is wrong, leaked, or partially completed.
- What approvals, redactions, or safer alternatives exist before proceeding.

## Operating rules
- Higher impact requires narrower scope and better verification.
- Prefer reversible steps and explicit approvals.
- State the blast radius before acting.

- Safety reviews are about what could go wrong, not confirming that things went right. Actively seek failure modes.
- Distinguish between known risks (document and mitigate), unknown risks (create detection mechanisms), and unknowable risks (set resilience buffers).
- The blast radius of any change must be named before the change is made. If you cannot describe the worst case, you are not ready to proceed.
- Automated safeguards beat manual ones. A checklist that requires human memory is a checklist that will be skipped under pressure.
- When in doubt, do not proceed. Safety gates exist to stop things, not to rubber-stamp them.
## Claude Code tool pattern
- Prefer observation, redaction, and user-mediated actions over direct handling of secrets or live credentials.
- Use the browser or shell only after the risk boundary is explicit and the action is reversible or approved.
- When a task crosses into high-impact territory, slow the workflow down and state the approval gate clearly.

## Expanded workflow
1. Define the proposed action and blast radius.
2. List the required checks, approvals, and rollback path.
3. Reduce scope or sequence if needed.
4. Return the safe execution boundary.
## Output contract
- Action and blast radius
- Checks and approvals
- Rollback path
- Go/no-go recommendation
- Risk summary with the protected surface named plainly.
- Approved handling path, redaction path, or stop-condition.

## Failure modes to avoid
- Treating convenience as a reason to bypass secret hygiene or approval paths.
- Repeating sensitive values in chat, logs, artifacts, or examples.
- Conflating 'possible' with 'safe enough to do now'.

## Handoff cues
- High-impact change safety plan: blast radius, rollback, monitoring, approval chain.
- Verification checklist for each change step.
- Escalation path if something goes wrong.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use high-Impact Change Gate to add extra caution before actions that could affect production, money, users, or public trust."
- Example: "Check the risky parts before we publish, deploy, or log in."
- Example: "Tell me the safest way to continue without exposing credentials or personal data."
- Often paired with: `core_risk_gate`, `safe_secret_hygiene`

## Quality bar

- Blast radius is explicitly defined: who and what is affected.
- Rollback plan is tested, not just documented.
- Monitoring is in place before the change, not after.
- The approval chain matches the impact level — bigger changes need more sign-offs.
- Every identified risk has a mitigation, an owner, or an explicit acceptance with rationale.
- The blast radius of the proposed change is documented.
- Automated safeguards exist for the highest-consequence risks.
- The review actively sought failure modes, not just confirmed existing controls.
## Related workflows
- Safety review: `safe_high_impact_changes` → `safe_external_claims` → `safe_pii_minimization`
