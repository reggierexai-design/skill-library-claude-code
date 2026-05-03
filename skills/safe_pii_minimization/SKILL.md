---
name: safe_pii_minimization
description: "Reduce exposure of personal data by default in prompts, notes, artifacts, examples, and logs."
user-invocable: false
metadata: {"openclaw":{"emoji":"🛡️"}}
---

## Purpose
- Reduce exposure of personal data by default in prompts, notes, artifacts, examples, and logs.
- This is a **safety specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when handling customer support data, user exports, interviews, CRM notes, or other personal information.

## Avoid when
- Do not collect more identity detail than the task actually needs.

## Inputs to gather
- What sensitive asset, account, production system, or public claim is in scope.
- Who could be impacted if the action is wrong, leaked, or partially completed.
- What approvals, redactions, or safer alternatives exist before proceeding.

## Operating rules
- Minimize, redact, and aggregate where possible.
- Prefer examples and summaries over raw personal records.
- Keep sensitive identifiers out of reusable artifacts by default.

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
1. Identify what personal data is present.
2. Remove or abstract unnecessary identifiers.
3. Continue with only the minimum detail needed.
4. State any remaining privacy caveats in the handoff.
## Output contract
- Data sensitivity note
- Redaction approach
- Safe working summary
- Residual risk
- Risk summary with the protected surface named plainly.
- Approved handling path, redaction path, or stop-condition.

## Failure modes to avoid
- Treating convenience as a reason to bypass secret hygiene or approval paths.
- Repeating sensitive values in chat, logs, artifacts, or examples.
- Conflating 'possible' with 'safe enough to do now'.

## Handoff cues

- PII minimization report: data inventory, risk assessment, minimization actions, compliance.
- Recommended data retention and deletion policies.
- Implementation plan for minimization actions.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use pII Minimization to reduce exposure of personal data by default in prompts, notes, artifacts, examples, and logs."
- Example: "Check the risky parts before we publish, deploy, or log in."
- Example: "Tell me the safest way to continue without exposing credentials or personal data."
- Often paired with: `core_risk_gate`, `safe_secret_hygiene`, `safe_high_impact_changes`

## Quality bar
- A privacy-aware pass preserves task usefulness while shrinking unnecessary exposure.
- Every identified risk has a mitigation, an owner, or an explicit acceptance with rationale.
- The blast radius of the proposed change is documented.
- Automated safeguards exist for the highest-consequence risks.
- The review actively sought failure modes, not just confirmed existing controls.
## Related workflows
- Safety review: `safe_high_impact_changes` → `safe_external_claims` → `safe_pii_minimization`
