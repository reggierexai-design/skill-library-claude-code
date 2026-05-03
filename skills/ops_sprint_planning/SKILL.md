---
name: ops_sprint_planning
description: "Shape the next work slice into a realistic sprint or cycle with clear priorities and tradeoffs."
user-invocable: true
metadata: {"openclaw":{"emoji":"📋"}}
---

## Purpose
- Shape the next work slice into a realistic sprint or cycle with clear priorities and tradeoffs.

## Use when
- Use when planning the next one to two weeks of execution for a product or project team.

## Avoid when
- Do not use when the scope is too undefined to estimate or prioritize honestly.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- Protect focus by limiting active priorities.
- Use real capacity and dependencies.
- Separate commitments from hopes.

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
1. List candidate work.
2. Rank by importance, urgency, and dependency order.
3. Fit the work to realistic capacity.
4. Return committed items, stretch items, and risks.
## Output contract
- Committed work
- Stretch work
- Key dependencies
- Sprint risks
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues
- Sprint plan: velocity, capacity, committed items, stretch goals, risks.
- Dependency map and blocker list.
- Sprint review date and demo plan.

## Example invocation
- Slash: `/ops_sprint_planning <task>`
- Natural language: "Use sprint Planning to shape the next work slice into a realistic sprint or cycle with clear priorities and tradeoffs."
- Example: "Turn this messy operating context into one artifact the team can actually use."
- Example: "Prepare the meeting, launch, or handoff so people leave with decisions and owners."
- Often paired with: `ops_project_brief`, `ops_status_update`, `ops_runbook_author`

## Quality bar

- Sprint capacity is based on historical velocity, not aspiration.
- Every item in the sprint has an owner and a definition of done.
- The sprint has slack capacity (10-20%) for unplanned work.
- No item enters the sprint without acceptance criteria.
- A new team member could execute the plan from the document alone.
- Rollback steps are explicit and tested, not theoretical.
- Blast radius is named for every change.
- Communication plan covers who to notify, when, and what to say.
## Related workflows
- Incident flow: `ops_support_triage` → `eng_incident_response` → `ops_postmortem_author`
- Sprint cycle: `ops_sprint_planning` → `ops_status_update` → `ops_launch_retrospective`
