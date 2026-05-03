---
name: ops_meeting_prep
description: "Prepare an agenda, questions, and decision frame so a meeting creates progress instead of recap."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udccb"}}
---

## Purpose
- Prepare an agenda, questions, and decision frame so a meeting creates progress instead of recap.

## Use when
- Use before stakeholder, team, research, sales, or partnership meetings.

## Avoid when
- Do not use for meetings that should probably not happen at all.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- Every meeting should have a purpose, owner, and desired output.
- Prep the few questions that unlock decisions.
- Cut status theater and reheated context.

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
1. Define the meeting objective and attendees.
2. List the decisions, risks, and open questions.
3. Draft agenda and key prompts.
4. Return prep notes and follow-up expectations.
## Output contract
- Objective
- Agenda
- Key questions
- Desired outputs
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues

- Meeting prep: agenda, objectives, pre-read materials, decision items, time allocation.
- Required attendees and their roles.
- Follow-up action tracker template.

## Example invocation
- Slash: `/ops_meeting_prep <task>`
- Natural language: "Use meeting Prep to prepare an agenda, questions, and decision frame so a meeting creates progress instead of recap."
- Example: "Turn this messy operating context into one artifact the team can actually use."
- Example: "Prepare the meeting, launch, or handoff so people leave with decisions and owners."
- Often paired with: `ops_project_brief`, `ops_status_update`, `ops_runbook_author`

## Quality bar
- A prepared meeting should shorten the number of future meetings.
- A new team member could execute the plan from the document alone.
- Rollback steps are explicit and tested, not theoretical.
- Blast radius is named for every change.
- Communication plan covers who to notify, when, and what to say.
## Related workflows
- Incident flow: `ops_support_triage` → `eng_incident_response` → `ops_postmortem_author`
- Sprint cycle: `ops_sprint_planning` → `ops_status_update` → `ops_launch_retrospective`
