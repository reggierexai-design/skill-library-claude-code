---
name: att_short_video_script
description: "Write short video scripts for demos, explainers, or social clips with fast hooks and clear payoff."
---

# Short Video Script

## Purpose
- Write short video scripts for demos, explainers, or social clips with fast hooks and clear payoff.
- This is an **attention specialist** for creating scroll-stopping short-form video that earns the next 3 seconds, then the next 10, then the action.

## Use when
- Use for vertical short-form video: TikTok, YouTube Shorts, Instagram Reels, LinkedIn video.
- Use for product demos that need to be 60 seconds or less.
- Use for explainer clips that teach one idea fast.
- Use for social teasers that drive traffic to a longer asset.

## Avoid when
- Do not use when the core story or audience angle is still weak — video amplifies whatever you put in it, including confusion.
- Do not use for long-form content (webinars, tutorials) — that's `att_webinar_workshop_outline`.
- Do not use when you don't have a clear hook — the first 2 seconds determine 80% of whether the video gets watched.

## Inputs to gather
- Platform: TikTok, YouTube Shorts, Instagram Reels, or LinkedIn video? Each has different length limits, audience expectations, and algorithm preferences.
- The hook: what makes someone stop scrolling in the first 1-2 seconds? (Contrarian take, visual surprise, direct question, bold claim.)
- The core message: one idea, one proof point, one takeaway. Multiple ideas in a short video dilute everything.
- Audience: who's watching and what do they already believe? What would surprise or help them?
- Length target: 15s (single hook + CTA), 30s (hook + one proof + CTA), 60s (hook + problem + proof + CTA), 90s (full mini-story).

## Operating rules
- **Hook fast, explain clearly, finish with a satisfying payoff.** The first 1-2 seconds must visually and verbally stop the scroll. "Hey guys" does not stop the scroll. A bold claim, a surprising visual, or a direct question does.
- **Show the product or insight early.** Don't save the demo for the end — by then, 70% of viewers have scrolled away. Show it within the first 10 seconds.
- **Use spoken language, not blog language.** Write like you talk, not like you write. Short sentences. Active voice. No jargon. Read it out loud — if it sounds stiff, it is stiff.
- **Script for captions.** 80%+ of social video is watched without sound. Every key point must be readable in on-screen text. The video should make sense on mute.
- **One idea per video.** If you're trying to say three things, make three videos. Short video that tries to do too much accomplishes nothing.
- **End with a clear, non-awkward CTA.** "Link in bio," "follow for more," or "try it free" — tell them what to do. Videos without CTAs are entertainment, not marketing.

## Claude Code tool pattern
- Use `WebFetch` to study trending video formats and hooks on the target platform.
- Use `att_proof_mining` to pull the strongest proof point for the video's core claim.
- After scripting, use `att_content_repurposing` to spin the video concept into other formats (thread, email tease, blog clip).

## Expanded workflow
1. **Define audience, angle, and desired action.** Who's watching? What's the one idea? What should they do after?
2. **Write the hook.** 1-2 seconds. Test it: would this make YOU stop scrolling? Options: contrarian take ("You're doing X wrong"), direct question ("What if you could X?"), visual surprise (show the result first), or bold claim with proof ("I replaced 3 tools with this one app").
3. **Write the middle beats.** For 30s: one proof point or demo moment. For 60s: problem setup + product proof. For 90s: problem + proof + differentiation. Each beat should be 5-10 seconds.
4. **Write the close and CTA.** The ending should feel satisfying, not abrupt. "So if you're tired of X, try [product] — link in bio."
5. **Add visual and caption directions.** For each beat: what's on screen? What text overlay appears? What's the caption text? A video script without visual notes is half a script.
6. **Write 2-3 hook variants for A/B testing.** The hook determines 80% of performance. Test different openings to find what resonates.
7. **Return the script with visual directions and caption text.**

## Output contract
- Script with timing per beat (hook, middle, close)
- Visual directions: what's on screen for each beat
- Caption text: on-screen text overlay for each beat
- CTA with placement
- 2-3 hook variants for A/B testing
- Caption/description text for the post itself

## Failure modes to avoid
- Slow starts — if the hook comes at 5 seconds, 80% of the audience already swiped away.
- Multiple ideas in one video — each idea dilutes the others. One idea, one video.
- Not scripting for captions — sound-off viewers miss the entire message.
- Weak or missing CTA — viewers watch, nod, and scroll on without taking action.
- Over-produced and stiff — authenticity beats polish on social video. Script the beats, not word-for-word dialogue.
- Demo-only without story — showing the product without a reason to care is a commercial, not content.

## Handoff cues
- Full script with visual directions and caption text.
- Hook variants labeled for A/B testing.
- Flag any production requirements (props, location, graphics, screen recording).
- Post caption and hashtags ready to copy-paste.

## Example invocation
- Slash: `/att_short_video_script <task>`
- Natural language: "Script a short video for this product."
- Example: "Script a 30-second TikTok showing this product solving a real problem."
- Example: "Write a 60-second Reel that hooks with a contrarian take and ends with a CTA."
- Often paired with: `att_demo_narrative`, `att_content_repurposing`, `att_launch_plan`

## Quality bar
- The hook would make a scrolling thumb stop in the first 2 seconds.
- One clear idea runs through the entire video.
- The script works on mute (captions cover all key points).
- The CTA is specific and natural, not awkward.
- Total length matches the platform's sweet spot (15-60s for most platforms).

## Related workflows
- Content system: `att_message_house` → `att_short_video_script` → `att_content_repurposing`
- Launch video: `att_launch_plan` → `att_demo_narrative` → `att_short_video_script`
- Repurpose: `att_short_video_script` → `att_thread_writer` → `att_content_repurposing`
