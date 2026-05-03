---
name: safe_secret_hygiene
description: "Keep credentials, tokens, cookies, and private data out of prompts, files, and logs."
user-invocable: false
---

## Purpose
- Keep credentials, tokens, cookies, and private data out of prompts, files, and logs.
- This is a **safety specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use whenever the task touches API keys, auth state, environment variables, production data, or screenshots that may contain sensitive information.

## Avoid when
- Do not use for ordinary public-only work.

## Inputs to gather
- What sensitive asset, account, production system, or public claim is in scope.
- Who could be impacted if the action is wrong, leaked, or partially completed.
- What approvals, redactions, or safer alternatives exist before proceeding.

## Operating rules
- Never ask for or echo raw credentials in chat.
- Prefer config, env injection, or manual user action over putting secrets into prompts or files.
- Treat screenshots, logs, URLs, and browser state as possible secret carriers.

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
1. Identify the sensitive material in play.
2. Choose the safest handling path.
3. Redact anything that might leak.
4. Continue only after the secret boundary is clear.
## Output contract
- Sensitive surface identified
- Safe handling choice
- Redactions or placeholders used
- Any remaining exposure risk
- Risk summary with the protected surface named plainly.
- Approved handling path, redaction path, or stop-condition.

## Failure modes to avoid
- Treating convenience as a reason to bypass secret hygiene or approval paths.
- Repeating sensitive values in chat, logs, artifacts, or examples.
- Conflating 'possible' with 'safe enough to do now'.

## Handoff cues

- Secret hygiene audit: secrets found, exposure risk, rotation status, remediation plan.
- Priority fixes for exposed or stale secrets.
- Ongoing hygiene monitoring plan.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use secret Hygiene to keep credentials, tokens, cookies, and private data out of prompts, files, and logs."
- Example: "Check the risky parts before we publish, deploy, or log in."
- Example: "Tell me the safest way to continue without exposing credentials or personal data."
- Often paired with: `core_risk_gate`, `safe_high_impact_changes`

## Quality bar
- Good secret handling is invisible when done well.
- Every identified risk has a mitigation, an owner, or an explicit acceptance with rationale.
- The blast radius of the proposed change is documented.
- Automated safeguards exist for the highest-consequence risks.
- The review actively sought failure modes, not just confirmed existing controls.
## Related workflows
- Safety review: `safe_high_impact_changes` → `safe_external_claims` → `safe_pii_minimization`
