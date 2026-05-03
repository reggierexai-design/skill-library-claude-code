---
name: safe_browser_login
description: "Handle authenticated browsing without taking custody of user credentials or live account secrets."
user-invocable: false
metadata: {"openclaw":{"requires":{"config":["browser.enabled"]},"emoji":"🛡️"}}
---

## Purpose
- Handle authenticated browsing without taking custody of user credentials or live account secrets.
- This is a **safety specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a task requires logging into a site, attaching to an existing user browser session, or working inside an authenticated web app.

## Avoid when
- Do not use for public web pages that do not require sign-in.

## Inputs to gather
- What sensitive asset, account, production system, or public claim is in scope.
- Who could be impacted if the action is wrong, leaked, or partially completed.
- What approvals, redactions, or safer alternatives exist before proceeding.

## Operating rules
- Manual user login is the default safe path.
- Do not ask the user to paste passwords, TOTP codes, session cookies, or recovery codes into chat.
- Stay inside the managed agent browser unless there is a clear reason to attach to a user profile.

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
1. Identify whether login is actually required.
2. Pick the safest browser profile and login path.
3. Proceed with the task after the user completes any manual auth step.
4. Avoid storing or repeating any auth material.
## Output contract
- Login requirement
- Safe browser path
- Any manual user step
- Post-login execution note
- Risk summary with the protected surface named plainly.
- Approved handling path, redaction path, or stop-condition.

## Failure modes to avoid
- Treating convenience as a reason to bypass secret hygiene or approval paths.
- Repeating sensitive values in chat, logs, artifacts, or examples.
- Conflating 'possible' with 'safe enough to do now'.

## Handoff cues

- Browser login safety assessment: risks identified, mitigations applied, remaining risks.
- Credential handling verification.
- Session management review results.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use browser Login Safety to handle authenticated browsing without taking custody of user credentials or live account secrets."
- Example: "Check the risky parts before we publish, deploy, or log in."
- Example: "Tell me the safest way to continue without exposing credentials or personal data."
- Often paired with: `core_risk_gate`, `safe_secret_hygiene`, `safe_high_impact_changes`

## Quality bar
- The agent should never become the storage layer for account credentials.
- Every identified risk has a mitigation, an owner, or an explicit acceptance with rationale.
- The blast radius of the proposed change is documented.
- Automated safeguards exist for the highest-consequence risks.
- The review actively sought failure modes, not just confirmed existing controls.
## Related workflows
- Safety review: `safe_high_impact_changes` → `safe_external_claims` → `safe_pii_minimization`
