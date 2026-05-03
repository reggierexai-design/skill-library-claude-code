---
name: solo_energy_audit
description: "Map your energy patterns and align your hardest work with your best hours."
user-invocable: true
metadata: {"openclaw":{"emoji":"🔋"}}
---

# Energy Audit

## Purpose
Map your energy patterns and align your hardest work with your best hours. Most founders schedule around the clock instead of around their energy — then wonder why they're exhausted but unproductive. Schedule around natural rhythms to get 2x output from the same hours.

## Use when
Use when you feel drained mid-day despite adequate sleep. Use when you're working long hours but output doesn't match the time invested. Use when you keep hitting the same afternoon wall.

## Avoid when
Don't use when your schedule is externally constrained (e.g., you must be available 9-5 for client calls). Don't use as a substitute for addressing real health issues — chronic fatigue needs a doctor, not a schedule tweak.

## Inputs to gather
- Sleep data: when do you sleep, how much, and how do you feel on waking?
- Energy self-assessment: rate your energy every 2 hours for a week (1-5 scale).
- Work output log: what did you actually produce during each energy level?
- Diet and exercise patterns: what supports or drains your energy?
- Current schedule: what's fixed vs flexible?

## Operating rules
- Measure, don't guess. Track your energy for at least 5 real workdays before designing around it. Your self-image of when you're sharpest is probably wrong.
- Energy mapping drives schedule design, not the other way around. Don't force your energy to fit your schedule.
- Distinguish physical energy from creative energy. They're different resources. You might have physical energy for a workout but zero creative energy for coding.
- Protect the peak. Your best 2-4 hours produce more than the other 8 combined.

## Claude Code tool pattern
- Use `solo_founder_rhythm` to build the schedule from the energy map.
- Use `core_context_budget` to match task importance to energy levels.
- Use `solo_context_switch` to minimize energy drain from switching.

## Expanded workflow
1. **Track energy for 5 workdays.** Rate every 2 hours: physical (1-5) and creative (1-5). Use a simple log.
2. **Identify patterns.** When are both high? When is only physical? When is neither? Look for the daily rhythm.
3. **Map task types to energy levels.** Deep creative work → peak creative. Admin → physical-only. Strategy → peak both.
4. **Design the schedule around the map.** Peak hours get the hardest work. Low hours get admin, breaks, or nothing.
5. **Identify energy drains.** What consistently tanks your energy? Long meetings? Certain people? Certain foods? Reduce or eliminate.
6. **Identify energy boosters.** What reliably restores energy? Exercise? Nap? Music? Build them into the schedule.
7. **Test for 2 weeks.** Does the energy-aligned schedule produce more output? Adjust based on results.

## Output contract
- Energy map: hour-by-hour for a typical day, labeled peak/steady/low
- Task-to-energy assignment: which work goes where
- Energy drains identified with mitigation plans
- Energy boosters built into the schedule
- Schedule template aligned with energy patterns

## Failure modes to avoid
- Guessing instead of measuring — your self-image of when you're sharpest is probably wrong.
- Ignoring the distinction between physical and creative energy.
- Not protecting the peak — meetings during your best hours is the most common mistake.
- No energy recovery built in — running on fumes by Wednesday.
- Designing the perfect schedule and then not following it.

## Handoff cues
- Energy map for the current week.
- Task-to-energy assignments.
- The single biggest energy drain and the plan to eliminate it.
- The next energy audit date.

## Example invocation
- Slash: `/solo_energy_audit <task>`
- Natural language: "Use solo_energy_audit to map your energy patterns and align your hardest work with your best hours."

## Quality bar
Energy tracked for at least 5 real workdays before schedule design. Peak hours are protected for deep work. Energy drains are identified with mitigation plans. Recovery is built into the daily schedule.

## Related workflows
- **Energy-first scheduling:** `solo_energy_audit` → `solo_founder_rhythm` → `solo_context_switch`
- **Burnout prevention:** `solo_energy_audit` → `solo_scope_guard` → `solo_founder_rhythm`
- **Output optimization:** `solo_energy_audit` → `core_context_budget` → `solo_rapid_ship`
