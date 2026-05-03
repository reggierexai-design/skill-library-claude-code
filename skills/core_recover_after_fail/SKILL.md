---
name: core_recover_after_fail
description: "Stabilize after a failed command, broken patch, bad assumption, or unexpected result."
user-invocable: false
---

## Purpose
- Stabilize after a failed command, broken patch, bad assumption, or unexpected result.
- This is a **core specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when the current path is failing, the environment disagrees with the plan, or the last action created uncertainty.
- The main bottleneck is best solved through core work rather than generic brainstorming.

## Avoid when
- Do not use to mask repeated guessing. Use it to reset on evidence.

## Inputs to gather
- User objective, scope boundary, deadline, and success condition.
- Known constraints, approvals, and any actions that must stay reversible.
- The smallest set of files, notes, tools, or prior decisions that affect the next move.

## Operating rules
- Stop the failure from cascading.
- Preserve evidence before changing more.
- Prefer diagnosis and rollback over improvising deeper into a bad state.

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
1. Freeze the current state and identify the exact failure point.
2. Separate confirmed facts from assumptions.
3. Choose one of: retry safely, patch the root cause, roll back, or escalate uncertainty.
4. Resume only after the path is coherent again.
## Output contract
- Failure summary
- Confirmed cause or leading hypotheses
- Recovery action
- New safe path forward
- Next action or decision recommendation.
- Dependencies, risks, and the smallest follow-up check that closes the loop.

## Failure modes to avoid
- Planning too much after the next action is already obvious.
- Skipping routing and forcing the wrong specialist to own the work.
- Producing ceremony instead of a decision-ready next step.

## Handoff cues

- Recovery log: what failed, what was tried, what worked, what's still broken.
- Root cause hypothesis if known.
- Follow-up actions to prevent recurrence.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use core Recover After Fail to stabilize after a failed command, broken patch, bad assumption, or unexpected result."
- Example: "Route this mixed request and tell me the smallest safe next step."
- Example: "Plan the task, then tell me what context actually matters before we touch files."
- Often paired with: `core_route_request`, `core_plan_task`, `core_verify_done`

## Quality bar
- Recovery is successful when uncertainty decreases and the task becomes tractable again.
- The next action is specific enough to start immediately without further clarification.
- Assumptions are explicitly named, not hidden in the plan.
- The plan states what would trigger a re-evaluation.
- Someone else could execute the plan from the document alone.
## Related workflows
- Planning cycle: `core_plan_task` → `core_execute_safely` → `core_review_changes` → `core_verify_done`
- Decision chain: `core_evidence_research` → `core_decision_record` → `core_handoff_summary`
