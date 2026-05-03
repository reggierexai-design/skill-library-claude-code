---
name: sec_appsec_review
description: "Review code or design for common application-security weaknesses and realistic exploit paths."
user-invocable: true
---

## Purpose
- Review code or design for common application-security weaknesses and realistic exploit paths.
- This is a **security specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when reviewing auth, input handling, uploads, rendering, storage, or privileged actions.

## Avoid when
- Do not use when there is no meaningful code, config, or design surface to inspect.

## Inputs to gather
- Application architecture: services, data flows, authN, authZ.
- Code changes under review.
- Threat landscape: relevant attack vectors.
- Security requirements: compliance, data classification, access policies.
- Previous open findings.

## Operating rules
- Review the security model, not just the code.
- Check input validation at every trust boundary.
- Verify authorization, not just authentication.
- Every finding needs severity, exploitability, and remediation.

- Use STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) as the threat enumeration framework unless the context demands a different model.
- Rate each threat by likelihood (1-5) x impact (1-5). Threats scoring 15+ need mitigations before ship. Threats scoring 8-14 need accepted-risk documentation. Below 8 is monitored.
- Every threat model must name the trust boundaries explicitly: where does untrusted input cross into a trusted zone? That boundary is the highest-value attack surface.
- Distinguish between threats to confidentiality, integrity, and availability. A threat to one is not necessarily a threat to the others.
- Threat models are attackergoal-first, not feature-first. Start from what an attacker wants to achieve, then trace backwards to how they could do it.
## Claude Code tool pattern
- Read the real data flow, auth model, config, and dependency surface before naming security posture.

## Expanded workflow
1. Map trust boundaries and data flows.
2. Review authN and authZ implementation.
3. Check input validation at every external entry point.
4. Review data protection: encryption, PII handling.
5. Check common vulnerabilities: injection, XSS, CSRF, IDOR, SSRF.
6. Document findings with severity, exploitability, remediation.
7. Prioritize fixes by exploitability x impact.

## Output contract
- Security review or model with risk ranking, exposure logic, and remediation direction.
- Assumptions, open questions, and where human security review is still required.

## Failure modes to avoid
- Code-level review without understanding the security model.
- Missing authorization checks â€” authenticating but not authorizing.
- Ignoring business logic vulnerabilities.
- Findings without remediation.

## Handoff cues
- AppSec review: findings, severity, remediation steps, risk acceptance decisions.
- Priority-ordered fix list with owners.
- Re-test requirements after fixes are applied.

## Example invocation
- Slash: `/sec_appsec_review <task>`
- Natural language: "Use security AppSec Review to review code or design for common application-security weaknesses and realistic exploit paths."
- Example: "Review this surface like a real security operator, not a checklist generator."
- Example: "Tell me the plausible threats, likely exposures, and highest-value mitigations."
- Often paired with: `sec_threat_model`, `safe_high_impact_changes`

## Quality bar
## Related workflows
- Security review: `sec_threat_model` â†’ `sec_appsec_review` â†’ `sec_data_flow_review`
- Every high-likelihood threat has a named mitigation or an explicitly accepted risk with rationale.
- Trust boundaries are diagrammed or clearly described.
- At least one insider threat scenario is included.
- The model is specific enough that an engineer could implement mitigations without guessing.
