---
name: ops_launch_retrospective
description: "Turn a launch or campaign into concrete lessons, wins, misses, and next changes."
user-invocable: true
---

## Purpose
- Turn a launch or campaign into concrete lessons, wins, misses, and next changes.

## Use when
- Use after a launch, release, campaign, or announcement when the team needs to capture what happened and what to improve.

## Avoid when
- Do not use before enough data, observations, or stakeholder input exist.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- Separate observations from interpretations.
- Keep blame out and decision quality in.
- Convert lessons into owner-ready next actions.

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
1. Define the launch scope and intended outcomes.
2. Capture wins, misses, surprises, and constraints.
3. Distill root lessons and the highest-leverage changes.
4. Return a concise retrospective with next actions.
## Output contract
- Scope and outcomes
- Wins and misses
- Lessons
- Next changes
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues
- Retro summary: what worked, what didn't, what to change, action items with owners.
- Timeline of key events during launch.
- Process improvements for next launch.

## Example invocation
- Slash: `/ops_launch_retrospective <task>`
- Natural language: "Use launch Retrospective to turn a launch or campaign into concrete lessons, wins, misses, and next changes."
- Example: "Turn this messy operating context into one artifact the team can actually use."
- Example: "Prepare the meeting, launch, or handoff so people leave with decisions and owners."
- Often paired with: `ops_project_brief`, `ops_status_update`, `ops_runbook_author`

## Quality bar

- Every phase of the launch is covered: planning, execution, and post-launch.
- At least 3 specific action items are captured with owners.
- What went well is documented, not just what went wrong.
- The retro produces improvements that are incorporated into the next launch plan.
- A new team member could execute the plan from the document alone.
- Rollback steps are explicit and tested, not theoretical.
- Blast radius is named for every change.
- Communication plan covers who to notify, when, and what to say.
## Related workflows
- Incident flow: `ops_support_triage` → `eng_incident_response` → `ops_postmortem_author`
- Sprint cycle: `ops_sprint_planning` → `ops_status_update` → `ops_launch_retrospective`
