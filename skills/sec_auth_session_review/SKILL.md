---
name: sec_auth_session_review
description: "Review authentication, session handling, and account-recovery flows for takeover risk."
user-invocable: true
---

## Purpose
- Review authentication, session handling, and account-recovery flows for takeover risk.
- This is a **security specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when changing login, signup, OAuth, invites, sessions, reset, or account-linking behavior.

## Avoid when
- Do not use when the system has no identity or session concept.

## Inputs to gather
- Authentication mechanism: password, SSO, MFA, tokens.
- Session management: creation, storage, validation, destruction.
- Token implementation: JWT, cookies, API keys.
- Privilege model and current auth incidents.

## Operating rules
- Authentication and session management are different problems. Review separately.
- Tokens should be short-lived with refresh capability.
- Session invalidation must work everywhere.
- MFA non-negotiable for high-privilege accounts.

- Use STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) as the threat enumeration framework unless the context demands a different model.
- Rate each threat by likelihood (1-5) x impact (1-5). Threats scoring 15+ need mitigations before ship. Threats scoring 8-14 need accepted-risk documentation. Below 8 is monitored.
- Every threat model must name the trust boundaries explicitly: where does untrusted input cross into a trusted zone? That boundary is the highest-value attack surface.
- Distinguish between threats to confidentiality, integrity, and availability. A threat to one is not necessarily a threat to the others.
- Threat models are attackergoal-first, not feature-first. Start from what an attacker wants to achieve, then trace backwards to how they could do it.
## Claude Code tool pattern
- Read the real data flow, auth model, config, and dependency surface before naming security posture.

## Expanded workflow
1. Map the authentication flow: login -> token -> session -> logout.
2. Review token implementation: type, lifetime, storage, revocation.
3. Check session management: creation, validation, expiration, invalidation.
4. Verify MFA implementation and enforcement.
5. Test common auth attacks: credential stuffing, session fixation, token theft.
6. Document findings with remediation priorities.

## Output contract
- Security review or model with risk ranking, exposure logic, and remediation direction.
- Assumptions, open questions, and where human security review is still required.

## Failure modes to avoid
- Long-lived tokens without revocation capability.
- Session fixation vulnerabilities.
- Missing MFA for privileged accounts.
- Incomplete session invalidation.
- Tokens stored in insecure locations.

## Handoff cues
- Auth/session review: findings, risk level, remediation steps, compliance status.
- Session management configuration assessment.
- Token handling and rotation recommendations.

## Example invocation
- Slash: `/sec_auth_session_review <task>`
- Natural language: "Use security Auth and Session Review to review authentication, session handling, and account-recovery flows for takeover risk."
- Example: "Review this surface like a real security operator, not a checklist generator."
- Example: "Tell me the plausible threats, likely exposures, and highest-value mitigations."
- Often paired with: `sec_threat_model`, `sec_appsec_review`, `safe_high_impact_changes`

## Quality bar
## Related workflows
- Security review: `sec_threat_model` â†’ `sec_appsec_review` â†’ `sec_data_flow_review`
- Every high-likelihood threat has a named mitigation or an explicitly accepted risk with rationale.
- Trust boundaries are diagrammed or clearly described.
- At least one insider threat scenario is included.
- The model is specific enough that an engineer could implement mitigations without guessing.
