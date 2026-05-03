---
name: pm_decision_meeting
description: "Prepare a meeting so it actually resolves a decision instead of circling the issue again."
user-invocable: true
---

## Purpose
- Prepare a meeting so it actually resolves a decision instead of circling the issue again.
- This is a **program specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a meeting should produce a real decision, alignment, or commitment.

## Avoid when
- Do not schedule a discussion when the decision and options are still undefined.

## Inputs to gather
- Program goal, timeline, dependencies, stakeholders, and the decision cadence.
- Known risks, scope pressure, reporting needs, and the state of the backlog or roadmap.
- What artifact is missing: milestone plan, risk register, roadmap scenario, or stakeholder update.

## Operating rules
- Decision meetings need a question, options, and owner.
- Pre-work beats live exposition.
- Capture the decision and follow-up before the room disperses.

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
1. Define the decision and owner.
2. Prepare options, criteria, and recommendation.
3. Set agenda, attendees, and pre-reads.
4. Return a meeting plan plus capture template.
## Output contract
- Decision statement
- Options and criteria
- Agenda and attendees
- Capture template
- Program artifact with owners, milestones, risks, and decision points.
- Tradeoff summary and the next escalation or approval needed.

## Failure modes to avoid
- Publishing a plan that ignores dependencies or unowned risks.
- Treating stakeholder communication as a substitute for real decision-making.
- Making the roadmap look tidy while underlying constraints stay unresolved.

## Handoff cues
- Decision output: decision made, rationale, commitments, follow-up actions.
- Dissenting opinions recorded.
- Review date for reversible decisions.

## Example invocation
- Slash: `/pm_decision_meeting <task>`
- Natural language: "Use decision Meeting to prepare a meeting so it actually resolves a decision instead of circling the issue again."
- Example: "Give me the clearest program view of this work, not just a prettier backlog."
- Example: "Map the milestones, dependencies, and tradeoffs so we can actually commit."
- Often paired with: `pm_milestone_plan`, `pm_risk_register`, `pm_scope_tradeoffs`

## Quality bar

- Every decision has a clear owner, not just consensus.
- Reversible decisions are made quickly; irreversible decisions get appropriate deliberation.
- Dissenting opinions are recorded, not suppressed.
- Follow-up actions have owners and deadlines — decisions without action items are wishes.
- Scope explicitly names what is out of scope, not just what is included.
- Every dependency has an owner and a resolution date.
- Stakeholder communication plan exists and is being followed.
- Milestones have objective, verifiable completion criteria.
## Related workflows
- Planning chain: `pm_milestone_plan` → `pm_dependency_map` → `pm_scope_tradeoffs` → `pm_stakeholder_update`
