---
name: legal_terms_review
description: "Review terms of service and privacy policy for gaps, risks, and compliance."
user-invocable: true
---

# Terms Review

## Purpose
Review terms of service and privacy policy for gaps, risks, and compliance with applicable regulations. These documents define your relationship with users and limit your liability. Gaps aren't just legal risks — they create user expectations you can't meet.

## Use when
Use before launching a new product or feature that changes user data handling. Use when expanding to new markets. Use annually as a compliance check.

## Avoid when
Don't use as a substitute for actual legal counsel. Don't use for regulated industries without professional legal review.

## Inputs to gather
- Current terms of service and privacy policy documents.
- Data handling practices: what data do you collect, store, process, and share?
- User jurisdictions: where do your users live?
- Third-party services: what APIs, CDNs, analytics, and payment processors touch user data?
- Business model: free, paid, subscription, advertising?

## Operating rules
- Terms must match actual practice. If terms say you don't sell data but you share with ad networks, fix the practice or the terms.
- Privacy policy must cover every data touchpoint. If you're not sure what you collect, you're not ready to write the policy.
- Include required clauses per jurisdiction: GDPR (EU), CCPA (California), COPPA (children). Not optional.
- Terms should be readable, not just legally defensible. If users can't understand what they're agreeing to, the terms aren't working.
- Review triggers: any change in data handling, user geography, or third-party tools requires a terms review.

## Claude Code tool pattern
- Use `legal_privacy_policy` for privacy-specific review.
- Use `legal_cookie_consent` for cookie and tracking compliance.
- Use `safe_pii_minimization` to reduce data that needs coverage.

## Expanded workflow
1. **Read current terms end to end.** Note anything vague, outdated, or missing. Read as a user, then read as a regulator.
2. **Map data practices.** What data is collected, stored, processed, shared, and deleted? Every touchpoint.
3. **Check jurisdiction requirements.** GDPR, CCPA, COPPA, industry-specific. List what's required vs what's present.
4. **Compare terms to practice.** Every clause must match what actually happens. Mismatches are liabilities.
5. **Check third-party data sharing.** Every API, analytics tool, and processor must be disclosed in the policy.
6. **Assess readability.** Can a non-lawyer understand the key points? If not, rewrite for clarity.
7. **List required changes with priority and risk level.** Critical gaps first, improvements second.

## Output contract
- Gap analysis: missing clauses, outdated language, practice mismatches
- Jurisdiction compliance checklist
- Third-party data sharing audit
- Readability assessment
- Priority-ordered change list with risk levels

## Failure modes to avoid
- Terms that don't match practice — the most common and dangerous gap.
- Missing jurisdiction-specific clauses — GDPR and CCPA are non-negotiable.
- Undisclosed third-party data sharing.
- Legalese that users can't understand.
- No review triggers — terms go stale the moment you add a new tool.

## Handoff cues
- Gap analysis with priority and risk per gap.
- Jurisdiction compliance status.
- Required changes with recommended language.
- Next review date and review triggers.

## Example invocation
- Slash: `/legal_terms_review <task>`
- Natural language: "Use legal_terms_review to review terms of service and privacy policy for gaps, risks, and compliance."

## Quality bar
Every data practice is reflected in the terms. All applicable jurisdiction requirements are met. Third-party data sharing is fully disclosed. Key sections are readable by non-lawyers. Review triggers are documented.

## Related workflows
- **Legal review suite:** `legal_terms_review` → `legal_privacy_policy` → `legal_cookie_consent` → `legal_disclaimer_audit`
- **Data safety:** `safe_pii_minimization` → `legal_privacy_policy` → `legal_terms_review`
- **Launch readiness:** `legal_terms_review` → `legal_ip_check` → `eng_release_readiness`
