---
name: att_social_proof_pack
description: "Turn testimonials, wins, screenshots, and adoption signals into reusable proof assets across channels."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udce3"}}
---

## Purpose
- Turn testimonials, wins, screenshots, and adoption signals into reusable proof assets across channels.

## Use when
- Use when the project has scattered proof that should be organized for site, sales, launch, or social use.

## Avoid when
- Do not manufacture proof or strip quotes of their real context.

## Inputs to gather

- Customer quotes: specific, attributed, and verifiable testimonials.
- Usage metrics: adoption numbers, time saved, error reduction, revenue impact.
- Case studies: before/after stories with named customers.
- Third-party validation: reviews, press mentions, awards, certifications.
- Audience: which proof types resonate most with the target buyer?

## Operating rules
- Proof is strongest when it is specific, attributed, and relevant to the buyer.
- Organize proof by audience question, not only by source.
- A small set of sharp proof assets beats a giant evidence drawer.

## Claude Code tool pattern
- Use `WebFetch` to research competitor content and current platform conventions.
- Read existing site copy, product pages, and proof assets before drafting so output fits the real product truth.
- When external claims appear, verify before publishing with `safe_external_claims`.
- After drafting, run `att_proof_mining` to verify every claim has backing.

## Expanded workflow
1. Inventory the available proof.
2. Group proof by claim, audience, or decision stage.
3. Draft reusable proof snippets and asset ideas.
4. Recommend where each proof asset should be deployed.
## Output contract
- Proof inventory
- Organized proof themes
- Reusable assets
- Deployment suggestions
## Failure modes to avoid

- Vague testimonials — 'Great product!' proves nothing. Specific outcomes prove everything.
- Unattributed quotes — 'A happy customer' is not social proof. Named sources with context are.
- Stale proof — a testimonial from 2020 about a product that's changed 5 times since isn't credible.
- Proof mismatch — showing enterprise case studies to SMB buyers creates doubt, not confidence.
- Hoarding proof in one place — social proof should be deployed across landing pages, emails, sales decks, and threads.

## Handoff cues

- Provide the proof pack organized by type and audience.
- Flag any proof that needs refreshing (stale or from outdated product versions).
- Note where each proof point should be deployed.
- List gaps: claims that still lack supporting proof.

## Example invocation
- Slash: `/att_social_proof_pack <task>`
- Natural language: "Use social Proof Pack to turn testimonials, wins, screenshots, and adoption signals into reusable proof assets across channels."
- Example: "Organize these 15 testimonials into a proof pack by claim and audience."
- Example: "I have usage data and 5 reviews. Build a social proof pack for the landing page."
- Often paired with: `att_message_house`, `att_launch_plan`, `att_proof_mining`

## Quality bar
- A social-proof pack makes credibility easier to deploy without exaggeration.

## Related workflows
- Content system: `att_message_house` → `att_content_calendar` → `att_content_repurposing`
- Launch sequence: `att_launch_plan` → `att_proof_mining` → `att_thread_writer`
- Proof deployment: `att_proof_mining` → `att_case_study_builder` → `att_social_proof_pack`
