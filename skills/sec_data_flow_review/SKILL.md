---
name: sec_data_flow_review
description: "Trace sensitive data through a system and find storage, exposure, retention, and permission risks."
user-invocable: true
---

## Purpose
- Trace sensitive data through a system and find storage, exposure, retention, and permission risks.
- This is a **security specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a system handles personal data, secrets, uploads, analytics events, or cross-system sync.

## Avoid when
- Do not use when no meaningful data movement or storage is involved.

## Inputs to gather
- Data classification: PII, financial, health, public?
- Data flow diagram: origin, transit, persistence.
- Encryption status: at rest and in transit?
- Access controls at each point. Compliance requirements.

## Operating rules
- Data flows must be encrypted at every boundary.
- Map where PII lives and flows.
- Access controls follow least privilege at every point.
- Data retention must be enforced, not just documented.

- Use STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) as the threat enumeration framework unless the context demands a different model.
- Rate each threat by likelihood (1-5) x impact (1-5). Threats scoring 15+ need mitigations before ship. Threats scoring 8-14 need accepted-risk documentation. Below 8 is monitored.
- Every threat model must name the trust boundaries explicitly: where does untrusted input cross into a trusted zone? That boundary is the highest-value attack surface.
- Distinguish between threats to confidentiality, integrity, and availability. A threat to one is not necessarily a threat to the others.
- Threat models are attackergoal-first, not feature-first. Start from what an attacker wants to achieve, then trace backwards to how they could do it.
## Claude Code tool pattern
- Read the real data flow, auth model, config, and dependency surface before naming security posture.

## Expanded workflow
1. Create or update the data flow diagram.
2. Classify data by sensitivity at each point.
3. Verify encryption at rest and in transit.
4. Review access controls at every boundary.
5. Check compliance: consent, retention, deletion, right-to-erasure.
6. Document findings with compliance mapping.

## Output contract
- Security review or model with risk ranking, exposure logic, and remediation direction.
- Assumptions, open questions, and where human security review is still required.

## Failure modes to avoid
- Unencrypted data at any point in the flow.
- Unknown PII storage in logs, caches, or backups.
- Overly broad access controls.
- Retention policy without enforcement.

## Handoff cues
- Data flow review: data paths, encryption status, access controls, compliance gaps.
- Priority fixes for unprotected data flows.
- Compliance mapping (GDPR, CCPA, SOC2) where applicable.

## Example invocation
- Slash: `/sec_data_flow_review <task>`
- Natural language: "Use security Data Flow Review to trace sensitive data through a system and find storage, exposure, retention, and permission risks."
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
