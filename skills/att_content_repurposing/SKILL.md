---
name: att_content_repurposing
description: "Turn one strong source asset into channel-ready derivatives without losing the core message."
user-invocable: true
---

## Purpose
- Turn one strong source asset into channel-ready derivatives without losing the core message.

## Use when
- Use when a launch, webinar, article, demo, or case study should feed multiple channels.

## Avoid when
- Do not use when the source material is too weak or incoherent to repurpose well.

## Inputs to gather
- Source content to repurpose: original deep piece (blog post, case study, video, webinar).
- Target channels: where derivatives need to land (X threads, LinkedIn posts, short video, email, Slack).
- Team capacity: how much derivative production is realistic.
- Performance data: which formats and channels already work for this audience.

## Operating rules
- One deep piece should produce 3-5 derivatives minimum. If you can't spin off 3, the original wasn't structured for repurposing.
- Match derivative format to channel convention, not to the original format. A LinkedIn post has its own rhythm.
- Preserve the hook and proof, compress the middle. Every derivative needs the hook and the proof.
- Derivatives should reference the original, not replace it. Drive back to the deep piece for the full story.

## Claude Code tool pattern
- Use `WebFetch` to research competitor content and current platform conventions.
- Read existing site copy, product pages, and proof assets before drafting so output fits the real product truth.
- When external claims appear, verify before publishing with `safe_external_claims`.
- After drafting, run `att_proof_mining` to verify every claim has backing.

## Expanded workflow
1. Identify the source piece and its core hook, proof, and CTA.
2. List target channels and the native format each requires.
3. For each channel, extract: the hook (adapted to channel style), 1-2 strongest proof points, and the CTA (linking back to original).
4. Write each derivative in the channel's native format and length.
5. Bundle all derivatives with the original for coordinated scheduling via `att_content_calendar`.

## Output contract
## Failure modes to avoid
- Copy-pasting the same content across channels without format adaptation â€” each platform has its own conventions.
- Creating derivatives weaker than the original â€” if a derivative can't stand alone, don't ship it.
- Forgetting the CTA back to the deep piece â€” derivatives that don't drive traffic are dead ends.
- Over-producing derivatives from thin originals â€” 5 derivatives of a shallow post just creates 6 shallow pieces.

## Handoff cues
- List all derivatives created and their target channels.
- Note the scheduling order: which derivative posts when relative to the original.
- Flag any channels where the derivative needs platform-specific editing before posting.

## Example invocation
- Slash: `/att_content_repurposing <task>`
- Natural language: "Use attention Content Repurposing to turn one strong source asset into channel-ready derivatives without losing the core message."
- Example: "I wrote a 2000-word blog post. Spin it into a thread, LinkedIn post, and email tease."
- Example: "This launch post got good engagement. Break it into 3 channel-native derivatives."
- Often paired with: `att_message_house`, `att_launch_plan`, `att_proof_mining`

## Quality bar
## Related workflows
- Content system: `att_message_house` â†’ `att_content_calendar` â†’ `att_content_repurposing`
- Launch sequence: `att_launch_plan` â†’ `att_proof_mining` â†’ `att_thread_writer`
- Proof deployment: `att_proof_mining` â†’ `att_case_study_builder` â†’ `att_social_proof_pack`
