---
name: pm_stakeholder_update
description: "Write a crisp update that explains progress, risk, decisions, and asks without noise."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udcec"}}
---

## Purpose
- Write a crisp update that explains progress, risk, decisions, and asks without noise.
- This is a **program specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when leaders, partners, or adjacent teams need a trustworthy project update.

## Avoid when
- Do not hide risk inside cheerful filler.

## Inputs to gather
- Program goal, timeline, dependencies, stakeholders, and the decision cadence.
- Known risks, scope pressure, reporting needs, and the state of the backlog or roadmap.
- What artifact is missing: milestone plan, risk register, roadmap scenario, or stakeholder update.

## Operating rules
- Lead with what changed and what needs attention.
- Separate facts, risks, and asks.
- Keep the update readable in one pass.

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
1. Define the audience and update objective.
2. Summarize progress, risks, and decisions.
3. Draft clear asks and next steps.
4. Return an update in the right tone and format.
## Output contract
- Audience
- Progress summary
- Risks and decisions
- Asks and next steps
- Program artifact with owners, milestones, risks, and decision points.
- Tradeoff summary and the next escalation or approval needed.

## Failure modes to avoid
- Publishing a plan that ignores dependencies or unowned risks.
- Treating stakeholder communication as a substitute for real decision-making.
- Making the roadmap look tidy while underlying constraints stay unresolved.

## Handoff cues
- Stakeholder update: progress, decisions needed, risks, next milestones.
- Tailored to stakeholder's concern level and decision authority.
- Specific asks with deadlines.

## Example invocation
- Slash: `/pm_stakeholder_update <task>`
- Natural language: "Use stakeholder Update to write a crisp update that explains progress, risk, decisions, and asks without noise."
- Example: "Give me the clearest program view of this work, not just a prettier backlog."
- Example: "Map the milestones, dependencies, and tradeoffs so we can actually commit."
- Often paired with: `pm_milestone_plan`, `pm_risk_register`, `pm_scope_tradeoffs`

## Quality bar

- The update answers the stakeholder's implicit question: am I on track, and do I need to do anything?
- Progress is specific: what shipped, what's blocked, what changed.
- Asks are explicit with deadlines, not implied.
- The update is concise enough to be read in 2 minutes.
- Scope explicitly names what is out of scope, not just what is included.
- Every dependency has an owner and a resolution date.
- Stakeholder communication plan exists and is being followed.
- Milestones have objective, verifiable completion criteria.
## Related workflows
- Planning chain: `pm_milestone_plan` → `pm_dependency_map` → `pm_scope_tradeoffs` → `pm_stakeholder_update`
