---
name: pm_scope_tradeoffs
description: "Clarify what to cut, defer, or simplify when time, quality, and capacity are in tension."
user-invocable: true
---

## Purpose
- Clarify what to cut, defer, or simplify when time, quality, and capacity are in tension.
- This is a **program specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a team cannot ship everything and needs a principled way to reduce scope.

## Avoid when
- Do not let scope creep masquerade as customer empathy.

## Inputs to gather
- Program goal, timeline, dependencies, stakeholders, and the decision cadence.
- Known risks, scope pressure, reporting needs, and the state of the backlog or roadmap.
- What artifact is missing: milestone plan, risk register, roadmap scenario, or stakeholder update.

## Operating rules
- Protect the core outcome before secondary polish.
- Name the cost of every cut and every keep.
- Prefer reversible cuts over permanent design debt where possible.

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
1. Define the target outcome and hard constraints.
2. Rank the work by user value and risk.
3. Identify cut, defer, simplify, and keep options.
4. Return a scope tradeoff recommendation.
## Output contract
- Constraints
- Keep/cut/defer list
- Tradeoffs
- Recommendation
- Program artifact with owners, milestones, risks, and decision points.
- Tradeoff summary and the next escalation or approval needed.

## Failure modes to avoid
- Publishing a plan that ignores dependencies or unowned risks.
- Treating stakeholder communication as a substitute for real decision-making.
- Making the roadmap look tidy while underlying constraints stay unresolved.

## Handoff cues

- Scope tradeoff analysis: options, what's included, what's cut, impact.
- Recommendation with rationale.
- Stakeholder communication plan.

## Example invocation
- Slash: `/pm_scope_tradeoffs <task>`
- Natural language: "Use scope Tradeoffs to clarify what to cut, defer, or simplify when time, quality, and capacity are in tension."
- Example: "Give me the clearest program view of this work, not just a prettier backlog."
- Example: "Map the milestones, dependencies, and tradeoffs so we can actually commit."
- Often paired with: `pm_milestone_plan`, `pm_risk_register`

## Quality bar
- Good scope management protects outcomes instead of just shrinking ambition blindly.
- Scope explicitly names what is out of scope, not just what is included.
- Every dependency has an owner and a resolution date.
- Stakeholder communication plan exists and is being followed.
- Milestones have objective, verifiable completion criteria.
## Related workflows
- Planning chain: `pm_milestone_plan` → `pm_dependency_map` → `pm_scope_tradeoffs` → `pm_stakeholder_update`
