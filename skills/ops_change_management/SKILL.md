---
name: ops_change_management
description: "Prepare a significant change with approvals, communication, rollout timing, and fallback plans."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udccb"}}
---

## Purpose
- Prepare a significant change with approvals, communication, rollout timing, and fallback plans.

## Use when
- Use when shipping changes that affect multiple teams, users, workflows, or support surfaces.

## Avoid when
- Do not use for isolated, low-blast-radius internal edits.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- Every change needs a rollback plan before it gets an approval.
- Communicate before, during, and after the change. Surprises destroy trust.
- Batch changes by risk level. Low-risk fast-tracked; high-risk needs full review.
- Track change success rate. If 30%+ cause incidents, the process is the problem.

- Operational decisions need runbook-level specificity. If a new operator could not follow the instruction without guessing, it is not specific enough.
- Distinguish between planned operations (deployments, rotations, scaling) and unplanned operations (incidents, outages, security events). They need different protocols.
- Every operational change needs a rollback plan stated before execution. If you cannot describe how to undo it, do not do it.
- Prefer small reversible changes over large irreversible ones. Batch changes create batch failures.
- Document the blast radius: if this operation fails, what breaks and how far does the impact spread?
## Claude Code tool pattern
- Read the live notes, trackers, metrics, and recent decisions before restructuring process or status artifacts.
- Optimize for clarity, accountability, and follow-through rather than adding management overhead.
- Use concise artifacts that can be updated repeatedly without creating a parallel bureaucracy.

## Expanded workflow
1. Document the change: what, why, impact, risk, rollback.
2. Assess risk level: low (fast-track), medium (peer review), high (full review + approval).
3. Notify affected stakeholders with timeline and expected impact.
4. Execute the change with monitoring in place.
5. Verify the change succeeded and communicate completion.
6. If issues arise, execute rollback and review.

## Output contract
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues
- Change management plan: change description, impact, stakeholders, communication plan.
- Approval chain and rollback criteria.
- Timeline with key checkpoints.

## Example invocation
- Slash: `/ops_change_management <task>`
- Natural language: "Use operations Change Management to prepare a significant change with approvals, communication, rollout timing, and fallback plans."
- Example: "Turn this messy operating context into one artifact the team can actually use."
- Example: "Prepare the meeting, launch, or handoff so people leave with decisions and owners."
- Often paired with: `ops_project_brief`, `ops_status_update`, `ops_runbook_author`

## Quality bar
## Related workflows
- Incident flow: `ops_support_triage` â†’ `eng_incident_response` â†’ `ops_postmortem_author`
- Sprint cycle: `ops_sprint_planning` â†’ `ops_status_update` â†’ `ops_launch_retrospective`
- A new team member could execute the plan from the document alone.
- Rollback steps are explicit and tested, not theoretical.
- Blast radius is named for every change.
- Communication plan covers who to notify, when, and what to say.