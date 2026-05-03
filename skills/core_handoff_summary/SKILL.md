---
name: core_handoff_summary
description: "Wrap up work so another operator can continue without re-discovering context."
user-invocable: false
metadata: {"openclaw":{"emoji":"🧭"}}
---

## Purpose
- Wrap up work so another operator can continue without re-discovering context.
- This is a **core specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use at the end of a substantial task, pause point, or partial completion.
- The main bottleneck is best solved through core work rather than generic brainstorming.

## Avoid when
- Do not use for trivial outputs that already contain their own full context.

## Inputs to gather
- User objective, scope boundary, deadline, and success condition.
- Known constraints, approvals, and any actions that must stay reversible.
- The smallest set of files, notes, tools, or prior decisions that affect the next move.

## Operating rules
- Keep the handoff compact but complete.
- Document decisions, evidence, and remaining risks.
- Make the next best action obvious.

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
1. Summarize the goal and the current state.
2. List what changed and what was verified.
3. Capture pending work and blockers.
4. Point to the files, pages, or artifacts that matter next.
## Output contract
- Goal
- What changed
- What was verified
- Open items and next action
- Next action or decision recommendation.
- Dependencies, risks, and the smallest follow-up check that closes the loop.

## Failure modes to avoid
- Planning too much after the next action is already obvious.
- Skipping routing and forcing the wrong specialist to own the work.
- Producing ceremony instead of a decision-ready next step.

## Handoff cues
- Handoff document: context, current state, what's done, what's next, what to watch.
- Key decisions and rationale preserved.
- Open questions and blockers flagged.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use core Handoff Summary to wrap up work so another operator can continue without re-discovering context."
- Example: "Route this mixed request and tell me the smallest safe next step."
- Example: "Plan the task, then tell me what context actually matters before we touch files."
- Often paired with: `core_route_request`, `core_plan_task`, `core_verify_done`

## Quality bar

- A new operator can pick up the work without asking clarifying questions.
- All open threads, blockers, and next actions are explicit.
- Context includes both what was done and why it was done that way.
- Handoff is testable: the receiver can verify the current state independently.
- The next action is specific enough to start immediately without further clarification.
- Assumptions are explicitly named, not hidden in the plan.
- The plan states what would trigger a re-evaluation.
- Someone else could execute the plan from the document alone.
## Related workflows
- Planning cycle: `core_plan_task` → `core_execute_safely` → `core_review_changes` → `core_verify_done`
- Decision chain: `core_evidence_research` → `core_decision_record` → `core_handoff_summary`
