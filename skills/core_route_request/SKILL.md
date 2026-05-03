---
name: core_route_request
description: "Classify the task, choose the right specialist path, and avoid premature action."
user-invocable: false
---

## Purpose
- Classify the task, choose the right specialist path, and avoid premature action.
- This is a **core specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use at the start of any non-trivial request to decide whether the work is research, product, engineering, growth, operations, or mixed.
- The main bottleneck is best solved through core work rather than generic brainstorming.

## Avoid when
- Do not use when the user asks for a tiny one-step action that is already obvious and low risk.

## Inputs to gather
- User objective, scope boundary, deadline, and success condition.
- Known constraints, approvals, and any actions that must stay reversible.
- The smallest set of files, notes, tools, or prior decisions that affect the next move.

## Operating rules
- Resolve the job before optimizing the style.
- Prefer the smallest sufficient path instead of loading many specialists.
- When the request mixes multiple domains, sequence them instead of blending them into one vague response.

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
1. Classify the request into one primary domain and any secondary domains.
2. State the working objective, constraints, and missing evidence.
3. Pick the next best specialist skill or a minimal direct action path.
4. If risk is non-trivial, invoke the risk gate before proceeding.
## Output contract
- Task classification
- Primary objective
- Constraints and assumptions
- Chosen next skill or execution path
- Next action or decision recommendation.
- Dependencies, risks, and the smallest follow-up check that closes the loop.

## Failure modes to avoid
- Planning too much after the next action is already obvious.
- Skipping routing and forcing the wrong specialist to own the work.
- Producing ceremony instead of a decision-ready next step.

## Handoff cues

- Routing decision: which specialist, why, and with what context.
- Any request decomposition if multiple specialists needed.
- Priority and deadline communicated.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use core Route Request to classify the task, choose the right specialist path, and avoid premature action."
- Example: "Route this mixed request and tell me the smallest safe next step."
- Example: "Plan the task, then tell me what context actually matters before we touch files."
- Often paired with: `core_plan_task`, `core_verify_done`

## Quality bar
- The route must reduce ambiguity, not add ceremony.
- If the likely path is wrong, make the uncertainty explicit.
- The next action is specific enough to start immediately without further clarification.
- Assumptions are explicitly named, not hidden in the plan.
- The plan states what would trigger a re-evaluation.
- Someone else could execute the plan from the document alone.
## Related workflows
- Planning cycle: `core_plan_task` → `core_execute_safely` → `core_review_changes` → `core_verify_done`
- Decision chain: `core_evidence_research` → `core_decision_record` → `core_handoff_summary`
