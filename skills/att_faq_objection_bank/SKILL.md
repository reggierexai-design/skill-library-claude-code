---
name: att_faq_objection_bank
description: "Build a reusable bank of buyer questions, objections, and grounded answers across site, sales, and support."
---

# FAQ & Objection Bank

## Purpose
- Build a reusable bank of buyer questions, objections, and grounded answers across site, sales, and support.
- This is an **attention specialist** for turning the questions that kill deals into the answers that close them.

## Use when
- Use when the same questions or objections keep appearing in launches, demos, calls, or support.
- Use when building or updating an FAQ page for a product site.
- Use when onboarding new sales or support team members who need objection handling guidance.
- Use when conversion rate drops because prospects hit the same unanswered concern.

## Avoid when
- Do not answer objections with vague reassurance and no proof — "we're very secure" is not an answer, it's a dodge.
- Do not use when you don't have real objection data yet — go collect it from sales calls, support tickets, and lost deals first.
- Do not use to create aspirational FAQs that answer questions you wish people asked instead of the ones they actually ask.

## Inputs to gather
- Top objections from sales calls, support tickets, and lost deals. Pull the actual language, not your interpretation of it.
- Audience: prospects, users, partners, or internal stakeholders? Each has different objections and needs different answers.
- Current FAQ content: what already exists on the site, in the sales deck, and in support docs? What's missing?
- Objection categories: pricing, capability, trust, timing, competitive, technical, compliance, switching cost.
- Proof inventory: for each objection, what evidence can you cite? (data, testimonials, comparisons, demos)

## Operating rules
- **The best FAQ answers reduce uncertainty, not just polish tone.** A well-written answer that doesn't address the real concern is marketing copy, not objection handling. Name the concern directly, acknowledge it honestly, then address it with proof.
- **Keep answers honest about fit, limits, and tradeoffs.** "We don't do X" is a better answer than "We do X... sort of... in some cases." Honesty builds trust; hedging destroys it.
- **Group objections by decision stage.** Pre-awareness objections ("what is this?"), evaluation objections ("is it better than X?"), and purchase objections ("can I afford this?") need different answer formats.
- **Answer the real objection, not the surface one.** "It's too expensive" usually means "I'm not sure the value justifies the cost." Answer the value question, not just the price question.
- **Include the counter-objection.** After you answer, what will they say next? Pre-handle it. Strong objection handling is a conversation, not a one-liner.

## Claude Code tool pattern
- Use `Read` to load support ticket exports, sales call notes, and chat transcripts where real objections live.
- Use `att_proof_mining` to find proof for each answer — every answer should have at least one proof point.
- After building the bank, deploy answers to: FAQ page (`att_landing_page_story`), sales deck (`sales_demo_flow`), and email sequences (`att_email_nurture_sequences`).

## Expanded workflow
1. **Collect real objections from real conversations.** Don't brainstorm — mine. Pull from support tickets, lost deal notes, sales calls, demo recordings, social comments, and app store reviews. Use the customer's actual language.
2. **Group them by theme and decision stage.** Pricing objections cluster together. Trust objections cluster together. Map which stage each objection typically appears: awareness, evaluation, decision, or post-purchase.
3. **Draft grounded answers with proof and next steps.** Each answer structure: (1) acknowledge the concern directly, (2) address it with a specific proof point, (3) reframe if needed, (4) suggest a next action that resolves remaining doubt.
4. **Add counter-objections.** For each answer, what will the skeptic say next? Pre-handle the follow-up.
5. **Prioritize the top 10-15.** A bank of 50 entries is unusable. A bank of 12 well-handled objections that cover 80% of real conversations is gold.
6. **Recommend where each answer should live.** Some belong on the FAQ page, some in the sales deck, some in email sequences, some in support macros. Not every answer belongs everywhere.
7. **Return the objection bank with deployment recommendations.**

## Output contract
- Top 10-15 objections with real customer language
- Each objection: theme, decision stage, answer with proof, counter-objection, and deployment location
- Proof gap analysis: which answers lack strong evidence
- Deployment plan: where each answer goes (site, sales, support, email)
- Maintenance note: when to review and update the bank

## Failure modes to avoid
- Answering the question you wish they asked instead of the real objection — this is the most common failure.
- Generic answers without proof — "we're very reliable" is not an answer to "what happens when it goes down?"
- Missing the most common objections because they're uncomfortable — the objections you avoid are the ones killing your conversion.
- Too many entries — focus on the top 10-15 that cover 80% of real conversations.
- Writing answers that sound defensive — confident, specific, and honest beats reactive and vague.

## Handoff cues
- Full objection bank with answers, proof, counter-objections, and deployment locations.
- Proof gaps flagged: answers that need stronger evidence before going public.
- Integration points: where this connects to landing page, sales deck, and email sequences.
- Review schedule: when to check if new objections are emerging and old answers need updating.

## Example invocation
- Slash: `/att_faq_objection_bank <task>`
- Natural language: "Build an objection bank from these support tickets and sales calls."
- Example: "We keep getting asked if this is just X. Build the objection bank."
- Example: "Extract the top 10 objections from these 50 support tickets and write grounded answers."
- Often paired with: `att_message_house`, `att_landing_page_story`, `sales_demo_flow`

## Quality bar
- Every answer addresses the real concern behind the objection, not just the surface question.
- Every answer includes at least one proof point (data, testimonial, comparison, or demo).
- The top 10 objections cover 80%+ of real customer concerns.
- Answers are honest about limitations, not defensive or evasive.
- The bank is organized by decision stage, not just topic.

## Related workflows
- Collection: `sales_discovery_call_plan` → `att_faq_objection_bank`
- Deployment: `att_faq_objection_bank` → `att_landing_page_story` → `att_email_nurture_sequences`
- Proof backing: `att_proof_mining` → `att_faq_objection_bank`
