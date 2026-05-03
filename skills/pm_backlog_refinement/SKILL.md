---
name: pm_backlog_refinement
description: "Clean a backlog into better-shaped work with priority signals, dependencies, and next actions."
user-invocable: true
---

## Purpose
- Clean a backlog into better-shaped work with priority signals, dependencies, and next actions.
- This is a **program specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when the backlog is noisy, duplicative, or too vague to plan from.

## Avoid when
- Do not spend hours grooming items no one intends to work on soon.

## Inputs to gather
- Program goal, timeline, dependencies, stakeholders, and the decision cadence.
- Known risks, scope pressure, reporting needs, and the state of the backlog or roadmap.
- What artifact is missing: milestone plan, risk register, roadmap scenario, or stakeholder update.

## Operating rules
- A backlog is a decision tool, not a storage attic.
- Clarify items that are near-term and archive the rest.
- Tie priority to real goals and constraints.

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
1. Triage the backlog by relevance and readiness.
2. Clarify the near-term items and group the rest.
3. Rank by outcome, urgency, and dependency.
4. Return a refined backlog view with next actions.
## Output contract
- Triage groups
- Clarified next items
- Priority signals
- Cleanup actions
- Program artifact with owners, milestones, risks, and decision points.
- Tradeoff summary and the next escalation or approval needed.

## Failure modes to avoid
- Publishing a plan that ignores dependencies or unowned risks.
- Treating stakeholder communication as a substitute for real decision-making.
- Making the roadmap look tidy while underlying constraints stay unresolved.

## Handoff cues

- Refined backlog: items prioritized, sized, dependencies mapped, ready status.
- Items deprioritized with rationale.
- Next refinement date and items to prepare.

## Example invocation
- Slash: `/pm_backlog_refinement <task>`
- Natural language: "Use backlog Refinement to clean a backlog into better-shaped work with priority signals, dependencies, and next actions."
- Example: "Give me the clearest program view of this work, not just a prettier backlog."
- Example: "Map the milestones, dependencies, and tradeoffs so we can actually commit."
- Often paired with: `pm_milestone_plan`, `pm_risk_register`, `pm_scope_tradeoffs`

## Quality bar
- A refined backlog lets the team plan faster with fewer hidden surprises.
- Scope explicitly names what is out of scope, not just what is included.
- Every dependency has an owner and a resolution date.
- Stakeholder communication plan exists and is being followed.
- Milestones have objective, verifiable completion criteria.
## Related workflows
- Planning chain: `pm_milestone_plan` → `pm_dependency_map` → `pm_scope_tradeoffs` → `pm_stakeholder_update`
