---
name: legal_privacy_policy
description: "Draft or update a privacy policy that covers your actual data practices and meets regulatory requirements."
user-invocable: true
---

# Privacy Policy

## Purpose
Draft or update a privacy policy that covers your actual data practices. A privacy policy that doesn't match reality is worse than no policy — it creates legal exposure and erodes trust. This skill ensures the policy reflects what you actually do.

## Use when
Use when launching a product that collects any user data. Use when adding new data collection. Use when expanding to new jurisdictions. Use when a third-party tool changes what data it processes.

## Avoid when
Don't use as a substitute for legal review in regulated industries (health, finance, children's products). Don't use a template without customizing it to your actual practices.

## Inputs to gather
- Current privacy policy (if exists).
- Data inventory: what data you collect, why, where it's stored, who processes it, how long you keep it.
- Third-party processors: every service that touches user data.
- User rights requests: how do users access, delete, or export their data?
- Applicable regulations: GDPR, CCPA, PIPEDA, etc.

## Operating rules
- The policy must describe what you actually do, not what you wish you did. If reality doesn't match the policy, change reality first.
- List every third-party processor. Missing even one creates a compliance gap that regulators notice.
- Data retention needs explicit timelines. "We keep data as long as needed" isn't a retention policy.
- User rights must be actionable. Describe exactly how users exercise each right — not just that they have it.
- Update the policy when data practices change, not just on a schedule. New tool = new policy update.

## Claude Code tool pattern
- Use `safe_pii_minimization` to reduce data collection before writing the policy.
- Use `legal_terms_review` for the broader terms review.
- Use `legal_cookie_consent` for tracking-specific compliance.

## Expanded workflow
1. **Inventory all data practices.** Collection, storage, processing, sharing, deletion. Every touchpoint.
2. **List all third-party processors.** APIs, analytics, payment, hosting, email services. If it touches user data, it goes in the list.
3. **Define retention periods.** How long do you keep each data type and why? Be specific.
4. **Document user rights processes.** Access, deletion, correction, portability. How does a user actually exercise each right?
5. **Draft the policy.** Clear language covering all of the above. Plain English, not legalese.
6. **Cross-check against applicable regulations.** GDPR, CCPA, PIPEDA, etc. Does the policy meet each requirement?
7. **Test readability.** Can a user understand what data you collect and why? If not, rewrite.

## Output contract
- Privacy policy draft covering all data practices
- Third-party processor list with data types per processor
- Data retention schedule
- User rights process documentation
- Regulation compliance checklist

## Failure modes to avoid
- Policy doesn't match practice — the most dangerous failure. Regulators and users both penalize this.
- Missing third-party processors — one missing processor can invalidate the whole policy.
- No retention timelines — "we keep data indefinitely" isn't a policy.
- User rights are described but not actionable — "you have the right to deletion" without explaining how.
- Template without customization — a privacy policy that doesn't reflect your actual practices.

## Handoff cues
- Privacy policy draft or updated version.
- Compliance gaps identified with remediation steps.
- Third-party processor inventory.
- Next review date and update triggers.

## Example invocation
- Slash: `/legal_privacy_policy <task>`
- Natural language: "Use legal_privacy_policy to draft or update a privacy policy that covers your actual data practices and meets regulatory requirements."

## Quality bar
Policy accurately describes all current data practices. Every third-party processor is listed. Retention periods are explicit. User rights are actionable, not just described. Policy is readable by non-lawyers.

## Related workflows
- **Privacy compliance suite:** `legal_privacy_policy` → `legal_cookie_consent` → `safe_pii_minimization` → `legal_terms_review`
- **Data safety:** `safe_pii_minimization` → `legal_privacy_policy` → `sec_data_flow_review`
- **Launch readiness:** `legal_privacy_policy` → `legal_disclaimer_audit` → `eng_release_readiness`
