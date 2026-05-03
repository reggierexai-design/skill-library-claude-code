---
name: safe_live_systems
description: "Handle production systems, live data, and user-facing environments with reversible, low-blast-radius steps."
user-invocable: false
---

## Purpose
- Handle production systems, live data, and user-facing environments with reversible, low-blast-radius steps.
- This is a **safety specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before touching production services, real customer data, billing surfaces, or customer-visible infrastructure.

## Avoid when
- Do not use as a substitute for knowing the actual environment and rollback path.

## Inputs to gather
- What sensitive asset, account, production system, or public claim is in scope.
- Who could be impacted if the action is wrong, leaked, or partially completed.
- What approvals, redactions, or safer alternatives exist before proceeding.

## Operating rules
- Read first, mutate second.
- Prefer reversible changes, narrow scopes, and explicit rollback.
- Never treat production like a sandbox.

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
1. Confirm the live surface, stakes, and rollback path.
2. Reduce the blast radius of the proposed action.
3. Define the verification signals and abort conditions.
4. Proceed only with the minimum safe change or recommendation.
## Output contract
- Live-systems risk summary
- Rollback path
- Verification signals
- Recommended next step
- Risk summary with the protected surface named plainly.
- Approved handling path, redaction path, or stop-condition.

## Failure modes to avoid
- Treating convenience as a reason to bypass secret hygiene or approval paths.
- Repeating sensitive values in chat, logs, artifacts, or examples.
- Conflating 'possible' with 'safe enough to do now'.

## Handoff cues

- Live system safety plan: what's changing, safeguards, rollback, monitoring, communication.
- Step-by-step execution plan with verification.
- Post-change verification results.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use safe Live Systems to handle production systems, live data, and user-facing environments with reversible, low-blast-radius steps."
- Example: "Check the risky parts before we publish, deploy, or log in."
- Example: "Tell me the safest way to continue without exposing credentials or personal data."
- Often paired with: `core_risk_gate`, `safe_secret_hygiene`, `safe_high_impact_changes`

## Quality bar
- A live-systems plan fails when it assumes safety instead of proving it.
- Every identified risk has a mitigation, an owner, or an explicit acceptance with rationale.
- The blast radius of the proposed change is documented.
- Automated safeguards exist for the highest-consequence risks.
- The review actively sought failure modes, not just confirmed existing controls.
## Related workflows
- Safety review: `safe_high_impact_changes` → `safe_external_claims` → `safe_pii_minimization`
