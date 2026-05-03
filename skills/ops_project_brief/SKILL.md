---
name: ops_project_brief
description: "Create a clear working brief for an initiative so collaborators can align fast."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udccb"}}
---

## Purpose
- Create a clear working brief for an initiative so collaborators can align fast.

## Use when
- Use when a cross-functional effort needs shared context, goals, owners, and constraints.

## Avoid when
- Do not use when a current brief already exists and only needs a small update.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- Keep the brief short enough to be read before the work starts.
- Define the owner, outcome, scope, and risks.
- Make assumptions visible instead of hiding them in prose.

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
1. Define the initiative and owner.
2. State goals, audience, scope, timeline, and constraints.
3. List dependencies, risks, and success signals.
4. Return the final brief in a reusable format.
## Output contract
- Owner and objective
- Scope and constraints
- Dependencies and risks
- Success signals
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues

- Project brief: objectives, scope, timeline, stakeholders, success criteria, risks.
- Resource requirements and constraints.
- Approval checkpoints and decision gates.

## Example invocation
- Slash: `/ops_project_brief <task>`
- Natural language: "Use project Brief to create a clear working brief for an initiative so collaborators can align fast."
- Example: "Turn this messy operating context into one artifact the team can actually use."
- Example: "Prepare the meeting, launch, or handoff so people leave with decisions and owners."
- Often paired with: `ops_status_update`, `ops_runbook_author`

## Quality bar
- The brief should make cross-functional work feel simpler.
- A new team member could execute the plan from the document alone.
- Rollback steps are explicit and tested, not theoretical.
- Blast radius is named for every change.
- Communication plan covers who to notify, when, and what to say.
## Related workflows
- Incident flow: `ops_support_triage` → `eng_incident_response` → `ops_postmortem_author`
- Sprint cycle: `ops_sprint_planning` → `ops_status_update` → `ops_launch_retrospective`
