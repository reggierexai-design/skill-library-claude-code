---
name: solo_rapid_ship
description: "Ship a meaningful improvement every week, even as a solo founder with limited capacity."
user-invocable: true
---

# Rapid Ship

## Purpose
Ship a meaningful improvement every week, even as a solo founder with limited capacity. Shipping momentum is the most powerful force for a solo founder — it builds user trust, market evidence, and personal morale. Stagnation kills faster than any competitor.

## Use when
Use when you've been "almost done" for weeks. Use when your users haven't seen a change in a month. Use when perfectionism is preventing progress.

## Avoid when
Don't use when shipping would break existing functionality — rapid is not reckless. Don't use for changes that need regulatory or security review. Don't ship what you haven't tested.

## Inputs to gather
- Shippable backlog: what's close to done and what's blocked?
- User pain points: what are users asking for most urgently?
- Time budget: how many ship-hours do you have this week?
- Risk assessment: what could break if this ships?
- Definition of done: what makes this improvement "shipped"?

## Operating rules
- Ship the smallest complete thing. Not a half-built feature — a complete tiny improvement. Done > perfect.
- Cut scope, not quality. Ship less but ship it working. A broken feature is worse than no feature.
- Every ship needs a user-facing change. If users can't perceive it, it doesn't count as shipping.
- Time-box the work. If it can't ship in a week, it's too big — break it down further.
- Ship before you're ready. The 80% version that's live beats the 100% version that's still local.

## Claude Code tool pattern
- Use `eng_minimal_patch` to find the smallest change that ships the improvement.
- Use `eng_feature_flag_rollout` for risky changes that need gradual exposure.
- Use `solo_scope_guard` to prevent ship scope from expanding.
- Use `qa_release_smoke_test` to verify the ship is safe.

## Expanded workflow
1. **Identify the top ship candidate.** What's closest to done that users actually want? Prioritize by impact and effort.
2. **Define the minimum shippable version.** Cut everything that's not essential. What's the smallest thing users would value?
3. **Time-box the work.** If it can't be done this week, break it smaller. The time box is the forcing function.
4. **Build, test, and ship.** No gold-plating. No scope expansion. No "while I'm in here."
5. **Communicate the ship.** Users need to know something changed. Changelog, email, social, in-app notice.
6. **Collect feedback.** Did the ship land? Any issues? What should next week's ship be?

## Output contract
- Ship candidate: what's going out this week
- Minimum viable version scope: what's in, what's cut
- Time-box estimate and actuals
- Ship communication: changelog, announcement
- Feedback collection mechanism

## Failure modes to avoid
- Perfectionism paralysis — 90% done for 3 weeks because the last 10% isn't perfect.
- Scope expansion mid-ship — "while I'm in here, let me also..."
- Shipping without testing — rapid doesn't mean reckless.
- No user communication — if users don't know it shipped, it didn't ship.
- No feedback loop — shipping into the void with no idea if it landed.

## Handoff cues
- What shipped this week and the user-facing impact.
- What was cut and why (for the next ship).
- Any issues from the ship and the fix plan.
- Next week's ship candidate.

## Example invocation
- Slash: `/solo_rapid_ship <task>`
- Natural language: "Use solo_rapid_ship to ship a meaningful improvement every week, even as a solo founder with limited capacity."

## Quality bar
Something meaningful ships every week (or every other week at minimum). Every ship has a user-facing change. Every ship is tested before release. Ship communication reaches users within 24 hours.

## Related workflows
- **Ship cycle:** `solo_rapid_ship` → `eng_minimal_patch` → `qa_release_smoke_test` → ship → `att_changelog_story`
- **Scope management:** `solo_scope_guard` → `solo_rapid_ship` → `pm_scope_tradeoffs`
- **Feature flags for safety:** `eng_feature_flag_rollout` → `solo_rapid_ship` → `eng_release_readiness`
