---
name: core_review_changes
description: "Review edits, plans, or outputs for correctness, fit, and hidden regressions before finalizing."
user-invocable: false
metadata: {"openclaw":{"emoji":"🧭"}}
---

## Purpose
- Review edits, plans, or outputs for correctness, fit, and hidden regressions before finalizing.
- This is a **core specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use after meaningful changes or when a draft seems acceptable but has not been pressure-tested.
- The main bottleneck is best solved through core work rather than generic brainstorming.

## Avoid when
- Do not use as nitpicking on low-value cosmetic tasks.

## Inputs to gather
- User objective, scope boundary, deadline, and success condition.
- Known constraints, approvals, and any actions that must stay reversible.
- The smallest set of files, notes, tools, or prior decisions that affect the next move.

## Operating rules
- Review against the user goal, not personal preference.
- Look for omission risk first, polish second.
- Check for regressions, contradictions, and invented claims.

- Before planning, audit the current state. Plans built on stale assumptions are worse than no plan.
- Prefer the smallest sufficient action. Overplanning is procrastination with a Gantt chart.
- Name the decision, the decider, and the deadline. Decisions without owners and deadlines are wishes.
- Every plan must state what would cause it to change. Rigid plans break; plans with exit criteria adapt.
- Distinguish between reversible and irreversible decisions. Spend 10x more time on irreversible ones and 10x less on reversible ones.
## Claude Code tool pattern
- Start by reading the local context that changes the decision instead of front-loading every file.
- Use search/read to map the problem first; only edit or execute after the plan and blast radius are clear.
- Leave a compact reasoning trail so later skills can pick up without repeating discovery work.

## Expanded workflow
1. Reconstruct the intended outcome.
2. Inspect the changed areas and adjacent impact surface.
3. List defects by severity.
4. Approve, patch, or send back for rework with concrete reasons.
## Output contract
- Verdict
- Critical issues
- Non-critical improvements
- Ready-to-ship note or rework note
- Next action or decision recommendation.
- Dependencies, risks, and the smallest follow-up check that closes the loop.

## Failure modes to avoid
- Planning too much after the next action is already obvious.
- Skipping routing and forcing the wrong specialist to own the work.
- Producing ceremony instead of a decision-ready next step.

## Handoff cues

- Review summary: approved, changes requested, or blocked.
- Specific issues that must be addressed.
- Follow-up items discovered during review.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use core Review Changes to review edits, plans, or outputs for correctness, fit, and hidden regressions before finalizing."
- Example: "Route this mixed request and tell me the smallest safe next step."
- Example: "Plan the task, then tell me what context actually matters before we touch files."
- Often paired with: `core_route_request`, `core_plan_task`, `core_verify_done`

## Quality bar
- A useful review protects quality without bloating scope.
- The next action is specific enough to start immediately without further clarification.
- Assumptions are explicitly named, not hidden in the plan.
- The plan states what would trigger a re-evaluation.
- Someone else could execute the plan from the document alone.
## Related workflows
- Planning cycle: `core_plan_task` → `core_execute_safely` → `core_review_changes` → `core_verify_done`
- Decision chain: `core_evidence_research` → `core_decision_record` → `core_handoff_summary`
