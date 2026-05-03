---
name: solo_wearing_hats
description: "Inventory your founder roles, estimate time each needs, and find delegation or automation opportunities."
user-invocable: true
metadata: {"openclaw":{"emoji":"🎩"}}
---

# Wearing Hats

## Purpose
Inventory your founder roles, estimate time each needs, and find delegation or automation opportunities. Solo founders wear every hat — knowing which hats burn your time is the first step to getting help. You can't delegate what you haven't named.

## Use when
Use when you feel pulled in too many directions. Use when you want to identify what to delegate or automate first. Use when you realize you spent the whole day on low-value work.

## Avoid when
Don't use when you already have a team handling most roles — this is for solo operators. Don't use as a substitute for actually delegating — the inventory is step one, action is step two.

## Inputs to gather
- Role list: every function you currently perform (product, engineering, marketing, sales, support, finance, legal, ops).
- Time per role: how many hours per week does each role actually take?
- Skill self-assessment: which roles are you good at vs struggling through?
- Energy cost: which roles drain you most?
- Delegation budget: can you afford to hire, contract, or automate?

## Operating rules
- Count time honestly, not aspirationally. If marketing takes 10 hours, write 10. If support takes 5, write 5.
- Distinguish competence from enjoyment. Good at it but drained = delegate. Bad at it but enjoy = learn or delegate.
- Delegation priority: high time cost + low competence + low enjoyment. Start there.
- Automation before hiring. Script it before paying someone to do it.
- Don't delegate the core. Whatever makes your product unique should stay with you.

## Claude Code tool pattern
- Use `solo_context_switch` to minimize switching overhead between roles.
- Use `solo_energy_audit` to map which roles drain vs energize you.
- Use `ops_vendor_eval` to evaluate automation tools or contractors.

## Expanded workflow
1. **List every role you fill.** Product, engineering, marketing, sales, support, finance, legal, ops. Name them all.
2. **Estimate weekly hours per role.** Be honest. Track for a week if unsure. Most founders underestimate.
3. **Rate each role: competence (1-5), enjoyment (1-5), energy cost (1-5).** This creates your delegation priority map.
4. **Calculate the delegation score.** High time + low competence + low enjoyment = delegate first. This is your action list.
5. **Identify automation opportunities.** What tasks are repetitive and scriptable? Zapier, cron jobs, templates, scripts.
6. **Prioritize delegation/automation.** Start with the highest-score roles. What gives you the most time back?
7. **Make a 30-day plan.** What gets delegated, automated, or eliminated this month? Specific actions, not vague intentions.

## Output contract
- Role inventory with hours, competence, enjoyment, and energy ratings
- Delegation score per role (priority ranking)
- Automation opportunities per role
- 30-day delegation/automation plan
- Core roles that must stay with the founder

## Failure modes to avoid
- Underestimating time per role — you spend more time on reactive work than you think.
- Delegating the wrong things — giving away core competency while keeping commodity work.
- No automation before hiring — paying people to do what a script could handle.
- Inventory without action — a beautiful spreadsheet that changes nothing.
- Ignoring energy cost — keeping draining roles because they feel "important."

## Handoff cues
- Complete role inventory with scores.
- Top 3 delegation/automation priorities.
- 30-day action plan with specific next steps.
- Core roles to protect from delegation.

## Example invocation
- Slash: `/solo_wearing_hats <task>`
- Natural language: "Use solo_wearing_hats to inventory your founder roles, estimate time each needs, and find delegation or automation opportunities."

## Quality bar
Every role has time, competence, enjoyment, and energy ratings. Delegation scores are calculated and priority-ranked. Automation opportunities are identified per role. The 30-day plan has specific, actionable next steps.

## Related workflows
- **Role optimization:** `solo_wearing_hats` → `solo_energy_audit` → `solo_context_switch` → `solo_founder_rhythm`
- **Delegation planning:** `solo_wearing_hats` → `ops_vendor_eval` → `ops_hiring_scorecard`
- **Solo operating system:** `solo_wearing_hats` → `solo_scope_guard` → `solo_rapid_ship` → weekly review
