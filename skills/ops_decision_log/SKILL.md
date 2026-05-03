---
name: ops_decision_log
description: "Keep a running decision log so workstreams stay aligned as choices, owners, and assumptions evolve."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udccb"}}
---

## Purpose
- Keep a running decision log so workstreams stay aligned as choices, owners, and assumptions evolve.

## Use when
- Use when a project has many moving decisions across product, engineering, marketing, or ops.

## Avoid when
- Do not let the log become a stale archive no one checks.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- Capture decisions with owner, date, and consequence.
- Separate confirmed choices from open questions.
- A log should reduce rework, not create bureaucracy.

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
1. Record the current decision or update.
2. Assign owner, rationale, and downstream effects.
3. Mark open questions and next review points.
4. Keep the log easy to scan across time.
## Output contract
- Decision entry
- Owner
- Rationale
- Dependencies
- Review date
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues

- Decision log entry: context, options, choice, rationale, outcome tracking.
- Reversal conditions and review schedule.
- Stakeholder acknowledgment record.

## Example invocation
- Slash: `/ops_decision_log <task>`
- Natural language: "Use decision Log to keep a running decision log so workstreams stay aligned as choices, owners, and assumptions evolve."
- Example: "Turn this messy operating context into one artifact the team can actually use."
- Example: "Prepare the meeting, launch, or handoff so people leave with decisions and owners."
- Often paired with: `ops_project_brief`, `ops_status_update`, `ops_runbook_author`

## Quality bar
- A useful decision log helps teams move faster with less repeated debate.
- A new team member could execute the plan from the document alone.
- Rollback steps are explicit and tested, not theoretical.
- Blast radius is named for every change.
- Communication plan covers who to notify, when, and what to say.
## Related workflows
- Incident flow: `ops_support_triage` → `eng_incident_response` → `ops_postmortem_author`
- Sprint cycle: `ops_sprint_planning` → `ops_status_update` → `ops_launch_retrospective`
