---
name: sec_threat_model
description: "Model assets, threats, trust boundaries, and mitigations before building or changing a system."
user-invocable: true
---

## Purpose
- Model assets, threats, trust boundaries, and mitigations before building or changing a system.
- This is a **security specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when planning a feature, integration, auth flow, or architecture change that could create abuse paths.

## Avoid when
- Do not use as a substitute for formal legal, compliance, or penetration-testing claims.

## Inputs to gather
- System architecture: components, data flows, trust boundaries.
- Asset inventory: what's valuable and where does it live?
- Threat actors: who might attack and what are their capabilities?
- Attack surface: external entry points and exposed services.
- Existing security controls and their effectiveness.

## Operating rules
- Model threats from the attacker's perspective, not the defender's. Attackers don't follow your architecture diagram â€” they find the weakest link.
- Prioritize by impact and likelihood. A nation-state attack on a todo app is low priority; a credential stuffing attack on a SaaS app is high priority.
- Every threat needs a mitigation or an accepted risk. A threat without a mitigation is an unmanaged risk.
- Threat models are living documents. Update when architecture changes, not just during annual reviews.

- Use STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) as the threat enumeration framework unless the context demands a different model.
- Rate each threat by likelihood (1-5) x impact (1-5). Threats scoring 15+ need mitigations before ship. Threats scoring 8-14 need accepted-risk documentation. Below 8 is monitored.
- Every threat model must name the trust boundaries explicitly: where does untrusted input cross into a trusted zone? That boundary is the highest-value attack surface.
- Distinguish between threats to confidentiality, integrity, and availability. A threat to one is not necessarily a threat to the others.
- Threat models are attackergoal-first, not feature-first. Start from what an attacker wants to achieve, then trace backwards to how they could do it.
## Claude Code tool pattern
- Read the real data flow, auth model, config, and dependency surface before naming security posture.

## Expanded workflow
1. Map the system architecture and trust boundaries.
2. Inventory assets and their value to attackers.
3. Identify threat actors and their capabilities.
4. Enumerate attack vectors using STRIDE or similar framework.
5. Assess each threat: likelihood x impact.
6. Define mitigations for high-priority threats.
7. Document accepted risks with rationale.
8. Schedule threat model review when architecture changes.

## Output contract
- Security review or model with risk ranking, exposure logic, and remediation direction.
- Assumptions, open questions, and where human security review is still required.

## Failure modes to avoid
- Modeling threats from the defender's perspective â€” attackers find the weak links.
- Ignoring insider threats â€” not all attackers are external.
- Listing threats without mitigations â€” unmanaged risks accumulate.
- Static threat models â€” architecture changes invalidate the model.
- Over-complicating the model â€” a useful threat model fits on one page.

## Handoff cues
- Threat model: assets, threat actors, attack vectors, mitigations, residual risk.
- Priority mitigations ranked by risk reduction.
- Validation plan: how to test that mitigations work.

## Example invocation
- Slash: `/sec_threat_model <task>`
- Natural language: "Use security Threat Model to model assets, threats, trust boundaries, and mitigations before building or changing a system."
- Example: "Review this surface like a real security operator, not a checklist generator."
- Example: "Tell me the plausible threats, likely exposures, and highest-value mitigations."
- Often paired with: `sec_appsec_review`, `safe_high_impact_changes`

## Quality bar
## Related workflows
- Security review: `sec_threat_model` â†’ `sec_appsec_review` â†’ `sec_data_flow_review`
- Every high-likelihood threat has a named mitigation or an explicitly accepted risk with rationale.
- Trust boundaries are diagrammed or clearly described.
- At least one insider threat scenario is included.
- The model is specific enough that an engineer could implement mitigations without guessing.
