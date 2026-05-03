---
name: solo_scope_guard
description: "Prevent scope creep and overcommitment when you're the only person who can do the work."
user-invocable: true
metadata: {"openclaw":{"emoji":"🛡️"}}
---

# Scope Guard

## Purpose
Prevent scope creep and overcommitment when you're the only person who can do the work. Every extra feature, every "quick call," every "can you also" comes directly from your finite hours.

## Use when
Use when your to-do list grows faster than your done list. Use when someone asks "can you also..." and you say yes without checking capacity. Use when you're three weeks behind on something you committed to last month.

## Avoid when
Don't use when the scope change is the right call based on new information. Scope guard prevents default yes, not every yes.

## Inputs to gather
- Current commitments: what's on your plate with deadlines and effort estimates?
- Capacity: how many hours of focused work do you have this week?
- Incoming requests: what's being asked of you and by whom?
- Ship deadline pressure: what's time-sensitive vs nice-to-have?

## Operating rules
- Default answer is "not now," not "yes." Every new commitment must justify why it beats what's already planned.
- One in, one out. If you add something, remove something of equal or greater size.
- The must-ship list should fit in your capacity with 20% buffer. If it doesn't, cut before adding.
- The 24-hour rule: wait 24 hours before committing to anything non-urgent. The urgency is usually inflated.
- Track your overcommitment rate. If you consistently plan 10 hours for an 8-hour day, your planning is the problem.

## Claude Code tool pattern
- Use `pm_scope_tradeoffs` for feature-level scope decisions.
- Use `core_context_budget` to decide what deserves your limited attention.
- Use `solo_energy_audit` to align scope with actual energy capacity.

## Expanded workflow
1. **List current commitments.** Everything in-flight with effort estimates and deadlines. Be honest about effort — multiply your first guess by 2.
2. **Calculate real capacity.** Available hours × 0.7 (buffer for the unexpected).
3. **Apply the overcommitment test.** If commitments > capacity, cut before adding anything new.
4. **Evaluate every new request against the cut list.** Is this more important than what's already committed?
5. **Apply one-in-one-out.** If you add, you must remove. No exceptions.
6. **Set the "not now" default.** Every request gets "let me check capacity and get back to you."
7. **Review weekly.** Are you still overcommitted? What slipped? What got cut?

## Output contract
- Capacity vs commitment comparison
- Must-ship list (fits in capacity with buffer)
- Deferred list with rationale for each deferral
- Overcommitment rate and trend
- Default response template for new requests

## Failure modes to avoid
- Default yes to everything — scope creep through agreeableness.
- No capacity calculation — planning by hope instead of math.
- Over-optimistic effort estimates — everything takes 2-3x longer than you think.
- No buffer for the unexpected — the unexpected is the only thing you can count on.
- Cutting the wrong things — keeping easy comfortable work over hard important work.

## Handoff cues
- Must-ship items for this week with effort estimates.
- Deferred items and their rationale.
- Current overcommitment rate.
- The next scope decision that needs to be made.

## Example invocation
- Slash: `/solo_scope_guard <task>`
- Natural language: "Use solo_scope_guard to prevent scope creep and overcommitment when you're the only person who can do the work."

## Quality bar
Commitments never exceed 80% of real capacity. Every deferred item has a documented rationale. The overcommitment rate is tracked and trending down. New requests get a 24-hour buffer before commitment.

## Related workflows
- **Scope management loop:** `solo_scope_guard` → `pm_scope_tradeoffs` → `solo_founder_rhythm`
- **Capacity planning:** `solo_energy_audit` → `solo_scope_guard` → `solo_rapid_ship`
- **Request triage:** `ops_support_triage` → `solo_scope_guard` → `core_route_request`
