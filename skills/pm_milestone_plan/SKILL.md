---
name: pm_milestone_plan
description: "Break a project into milestones, exit criteria, and dependencies that can actually be tracked."
user-invocable: true
---

## Purpose
- Break a project into milestones, exit criteria, and dependencies that can actually be tracked.
- This is a **program specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a project needs a clearer path from now to launch, migration, or delivery.

## Avoid when
- Do not confuse a task dump with a milestone plan.

## Inputs to gather
- Program goal, timeline, dependencies, stakeholders, and the decision cadence.
- Known risks, scope pressure, reporting needs, and the state of the backlog or roadmap.
- What artifact is missing: milestone plan, risk register, roadmap scenario, or stakeholder update.

## Operating rules
- Milestones should mark decision points or integrated outcomes.
- Define exit criteria, not just dates.
- Expose cross-team dependencies early.

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
1. Define the target outcome and deadline.
2. Split the work into milestone stages.
3. Set exit criteria, owners, and dependencies.
4. Return a milestone plan with review points.
## Output contract
- Target outcome
- Milestones
- Exit criteria and owners
- Dependencies and risks
- Program artifact with owners, milestones, risks, and decision points.
- Tradeoff summary and the next escalation or approval needed.

## Failure modes to avoid
- Publishing a plan that ignores dependencies or unowned risks.
- Treating stakeholder communication as a substitute for real decision-making.
- Making the roadmap look tidy while underlying constraints stay unresolved.

## Handoff cues
- Milestone plan: milestones, dates, deliverables, dependencies, risk buffers.
- Critical path analysis.
- Milestone review schedule and criteria.

## Example invocation
- Slash: `/pm_milestone_plan <task>`
- Natural language: "Use milestone Plan to break a project into milestones, exit criteria, and dependencies that can actually be tracked."
- Example: "Give me the clearest program view of this work, not just a prettier backlog."
- Example: "Map the milestones, dependencies, and tradeoffs so we can actually commit."
- Often paired with: `pm_risk_register`, `pm_scope_tradeoffs`

## Quality bar

- Every milestone has a date, deliverable, and verification criteria.
- Risk buffer is built into the schedule, not added after the fact.
- Dependencies between milestones are explicit and tracked.
- Milestones are spaced close enough to catch drift before it becomes a crisis.
- Scope explicitly names what is out of scope, not just what is included.
- Every dependency has an owner and a resolution date.
- Stakeholder communication plan exists and is being followed.
- Milestones have objective, verifiable completion criteria.
## Related workflows
- Planning chain: `pm_milestone_plan` → `pm_dependency_map` → `pm_scope_tradeoffs` → `pm_stakeholder_update`
