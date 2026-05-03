---
name: att_thread_writer
description: "Write social threads that teach, provoke, or persuade without sounding generic or inflated."
---

# Thread Writer

## Purpose
- Write social threads that teach, provoke, or persuade without sounding generic or inflated.
- This is an **attention specialist** for building scroll-stopping multi-post narratives on short-form platforms.

## Use when
- Use when the user needs a multi-post thread for X/Twitter, Bluesky, Threads, or similar platforms.
- Use when repurposing long-form content into a threaded format.
- Use when a launch, insight, or story needs a native social expression — not just a link drop.

## Avoid when
- Do not use when the idea is still weak — sharpen the insight first, then thread it.
- Do not use for single-tweet hot takes — that's a different format.
- Do not use when the audience needs long-form depth (write a blog post or essay instead).

## Inputs to gather
- The core insight: what's the one thing the reader should believe or do after reading?
- The audience: who's reading and what do they already know about this topic?
- The hook: what makes someone stop scrolling and read tweet 1?
- Proof points: what evidence supports the insight? (data, anecdotes, specific examples)
- CTA: what should the reader do at the end? (follow, reply, click, try, share)
- Platform: X (280 char), Bluesky (300 char), Threads (500 char) — limits shape the thread

## Operating rules
- **Hook types that work:** contrarian take ("Everyone says X. They're wrong."), personal story ("I spent 6 months doing X. Here's what happened →"), data reveal ("Only 3% of founders do X. The other 97% are leaving money on the table."), or tension setup ("The biggest mistake I see is X. It costs you Y."). Match the hook to the audience's current belief.
- **Thread length:** 5-7 tweets for a single insight, 8-12 for a story or how-to, 15+ is a blog post — split it. Every tweet beyond 10 loses ~15% of readers.
- **Pacing:** Tweet 1 = hook. Tweets 2-3 = the insight or setup. Middle tweets = proof/meat. Penultimate = the turn or key takeaway. Last = CTA. Never put the best stuff in the middle where drop-off kills it.
- **Self-contained tweets:** Every tweet should make sense if screenshotted alone. People share individual tweets, not whole threads.
- **Specificity beats cleverness:** "I grew revenue 40%" beats "Revenue went up significantly." Specific numbers, specific stories, specific proof.
- **No engagement bait:** "Like and subscribe" or "Retweet if you agree" is noise. Earn the share through value, not begging.

## Claude Code tool pattern
- Read existing site copy, product pages, and proof assets before drafting so the thread fits the real product truth.
- Use `WebFetch` to check competitor threads and current platform conventions if freshness matters.
- When external claims appear in the thread, verify before publishing — `safe_external_claims` applies.
- After drafting, run `att_proof_mining` on the output to check that every claim has backing.

## Expanded workflow
1. **Define the angle.** What's the one thing this thread proves or teaches? Write it in one sentence. If you can't, the thread isn't focused enough.
2. **Choose the hook type.** Match it to audience tension — what do they believe now that this thread will change?
3. **Outline the progression.** 5-7 beats max. Each beat = one tweet. Label each beat: hook → setup → proof 1 → proof 2 → insight → CTA.
4. **Write tweet by tweet.** Respect the character limit. Each tweet needs its own internal logic while pulling to the next. End mid-thought or with a "→" to create pull.
5. **Write 2-3 hook variants.** The hook determines 80% of the thread's reach. Test different openings: contrarian vs story vs data.
6. **Tighten for pace.** Cut every word that doesn't change the meaning. Shorter sentences. Active voice. No hedging.
7. **Add visual notes.** Flag tweets that would be stronger with a chart, screenshot, or image. Specify what the visual should show.
8. **Return the thread, variants, and posting guidance.** Include optimal posting time, whether to pin the hook, and follow-up reply strategy.

## Output contract
- Thread with numbered tweets (1/N format)
- 2-3 alternate hooks for A/B testing
- Visual notes per tweet (where graphics would help)
- Posting guidance: optimal time, pin recommendation, reply strategy
- Audience assumptions and proof gaps flagged

## Failure modes to avoid
- No hook in tweet 1 — if the first tweet doesn't stop the scroll, nothing else matters.
- Insight buried past tweet 3 — drop-off is brutal; front-load the value.
- Thread too long — 7-10 is the sweet spot. 20+ is a blog post nobody reads.
- No CTA at the end — readers finish, nod, and do nothing. Tell them what to do.
- Generic advice anyone could write — specific proof and unique perspective make threads shareable.
- All substance, no rhythm — threads need variation: short punchy tweets mixed with longer explanatory ones.
- Engagement baiting — "Drop a 🙌 if you agree" is noise. Value earns shares.

## Handoff cues
- Full thread with tweet numbers, ready to copy-paste.
- Hook variants labeled for A/B testing.
- Visual notes: which tweets need graphics and what they should show.
- Posting time recommendation for the target audience's peak activity.
- Follow-up reply strategy: what to post as reply 30 min after to boost the thread.

## Example invocation
- Slash: `/att_thread_writer <task>`
- Natural language: "Write a thread about this insight for X."
- Example: "Turn this product launch into a 7-tweet thread with a contrarian hook."
- Example: "I have this data point — make it into a thread that stops the scroll."
- Often paired with: `att_message_house`, `att_launch_plan`, `att_proof_mining`

## Quality bar
- Tweet 1 is a hook that would make YOU stop scrolling.
- The core insight is clear by tweet 3.
- Total length is 5-10 tweets (unless the story demands more).
- Every tweet is screenshot-shareable on its own.
- The thread ends with a specific, non-begging CTA.
- At least one specific number, example, or proof point appears.
- No filler tweets — every tweet advances the argument.

## Related workflows
- Content system: `att_message_house` → `att_content_calendar` → `att_thread_writer` → `att_content_repurposing`
- Launch sequence: `att_launch_plan` → `att_proof_mining` → `att_thread_writer`
- Proof deployment: `att_proof_mining` → `att_thread_writer` → `att_social_proof_pack`
