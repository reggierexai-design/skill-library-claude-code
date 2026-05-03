---
name: ops_interview_loop
description: "Design an interview loop with role fit, evidence coverage, and clear decision ownership."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\uddd3\ufe0f"}}
---

## Purpose
- Design an interview loop with role fit, evidence coverage, and clear decision ownership.

## Use when
- Use when assembling a hiring process for a new or revised role.

## Avoid when
- Do not use when the hiring loop is already stable and working well.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- Each interview tests 2-3 competencies maximum.
- Structured interviews outperform unstructured 2-3x.
- Separate assessment from selling.
- Debrief within 24 hours.

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
1. Build the loop: map competencies to interview sessions.
2. Assign interviewers with clear focus areas and question banks.
3. Schedule with candidate-friendly timing.
4. Conduct structured interviews with rubric scoring.
5. Debrief within 24 hours.
6. Move fast on strong candidates.

## Output contract
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues
- Interview plan: role, loop structure, interviewers, focus areas, schedule.
- Question bank mapped to competencies.
- Debrief process and decision criteria.

## Example invocation
- Slash: `/ops_interview_loop <task>`
- Natural language: "Use operations Interview Loop to design an interview loop with role fit, evidence coverage, and clear decision ownership."
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