---
name: pm_stakeholder_update
description: "Write a crisp update that explains progress, risk, decisions, and asks without noise."
user-invocable: true
disable-model-invocation: true
---


# Stakeholder Update

## Purpose
- Write a crisp update that explains progress, risk, decisions, and asks without noise.
- This is a **program specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when leaders, partners, or adjacent teams need a trustworthy project update.
- The main bottleneck is best solved through program work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not hide risk inside cheerful filler.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Program goal, timeline, dependencies, stakeholders, and the decision cadence.
- Known risks, scope pressure, reporting needs, and the state of the backlog or roadmap.
- What artifact is missing: milestone plan, risk register, roadmap scenario, or stakeholder update.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Lead with what changed and what needs attention.
- Separate facts, risks, and asks.
- Keep the update readable in one pass.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read the latest plans, notes, tickets, and status sources before restructuring the program view.
- Reduce ambiguity in ownership, sequencing, and decision rights before adding more tracking detail.
- Make tradeoffs explicit so the program can move without hidden assumptions.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the audience and update objective.
2. Summarize progress, risks, and decisions.
3. Draft clear asks and next steps.
4. Return an update in the right tone and format.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Audience
- Progress summary
- Risks and decisions
- Asks and next steps
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
- Slash: `/pm_stakeholder_update <task>`
- Natural language: "Use stakeholder Update to write a crisp update that explains progress, risk, decisions, and asks without noise."
- Example: "Give me the clearest program view of this work, not just a prettier backlog."
- Example: "Map the milestones, dependencies, and tradeoffs so we can actually commit."
- Often paired with: `pm_milestone_plan`, `pm_risk_register`, `pm_scope_tradeoffs`

## Quality bar
- A good update reduces backchannel confusion and unblock time.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.
