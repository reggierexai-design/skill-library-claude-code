---
name: sec_dependency_audit
description: "Review dependency trust, maintenance posture, and supply-chain risk before adoption or upgrade."
user-invocable: true
---

## Purpose
- Review dependency trust, maintenance posture, and supply-chain risk before adoption or upgrade.
- This is a **security specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before adding dependencies, SDKs, plugins, or external services to a stack.

## Avoid when
- Do not use as a vulnerability-scanner replacement when scanner output already exists.

## Inputs to gather
- Dependency inventory: direct and transitive, with versions and licenses.
- Vulnerability database: known CVEs for current versions.
- Supply chain risk: maintenance status, maintainer trust.
- License compliance: conflicts with distribution model?

## Operating rules
- Audit transitive dependencies, not just direct.
- License compliance is as important as vulnerability scanning.
- Popular does not equal maintained. Check activity, not stars.
- Automated scanning on every PR beats manual auditing.

- Use STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) as the threat enumeration framework unless the context demands a different model.
- Rate each threat by likelihood (1-5) x impact (1-5). Threats scoring 15+ need mitigations before ship. Threats scoring 8-14 need accepted-risk documentation. Below 8 is monitored.
- Every threat model must name the trust boundaries explicitly: where does untrusted input cross into a trusted zone? That boundary is the highest-value attack surface.
- Distinguish between threats to confidentiality, integrity, and availability. A threat to one is not necessarily a threat to the others.
- Threat models are attackergoal-first, not feature-first. Start from what an attacker wants to achieve, then trace backwards to how they could do it.
## Claude Code tool pattern
- Read the real data flow, auth model, config, and dependency surface before naming security posture.

## Expanded workflow
1. Generate the full dependency tree (direct + transitive).
2. Run automated vulnerability scanning.
3. Check license compliance for every dependency.
4. Assess maintenance health: last release, issue response, maintainer count.
5. Prioritize: critical CVEs first, license conflicts second, unmaintained third.
6. Set up automated scanning for ongoing monitoring.

## Output contract
- Security review or model with risk ranking, exposure logic, and remediation direction.
- Assumptions, open questions, and where human security review is still required.

## Failure modes to avoid
- Ignoring transitive dependencies â€” CVEs are often two levels deep.
- No license audit â€” GPL in proprietary code is legal risk.
- Assuming popular packages are maintained.
- One-time audit without ongoing monitoring.

## Handoff cues
- Dependency audit: vulnerabilities, license issues, unmaintained packages, remediation plan.
- Priority-ordered upgrade/replace actions.
- Ongoing monitoring recommendations.

## Example invocation
- Slash: `/sec_dependency_audit <task>`
- Natural language: "Use security Dependency Audit to review dependency trust, maintenance posture, and supply-chain risk before adoption or upgrade."
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
