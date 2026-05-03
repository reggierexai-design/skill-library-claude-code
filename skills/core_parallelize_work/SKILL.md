---
name: core_parallelize_work
description: "Split a task into safe parallel tracks while keeping dependencies and merge points explicit."
user-invocable: false
metadata: {"openclaw":{"emoji":"\ud83e\ude93"}}
---

## Purpose
- Split a task into safe parallel tracks while keeping dependencies and merge points explicit.
- This is a **core specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a request is too broad for one linear pass and can be decomposed cleanly.
- The main bottleneck is best solved through core work rather than generic brainstorming.

## Avoid when
- Do not parallelize tightly coupled work that depends on one shared unknown.

## Inputs to gather
- User objective, scope boundary, deadline, and success condition.
- Known constraints, approvals, and any actions that must stay reversible.
- The smallest set of files, notes, tools, or prior decisions that affect the next move.

## Operating rules
- Parallelism helps only when tracks can rejoin cleanly.
- Define ownership, boundaries, and merge criteria.
- Keep shared assumptions visible.

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
1. Map the work and shared dependencies.
2. Split it into bounded parallel tracks.
3. Define merge points and success checks.
4. Return an execution plan with clear boundaries.
## Output contract
- Tracks
- Dependencies
- Merge plan
- Success checks
- Next action or decision recommendation.
- Dependencies, risks, and the smallest follow-up check that closes the loop.

## Failure modes to avoid
- Planning too much after the next action is already obvious.
- Skipping routing and forcing the wrong specialist to own the work.
- Producing ceremony instead of a decision-ready next step.

## Handoff cues

- Parallelization plan: tasks, dependencies, assignment, merge strategy.
- Dependency graph documented.
- Merge conflict resolution approach.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use parallelize Work to split a task into safe parallel tracks while keeping dependencies and merge points explicit."
- Example: "Route this mixed request and tell me the smallest safe next step."
- Example: "Plan the task, then tell me what context actually matters before we touch files."
- Often paired with: `core_route_request`, `core_plan_task`, `core_verify_done`

## Quality bar
- Good parallelization saves time without multiplying confusion.
- The next action is specific enough to start immediately without further clarification.
- Assumptions are explicitly named, not hidden in the plan.
- The plan states what would trigger a re-evaluation.
- Someone else could execute the plan from the document alone.
## Related workflows
- Planning cycle: `core_plan_task` → `core_execute_safely` → `core_review_changes` → `core_verify_done`
- Decision chain: `core_evidence_research` → `core_decision_record` → `core_handoff_summary`
