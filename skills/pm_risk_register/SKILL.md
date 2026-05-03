---
name: pm_risk_register
description: "Build a practical risk register with triggers, owners, mitigations, and review cadence."
user-invocable: true
metadata: {"openclaw":{"emoji":"\u26a0\ufe0f"}}
---

## Purpose
- Build a practical risk register with triggers, owners, mitigations, and review cadence.
- This is a **program specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a project has meaningful uncertainty across delivery, security, legal, data, or partners.

## Avoid when
- Do not create a risk register that no one reviews or owns.

## Inputs to gather
- Program goal, timeline, dependencies, stakeholders, and the decision cadence.
- Known risks, scope pressure, reporting needs, and the state of the backlog or roadmap.
- What artifact is missing: milestone plan, risk register, roadmap scenario, or stakeholder update.

## Operating rules
- Risks need owners and triggers, not just scary labels.
- Separate likelihood from impact.
- Update the register as the project changes.

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
1. Define the project scope and risk horizon.
2. List the main risks, triggers, and owners.
3. Assign mitigations and contingency actions.
4. Return a risk register with review cadence.
## Output contract
- Risk list
- Owners and triggers
- Mitigations
- Review cadence
- Program artifact with owners, milestones, risks, and decision points.
- Tradeoff summary and the next escalation or approval needed.

## Failure modes to avoid
- Publishing a plan that ignores dependencies or unowned risks.
- Treating stakeholder communication as a substitute for real decision-making.
- Making the roadmap look tidy while underlying constraints stay unresolved.

## Handoff cues
- Risk register: risks, probability, impact, mitigation, owner, status.
- Top 5 risks with active mitigation plans.
- Risk review schedule.

## Example invocation
- Slash: `/pm_risk_register <task>`
- Natural language: "Use risk Register to build a practical risk register with triggers, owners, mitigations, and review cadence."
- Example: "Give me the clearest program view of this work, not just a prettier backlog."
- Example: "Map the milestones, dependencies, and tradeoffs so we can actually commit."
- Often paired with: `pm_milestone_plan`, `pm_scope_tradeoffs`

## Quality bar

- Every risk has probability, impact, mitigation, and owner — no orphans.
- Top risks have active mitigations in progress, not just monitoring.
- The register is reviewed at a regular cadence, not just at project start.
- Risks that have materialized are converted to issues and removed from the register.
- Scope explicitly names what is out of scope, not just what is included.
- Every dependency has an owner and a resolution date.
- Stakeholder communication plan exists and is being followed.
- Milestones have objective, verifiable completion criteria.
## Related workflows
- Planning chain: `pm_milestone_plan` → `pm_dependency_map` → `pm_scope_tradeoffs` → `pm_stakeholder_update`
