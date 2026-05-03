---
name: legal_disclaimer_audit
description: "Audit all disclaimers, disclosures, and legal notices across your product surfaces."
user-invocable: true
metadata: {"openclaw":{"emoji":"⚠️"}}
---

# Disclaimer Audit

## Purpose
Audit all disclaimers, disclosures, and legal notices across your product surfaces. Missing disclaimers don't just expose you to liability — they create user expectations you can't meet. A product that claims to "help with finances" without a "not financial advice" disclaimer creates legal and trust problems.

## Use when
Use before launch. Use when adding new features that change what your product does or doesn't do. Use when expanding to regulated-adjacent markets (health, finance, legal).

## Avoid when
Don't use as a substitute for legal advice on what disclaimers are required for your specific industry. Don't add disclaimers that contradict your product's actual behavior.

## Inputs to gather
- Product surfaces: website, app, emails, social media, ads, docs.
- Claims made: what does your product say it does?
- Limitations: what doesn't it do? What can't it guarantee?
- Industry regulations: are there required disclaimers for your category?
- User expectations: what do users think they're getting?

## Operating rules
- Every claim needs a corresponding limitation. If you say "AI-powered," you need to say what the AI does and doesn't do.
- Required disclosures are non-negotiable. If your industry requires a disclaimer, it must be present and prominent.
- Disclaimers must be visible, not buried. Footer text that users never scroll to isn't a disclaimer — it's a fig leaf.
- Testimonials need disclosure. If you show user quotes, disclose any compensation or relationship.
- Health/financial/legal claims are the highest risk. If your product touches any of these, get professional legal review.

## Claude Code tool pattern
- Use `legal_terms_review` for the overall terms audit.
- Use `safe_external_claims` for claim substantiation.
- Use `att_message_house` for marketing claim alignment.

## Expanded workflow
1. **Inventory all product surfaces.** Website, app, emails, ads, social, docs, in-app messaging.
2. **List all claims.** What does each surface say your product does? Be thorough — implicit claims count too.
3. **Identify required disclaimers.** Industry regulations, FTC guidelines, jurisdiction-specific requirements.
4. **Match claims to limitations.** Every claim needs a corresponding disclaimer or limitation.
5. **Check visibility.** Are disclaimers where users can actually see them? Above the fold? Near the claim?
6. **Audit testimonials.** Are disclosures present for compensated quotes? Are they genuine?
7. **Create a disclaimer inventory.** Surface, claim, disclaimer, visibility, status (present/missing/buried).

## Output contract
- Disclaimer inventory: surface, claim, disclaimer, visibility, status
- Required disclosures: present vs missing
- Claim-limitation pairs: every claim has a corresponding limitation
- Visibility assessment: prominent vs buried
- High-risk claims flagged for legal review

## Failure modes to avoid
- Making claims without corresponding disclaimers.
- Burying disclaimers where users can't see them — if they have to scroll to the footer, it's buried.
- Missing industry-required disclosures.
- Testimonials without compensation disclosure.
- Health/financial/legal claims without professional legal review.

## Handoff cues
- Disclaimer inventory with gaps identified.
- Required disclosures: present or missing per surface.
- High-risk claims flagged for immediate legal review.
- Visibility improvements needed.

## Example invocation
- Slash: `/legal_disclaimer_audit <task>`
- Natural language: "Use legal_disclaimer_audit to audit all disclaimers, disclosures, and legal notices across your product surfaces."

## Quality bar
Every claim has a corresponding limitation. Required disclosures are present and prominent. Testimonials include compensation disclosure. High-risk claims are flagged for legal review. Disclaimer inventory is complete and current.

## Related workflows
- **Disclaimer audit:** `legal_disclaimer_audit` → `safe_external_claims` → `legal_terms_review`
- **Marketing compliance:** `att_message_house` → `legal_disclaimer_audit` → `att_launch_plan`
- **Launch readiness:** `legal_disclaimer_audit` → `legal_ip_check` → `eng_release_readiness`
