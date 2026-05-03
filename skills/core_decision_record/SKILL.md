---
name: core_decision_record
description: "Capture options, tradeoffs, and the chosen path so future work does not repeat the same debate."
user-invocable: false
---

## Purpose
- Capture options, tradeoffs, and the chosen path so future work does not repeat the same debate.
- This is a **core specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use after a meaningful choice about scope, architecture, launch timing, pricing, or process.
- The main bottleneck is best solved through core work rather than generic brainstorming.

## Avoid when
- Do not use for trivial choices that have no durable consequence.

## Inputs to gather
- User objective, scope boundary, deadline, and success condition.
- Known constraints, approvals, and any actions that must stay reversible.
- The smallest set of files, notes, tools, or prior decisions that affect the next move.

## Operating rules
- Record the decision while the context is still fresh.
- Separate facts, assumptions, and judgment calls.
- Note what would cause the decision to be revisited.

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
1. State the decision and the problem it resolves.
2. List the main options and tradeoffs.
3. Explain why the chosen path won now.
4. Record risks, follow-ups, and review triggers.
## Output contract
- Decision
- Context
- Options considered
- Rationale
- Risks and review triggers
- Next action or decision recommendation.
- Dependencies, risks, and the smallest follow-up check that closes the loop.

## Failure modes to avoid
- Planning too much after the next action is already obvious.
- Skipping routing and forcing the wrong specialist to own the work.
- Producing ceremony instead of a decision-ready next step.

## Handoff cues

- Decision document: context, options considered, choice, rationale, risks.
- Date and participants recorded.
- Reversal conditions documented.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use decision Record to capture options, tradeoffs, and the chosen path so future work does not repeat the same debate."
- Example: "Route this mixed request and tell me the smallest safe next step."
- Example: "Plan the task, then tell me what context actually matters before we touch files."
- Often paired with: `core_route_request`, `core_plan_task`, `core_verify_done`

## Quality bar
- A decision record is good when a future operator can understand why the team chose this path and when to revisit it.
- The next action is specific enough to start immediately without further clarification.
- Assumptions are explicitly named, not hidden in the plan.
- The plan states what would trigger a re-evaluation.
- Someone else could execute the plan from the document alone.
## Related workflows
- Planning cycle: `core_plan_task` → `core_execute_safely` → `core_review_changes` → `core_verify_done`
- Decision chain: `core_evidence_research` → `core_decision_record` → `core_handoff_summary`
