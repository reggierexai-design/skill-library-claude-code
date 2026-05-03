---
name: comm_onboarding_flow
description: "Design a community onboarding flow that turns newcomers into active participants."
user-invocable: true
metadata: {"openclaw":{"emoji":"🚪"}}
---

# Onboarding Flow

## Purpose
Design a community onboarding flow that turns newcomers into active participants. Most communities lose people in the first week because there's no clear path from "just joined" to "feels at home." A good onboarding flow bridges that gap.

## Use when
Use when launching a new community. Use when your community has low activation rates (people join but don't participate). Use when new members regularly go silent after their first week.

## Avoid when
Don't use when your community is already small and intimate — formal onboarding can feel corporate. Don't over-automate the human touch — community is about people, not workflows.

## Inputs to gather
- Community platform: Discord, Slack, Circle, Forum, other?
- Current onboarding: what happens when someone joins right now?
- Activation data: what percentage of new members post in their first week?
- Community norms: what behavior do you want to encourage?
- Personas: who joins your community and why?

## Operating rules
- First 24 hours determine retention. If a new member doesn't engage in their first day, they probably never will.
- Give newcomers a clear first action. Not "explore the community" — that's overwhelming. "Introduce yourself in #intros" is specific.
- Connect newcomers to a person, not just a channel. A buddy, a mentor, or a welcome from a human (not a bot).
- Make the rules visible but welcoming. Not a wall of don'ts — a clear, brief guide to how the community works.
- Celebrate first contributions. A like, a reply, a mention — any signal that someone noticed their participation.

## Claude Code tool pattern
- Use `comm_ritual_design` to create welcoming rituals for new members.
- Use `comm_growth_loop` to connect onboarding to community growth.
- Use `prod_onboarding_design` for product onboarding that integrates with community onboarding.

## Expanded workflow
1. **Map the current onboarding experience.** What happens from the moment someone joins? Walk through it yourself.
2. **Identify the drop-off points.** Where do new members go silent? After joining? After their first post? After a week?
3. **Design the first 24 hours.** Welcome message → first action → human connection → first contribution → recognition.
4. **Create a welcome sequence.** Day 1: welcome + first action. Day 3: check-in + suggestion. Day 7: invite to participate + highlight.
5. **Assign a human touchpoint.** Buddy system, mentor program, or designated welcomers. Not a bot — a person.
6. **Make the first action easy and low-risk.** Introduction, poll, icebreaker — not a complex task or high-stakes contribution.
7. **Test with real newcomers.** Watch 5 new members go through the flow. What's confusing? What works?

## Output contract
- Onboarding flow map: join → first action → human connection → first contribution → recognition
- Welcome sequence: messages and timing for days 1, 3, 7
- First action prompts: easy, low-risk ways to participate immediately
- Human touchpoint assignment: who connects with newcomers
- Drop-off points identified with mitigation plans

## Failure modes to avoid
- No clear first action — "explore the community" is not a call to action.
- All bot, no human — automated welcome without human connection feels cold.
- Information overload — a wall of rules, channels, and guides on day 1 is overwhelming.
- Ignoring lurkers — some people need time before contributing. Don't pressure, but don't ignore.
- Not testing with real newcomers — your assumptions about what works are probably wrong.

## Handoff cues
- Onboarding flow design with touchpoints and timing.
- Welcome sequence messages drafted.
- First action prompts ready.
- Drop-off points and mitigation plans.
- Next test date with real newcomers.

## Example invocation
- Slash: `/comm_onboarding_flow <task>`
- Natural language: "Use comm_onboarding_flow to design a community onboarding flow that turns newcomers into active participants."

## Quality bar
New members have a clear first action within 5 minutes of joining. A human (not just a bot) connects with every new member within 24 hours. The first contribution is easy and low-risk. The welcome sequence spans days 1-7. Drop-off points are identified and mitigated.

## Related workflows
- **Community building:** `comm_onboarding_flow` → `comm_ritual_design` → `comm_growth_loop`
- **Retention focus:** `comm_onboarding_flow` → `comm_retention_audit` → `comm_feedback_system`
- **Product-community integration:** `prod_onboarding_design` → `comm_onboarding_flow` → unified experience
