---
name: sec_safe_disclosure_writeup
description: "Write a precise security issue report with impact, evidence, and safe remediation guidance."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udce3"}}
---

## Purpose
- Write a precise security issue report with impact, evidence, and safe remediation guidance.
- This is a **security specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when documenting a security issue for maintainers, internal teams, or responsible disclosure.

## Avoid when
- Do not use to write exploitation instructions or public proof-of-concept detail.

## Inputs to gather
- Vulnerability details: issue, severity, affected versions.
- Discovery timeline: when found, by whom, exploited?
- Fix status: patch available, in progress, not started?
- Reporter expectations: credit, bounty, timing.
- Regulatory requirements: mandatory disclosure timelines?

## Operating rules
- Coordinated disclosure over full disclosure.
- Be precise about affected versions.
- Credit the reporter unless they request anonymity.
- Include remediation steps, not just the vulnerability.

- Use STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) as the threat enumeration framework unless the context demands a different model.
- Rate each threat by likelihood (1-5) x impact (1-5). Threats scoring 15+ need mitigations before ship. Threats scoring 8-14 need accepted-risk documentation. Below 8 is monitored.
- Every threat model must name the trust boundaries explicitly: where does untrusted input cross into a trusted zone? That boundary is the highest-value attack surface.
- Distinguish between threats to confidentiality, integrity, and availability. A threat to one is not necessarily a threat to the others.
- Threat models are attackergoal-first, not feature-first. Start from what an attacker wants to achieve, then trace backwards to how they could do it.
## Claude Code tool pattern
- Read the real data flow, auth model, config, and dependency surface before naming security posture.

## Expanded workflow
1. Document the vulnerability: description, severity, affected versions, PoC.
2. Contact the vendor privately with 90-day fix timeline.
3. Maintain communication on fix progress.
4. If vendor unresponsive after deadline, prepare public disclosure.
5. Write the disclosure: vulnerability, impact, versions, remediation, credit.
6. Coordinate public release with vendor patch when possible.

## Output contract
- Security review or model with risk ranking, exposure logic, and remediation direction.
- Assumptions, open questions, and where human security review is still required.

## Failure modes to avoid
- Full disclosure without vendor notification.
- Imprecise affected versions â€” 'some versions' causes panic or complacency.
- Not crediting the researcher.
- Missing remediation steps â€” users need to know how to protect themselves.

## Handoff cues
- Disclosure writeup: vulnerability description, impact, timeline, remediation, coordination status.
- Reporter communication log.
- Public disclosure timeline and responsible parties.

## Example invocation
- Slash: `/sec_safe_disclosure_writeup <task>`
- Natural language: "Use security Safe Disclosure Writeup to write a precise security issue report with impact, evidence, and safe remediation guidance."
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