---
name: legal_vendor_dpa
description: "Review data processing agreements with vendors who handle user data."
user-invocable: true
metadata: {"openclaw":{"emoji":"🤝"}}
---

# Vendor DPA

## Purpose
Review data processing agreements with vendors who handle user data. If a vendor processes your users' data, you need a DPA that meets GDPR and other privacy regulation requirements. Without a DPA, you're liable for the vendor's compliance failures.

## Use when
Use when onboarding any vendor that touches user data. Use when updating existing vendor agreements. Use when expanding to EU/UK markets.

## Avoid when
Don't sign a vendor's standard DPA without reviewing it. Don't assume vendor compliance claims are accurate — verify the terms match the claims.

## Inputs to gather
- Vendor inventory: every service that processes user data on your behalf.
- Data types: what user data does each vendor process?
- Current agreements: do DPAs exist for each vendor?
- GDPR requirements: art. 28 processor obligations checklist.
- Data transfer mechanisms: are cross-border transfers covered?

## Operating rules
- Every vendor that processes user data needs a DPA. No exceptions. "They said they're GDPR compliant" is not a DPA.
- The DPA must cover GDPR Art. 28 requirements: processing scope, sub-processors, data deletion, audit rights.
- Cross-border data transfers need adequate safeguards: SCCs, adequacy decisions, or approved frameworks.
- Sub-processor notification: vendors must notify you before adding sub-processors. You should have the right to object.
- Data deletion on termination: vendors must delete or return all data when the agreement ends. "We'll archive it" isn't deletion.

## Claude Code tool pattern
- Use `legal_privacy_policy` to ensure your privacy policy lists all vendors.
- Use `safe_pii_minimization` to reduce what vendors can access.
- Use `sec_data_flow_review` to map data flows to vendors.

## Expanded workflow
1. **Inventory all vendors processing user data.** Hosting, analytics, payment, email, support, CDNs, databases.
2. **Check for existing DPAs.** Which vendors have signed agreements? Which are operating without one?
3. **Review each DPA against GDPR Art. 28.** Processing scope defined? Sub-processor controls? Deletion guarantees? Audit rights?
4. **Check cross-border transfers.** Are adequate safeguards in place? SCCs signed? Adequacy decisions applicable?
5. **Flag vendors without DPAs.** Prioritize by data sensitivity and volume. Payment data > analytics data > CDN logs.
6. **Negotiate missing terms.** Sub-processor notification, deletion on termination, audit rights, breach notification timeline.
7. **Create a vendor DPA tracker.** Vendor, data types, DPA status, gaps, priority, renewal date.

## Output contract
- Vendor DPA tracker: vendor, data types, DPA status, gaps, priority
- GDPR Art. 28 compliance per vendor
- Cross-border transfer mechanisms per vendor
- Vendors requiring DPA negotiation
- DPA renewal schedule

## Failure modes to avoid
- Vendors processing user data without a DPA — you're liable for their compliance failures.
- DPAs that don't cover GDPR Art. 28 requirements — a signed document that doesn't protect you.
- No cross-border transfer safeguards — data exports without SCCs or adequacy decisions.
- No sub-processor notification — vendors can add sub-processors without telling you.
- No data deletion on termination — your users' data persists after you end the relationship.

## Handoff cues
- Vendor DPA tracker with compliance status.
- Vendors requiring DPA negotiation, prioritized.
- Cross-border transfer gaps.
- Next review and renewal dates.

## Example invocation
- Slash: `/legal_vendor_dpa <task>`
- Natural language: "Use legal_vendor_dpa to review data processing agreements with vendors who handle user data."

## Quality bar
Every vendor processing user data has a signed DPA. DPAs cover GDPR Art. 28 requirements. Cross-border transfers have adequate safeguards. Sub-processor notification is required. Data deletion on termination is guaranteed.

## Related workflows
- **Vendor compliance:** `legal_vendor_dpa` → `sec_data_flow_review` → `legal_privacy_policy`
- **Vendor onboarding:** `ops_vendor_eval` → `legal_vendor_dpa` → `safe_install_gate`
- **Privacy audit:** `legal_vendor_dpa` → `legal_privacy_policy` → `legal_terms_review`
