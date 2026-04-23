---
name: ops_vendor_eval
description: "Evaluate tools, vendors, and service providers for fit, lock-in risk, cost, and operating burden."
user-invocable: true
disable-model-invocation: true
---


# Vendor Evaluation

## Purpose
- Evaluate tools, vendors, and service providers for fit, lock-in risk, cost, and operating burden.
- This is an **operations specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use before adopting a new SaaS tool, agency, infra service, or vendor dependency.
- The main bottleneck is best solved through operations work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not choose based on feature checklists alone.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Current operating context, owners, cadence, dependencies, and the artifact the team needs next.
- What is blocked, what is ambiguous, and what communication or process gap is hurting execution.
- Any timing, meeting, launch, support, or vendor constraints that change the operating decision.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- A good vendor fit includes workflow fit, not just capability.
- Hidden costs include migration, ownership, support, and exit difficulty.
- Fewer vendors is often a strategic advantage.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read the live notes, trackers, metrics, and recent decisions before restructuring process or status artifacts.
- Optimize for clarity, accountability, and follow-through rather than adding management overhead.
- Use concise artifacts that can be updated repeatedly without creating a parallel bureaucracy.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the vendor job and non-negotiables.
2. Compare candidates against fit, burden, and risk.
3. Assess switching cost and exit difficulty.
4. Recommend the best path with caveats.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

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
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/ops_vendor_eval <task>`
- Natural language: "Use vendor Evaluation to evaluate tools, vendors, and service providers for fit, lock-in risk, cost, and operating burden."
- Example: "Turn this messy operating context into one artifact the team can actually use."
- Example: "Prepare the meeting, launch, or handoff so people leave with decisions and owners."
- Often paired with: `ops_project_brief`, `ops_status_update`, `ops_runbook_author`

## Quality bar
- A good vendor eval protects the team from expensive complexity disguised as convenience.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.
