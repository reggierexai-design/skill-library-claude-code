---
name: sec_logging_exposure_check
description: "Check logs, traces, and telemetry for secrets, personal data, and unsafe diagnostic leakage."
user-invocable: true
---

## Purpose
- Check logs, traces, and telemetry for secrets, personal data, and unsafe diagnostic leakage.
- This is a **security specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when adding logging, tracing, analytics, support dumps, or debugging instrumentation.

## Avoid when
- Do not use when there is no diagnostic or observability output involved.

## Inputs to gather
- Log destinations and who can access them.
- Log content at each level.
- PII inventory: what sensitive data might leak into logs?
- Log retention and access controls.

## Operating rules
- Assume logs will be read by unauthorized parties.
- Scan for PII, secrets, tokens, and internal IPs.
- Log the event, not the data.
- Log access needs its own access control.

- Use STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) as the threat enumeration framework unless the context demands a different model.
- Rate each threat by likelihood (1-5) x impact (1-5). Threats scoring 15+ need mitigations before ship. Threats scoring 8-14 need accepted-risk documentation. Below 8 is monitored.
- Every threat model must name the trust boundaries explicitly: where does untrusted input cross into a trusted zone? That boundary is the highest-value attack surface.
- Distinguish between threats to confidentiality, integrity, and availability. A threat to one is not necessarily a threat to the others.
- Threat models are attackergoal-first, not feature-first. Start from what an attacker wants to achieve, then trace backwards to how they could do it.
## Claude Code tool pattern
- Read the real data flow, auth model, config, and dependency surface before naming security posture.

## Expanded workflow
1. Inventory all log destinations and access controls.
2. Scan recent logs for PII, secrets, tokens, internal IPs.
3. Review code for logging statements that capture sensitive data.
4. Implement log redaction for sensitive fields.
5. Set up automated scanning for exposure detection.
6. Document findings and remediation.

## Output contract
- Security review or model with risk ranking, exposure logic, and remediation direction.
- Assumptions, open questions, and where human security review is still required.

## Failure modes to avoid
- Logging passwords, tokens, or API keys.
- No log access controls.
- Assuming log data is safe because it's 'internal'.
- No automated scanning â€” manual review catches 10% of what automated does.

## Handoff cues
- Logging exposure check: sensitive data found in logs, exposure risk, remediation steps.
- Log redaction recommendations.
- Monitoring and alerting for future exposure.

## Example invocation
- Slash: `/sec_logging_exposure_check <task>`
- Natural language: "Use security Logging Exposure Check to check logs, traces, and telemetry for secrets, personal data, and unsafe diagnostic leakage."
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
