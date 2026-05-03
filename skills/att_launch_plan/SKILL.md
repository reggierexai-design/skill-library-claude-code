--- name: att_launch_plan description: "Design a focused launch plan with narrative, assets, timing, and channel sequencing." user-invocable: true disable-model-invocation: false metadata: {"openclaw":{"emoji":"\ud83d\ude80"}} ---
# Launch Plan

## Purpose
- Design a focused launch plan with narrative, assets, timing, and channel sequencing.
- This is an **attention specialist** for turning a ship moment into a coordinated campaign that captures attention, drives activation, and builds momentum beyond day 1.

## Use when
- Use when preparing a release, beta, announcement, major feature drop, or project reveal.
- Use when you have a specific launch date and need the narrative, assets, and channel plan to make it land.
- Use when launching with zero audience — the plan needs to account for cold-start distribution, not just notifying existing fans.

## Avoid when
- Do not use for always-on content planning with no distinct launch moment — that's `att_content_calendar`.
- Do not use when the product isn't ready to ship — a launch plan can't fix a product that breaks on first use.
- Do not use for internal milestones with no external-facing moment.

## Inputs to gather
- Launch date and what's shipping (specific feature set, not roadmap promises).
- Audience readiness: existing waitlist, community size, email list, or zero audience?
- Proof inventory: what results, testimonials, or data can you show on launch day?
- Channel inventory: email list, social following, communities, press contacts, directory sites.
- Team capacity: who's available for support and follow-up during launch week? Solo founders: this is you + the bot.
- Competitive timing: is anything else launching the same day/week that would drown you?

## Operating rules
- **A launch needs a reason to care now.** "We launched a thing" isn't a story. "The first X that does Y" or "After 6 months of building, here's what happened" is. Find the tension, surprise, or proof that makes this moment worth paying attention to.
- **Build around one sharp story, not many weak angles.** One narrative, one hook, one core proof point. Everything else supports it. Multiple angles dilute the launch.
- **The 7-day runway, not just day 0.** Launch day is 20% of the impact. Days 1-6 are the follow-through: replies, follow-up posts, email sequences, community engagement, and catching latecomers. Plan the full arc.
- **Zero-audience launches need distribution strategy, not just content.** If you have no following, your launch plan must include where strangers will find you: directories, communities, cross-posting, partnerships, Product Hunt, Hacker News, Reddit. Content alone won't distribute itself.
- **Proof on launch day or don't claim it.** "Our users love it" without testimonials is hollow. "Reduces X by Y%" without data is a guess. Ship proof with the product, or underclaim.

## Claude Code tool pattern
- Use `att_proof_mining` to inventory what proof is available before launch day.
- Use `att_message_house` output to keep launch messaging consistent across channels.
- Use `WebFetch` to check directory sites and submission requirements (Product Hunt, AlternativeTo, etc.).
- Use `att_thread_writer` to draft the launch-day thread(s).
- Use `att_content_repurposing` to turn one launch asset into channel-native variants.
- For solo founders: use `solo_rapid_ship` to ensure something actually ships on launch day.

## Expanded workflow
1. **Define the launch objective.** Not "get traffic" — what's the specific activation? Signups? Downloads? First action? Name the one metric that defines success.
2. **Choose the main story and hook.** What makes this launch worth paying attention to? Write the hook in one sentence. If it doesn't create tension or surprise, keep working.
3. **Inventory proof assets.** What can you show on launch day? Testimonials, data, demos, screenshots, before/after. If proof is thin, either underclaim or delay until you have it.
4. **Plan the channel sequence.** Not all channels fire at once. Sequence: early access / presale → launch announcement → follow-up content → community engagement → directory submissions → ongoing momentum.
5. **Build the asset plan.** What needs to be created for each channel: thread, email, landing page update, demo video, changelog, social assets. Assign owners (or time-blocks for solo).
6. **Plan the 7-day runway.** Day 0: launch announcement everywhere. Days 1-2: reply to every response, post follow-up content. Days 3-4: submit to directories, cross-post to communities. Days 5-7: share results, testimonials, learnings. The launch isn't one day — it's a week.
7. **Set up tracking.** How will you measure the success metric? UTM params, signup source tracking, analytics. If you can't measure it, you can't learn from it.
8. **Plan support coverage.** Who's watching for bugs, responding to questions, triaging issues in the first 48 hours? Solo: block your calendar and set up alerts.
9. **Return the full launch plan** with timeline, assets, channel sequence, and success metric.

## Output contract
- Launch objective and success metric
- Main narrative and hook
- Proof asset inventory (what's ready, what's missing)
- 7-day timeline with channel sequence
- Asset plan per channel (what to create, who creates it)
- Support coverage plan
- Tracking setup
- Zero-audience distribution plan (if applicable)

## Failure modes to avoid
- One-day launch with no follow-up — the spike fades with nothing to catch latecomers. Plan 7 days minimum.
- No proof on launch day — hype triggers skepticism, not signups. Underclaim or delay.
- Measuring traffic instead of activation — visitors who don't activate are not success.
- No support plan — product breaks under traffic and nobody triages. This kills launch credibility fast.
- Ignoring zero-audience reality — "we'll post on social" doesn't work when you have 0 followers. Plan distribution channels that don't require an existing audience.
- Launching into a competitor's launch day — check the calendar.
- Overclaiming without proof — "revolutionary" without proof reads as "unproven."

## Handoff cues
- 7-day runway plan with assets for each day.
- Success metric and tracking method confirmed.
- Proof gaps flagged: what to generate before launch day.
- Team coverage confirmed for launch week (or solo time-blocks).
- Distribution channels identified for zero-audience scenario.

## Example invocation
- Slash: `/att_launch_plan <task>`
- Natural language: "Build a launch plan for this product release."
- Example: "I'm launching next Friday with zero audience — help me plan distribution, not just content."
- Example: "We have a waitlist of 200 — plan the launch week to maximize activation."
- Often paired with: `att_message_house`, `att_proof_mining`, `att_thread_writer`

## Quality bar
- The plan covers 7 days, not just launch day.
- Proof assets are inventoried and ready (or gaps are explicitly named).
- All channels have prepared assets, not just "post on social."
- Support coverage is arranged for the first 48 hours.
- Success metric is activation, not just traffic.
- Zero-audience launches have a distribution strategy beyond "post and hope."

## Related workflows
- Positioning first: `att_positioning_workshop` → `att_message_house` → `att_launch_plan`
- Launch sequence: `att_launch_plan` → `att_proof_mining` → `att_thread_writer`
- Follow-through: `att_launch_plan` → `att_content_repurposing` → `att_content_calendar`
- Solo launch: `solo_rapid_ship` → `att_launch_plan` → `solo_founder_rhythm`
