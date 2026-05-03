---
name: solo_context_switch
description: "Minimize the cognitive cost of switching between founder roles throughout the day."
user-invocable: true
metadata: {"openclaw":{"emoji":"🔄"}}
---

# Context Switch

## Purpose
Minimize the cognitive cost of switching between founder roles. Every context switch costs 15-25 minutes of refocusing. A solo founder wearing 5 hats can lose 2+ hours per day to switching overhead alone.

## Use when
Use when you feel mentally exhausted but haven't done that much actual work. Use when you're jumping between roles in the same hour. Use when you sit down to code and spend 15 minutes remembering what you were doing.

## Avoid when
Don't use when your work is naturally single-threaded. The goal is to minimize switches, not eliminate them.

## Inputs to gather
- Role inventory: which hats do you wear and how often?
- Switching patterns: when do you switch and what triggers it?
- Refocusing time: how long does it take you to get into flow after an interruption?
- Task dependencies: which tasks must happen in sequence vs can be batched?

## Operating rules
- Batch similar roles into contiguous blocks. Coding + debugging = same block. Coding + customer support = different blocks.
- Close everything unrelated. When coding, close email, Slack, and the customer dashboard.
- Use transition rituals. A 2-minute physical reset between blocks signals your brain to switch contexts.
- The 5-minute rule: if a task takes less than 5 minutes and you're in the wrong context, write it down, don't switch.
- Protect the longest flow block. If you get one 3-hour coding window per day, defend it with your life.

## Claude Code tool pattern
- Use `solo_wearing_hats` to inventory your roles.
- Use `solo_founder_rhythm` to design blocks that minimize switching.
- Use `core_context_budget` to prioritize which context is worth entering.

## Expanded workflow
1. **Inventory your roles.** List every hat — product, engineering, marketing, sales, support, finance, ops.
2. **Measure switching cost.** Track how long it takes to refocus after each switch. Most founders underestimate this.
3. **Map your daily switches.** How many per day? What triggers them? Slack notifications? Email anxiety?
4. **Design role blocks.** Group cognitively similar roles into contiguous time blocks.
5. **Create transition rituals.** Physical reset actions between role blocks: walk, water, stretch, close apps, open new apps.
6. **Set up switch barriers.** Close unrelated apps, mute unrelated channels, set DND during maker blocks.
7. **Batch the micro-tasks.** 5-minute tasks that trigger switches get collected and batched into a single reactive block.

## Output contract
- Role inventory with cognitive similarity grouping
- Daily block design minimizing switches
- Transition rituals between role blocks
- Micro-task batching system
- Switch barrier checklist per role

## Failure modes to avoid
- Trying to eliminate all switching — some is necessary; optimize, don't eliminate.
- No transition rituals — your brain doesn't instantly switch just because you opened a new app.
- Not closing unrelated contexts — notifications destroy focus even when you ignore them.
- Over-batching — grouping too many roles creates fatigue, not efficiency.
- Ignoring the switching cost data — measuring once and assuming it's fixed forever.

## Handoff cues
- Role blocks defined with transition rituals.
- Switch barriers (apps to close, channels to mute) per block.
- Micro-task batch collection point.
- Switching cost data and the biggest improvement opportunity.

## Example invocation
- Slash: `/solo_context_switch <task>`
- Natural language: "Use solo_context_switch to minimize the cognitive cost of switching between founder roles throughout the day."

## Quality bar
Daily context switches reduced by at least 30% from baseline. Every role block has a transition ritual. Unrelated contexts are closed during deep work blocks. The longest flow block per day is protected.

## Related workflows
- **Cognitive load reduction:** `solo_wearing_hats` → `solo_context_switch` → `solo_founder_rhythm`
- **Flow protection:** `solo_context_switch` → `core_context_budget` → `solo_rapid_ship`
- **Interruption management:** `solo_context_switch` → `ops_support_triage` → `core_recover_after_fail`
