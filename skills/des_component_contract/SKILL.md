---
name: des_component_contract
description: "Define a UI component by purpose, variants, states, and constraints so teams use it consistently."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83e\uddf1"}}
---

## Purpose
- Define a UI component by purpose, variants, states, and constraints so teams use it consistently.
- This is a **design specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a component is reused often but implemented differently across the product.

## Avoid when
- Do not standardize a component whose purpose is still unclear.

## Inputs to gather
- Target user state, screen or flow, product goal, and any platform or brand constraints.
- Existing screens, components, copy, research, and accessibility or localization requirements.
- What decision is needed now: critique, brief, direction, spec, or usability plan.

## Operating rules
- Name the component job before the visuals.
- Define allowed variants and forbidden misuse.
- Cover accessibility and state behavior explicitly.

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
1. Define the component purpose and user need.
2. List the variants, states, and constraints.
3. Specify content, accessibility, and interaction rules.
4. Return a component contract ready for system work.
## Output contract
- Purpose
- Variants and states
- Rules and constraints
- Accessibility notes
- Actionable critique, brief, spec, or copy direction tied to user outcomes.
- Priority issues, rationale, and the smallest next design move.

## Failure modes to avoid
- Confusing taste with user-centered rationale.
- Critiquing a single screen while ignoring the surrounding flow and state transitions.
- Producing abstract design language with no implementable next step.

## Handoff cues
- Component contract: props, events, slots, variants, accessibility requirements.
- Usage examples and edge cases.
- Implementation notes for developers.

## Example invocation
- Slash: `/des_component_contract <task>`
- Natural language: "Use component Contract to define a ui component by purpose, variants, states, and constraints so teams use it consistently."
- Example: "Review this flow for clarity, hierarchy, and completion risk."
- Example: "Translate the product problem into a buildable design brief or wireframe spec."
- Often paired with: `des_design_brief`, `des_design_critique`, `des_accessibility_review`

## Quality bar

- Every prop is typed and documented with valid range and default.
- Events are named by what happens, not by implementation detail (click, not handleClick).
- Accessibility requirements are part of the contract, not an afterthought.
- The contract is complete enough for a developer to implement without asking questions.
- Every design decision traces to a user need or brand principle.
- The most common user path is optimized first.
- Accessibility requirements are met (WCAG 2.1 AA minimum).
- The design has been tested or is ready to test with real users.
## Related workflows
- Design flow: `des_design_brief` → `des_wireframe_spec` → `des_design_critique` → `des_usability_test_plan`
