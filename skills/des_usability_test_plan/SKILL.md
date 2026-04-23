---
name: des_usability_test_plan
description: "Plan lightweight usability sessions that reveal friction, confusion, and unmet expectations."
user-invocable: true
disable-model-invocation: true
---


# Usability Test Plan

## Purpose
- Plan lightweight usability sessions that reveal friction, confusion, and unmet expectations.
- This is a **design specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use before testing a prototype, new workflow, onboarding, or content-heavy flow.
- The main bottleneck is best solved through design work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not run sessions with no task script or learning goal.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Target user state, screen or flow, product goal, and any platform or brand constraints.
- Existing screens, components, copy, research, and accessibility or localization requirements.
- What decision is needed now: critique, brief, direction, spec, or usability plan.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Test tasks, not opinions.
- Prefer realistic scenarios over feature tours.
- Capture evidence before interpreting it.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read the product context and surrounding flow before critiquing or proposing a design change.
- Anchor design decisions in hierarchy, clarity, accessibility, and completion of the user task.
- Keep design outputs specific enough that product and engineering can act on them.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the research goal and target participants.
2. Write realistic tasks and prompts.
3. Set observation notes and debrief questions.
4. Return a usability test plan with logistics.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Goal and participants
- Tasks and prompts
- Observation framework
- Logistics
- Actionable critique, brief, spec, or copy direction tied to user outcomes.
- Priority issues, rationale, and the smallest next design move.

## Failure modes to avoid
- Confusing taste with user-centered rationale.
- Critiquing a single screen while ignoring the surrounding flow and state transitions.
- Producing abstract design language with no implementable next step.
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/des_usability_test_plan <task>`
- Natural language: "Use usability Test Plan to plan lightweight usability sessions that reveal friction, confusion, and unmet expectations."
- Example: "Review this flow for clarity, hierarchy, and completion risk."
- Example: "Translate the product problem into a buildable design brief or wireframe spec."
- Often paired with: `des_design_brief`, `des_design_critique`, `des_accessibility_review`

## Quality bar
- A strong test plan turns vague feedback into actionable evidence.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.
