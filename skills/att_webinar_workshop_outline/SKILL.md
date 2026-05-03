---
name: att_webinar_workshop_outline
description: "Outline webinars and workshops that teach something useful while creating qualified attention for the project."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udce3"}}
---

## Purpose
- Outline webinars and workshops that teach something useful while creating qualified attention for the project.

## Use when
- Use when planning a live workshop, webinar, demo session, or educational event tied to the project.

## Avoid when
- Do not turn a workshop into a disguised pitch with no teaching value.

## Inputs to gather

- Topic and audience: what will be covered and who's attending?
- Duration: 30 min, 60 min, or 90 min?
- Format: lecture, demo, workshop (hands-on), panel, or Q&A-heavy?
- Desired outcome: what should attendees know or do afterward?
- Speaker expertise: what can the speaker credibly teach vs what needs guest support?

## Operating rules
- Lead with a real problem and a useful takeaway.
- Give the audience a reason to stay through the whole session.
- Design the event so follow-up conversion feels natural, not forced.

## Claude Code tool pattern
- Use `WebFetch` to research competitor content and current platform conventions.
- Read existing site copy, product pages, and proof assets before drafting so output fits the real product truth.
- When external claims appear, verify before publishing with `safe_external_claims`.
- After drafting, run `att_proof_mining` to verify every claim has backing.

## Expanded workflow
1. Choose the audience and session promise.
2. Map the teaching arc and key examples.
3. Add interaction points and follow-up calls to action.
4. Prepare derivative assets for replay, clips, and email.
## Output contract
- Session promise
- Outline
- Interactive elements
- Follow-up asset plan
## Failure modes to avoid

- No interaction for 60 minutes — attention drops after 10 minutes of passive content. Build in questions, polls, or exercises every 10-15 minutes.
- Covering too much — a webinar that tries to teach 10 things teaches nothing well.
- All theory, no practice — attendees need to see or do something, not just hear about it.
- No follow-up plan — the webinar ends and attendees disappear. The real value is in the post-event nurture.
- Over-relying on slides — demos, live exercises, and visual storytelling outperform bullet-heavy slides.

## Handoff cues

- Provide the full outline with timing per section.
- List interaction points (polls, exercises, Q&A) with when they happen.
- Flag any technical requirements (screen share, breakout rooms, polling tool).
- Note the follow-up email sequence plan.

## Example invocation
- Slash: `/att_webinar_workshop_outline <task>`
- Natural language: "Use webinar or Workshop Outline to outline webinars and workshops that teach something useful while creating qualified attention for the project."
- Example: "Outline a 60-minute workshop on building an AI workforce as a solo founder."
- Example: "Design a 30-min webinar that teaches one useful thing and naturally leads to product interest."
- Often paired with: `att_message_house`, `att_launch_plan`, `att_proof_mining`

## Quality bar
- A strong workshop outline creates value during the event and attention afterward.

## Related workflows
- Content system: `att_message_house` → `att_content_calendar` → `att_content_repurposing`
- Launch sequence: `att_launch_plan` → `att_proof_mining` → `att_thread_writer`
- Proof deployment: `att_proof_mining` → `att_case_study_builder` → `att_social_proof_pack`
