---
name: safe_install_gate
description: "Review package installs, bootstrap scripts, and setup commands before execution."
user-invocable: false
---

## Purpose
- Review package installs, bootstrap scripts, and setup commands before execution.
- This is a **safety specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before running installers, package managers, curl-pipe-shell snippets, migration helpers, or project setup commands with side effects.

## Avoid when
- Do not use for already-reviewed, routine local commands with no material risk.

## Inputs to gather
- What sensitive asset, account, production system, or public claim is in scope.
- Who could be impacted if the action is wrong, leaked, or partially completed.
- What approvals, redactions, or safer alternatives exist before proceeding.

## Operating rules
- Inspect what will be installed, from where, and with what permissions.
- Prefer official docs and package managers over opaque shell snippets.
- If a dependency is unnecessary for the user goal, skip the install.

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
1. Identify the install objective and whether it is truly needed.
2. Check source, version, scope, and side effects.
3. Choose the narrowest safe install path or defer.
4. Record any assumptions that remain unverified.
## Output contract
- Install objective
- Package or script reviewed
- Chosen safe path
- Residual risk or refusal
- Risk summary with the protected surface named plainly.
- Approved handling path, redaction path, or stop-condition.

## Failure modes to avoid
- Treating convenience as a reason to bypass secret hygiene or approval paths.
- Repeating sensitive values in chat, logs, artifacts, or examples.
- Conflating 'possible' with 'safe enough to do now'.

## Handoff cues

- Install gate assessment: package safety, permissions, supply chain risk, recommendations.
- Allow/deny decision with rationale.
- Ongoing monitoring plan for installed dependencies.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use install Gate to review package installs, bootstrap scripts, and setup commands before execution."
- Example: "Check the risky parts before we publish, deploy, or log in."
- Example: "Tell me the safest way to continue without exposing credentials or personal data."
- Often paired with: `core_risk_gate`, `safe_secret_hygiene`, `safe_high_impact_changes`

## Quality bar
- Setup speed never beats provenance and blast-radius control.
- Every identified risk has a mitigation, an owner, or an explicit acceptance with rationale.
- The blast radius of the proposed change is documented.
- Automated safeguards exist for the highest-consequence risks.
- The review actively sought failure modes, not just confirmed existing controls.
## Related workflows
- Safety review: `safe_high_impact_changes` → `safe_external_claims` → `safe_pii_minimization`
