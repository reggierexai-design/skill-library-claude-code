---
name: ops_vendor_eval
description: "Evaluate tools, vendors, and service providers for fit, lock-in risk, cost, and operating burden."
user-invocable: true
---

## Purpose
- Evaluate tools, vendors, and service providers for fit, lock-in risk, cost, and operating burden.

## Use when
- Use before adopting a new SaaS tool, agency, infra service, or vendor dependency.

## Avoid when
- Do not choose based on feature checklists alone.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.

## Operating rules
- A good vendor fit includes workflow fit, not just capability.
- Hidden costs include migration, ownership, support, and exit difficulty.
- Fewer vendors is often a strategic advantage.

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
1. Define the vendor job and non-negotiables.
2. Compare candidates against fit, burden, and risk.
3. Assess switching cost and exit difficulty.
4. Recommend the best path with caveats.
## Output contract
- Evaluation criteria
- Candidate comparison
- Risks
- Recommendation
- Operator-ready artifact: brief, agenda, runbook, review, scorecard, or update.
- Named owners, deadlines or review points, and the next coordination move.

## Failure modes to avoid
- Generating admin output with no owner, decision, or next action attached.
- Using process language to hide unresolved prioritization problems.
- Documenting a workflow nobody can realistically maintain.

## Handoff cues

- Vendor evaluation: criteria scores, risk assessment, cost analysis, recommendation.
- Contract negotiation points.
- Integration complexity assessment.

## Example invocation
- Slash: `/ops_vendor_eval <task>`
- Natural language: "Use vendor Evaluation to evaluate tools, vendors, and service providers for fit, lock-in risk, cost, and operating burden."
- Example: "Turn this messy operating context into one artifact the team can actually use."
- Example: "Prepare the meeting, launch, or handoff so people leave with decisions and owners."
- Often paired with: `ops_project_brief`, `ops_status_update`, `ops_runbook_author`

## Quality bar
- A good vendor eval protects the team from expensive complexity disguised as convenience.
- A new team member could execute the plan from the document alone.
- Rollback steps are explicit and tested, not theoretical.
- Blast radius is named for every change.
- Communication plan covers who to notify, when, and what to say.
## Related workflows
- Incident flow: `ops_support_triage` → `eng_incident_response` → `ops_postmortem_author`
- Sprint cycle: `ops_sprint_planning` → `ops_status_update` → `ops_launch_retrospective`
