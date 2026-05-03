---
name: pm_dependency_map
description: "Map the teams, systems, approvals, and sequencing that could block delivery."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udd78\ufe0f"}}
---

## Purpose
- Map the teams, systems, approvals, and sequencing that could block delivery.
- This is a **program specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a project touches many owners or handoffs and hidden blockers are likely.

## Avoid when
- Do not treat dependencies as an afterthought on cross-functional work.

## Inputs to gather
- Program goal, timeline, dependencies, stakeholders, and the decision cadence.
- Known risks, scope pressure, reporting needs, and the state of the backlog or roadmap.
- What artifact is missing: milestone plan, risk register, roadmap scenario, or stakeholder update.

## Operating rules
- Name dependencies early and concretely.
- Differentiate hard blockers from coordination preferences.
- Map owners and timing, not just systems.

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
1. Define the project scope and major milestones.
2. List upstream and downstream dependencies.
3. Rank them by criticality, lead time, and uncertainty.
4. Return a dependency map with owner asks.
## Output contract
- Scope and milestones
- Dependencies
- Criticality and uncertainty
- Owner asks
- Program artifact with owners, milestones, risks, and decision points.
- Tradeoff summary and the next escalation or approval needed.

## Failure modes to avoid
- Publishing a plan that ignores dependencies or unowned risks.
- Treating stakeholder communication as a substitute for real decision-making.
- Making the roadmap look tidy while underlying constraints stay unresolved.

## Handoff cues
- Dependency map: items, dependencies, critical path, risk areas, mitigation plans.
- Blocked items and what's needed to unblock.
- Cross-team dependencies requiring coordination.

## Example invocation
- Slash: `/pm_dependency_map <task>`
- Natural language: "Use dependency Map to map the teams, systems, approvals, and sequencing that could block delivery."
- Example: "Give me the clearest program view of this work, not just a prettier backlog."
- Example: "Map the milestones, dependencies, and tradeoffs so we can actually commit."
- Often paired with: `pm_milestone_plan`, `pm_risk_register`, `pm_scope_tradeoffs`

## Quality bar

- Every dependency has a direction, type, and owner.
- Critical path items are identified and have buffer time.
- Cross-team dependencies have explicit coordination points.
- The map is updated when dependencies change, not just at project start.
- Scope explicitly names what is out of scope, not just what is included.
- Every dependency has an owner and a resolution date.
- Stakeholder communication plan exists and is being followed.
- Milestones have objective, verifiable completion criteria.
## Related workflows
- Planning chain: `pm_milestone_plan` → `pm_dependency_map` → `pm_scope_tradeoffs` → `pm_stakeholder_update`
