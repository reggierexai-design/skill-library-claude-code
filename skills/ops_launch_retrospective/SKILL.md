---
name: ops_launch_retrospective
description: "Turn a launch or campaign into concrete lessons, wins, misses, and next changes."
user-invocable: true
disable-model-invocation: true
---


# Launch Retrospective

## Purpose
- Turn a launch or campaign into concrete lessons, wins, misses, and next changes.
- This is an **operations specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use after a launch, release, campaign, or announcement when the team needs to capture what happened and what to improve.
- The main bottleneck is best solved through operations work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not use before enough data, observations, or stakeholder input exist.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Separate observations from interpretations.
- Keep blame out and decision quality in.
- Convert lessons into owner-ready next actions.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read the live notes, trackers, metrics, and recent decisions before restructuring process or status artifacts.
- Optimize for clarity, accountability, and follow-through rather than adding management overhead.
- Use concise artifacts that can be updated repeatedly without creating a parallel bureaucracy.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the launch scope and intended outcomes.
2. Capture wins, misses, surprises, and constraints.
3. Distill root lessons and the highest-leverage changes.
4. Return a concise retrospective with next actions.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

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
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/ops_launch_retrospective <task>`
- Natural language: "Use launch Retrospective to turn a launch or campaign into concrete lessons, wins, misses, and next changes."
- Example: "Turn this messy operating context into one artifact the team can actually use."
- Example: "Prepare the meeting, launch, or handoff so people leave with decisions and owners."
- Often paired with: `ops_project_brief`, `ops_status_update`, `ops_runbook_author`

## Quality bar
- A good retrospective changes the next launch.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.
