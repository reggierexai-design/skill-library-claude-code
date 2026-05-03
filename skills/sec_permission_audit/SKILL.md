---
name: sec_permission_audit
description: "Audit roles, scopes, and permissions for least-privilege gaps and over-broad access."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83e\udeaa"}}
---

## Purpose
- Audit roles, scopes, and permissions for least-privilege gaps and over-broad access.
- This is a **security specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a product has roles, scopes, admin actions, integration tokens, or shared workspaces.

## Avoid when
- Do not use before the access model is visible in code, config, or docs.

## Inputs to gather
- Permission model: roles, permissions, assignment rules.
- Current access state: who has what right now.
- Least privilege policy: minimum access per role.
- Orphaned accounts: any that should no longer have access?

## Operating rules
- Audit actual access, not just the permission model.
- Check for privilege accumulation â€” role changes without permission cleanup.
- Orphaned accounts are attack surface.
- Automate access reviews â€” manual quarterly reviews miss 40%+.

- Use STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) as the threat enumeration framework unless the context demands a different model.
- Rate each threat by likelihood (1-5) x impact (1-5). Threats scoring 15+ need mitigations before ship. Threats scoring 8-14 need accepted-risk documentation. Below 8 is monitored.
- Every threat model must name the trust boundaries explicitly: where does untrusted input cross into a trusted zone? That boundary is the highest-value attack surface.
- Distinguish between threats to confidentiality, integrity, and availability. A threat to one is not necessarily a threat to the others.
- Threat models are attackergoal-first, not feature-first. Start from what an attacker wants to achieve, then trace backwards to how they could do it.
## Claude Code tool pattern
- Read the real data flow, auth model, config, and dependency surface before naming security posture.

## Expanded workflow
1. Export current access state: who has what permissions.
2. Compare actual access to least-privilege policy.
3. Identify over-provisioned accounts.
4. Find orphaned accounts: no owner, no recent activity.
5. Check for privilege accumulation.
6. Remediate: revoke excess, disable orphans.
7. Set up automated access review cadence.

## Output contract
- Security review or model with risk ranking, exposure logic, and remediation direction.
- Assumptions, open questions, and where human security review is still required.

## Failure modes to avoid
- Auditing the model but not the actual access assignments.
- Ignoring privilege accumulation.
- Leaving orphaned accounts active.
- One-time audit without ongoing review.

## Handoff cues
- Permission audit: roles, permissions, over-provisioning, least-violation findings, remediation.
- Priority fixes for over-provisioned access.
- Ongoing access review cadence recommendation.

## Example invocation
- Slash: `/sec_permission_audit <task>`
- Natural language: "Use security Permission Audit to audit roles, scopes, and permissions for least-privilege gaps and over-broad access."
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