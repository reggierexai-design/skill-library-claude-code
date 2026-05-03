---
name: pm_governance_model
description: "Define decision rights, review cadence, escalation paths, and operating rules for a program."
user-invocable: true
---

## Purpose
- Define decision rights, review cadence, escalation paths, and operating rules for a program.
- This is a **program specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a cross-functional program lacks clear ownership or repeatedly stalls on decisions.

## Avoid when
- Do not use for small one-owner projects with obvious governance already.

## Inputs to gather
- Program goal, timeline, dependencies, stakeholders, and the decision cadence.
- Known risks, scope pressure, reporting needs, and the state of the backlog or roadmap.
- What artifact is missing: milestone plan, risk register, roadmap scenario, or stakeholder update.

## Operating rules
- Governance should enable decisions, not prevent them. If your governance model slows decisions more than it improves them, it's bureaucracy.
- Define who decides, not just who approves. The difference: deciders own the outcome; approvers just say no.
- Include reversal criteria. Not every decision needs the same level of review â€” reversible decisions should be fast.
- The model must include its own update process. Governance that can't change becomes obsolete.

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
1. List decision types and their current pain points.
2. Define decision rights: who decides, who advises, who informs.
3. Set escalation paths for deadlocked decisions.
4. Differentiate reversible vs irreversible decisions â€” different review levels.
5. Define the review cadence for the governance model itself.
6. Document and communicate to all stakeholders.

## Output contract
- Program artifact with owners, milestones, risks, and decision points.
- Tradeoff summary and the next escalation or approval needed.

## Failure modes to avoid
- Publishing a plan that ignores dependencies or unowned risks.
- Treating stakeholder communication as a substitute for real decision-making.
- Making the roadmap look tidy while underlying constraints stay unresolved.

## Handoff cues
- Governance model: decision rights, approval levels, escalation paths, review cadence.
- Roles and responsibilities matrix.
- Process for updating the governance model itself.

## Example invocation
- Slash: `/pm_governance_model <task>`
- Natural language: "Use program Governance Model to define decision rights, review cadence, escalation paths, and operating rules for a program."
- Example: "Give me the clearest program view of this work, not just a prettier backlog."
- Example: "Map the milestones, dependencies, and tradeoffs so we can actually commit."
- Often paired with: `pm_milestone_plan`, `pm_risk_register`, `pm_scope_tradeoffs`

## Quality bar
## Related workflows
- Planning chain: `pm_milestone_plan` â†’ `pm_dependency_map` â†’ `pm_scope_tradeoffs` â†’ `pm_stakeholder_update`
- Scope explicitly names what is out of scope, not just what is included.
- Every dependency has an owner and a resolution date.
- Stakeholder communication plan exists and is being followed.
- Milestones have objective, verifiable completion criteria.
