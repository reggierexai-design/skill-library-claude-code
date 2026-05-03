---
name: ops_kpi_review
description: "Turn weekly or monthly metrics into a decision-oriented review instead of a passive reporting recap."
user-invocable: true
metadata: {"openclaw":{"emoji":"📋"}}
---

## Purpose
- Turn weekly or monthly metrics into a decision-oriented review instead of a passive reporting recap.

## Use when
- Use when the team has numbers to review but needs sharper interpretation and action.

## Avoid when
- Do not present dashboards without explaining what changed and what to do next.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- Review metrics in the context of goals, seasonality, and recent changes.
- Separate signal from noise and lagging from leading indicators.
- Every KPI review should end in decisions or investigations.

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
1. Frame the review period and top goals.
2. Summarize the key metric movements and likely causes.
3. Identify what needs action, deeper investigation, or no change.
4. Turn the review into owner-linked next steps.
## Output contract
- Goal context
- Metric summary
- Interpretation
- Next actions
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues
- KPI review: metrics, trends, targets, root causes for misses, action items.
- Recommended KPI adjustments if targets are stale.
- Next review date and responsible owners.

## Example invocation
- Slash: `/ops_kpi_review <task>`
- Natural language: "Use kPI Review to turn weekly or monthly metrics into a decision-oriented review instead of a passive reporting recap."
- Example: "Turn this messy operating context into one artifact the team can actually use."
- Example: "Prepare the meeting, launch, or handoff so people leave with decisions and owners."
- Often paired with: `ops_project_brief`, `ops_status_update`, `ops_runbook_author`

## Quality bar

- Every KPI has a target, actual, and trend direction.
- KPIs that are off-target have a root cause and action item, not just a red indicator.
- The review distinguishes between signal and noise — one bad week isn't a trend.
- Action items from the review are assigned to owners with deadlines.
- A new team member could execute the plan from the document alone.
- Rollback steps are explicit and tested, not theoretical.
- Blast radius is named for every change.
- Communication plan covers who to notify, when, and what to say.
## Related workflows
- Incident flow: `ops_support_triage` → `eng_incident_response` → `ops_postmortem_author`
- Sprint cycle: `ops_sprint_planning` → `ops_status_update` → `ops_launch_retrospective`
