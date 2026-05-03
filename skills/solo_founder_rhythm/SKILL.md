---
name: solo_founder_rhythm
description: "Design a sustainable daily and weekly rhythm that protects deep work, ships product, and prevents burnout."
user-invocable: true
---

# Founder Rhythm

## Purpose
Design a sustainable daily and weekly rhythm that protects deep work, ships product, and prevents burnout. Solo founders don't have a manager setting their schedule — they have to build their own operating system or drown in reactive work.

## Use when
Use when your days feel like firefighting with no progress on what matters. Use when you're working 12-hour days but nothing ships. Use when you can't remember the last time you did focused creative work without interruption.

## Avoid when
Don't use this to optimize a schedule that's already working. Don't use when the crisis is real and temporary; rhythm is for sustain, not emergencies.

## Inputs to gather
- Current weekly calendar: how do you actually spend your time?
- Energy patterns: when are you sharpest? When do you crash?
- Ship commitments: what has to go out this week/month?
- Recovery needs: how much sleep, exercise, and offline time do you need?
- Role inventory: which hats are you wearing and how much time does each need?

## Operating rules
- Protect maker time ruthlessly. The #1 killer of solo founder progress is meetings and Slack eroding deep work hours.
- Batch context switching. Group similar tasks into contiguous blocks rather than jumping between roles every 30 minutes.
- Design for your energy, not the clock. If you're useless before 10am, don't schedule deep work at 8am.
- Ship something every week. Even if it's small. Momentum matters more than perfection.
- Build recovery into the schedule, not after burnout. If you don't schedule rest, your body will schedule it for you — at the worst possible time.

## Claude Code tool pattern
- Use `core_plan_task` to break weekly goals into daily action items.
- Use `solo_energy_audit` to map energy patterns before designing the rhythm.
- Use `ops_sprint_planning` adapted for one-person sprints.

## Expanded workflow
1. **Audit your actual time.** Track a real week — every 30 minutes. Not what you planned, what actually happened.
2. **Map your energy curve.** Label your hours: peak, steady, low. Most founders discover their "best hours" are misaligned with their schedule.
3. **Identify the non-negotiables.** Ship dates, customer commitments, health needs. These don't move.
4. **Block maker time.** 2-4 hours of uninterrupted deep work during your peak energy. This is the most important block in your week.
5. **Batch the reactive work.** Email, DMs, support — 2-3 fixed blocks per day. Never in your maker time.
6. **Assign hat-specific blocks.** Group cognitively similar roles into the same time window.
7. **Schedule recovery.** Exercise, meals, sleep, offline. Non-negotiable.
8. **Review weekly.** Did the rhythm hold? What slipped? Adjust. The rhythm is a living system, not a rigid rule.

## Output contract
- Weekly rhythm template: maker blocks, reactive blocks, hat blocks, recovery blocks
- Energy map: peak, steady, and low hours labeled
- Non-negotiable commitments with their time allocations
- Review checklist for weekly rhythm adjustment

## Failure modes to avoid
- Optimizing for hours worked instead of output produced.
- No maker time protection — every block gets interrupted by "just one thing."
- Ignoring energy patterns — scheduling deep creative work during your afternoon slump.
- No recovery built in — burnout by month 3.
- Rigid schedule that breaks on the first surprise instead of bending.

## Handoff cues
- Weekly rhythm template with time blocks and energy mapping.
- The three non-negotiables for this week.
- Any rhythm violations from last week and the adjustment.
- Next review date.

## Example invocation
- Slash: `/solo_founder_rhythm <task>`
- Natural language: "Use solo_founder_rhythm to design a sustainable daily and weekly rhythm that protects deep work, ships product, and prevents burnout."

## Quality bar
The rhythm survives a real week without total collapse. At least 2 hours of protected maker time per day. Recovery is scheduled, not aspirational. The review mechanism catches drift before burnout.

## Related workflows
- **Weekly operating system:** `solo_founder_rhythm` → `solo_energy_audit` → `core_plan_task` → weekly review
- **Ship cadence:** `solo_rapid_ship` → `solo_founder_rhythm` → ship → review
- **Burnout prevention:** `solo_energy_audit` → `solo_founder_rhythm` → `solo_scope_guard`
