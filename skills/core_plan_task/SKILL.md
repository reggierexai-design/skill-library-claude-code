---
name: core_plan_task
description: "Turn a request into a short, executable plan with checkpoints and exit criteria."
user-invocable: false
disable-model-invocation: false
---


# Core Plan Task

## Purpose
- Turn a request into a short, executable plan with checkpoints and exit criteria.
- This is a **core specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use before multi-step work, risky changes, or any task where success criteria are not already concrete.
- The main bottleneck is best solved through core work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not use when the task can be completed safely in one obvious step.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- User objective, scope boundary, deadline, and success condition.
- Known constraints, approvals, and any actions that must stay reversible.
- The smallest set of files, notes, tools, or prior decisions that affect the next move.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Keep plans short enough to execute, inspect, and revise.
- Define what done means before writing or changing much.
- Prefer serial milestones over sprawling checklists.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Start by reading the local context that changes the decision instead of front-loading every file.
- Use search/read to map the problem first; only edit or execute after the plan and blast radius are clear.
- Leave a compact reasoning trail so later skills can pick up without repeating discovery work.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Restate the task in outcome terms.
2. Break it into the minimum meaningful steps.
3. Attach a verification checkpoint to each major step.
4. Call out dependencies, risks, and fallback paths.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Outcome statement
- Step plan
- Verification checkpoints
- Risks and fallback
- Next action or decision recommendation.
- Dependencies, risks, and the smallest follow-up check that closes the loop.

## Failure modes to avoid
- Planning too much after the next action is already obvious.
- Skipping routing and forcing the wrong specialist to own the work.
- Producing ceremony instead of a decision-ready next step.
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use core Plan Task to turn a request into a short, executable plan with checkpoints and exit criteria."
- Example: "Route this mixed request and tell me the smallest safe next step."
- Example: "Plan the task, then tell me what context actually matters before we touch files."
- Often paired with: `core_route_request`, `core_verify_done`

## Quality bar
- A plan is good when another agent could execute it without guessing.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.
