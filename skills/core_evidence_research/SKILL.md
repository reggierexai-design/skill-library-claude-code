---
name: core_evidence_research
description: "Gather fresh evidence with source discipline, concise notes, and clear uncertainty."
user-invocable: false
metadata: {"openclaw":{"emoji":"🧭"}}
---

## Purpose
- Gather fresh evidence with source discipline, concise notes, and clear uncertainty.
- This is a **core specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use for any research, validation, competitor check, market question, or factual claim that may have changed.
- The main bottleneck is best solved through core work rather than generic brainstorming.

## Avoid when
- Do not use when the answer can be grounded entirely in the local workspace and stable knowledge.

## Inputs to gather
- User objective, scope boundary, deadline, and success condition.
- Known constraints, approvals, and any actions that must stay reversible.
- The smallest set of files, notes, tools, or prior decisions that affect the next move.

## Operating rules
- Prioritize primary sources, official docs, and current evidence.
- Separate facts, inferences, and open questions.
- Stop when the decision can be made with confidence, not when every angle is exhausted.

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
1. Define the question and the decision it supports.
2. Gather a small, high-quality source set.
3. Compare sources and resolve conflicts.
4. Return the answer with evidence, caveats, and action implications.
## Output contract
- Research question
- Key findings
- Evidence trail
- Implications and open risks
- Next action or decision recommendation.
- Dependencies, risks, and the smallest follow-up check that closes the loop.

## Failure modes to avoid
- Planning too much after the next action is already obvious.
- Skipping routing and forcing the wrong specialist to own the work.
- Producing ceremony instead of a decision-ready next step.

## Handoff cues

- Evidence summary: sources found, credibility rating, key findings.
- Gaps: what evidence is still missing.
- Recommended next steps based on available evidence.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use core Evidence Research to gather fresh evidence with source discipline, concise notes, and clear uncertainty."
- Example: "Route this mixed request and tell me the smallest safe next step."
- Example: "Plan the task, then tell me what context actually matters before we touch files."
- Often paired with: `core_route_request`, `core_plan_task`, `core_verify_done`

## Quality bar
- Research is complete when the user can act, not when the notes are long.
- The next action is specific enough to start immediately without further clarification.
- Assumptions are explicitly named, not hidden in the plan.
- The plan states what would trigger a re-evaluation.
- Someone else could execute the plan from the document alone.
## Related workflows
- Planning cycle: `core_plan_task` → `core_execute_safely` → `core_review_changes` → `core_verify_done`
- Decision chain: `core_evidence_research` → `core_decision_record` → `core_handoff_summary`
