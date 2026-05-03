---
name: ops_runbook_author
description: "Write operational runbooks that are easy to follow under pressure."
user-invocable: true
---

## Purpose
- Write operational runbooks that are easy to follow under pressure.

## Use when
- Use when documenting support flows, release steps, incident procedures, or repeatable internal operations.

## Avoid when
- Do not use when the process is still too unstable or unknown to document responsibly.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- Write for someone who is competent but not telepathic.
- Prefer steps, checks, and rollback paths over narrative prose.
- Document the stop conditions and escalation paths clearly.

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
1. Define the runbook purpose and operator.
2. Document prerequisites, steps, checks, and rollback.
3. List failure points and escalation triggers.
4. Return the final runbook with a verification checklist.
## Output contract
- Purpose and owner
- Prerequisites
- Steps and checks
- Rollback and escalation
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues

- Runbook: procedure name, trigger conditions, step-by-step actions, verification, escalation.
- Prerequisites and access requirements.
- Review and test schedule for accuracy.

## Example invocation
- Slash: `/ops_runbook_author <task>`
- Natural language: "Use runbook Author to write operational runbooks that are easy to follow under pressure."
- Example: "Turn this messy operating context into one artifact the team can actually use."
- Example: "Prepare the meeting, launch, or handoff so people leave with decisions and owners."
- Often paired with: `ops_project_brief`, `ops_status_update`

## Quality bar
- A runbook succeeds when it prevents panic and improvisation.
- A new team member could execute the plan from the document alone.
- Rollback steps are explicit and tested, not theoretical.
- Blast radius is named for every change.
- Communication plan covers who to notify, when, and what to say.
## Related workflows
- Incident flow: `ops_support_triage` → `eng_incident_response` → `ops_postmortem_author`
- Sprint cycle: `ops_sprint_planning` → `ops_status_update` → `ops_launch_retrospective`
