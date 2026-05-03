---
name: des_usability_test_plan
description: "Plan lightweight usability sessions that reveal friction, confusion, and unmet expectations."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83e\uddea"}}
---

## Purpose
- Plan lightweight usability sessions that reveal friction, confusion, and unmet expectations.
- This is a **design specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before testing a prototype, new workflow, onboarding, or content-heavy flow.

## Avoid when
- Do not run sessions with no task script or learning goal.

## Inputs to gather
- Target user state, screen or flow, product goal, and any platform or brand constraints.
- Existing screens, components, copy, research, and accessibility or localization requirements.
- What decision is needed now: critique, brief, direction, spec, or usability plan.

## Operating rules
- Test tasks, not opinions.
- Prefer realistic scenarios over feature tours.
- Capture evidence before interpreting it.

- Design for the most common path first, then handle edge cases. Optimizing for edge cases creates mediocre mainstream experiences.
- Every design decision should be traceable to a user need or a brand principle. Decorative decisions without rationale accumulate as design debt.
- Consistency reduces cognitive load. A consistent mediocre pattern beats an inconsistent brilliant one.
- Accessibility is not optional. If a design excludes users with disabilities, it fails regardless of its aesthetic quality.
- Test with real users, not stakeholders. Stakeholder preferences are not user needs.
## Claude Code tool pattern
- Read the product context and surrounding flow before critiquing or proposing a design change.
- Anchor design decisions in hierarchy, clarity, accessibility, and completion of the user task.
- Keep design outputs specific enough that product and engineering can act on them.

## Expanded workflow
1. Define the research goal and target participants.
2. Write realistic tasks and prompts.
3. Set observation notes and debrief questions.
4. Return a usability test plan with logistics.
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

## Handoff cues
- Test plan: scenarios, tasks, success metrics, participant criteria.
- Moderator script and observation checklist.
- Analysis framework for findings.

## Example invocation
- Slash: `/des_usability_test_plan <task>`
- Natural language: "Use usability Test Plan to plan lightweight usability sessions that reveal friction, confusion, and unmet expectations."
- Example: "Review this flow for clarity, hierarchy, and completion risk."
- Example: "Translate the product problem into a buildable design brief or wireframe spec."
- Often paired with: `des_design_brief`, `des_design_critique`, `des_accessibility_review`

## Quality bar

- Scenarios are written in the user's language, not the product's.
- Tasks are specific enough to observe success/failure but open enough to discover unexpected behavior.
- Participant criteria match the target user profile.
- The plan includes both quantitative metrics and qualitative observation.
- Every design decision traces to a user need or brand principle.
- The most common user path is optimized first.
- Accessibility requirements are met (WCAG 2.1 AA minimum).
- The design has been tested or is ready to test with real users.
## Related workflows
- Design flow: `des_design_brief` → `des_wireframe_spec` → `des_design_critique` → `des_usability_test_plan`
