---
name: des_wireframe_spec
description: "Describe screens, states, and interactions clearly enough to build or critique without mockups."
user-invocable: true
---

## Purpose
- Describe screens, states, and interactions clearly enough to build or critique without mockups.
- This is a **design specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a team needs a low-fidelity spec for a workflow before visual design.

## Avoid when
- Do not treat wireframes as a substitute for product decisions.

## Inputs to gather
- Target user state, screen or flow, product goal, and any platform or brand constraints.
- Existing screens, components, copy, research, and accessibility or localization requirements.
- What decision is needed now: critique, brief, direction, spec, or usability plan.

## Operating rules
- Describe user intent, not just boxes.
- Cover empty, loading, success, and failure states.
- Keep the flow coherent across screens.

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
1. Define the workflow and entry points.
2. List the screens, states, and transitions.
3. Specify validation, errors, and edge cases.
4. Return a wireframe-ready screen spec.
## Output contract
- Workflow
- Screen-by-screen spec
- States and validation
- Open issues
- Actionable critique, brief, spec, or copy direction tied to user outcomes.
- Priority issues, rationale, and the smallest next design move.

## Failure modes to avoid
- Confusing taste with user-centered rationale.
- Critiquing a single screen while ignoring the surrounding flow and state transitions.
- Producing abstract design language with no implementable next step.

## Handoff cues
- Wireframe spec: screens, flows, component placement, interaction notes.
- Responsive breakpoints and adaptation strategy.
- Annotations for developers on behavior and states.

## Example invocation
- Slash: `/des_wireframe_spec <task>`
- Natural language: "Use wireframe Spec to describe screens, states, and interactions clearly enough to build or critique without mockups."
- Example: "Review this flow for clarity, hierarchy, and completion risk."
- Example: "Translate the product problem into a buildable design brief or wireframe spec."
- Often paired with: `des_design_brief`, `des_design_critique`, `des_accessibility_review`

## Quality bar

- Every screen has enough detail for a developer to implement without guessing.
- Edge cases are wired: empty states, error states, loading states.
- Responsive behavior is specified at every breakpoint.
- Interaction notes cover what happens, not just what it looks like.
- Every design decision traces to a user need or brand principle.
- The most common user path is optimized first.
- Accessibility requirements are met (WCAG 2.1 AA minimum).
- The design has been tested or is ready to test with real users.
## Related workflows
- Design flow: `des_design_brief` → `des_wireframe_spec` → `des_design_critique` → `des_usability_test_plan`
