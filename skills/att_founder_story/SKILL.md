---
name: att_founder_story
description: "Craft a believable founder or project origin story that builds trust without sounding manufactured."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udce3"}}
---

## Purpose
- Craft a believable founder or project origin story that builds trust without sounding manufactured.

## Use when
- Use for about pages, intros, investor or community blurbs, podcasts, and launch narratives.

## Avoid when
- Do not use if the user explicitly wants a brand voice with no founder presence.

## Inputs to gather
- The founder's real experience: what problem did they face, what did they try, what failed, what worked?
- Audience: investors, customers, hires, or press? Each needs a different angle.
- The vulnerability level: how honest can the founder be about failures and struggles?
- The connection to the product: how does the personal story prove the product's reason to exist?

## Operating rules
- Tell the origin in terms of a real problem, obsession, or unfair insight.
- Keep the hero as the user or mission, not the ego of the founder.
- Avoid fake struggle arcs and hype clichés.

## Claude Code tool pattern
- Use `WebFetch` to research competitor content and current platform conventions.
- Read existing site copy, product pages, and proof assets before drafting so output fits the real product truth.
- When external claims appear, verify before publishing with `safe_external_claims`.
- After drafting, run `att_proof_mining` to verify every claim has backing.

## Expanded workflow
1. Identify the key origin signal, pain, or insight.
2. Choose the credible narrative spine.
3. Write the story in the required length and tone.
4. Check it for trust, humility, and memorability.
## Output contract
- Story spine
- Short version
- Longer version if needed
- Notes on trust and proof
## Failure modes to avoid
- Triumph narratives without struggle.
- Disconnecting the story from the product.
- Ghostwriting in a voice that doesn't match the founder's style.
- Over-polishing — removing the warts that make the story credible.

## Handoff cues
- Provide all versions (2-min, 5-min, 30-sec) with context on where each fits.
- Flag any details the founder wants kept private.
- Note where this integrates: about page, investor deck, press kit.

## Example invocation
- Slash: `/att_founder_story <task>`
- Natural language: "Use founder Story to craft a believable founder or project origin story that builds trust without sounding manufactured."
- Example: "I am a disabled vet who taught myself to code and launched a SaaS. Craft the origin story."
- Example: "Write a 2-minute founder story for an investor meeting that connects my experience to the product."
- Often paired with: `att_message_house`, `att_launch_plan`, `att_proof_mining`

## Quality bar

- The story has a clear struggle → breaking point → solution arc.
- A reader finishes thinking 'I understand why this product exists.'
- The founder confirms it sounds like their actual voice.
- Multiple lengths available.

## Related workflows
- Content system: `att_message_house` → `att_content_calendar` → `att_content_repurposing`
- Launch sequence: `att_launch_plan` → `att_proof_mining` → `att_thread_writer`
- Proof deployment: `att_proof_mining` → `att_case_study_builder` → `att_social_proof_pack`
