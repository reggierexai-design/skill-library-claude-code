---
name: core_risk_gate
description: "Slow down risky actions involving installs, secrets, destructive edits, money, or live accounts."
user-invocable: false
---

## Purpose
- Slow down risky actions involving installs, secrets, destructive edits, money, or live accounts.
- This is a **core specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before any action that could cause loss, leakage, account lockout, broad system changes, or irreversible effects.
- The main bottleneck is best solved through core work rather than generic brainstorming.

## Avoid when
- Do not use to block harmless local reading or reversible drafting work.

## Inputs to gather
- User objective, scope boundary, deadline, and success condition.
- Known constraints, approvals, and any actions that must stay reversible.
- The smallest set of files, notes, tools, or prior decisions that affect the next move.

## Operating rules
- Prefer least privilege and reversible steps.
- Treat secrets, credentials, and live production access as high risk by default.
- If a safer offline or read-only path exists, choose it first.

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
1. Classify the action by risk level and blast radius.
2. Identify the safer alternatives.
3. Proceed only with the minimum action that preserves user intent.
4. Record any unverified risk that remains.
## Output contract
- Risk level
- Why it is risky
- Safer path chosen
- Residual risk
- Next action or decision recommendation.
- Dependencies, risks, and the smallest follow-up check that closes the loop.

## Failure modes to avoid
- Planning too much after the next action is already obvious.
- Skipping routing and forcing the wrong specialist to own the work.
- Producing ceremony instead of a decision-ready next step.

## Handoff cues

- Risk gate assessment: pass, conditional pass, or block.
- Specific risks flagged with severity and mitigation.
- Conditions that must be met before proceeding.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use core Risk Gate to slow down risky actions involving installs, secrets, destructive edits, money, or live accounts."
- Example: "Route this mixed request and tell me the smallest safe next step."
- Example: "Plan the task, then tell me what context actually matters before we touch files."
- Often paired with: `core_route_request`, `core_plan_task`, `core_verify_done`

## Quality bar
- The risk gate should reduce blast radius without paralyzing normal work.
- The next action is specific enough to start immediately without further clarification.
- Assumptions are explicitly named, not hidden in the plan.
- The plan states what would trigger a re-evaluation.
- Someone else could execute the plan from the document alone.
## Related workflows
- Planning cycle: `core_plan_task` → `core_execute_safely` → `core_review_changes` → `core_verify_done`
- Decision chain: `core_evidence_research` → `core_decision_record` → `core_handoff_summary`
