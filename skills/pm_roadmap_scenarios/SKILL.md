---
name: pm_roadmap_scenarios
description: "Turn competing ideas into roadmap scenarios with tradeoffs, dependencies, and downside risks."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\uddfa\ufe0f"}}
---

## Purpose
- Turn competing ideas into roadmap scenarios with tradeoffs, dependencies, and downside risks.
- This is a **program specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when planning work across quarters, launches, or teams with more ideas than capacity.

## Avoid when
- Do not present one roadmap as fate when there are real tradeoffs.

## Inputs to gather
- Program goal, timeline, dependencies, stakeholders, and the decision cadence.
- Known risks, scope pressure, reporting needs, and the state of the backlog or roadmap.
- What artifact is missing: milestone plan, risk register, roadmap scenario, or stakeholder update.

## Operating rules
- A roadmap is a bet portfolio, not a wish list.
- Show what is delayed or dropped in each scenario.
- Expose dependency and staffing assumptions.

- Scope is defined by what is excluded, not just what is included. A project that includes everything includes nothing on time.
- Dependencies are risks until they are resolved. Track them actively, not just list them.
- Stakeholder communication is a deliverable, not an afterthought. A project that succeeds technically but fails politically has failed.
- Milestones need objective completion criteria. A milestone that requires a meeting to confirm it is done is not a milestone.
- Risk management is ongoing, not a one-time exercise. Review the risk register weekly, not just at kickoff.
## Claude Code tool pattern
- Read the latest plans, notes, tickets, and status sources before restructuring the program view.
- Reduce ambiguity in ownership, sequencing, and decision rights before adding more tracking detail.
- Make tradeoffs explicit so the program can move without hidden assumptions.

## Expanded workflow
1. List goals, constraints, and candidate bets.
2. Build a few roadmap scenarios with explicit assumptions.
3. Compare upside, downside, and dependencies.
4. Return a scenario set plus recommendation.
## Output contract
- Planning horizon
- Scenarios
- Tradeoffs and dependencies
- Recommendation
- Program artifact with owners, milestones, risks, and decision points.
- Tradeoff summary and the next escalation or approval needed.

## Failure modes to avoid
- Publishing a plan that ignores dependencies or unowned risks.
- Treating stakeholder communication as a substitute for real decision-making.
- Making the roadmap look tidy while underlying constraints stay unresolved.

## Handoff cues
- Roadmap scenarios: optimistic, expected, conservative paths with assumptions.
- Decision points that trigger scenario switches.
- Resource requirements per scenario.

## Example invocation
- Slash: `/pm_roadmap_scenarios <task>`
- Natural language: "Use roadmap Scenarios to turn competing ideas into roadmap scenarios with tradeoffs, dependencies, and downside risks."
- Example: "Give me the clearest program view of this work, not just a prettier backlog."
- Example: "Map the milestones, dependencies, and tradeoffs so we can actually commit."
- Often paired with: `pm_milestone_plan`, `pm_risk_register`, `pm_scope_tradeoffs`

## Quality bar

- Each scenario has explicit assumptions that differentiate it.
- Decision points that trigger scenario switches are identified.
- Resource requirements are realistic for each scenario.
- The most likely scenario has a detailed execution plan; others have outlines.
- Scope explicitly names what is out of scope, not just what is included.
- Every dependency has an owner and a resolution date.
- Stakeholder communication plan exists and is being followed.
- Milestones have objective, verifiable completion criteria.
## Related workflows
- Planning chain: `pm_milestone_plan` → `pm_dependency_map` → `pm_scope_tradeoffs` → `pm_stakeholder_update`
