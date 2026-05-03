---
name: att_outbound_sequences
description: "Write founder-led or team outbound messages that earn replies without spammy patterns."
---

# Outbound Sequences

## Purpose
- Write founder-led or team outbound messages that earn replies without spammy patterns.
- This is an **attention specialist** for building outreach sequences that respect the recipient's time while earning their attention.

## Use when
- Use for partnerships, user discovery, waitlist invites, sales outreach, or creator collaboration asks.
- Use when cold-reaching to prospects who don't know you yet and need a reason to care.
- Use when warm-reaching to people who expressed interest but haven't converted yet.

## Avoid when
- Do not use when the list quality and audience fit are still unknown — bad lists produce bad outreach regardless of copy quality.
- Do not use when you haven't defined what a "reply" looks like — a reply that doesn't advance the conversation is wasted effort.
- Do not use when you plan to send the same message to 500 people unchanged — that's spam, not outreach.

## Inputs to gather
- Target persona: title, company size, likely pain points, what they care about right now.
- Offer and proof: what are you offering and what evidence supports it? Why should they believe you?
- Sequence length: how many touches before stopping? (3-5 is typical; more than 5 is pestering.)
- Channel: email, LinkedIn, or mixed? Each has different norms, response rates, and acceptable frequency.
- Existing reply data: what subject lines, angles, and formats already get responses? Double down on what works.

## Operating rules
- **Make the message about the recipient's context, not your excitement alone.** "I built something amazing" is about you. "I noticed your team is dealing with X — we solved that for [similar company]" is about them. Lead with relevance.
- **Lead with relevance, value, or an honest reason for contact.** Why THIS person? Why now? If you can't answer that specifically, your list isn't targeted enough.
- **Keep the ask small and specific.** "Can I show you a demo?" is a big ask. "Would it be useful to see how [similar company] cut X by Y%?" is a small ask with a clear value proposition.
- **Each touch must add new value.** Touch 1: relevance + value proposition. Touch 2: new proof point or insight. Touch 3: new angle or smaller ask. Repetition without addition = spam.
- **Include a break-up email.** The final touch should explicitly close the loop: "I won't keep reaching out, but here's one last thing in case it's useful." This respects their time and sometimes triggers the reply that silence didn't.
- **One CTA per email.** "Let's chat, or check out our blog, or reply with questions" is three CTAs. Pick one.

## Claude Code tool pattern
- Use `WebFetch` to research the prospect's company, recent news, and relevant context before personalizing outreach.
- Use `att_proof_mining` to pull the strongest proof point for each sequence's value proposition.
- After sequences are running, track opens, replies, and conversion to optimize subject lines and angles.

## Expanded workflow
1. **Define the audience segment and desired reply.** Not just "any reply" — what conversation do you want to start? A demo request? A pilot discussion? A content collaboration? The desired reply shapes the ask.
2. **Write the opener (touch 1).** Structure: (1) context line — why them, why now, (2) value line — what they get, (3) ask — one small specific action, (4) proof — one supporting evidence. Keep it under 100 words.
3. **Write the follow-up (touch 2, 3-5 days later).** Add a new proof point, insight, or angle. Don't repeat touch 1. Reference the previous email briefly. Same CTA, framed differently.
4. **Write touch 3 (if needed).** Smaller ask or different angle. Share a relevant resource they'd find useful regardless of whether they reply. Build goodwill even in silence.
5. **Write the break-up email (final touch).** Explicitly close the sequence. Leave the door open. Sometimes this is the one that gets the reply.
6. **Create subject line variants.** Subject lines determine 50%+ of open rates. Write 3-5 per touch: specific vs curious vs personal. Plan A/B tests.
7. **Return the full sequence with tracking plan.** Touches, timing, subject variants, and what to measure.

## Output contract
- Audience segment and desired reply type
- Full sequence: 3-5 touches with subject lines, body copy, and CTAs
- Subject line variants for A/B testing
- Break-up email
- Tracking plan: opens, replies, meetings booked, conversion rate
- Personalization tokens: what to customize per recipient vs what stays constant

## Failure modes to avoid
- All emails repeat the same pitch — each touch must add new value, not just repeat the ask.
- Over-personalizing to the point of creepiness — mentioning their LinkedIn activity from 3 weeks ago reads as surveillance, not relevance.
- No break-up email — open sequences that never end are spam. Close the loop.
- Weak CTAs — "let me know if interested" is not a call to action. "Would a 15-minute call on Tuesday work?" is.
- Ignoring reply data — double down on what works, kill what doesn't.
- Sending unmodified templates — every email should have at least one personalized element.

## Handoff cues
- Full sequence with subject lines, timing, and CTAs ready to load into the email tool.
- A/B test variants for touch 1 subject line.
- Tracking plan: what to measure and when to optimize.
- Personalization checklist: what to customize per recipient.

## Example invocation
- Slash: `/att_outbound_sequences <task>`
- Natural language: "Write an outbound sequence for these prospects."
- Example: "Write a 3-touch cold email sequence to potential beta testers."
- Example: "I am reaching out to 20 podcast hosts. Craft a sequence that earns replies."
- Often paired with: `att_message_house`, `sales_discovery_call_plan`, `att_partnership_pitch`

## Quality bar
- Every sequence has a clear hypothesis: what belief are you changing or what action are you prompting?
- Each touch adds new value — no repetition without addition.
- Subject lines are specific, not clickbait.
- The break-up email is included and explicitly closes the loop.
- Templates include personalization tokens, not just find-replace names.

## Related workflows
- Sales pipeline: `sales_discovery_call_plan` → `att_outbound_sequences` → `sales_followup_sequence`
- Partnership outreach: `att_partnership_pitch` → `att_outbound_sequences`
- Proof backing: `att_proof_mining` → `att_outbound_sequences`
