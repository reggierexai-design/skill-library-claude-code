---
name: des_design_brief
description: "Translate a product problem into a design brief with users, constraints, and success criteria."
user-invocable: true
---

## Purpose
- Translate a product problem into a design brief with users, constraints, and success criteria.
- This is a **design specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when design work is about to start but the problem framing is still loose.

## Avoid when
- Do not jump to screens before clarifying the user job and constraints.

## Inputs to gather
- Target user state, screen or flow, product goal, and any platform or brand constraints.
- Existing screens, components, copy, research, and accessibility or localization requirements.
- What decision is needed now: critique, brief, direction, spec, or usability plan.

## Operating rules
- Frame the problem before proposing the interface.
- Name the audience, context, and tradeoffs.
- Define what success and failure look like.

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
1. Define the user, context, and problem.
2. List constraints, risks, and known inputs.
3. Set success criteria and open questions.
4. Return a design brief ready for critique or execution.
## Output contract
- Problem and users
- Constraints and inputs
- Success criteria
- Open questions
- Actionable critique, brief, spec, or copy direction tied to user outcomes.
- Priority issues, rationale, and the smallest next design move.

## Failure modes to avoid
- Confusing taste with user-centered rationale.
- Critiquing a single screen while ignoring the surrounding flow and state transitions.
- Producing abstract design language with no implementable next step.

## Handoff cues
- Design brief: problem, audience, constraints, success criteria, inspiration.
- Scope boundaries: what's in and out.
- Timeline and review checkpoints.

## Example invocation
- Slash: `/des_design_brief <task>`
- Natural language: "Use design Brief to translate a product problem into a design brief with users, constraints, and success criteria."
- Example: "Review this flow for clarity, hierarchy, and completion risk."
- Example: "Translate the product problem into a buildable design brief or wireframe spec."
- Often paired with: `des_design_critique`, `des_accessibility_review`

## Quality bar

- The brief constrains the design enough to prevent scope creep but not so much that it eliminates creativity.
- Success criteria are measurable: completion rate, time-on-task, satisfaction score.
- Constraints are explicit: brand guidelines, technical limits, timeline.
- A second designer could produce aligned work from this brief alone.
- Every design decision traces to a user need or brand principle.
- The most common user path is optimized first.
- Accessibility requirements are met (WCAG 2.1 AA minimum).
- The design has been tested or is ready to test with real users.
## Related workflows
- Design flow: `des_design_brief` → `des_wireframe_spec` → `des_design_critique` → `des_usability_test_plan`
