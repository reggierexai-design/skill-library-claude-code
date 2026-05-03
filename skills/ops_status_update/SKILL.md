---
name: ops_status_update
description: "Write concise status updates that show progress, risk, and next steps without hiding reality."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udccb"}}
---

## Purpose
- Write concise status updates that show progress, risk, and next steps without hiding reality.

## Use when
- Use for internal updates, stakeholder notes, investor snippets, or async team check-ins.

## Avoid when
- Do not use when there is no meaningful change or when a fuller handoff is needed instead.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- Lead with what changed, not with process activity.
- Name risks plainly.
- Keep the next step obvious.

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
1. Define the audience and update purpose.
2. Summarize progress, blockers, and next steps.
3. Tighten the message for honesty and clarity.
4. Return the final status note.
## Output contract
- Progress
- Blockers or risks
- Next step
- Ask if any
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues

- Status update: progress, blockers, risks, next steps, help needed.
- RAG status for each workstream.
- Decisions needed from stakeholders.

## Example invocation
- Slash: `/ops_status_update <task>`
- Natural language: "Use status Update to write concise status updates that show progress, risk, and next steps without hiding reality."
- Example: "Turn this messy operating context into one artifact the team can actually use."
- Example: "Prepare the meeting, launch, or handoff so people leave with decisions and owners."
- Often paired with: `ops_project_brief`, `ops_runbook_author`

## Quality bar
- A status update should create alignment in one read.
- A new team member could execute the plan from the document alone.
- Rollback steps are explicit and tested, not theoretical.
- Blast radius is named for every change.
- Communication plan covers who to notify, when, and what to say.
## Related workflows
- Incident flow: `ops_support_triage` → `eng_incident_response` → `ops_postmortem_author`
- Sprint cycle: `ops_sprint_planning` → `ops_status_update` → `ops_launch_retrospective`
