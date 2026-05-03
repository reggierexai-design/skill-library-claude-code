---
name: ops_postmortem_author
description: "Write a blameless postmortem with impact, timeline, causes, and durable follow-up actions."
user-invocable: true
---

## Purpose
- Write a blameless postmortem with impact, timeline, causes, and durable follow-up actions.

## Use when
- Use after incidents, failed launches, missed deadlines, or costly execution breakdowns.

## Avoid when
- Do not use while facts are still too incomplete for a stable timeline.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- Blameless language always. Fix the system, not the person.
- Root cause, not proximate cause. Ask 'why' at least 3 times.
- Action items must have owners and deadlines.
- Postmortems are for learning, not punishment.

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
1. Gather timeline from incident commander, logs, and comms.
2. Identify root cause (ask 'why' at least 3 times).
3. Document impact with specific numbers.
4. List remediation actions already taken.
5. Define prevention actions with owners and deadlines.
6. Write in blameless language throughout.
7. Share within 5 business days.

## Output contract
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues
- Postmortem document: incident timeline, root cause, impact, remediation, action items.
- Blameless language throughout.
- Follow-up actions with owners and deadlines.

## Example invocation
- Slash: `/ops_postmortem_author <task>`
- Natural language: "Use operations Postmortem Author to write a blameless postmortem with impact, timeline, causes, and durable follow-up actions."
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
