---
name: ops_hiring_scorecard
description: "Create a role scorecard with outcomes, competencies, and structured interview signals."
user-invocable: true
---

## Purpose
- Create a role scorecard with outcomes, competencies, and structured interview signals.

## Use when
- Use when hiring for a role and the team needs sharper evaluation criteria.

## Avoid when
- Do not use as a legal or HR compliance substitute.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- Score against the job, not against other candidates.
- Weight competencies by job impact. Top 3 drive 70% of the decision.
- Every score needs evidence, not impression.
- Calibrate interviewers before the loop.

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
1. Define top 5 competencies with behavioral indicators.
2. Weight competencies: top 3 drive 70% of the decision.
3. Map interview questions to specific competencies.
4. Calibrate interviewers on scoring rubric.
5. Collect evidence-based scores after each interview.
6. Debrief: aggregate scores, discuss evidence gaps, decide.

## Output contract
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues
- Scorecard: role, competencies, weights, evaluation criteria, scoring rubric.
- Interview question mapping to competencies.
- Calibration notes for interviewer consistency.

## Example invocation
- Slash: `/ops_hiring_scorecard <task>`
- Natural language: "Use operations Hiring Scorecard to create a role scorecard with outcomes, competencies, and structured interview signals."
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
