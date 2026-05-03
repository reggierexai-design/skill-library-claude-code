---
name: core_execute_safely
description: "Execute the chosen plan with minimal diffs, bounded commands, and steady verification."
user-invocable: false
metadata: {"openclaw":{"emoji":"🧭"}}
---

## Purpose
- Execute the chosen plan with minimal diffs, bounded commands, and steady verification.
- This is a **core specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use while carrying out edits, commands, or browser work that has already been scoped.
- The main bottleneck is best solved through core work rather than generic brainstorming.

## Avoid when
- Do not use before the objective and constraints are clear.

## Inputs to gather
- User objective, scope boundary, deadline, and success condition.
- Known constraints, approvals, and any actions that must stay reversible.
- The smallest set of files, notes, tools, or prior decisions that affect the next move.

## Operating rules
- Prefer the smallest irreversible action that advances the task.
- Read before edit. Diff before claiming success.
- Do not batch unrelated changes together.

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
1. Execute one meaningful step at a time.
2. Check the effect immediately after each step.
3. If evidence diverges from the plan, stop and re-route instead of bulldozing forward.
4. Keep a concise running note of what changed and why.
## Output contract
- Actions taken
- Evidence after each step
- Files or pages changed
- Next remaining step or completion note
- Next action or decision recommendation.
- Dependencies, risks, and the smallest follow-up check that closes the loop.

## Failure modes to avoid
- Planning too much after the next action is already obvious.
- Skipping routing and forcing the wrong specialist to own the work.
- Producing ceremony instead of a decision-ready next step.

## Handoff cues

- Execution log: what was done, what changed, what was verified.
- Any deviations from the plan and why.
- Remaining risks and follow-up checks.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use core Execute Safely to execute the chosen plan with minimal diffs, bounded commands, and steady verification."
- Example: "Route this mixed request and tell me the smallest safe next step."
- Example: "Plan the task, then tell me what context actually matters before we touch files."
- Often paired with: `core_route_request`, `core_plan_task`, `core_verify_done`

## Quality bar
- Fast work is only useful if it remains reversible and legible.
- The next action is specific enough to start immediately without further clarification.
- Assumptions are explicitly named, not hidden in the plan.
- The plan states what would trigger a re-evaluation.
- Someone else could execute the plan from the document alone.
## Related workflows
- Planning cycle: `core_plan_task` → `core_execute_safely` → `core_review_changes` → `core_verify_done`
- Decision chain: `core_evidence_research` → `core_decision_record` → `core_handoff_summary`
