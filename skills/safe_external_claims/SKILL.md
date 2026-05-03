---
name: safe_external_claims
description: "Check public-facing claims for evidence, dates, and overstatement before publishing them."
user-invocable: false
metadata: {"openclaw":{"emoji":"\ud83d\udee1\ufe0f"}}
---

## Purpose
- Check public-facing claims for evidence, dates, and overstatement before publishing them.
- This is a **safety specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when writing marketing, press, investor, recruiting, or product claims about the outside world.

## Avoid when
- Do not publish time-sensitive claims from memory alone.

## Inputs to gather
- What sensitive asset, account, production system, or public claim is in scope.
- Who could be impacted if the action is wrong, leaked, or partially completed.
- What approvals, redactions, or safer alternatives exist before proceeding.

## Operating rules
- Claims need dates and sources when they can age.
- Rank confidence and separate fact from inference.
- Cut superlatives that the evidence cannot support.

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
1. List the external claims in scope.
2. Check the evidence and freshness for each one.
3. Rewrite or remove weak claims.
4. Return a safer public-facing set of claims.
## Output contract
- Claims reviewed
- Evidence status
- Rewrites or removals
- Open verification needs
- Risk summary with the protected surface named plainly.
- Approved handling path, redaction path, or stop-condition.

## Failure modes to avoid
- Treating convenience as a reason to bypass secret hygiene or approval paths.
- Repeating sensitive values in chat, logs, artifacts, or examples.
- Conflating 'possible' with 'safe enough to do now'.

## Handoff cues
- External claims review: claims, evidence strength, risk level, recommended actions.
- Claims to remove, qualify, or add evidence for.
- Compliance implications if any claims are misleading.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use external Claims Guard to check public-facing claims for evidence, dates, and overstatement before publishing them."
- Example: "Check the risky parts before we publish, deploy, or log in."
- Example: "Tell me the safest way to continue without exposing credentials or personal data."
- Often paired with: `core_risk_gate`, `safe_secret_hygiene`, `safe_high_impact_changes`

## Quality bar

- Every external claim is traceable to a source that can be verified.
- Claims that can't be verified are flagged for removal or qualification.
- Comparative claims (faster, better, #1) have specific evidence or are rewritten.
- The review covers all public surfaces: website, docs, ads, social, press.
- Every identified risk has a mitigation, an owner, or an explicit acceptance with rationale.
- The blast radius of the proposed change is documented.
- Automated safeguards exist for the highest-consequence risks.
- The review actively sought failure modes, not just confirmed existing controls.
## Related workflows
- Safety review: `safe_high_impact_changes` → `safe_external_claims` → `safe_pii_minimization`
