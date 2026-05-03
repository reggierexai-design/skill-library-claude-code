---
name: ops_oncall_handoff
description: "Prepare a crisp handoff of active incidents, risks, watches, and next actions for the next operator."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udd04"}}
---

## Purpose
- Prepare a crisp handoff of active incidents, risks, watches, and next actions for the next operator.

## Use when
- Use during shift changes, escalations, vacations, or ownership transfers on active work.

## Avoid when
- Do not use when there is no live operational context to transfer.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- Written handoff beats verbal. Verbal is forgotten; written is searchable.
- Include what you're worried about, not just what happened.
- Prioritize: active incidents > watch items > follow-up tasks.
- Test escalation paths before handoff.

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
1. Summarize current system health with specific metrics.
2. List active incidents with status and next steps.
3. List watch items: things that could become incidents.
4. List recent changes that might cause issues.
5. Confirm escalation contacts are reachable.
6. Document in persistent, searchable format.

## Output contract
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues
- Oncall handoff: current incidents, ongoing investigations, recent changes, watch items.
- Escalation paths and contact info.
- System health summary and known fragile areas.

## Example invocation
- Slash: `/ops_oncall_handoff <task>`
- Natural language: "Use operations On-Call Handoff to prepare a crisp handoff of active incidents, risks, watches, and next actions for the next operator."
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