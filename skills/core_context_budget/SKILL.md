---
name: core_context_budget
description: "Keep a run lean by selecting only the context and skills that change the next decision."
user-invocable: false
metadata: {"openclaw":{"emoji":"\ud83e\uddee"}}
---

## Purpose
- Keep a run lean by selecting only the context and skills that change the next decision.
- This is a **core specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before pulling in many files, tools, or skills for one task.
- The main bottleneck is best solved through core work rather than generic brainstorming.

## Avoid when
- Do not load broad context just because it exists.

## Inputs to gather
- User objective, scope boundary, deadline, and success condition.
- Known constraints, approvals, and any actions that must stay reversible.
- The smallest set of files, notes, tools, or prior decisions that affect the next move.

## Operating rules
- Context should be chosen, not inherited by accident.
- Prefer narrow evidence to broad familiarity.
- Cut anything that does not change the next action.

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
1. List candidate context sources.
2. Keep the few that change the decision.
3. Drop or defer the rest.
4. Return a lean context plan for the run.
## Output contract
- Included context
- Excluded context
- Reasoning
- Next action
- Next action or decision recommendation.
- Dependencies, risks, and the smallest follow-up check that closes the loop.

## Failure modes to avoid
- Planning too much after the next action is already obvious.
- Skipping routing and forcing the wrong specialist to own the work.
- Producing ceremony instead of a decision-ready next step.

## Handoff cues
- Context budget allocation per task type.
- Compression decisions made and tradeoffs.
- Token usage tracking dashboard or method.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use context Budget Gate to keep a run lean by selecting only the context and skills that change the next decision."
- Example: "Route this mixed request and tell me the smallest safe next step."
- Example: "Plan the task, then tell me what context actually matters before we touch files."
- Often paired with: `core_route_request`, `core_plan_task`, `core_verify_done`

## Quality bar

- Every token in the prompt earns its place; any token that can be removed without changing the output should be.
- The prompt fits within the model's effective context window, not just the maximum.
- Key instructions are positioned where the model attends most (beginning and end).
- A second operator can reproduce the budget decisions from the documentation.
- The next action is specific enough to start immediately without further clarification.
- Assumptions are explicitly named, not hidden in the plan.
- The plan states what would trigger a re-evaluation.
- Someone else could execute the plan from the document alone.
## Related workflows
- Planning cycle: `core_plan_task` → `core_execute_safely` → `core_review_changes` → `core_verify_done`
- Decision chain: `core_evidence_research` → `core_decision_record` → `core_handoff_summary`
