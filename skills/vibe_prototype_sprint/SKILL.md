---
name: vibe_prototype_sprint
description: "Run a focused 1-5 day sprint to build and validate a working prototype."
user-invocable: true
---

# Prototype Sprint

## Purpose
Run a focused 1-5 day sprint to build and validate a working prototype. A prototype sprint compresses the idea-to-working-demo cycle into a short, intense burst. The goal isn't perfection — it's a working thing you can put in front of users to learn.

## Use when
Use when you have an idea and need to validate it fast. Use when you're considering a pivot and need to test a new direction. Use when you want a demo for investors or partners.

## Avoid when
Don't use when the product is already defined and you need production quality. Don't use for features that require regulatory compliance. Don't use when you can't dedicate focused time to the sprint.

## Inputs to gather
- Sprint goal: what one thing will the prototype demonstrate?
- Time box: how many days can you dedicate? 1-5 is the range.
- Success criteria: what does "working" look like at the end?
- User validation plan: who will you show it to and what will you ask?
- Stack choice: what tools and frameworks will you use?

## Operating rules
- One core flow, nothing else. The prototype demonstrates one thing. Features that don't support that one thing are cut.
- Time box is sacred. If it doesn't work in 5 days, the idea needs rethinking, not more time.
- Ship ugly. Design polish is for later. Function over form in a prototype sprint.
- Validate with real users. A prototype without user feedback is just a fun coding exercise.
- Document decisions. You'll forget why you chose X over Y by next week.

## Claude Code tool pattern
- Use `vibe_prompt_to_app` for the initial prototype generation.
- Use `vibe_debug_no_code` for issues during the sprint.
- Use `vibe_deploy_novice` to get the prototype live for user testing.
- Use `solo_rapid_ship` for the shipping mindset.

## Expanded workflow
1. **Define the sprint goal.** One sentence: "In [N] days, I will have a working prototype that [demonstrates X]."
2. **Identify the core user flow.** The minimum path a user takes to experience the value proposition.
3. **Cut everything else.** No auth, no settings, no secondary features. Just the core flow.
4. **Choose the fastest stack.** Not the best stack — the fastest one you can use. Familiarity beats capability.
5. **Build in focused blocks.** 2-4 hour deep work sessions. No distractions. No meetings.
6. **Deploy daily.** Even if it's broken, get it on the internet. Deployment problems compound if left to the end.
7. **Validate with users on the last day.** Show it to 3-5 real potential users. Watch them use it. Note what's confusing.
8. **Decide: pivot, persist, or park.** Based on user feedback, does this idea have legs?

## Output contract
- Working prototype at a live URL
- Sprint goal and whether it was met
- User validation results: what worked, what confused, what was missing
- Decision: pivot, persist, or park
- Next steps based on the decision

## Failure modes to avoid
- Scope creep during the sprint — adding "just one more feature" kills the time box.
- Choosing an unfamiliar stack — learning a new tool during a sprint wastes days.
- Not deploying until the last minute — deployment issues eat your validation time.
- No user validation — building without testing is the most expensive mistake.
- Perfectionism — a beautiful prototype that took 3 weeks is worse than an ugly one that took 3 days with user feedback.

## Handoff cues
- Prototype URL and sprint goal status.
- User validation results.
- Pivot/persist/park decision and rationale.
- Next sprint or next steps.

## Example invocation
- Slash: `/vibe_prototype_sprint <task>`
- Natural language: "Use vibe_prototype_sprint to run a focused 1-5 day sprint to build and validate a working prototype."

## Quality bar
Sprint goal is defined in one sentence. Core flow works end to end. Prototype is deployed and accessible. At least 3 users have tested it. A clear pivot/persist/park decision has been made.

## Related workflows
- **Validation sprint:** `vibe_prototype_sprint` → `vibe_prompt_to_app` → `vibe_deploy_novice` → user test → decision
- **Rapid iteration:** `vibe_prototype_sprint` → `vibe_debug_no_code` → `vibe_ai_pair_program` → improved prototype
- **Ship cycle:** `vibe_prototype_sprint` → `solo_rapid_ship` → `att_changelog_story` → feedback
