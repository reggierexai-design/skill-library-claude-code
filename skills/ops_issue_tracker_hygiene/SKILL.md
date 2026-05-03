---
name: ops_issue_tracker_hygiene
description: "Clean up issues, labels, priorities, and ownership so the tracker supports action instead of confusion."
user-invocable: true
---

## Purpose
- Clean up issues, labels, priorities, and ownership so the tracker supports action instead of confusion.

## Use when
- Use when the issue tracker has duplicates, unclear priorities, stale tickets, or confused ownership.

## Avoid when
- Do not spend more effort polishing tickets than fixing the highest-value work.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- A clean tracker clarifies next action, owner, and status.
- Backlogs should contain real options, not every thought anyone had.
- Status labels should mean something operationally.

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
1. Assess the current tracker mess and goals.
2. Define a lighter taxonomy for status, type, and priority.
3. Recommend cleanup actions and triage rules.
4. Document a maintenance routine to keep it clean.
## Output contract
- Tracker problems
- Recommended taxonomy
- Cleanup actions
- Maintenance rules
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues

- Hygiene report: stale issues, missing fields, mislabeled items, duplicates.
- Recommended cleanup actions with priority.
- Process improvements to prevent hygiene decay.

## Example invocation
- Slash: `/ops_issue_tracker_hygiene <task>`
- Natural language: "Use issue Tracker Hygiene to clean up issues, labels, priorities, and ownership so the tracker supports action instead of confusion."
- Example: "Turn this messy operating context into one artifact the team can actually use."
- Example: "Prepare the meeting, launch, or handoff so people leave with decisions and owners."
- Often paired with: `ops_project_brief`, `ops_status_update`, `ops_runbook_author`

## Quality bar
- Good tracker hygiene increases execution clarity without adding process drag.
- A new team member could execute the plan from the document alone.
- Rollback steps are explicit and tested, not theoretical.
- Blast radius is named for every change.
- Communication plan covers who to notify, when, and what to say.
## Related workflows
- Incident flow: `ops_support_triage` → `eng_incident_response` → `ops_postmortem_author`
- Sprint cycle: `ops_sprint_planning` → `ops_status_update` → `ops_launch_retrospective`
