---
name: pm_scope_tradeoffs
description: "Clarify what to cut, defer, or simplify when time, quality, and capacity are in tension."
user-invocable: true
disable-model-invocation: false
---


# Scope Tradeoffs

## Purpose
- Clarify what to cut, defer, or simplify when time, quality, and capacity are in tension.
- This is a **program specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when a team cannot ship everything and needs a principled way to reduce scope.
- The main bottleneck is best solved through program work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not let scope creep masquerade as customer empathy.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Program goal, timeline, dependencies, stakeholders, and the decision cadence.
- Known risks, scope pressure, reporting needs, and the state of the backlog or roadmap.
- What artifact is missing: milestone plan, risk register, roadmap scenario, or stakeholder update.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Protect the core outcome before secondary polish.
- Name the cost of every cut and every keep.
- Prefer reversible cuts over permanent design debt where possible.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read the latest plans, notes, tickets, and status sources before restructuring the program view.
- Reduce ambiguity in ownership, sequencing, and decision rights before adding more tracking detail.
- Make tradeoffs explicit so the program can move without hidden assumptions.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the target outcome and hard constraints.
2. Rank the work by user value and risk.
3. Identify cut, defer, simplify, and keep options.
4. Return a scope tradeoff recommendation.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Constraints
- Keep/cut/defer list
- Tradeoffs
- Recommendation
- Program artifact with owners, milestones, risks, and decision points.
- Tradeoff summary and the next escalation or approval needed.

## Failure modes to avoid
- Publishing a plan that ignores dependencies or unowned risks.
- Treating stakeholder communication as a substitute for real decision-making.
- Making the roadmap look tidy while underlying constraints stay unresolved.
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/pm_scope_tradeoffs <task>`
- Natural language: "Use scope Tradeoffs to clarify what to cut, defer, or simplify when time, quality, and capacity are in tension."
- Example: "Give me the clearest program view of this work, not just a prettier backlog."
- Example: "Map the milestones, dependencies, and tradeoffs so we can actually commit."
- Often paired with: `pm_milestone_plan`, `pm_risk_register`

## Quality bar
- Good scope management protects outcomes instead of just shrinking ambition blindly.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.
