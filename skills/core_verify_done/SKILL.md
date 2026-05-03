---
name: core_verify_done
description: "Prove the task is complete with checks tied to the original request and the actual changes made."
user-invocable: false
---

## Purpose
- Prove the task is complete with checks tied to the original request and the actual changes made.
- This is a **core specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before declaring completion on any task that involved reasoning, editing, research, or execution.
- The main bottleneck is best solved through core work rather than generic brainstorming.

## Avoid when
- Do not use as a substitute for doing the work.

## Inputs to gather
- User objective, scope boundary, deadline, and success condition.
- Known constraints, approvals, and any actions that must stay reversible.
- The smallest set of files, notes, tools, or prior decisions that affect the next move.

## Operating rules
- Verify the user outcome, not just intermediate steps.
- Prefer direct evidence over confidence language.
- If something remains unverified, say so plainly.

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
1. Restate what success required.
2. Run the smallest checks that can prove it.
3. Compare the final state with the original request.
4. List anything not verified and why.
## Output contract
- Completion verdict
- Evidence
- Remaining gaps
- Suggested next check if needed
- Next action or decision recommendation.
- Dependencies, risks, and the smallest follow-up check that closes the loop.

## Failure modes to avoid
- Planning too much after the next action is already obvious.
- Skipping routing and forcing the wrong specialist to own the work.
- Producing ceremony instead of a decision-ready next step.

## Handoff cues

- Verification report: what was checked, what passed, what failed.
- Any remaining gaps or assumptions.
- Confirmation that exit criteria are met or list of what's still needed.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use core Verify Done to prove the task is complete with checks tied to the original request and the actual changes made."
- Example: "Route this mixed request and tell me the smallest safe next step."
- Example: "Plan the task, then tell me what context actually matters before we touch files."
- Often paired with: `core_route_request`, `core_plan_task`

## Quality bar
- Done means verified enough that a careful operator would trust the result.
- The next action is specific enough to start immediately without further clarification.
- Assumptions are explicitly named, not hidden in the plan.
- The plan states what would trigger a re-evaluation.
- Someone else could execute the plan from the document alone.
## Related workflows
- Planning cycle: `core_plan_task` → `core_execute_safely` → `core_review_changes` → `core_verify_done`
- Decision chain: `core_evidence_research` → `core_decision_record` → `core_handoff_summary`
