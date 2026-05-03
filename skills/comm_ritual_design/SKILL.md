---
name: comm_ritual_design
description: "Design community rituals that create belonging, rhythm, and recurring engagement."
user-invocable: true
metadata: {"openclaw":{"emoji":"🔮"}}
---

# Ritual Design

## Purpose
Design community rituals that create belonging, rhythm, and recurring engagement. Rituals are the heartbeat of a community — they give people a reason to show up, something to participate in, and a sense that the community is alive. Without rituals, communities drift into ghost towns.

## Use when
Use when your community feels stagnant. Use when participation is declining. Use when members say they don't know what's happening. Use when launching a new community.

## Avoid when
Don't create rituals that feel forced or corporate. Don't schedule more rituals than the community can sustain. Don't impose rituals — let them emerge from member behavior when possible.

## Inputs to gather
- Current community activity: what's happening now? Any existing rituals?
- Member time zones and availability: when can people participate?
- Community values: what does the community care about?
- Platform capabilities: what features support scheduled events or recurring posts?
- Participation data: who's active and when?

## Operating rules
- Start with one weekly ritual. Not five. One reliable weekly event beats five inconsistent ones.
- Make rituals participatory, not performative. A Q&A where members ask questions > a webinar where one person talks.
- Rituals should serve the community, not the founder. If members don't value it, retire it.
- Consistency beats quality. A mediocre ritual that happens every week builds more trust than a perfect one that happens once.
- Let rituals evolve. Start simple, see what members respond to, then adjust.

## Claude Code tool pattern
- Use `comm_onboarding_flow` to introduce new members to community rituals.
- Use `comm_growth_loop` to connect rituals to community growth.
- Use `att_content_calendar` to schedule ritual content alongside other content.

## Expanded workflow
1. **Inventory existing rituals.** What already happens regularly? Even informal patterns count.
2. **Identify ritual opportunities.** What do members ask for repeatedly? What brings people together naturally?
3. **Design one weekly ritual.** Weekly wins, show and tell, ask me anything, coworking session, Friday recap.
4. **Define the format.** Time, platform, duration, participation method. Keep it simple.
5. **Announce and run it for 4 weeks.** Don't judge success after one attempt. Give it a month.
6. **Assess participation.** Who showed up? What was the energy like? What could improve?
7. **Evolve based on feedback.** Adjust the format, timing, or content. Don't be afraid to retire what isn't working.
8. **Add a second ritual only when the first is stable.** Don't scale rituals before they're proven.

## Output contract
- Ritual inventory: existing and planned
- Weekly ritual design: name, time, format, participation method
- 4-week launch plan with announcements
- Participation tracking method
- Ritual health assessment criteria

## Failure modes to avoid
- Too many rituals at once — the community can't sustain them and the founder burns out.
- Performative rituals — one person talking while everyone watches isn't community.
- Inconsistent scheduling — a ritual that happens "whenever" isn't a ritual.
- Founder-centric rituals — if the ritual dies when the founder is absent, it's not a community ritual.
- No feedback loop — continuing a ritual that members don't value.

## Handoff cues
- Ritual design with format and schedule.
- Launch announcement drafted.
- Participation tracking plan.
- 4-week assessment date.

## Example invocation
- Slash: `/comm_ritual_design <task>`
- Natural language: "Use comm_ritual_design to design community rituals that create belonging, rhythm, and recurring engagement."

## Quality bar
At least one reliable weekly ritual is established. Rituals are participatory, not performative. The ritual happens consistently for at least 4 weeks before assessment. Members have a voice in ritual evolution. The ritual can survive the founder's absence.

## Related workflows
- **Community building:** `comm_onboarding_flow` → `comm_ritual_design` → `comm_growth_loop` → `comm_retention_audit`
- **Engagement system:** `comm_ritual_design` → `comm_feedback_system` → `comm_conflict_resolution`
- **Content and community:** `att_content_calendar` → `comm_ritual_design` → unified schedule
