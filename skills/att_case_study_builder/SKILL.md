---
name: att_case_study_builder
description: "Shape a customer story into a credible case study with before, after, mechanism, and proof."
user-invocable: true
disable-model-invocation: true
---


# Case Study Builder

## Purpose
- Shape a customer story into a credible case study with before, after, mechanism, and proof.
- This is an **attention specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when the project has a user win, transformation, or measurable result worth publishing.
- The main bottleneck is best solved through attention work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not use when there is no real result or permission to tell the story.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Audience, offer, proof, timing, channel mix, and the action you want people to take.
- Existing assets, customer language, constraints, and how bold or conservative the positioning can be.
- Whether the goal is launch attention, ongoing demand, activation, conversion, or reputation building.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- A case study needs context, conflict, solution, and proof.
- Specificity beats adjectives.
- Keep the customer as the protagonist.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Ground messaging in real proof, user language, and the current product truth before polishing copy.
- Read existing site copy, launch assets, notes, or research so the new output fits the system instead of floating beside it.
- When external facts or competitors matter, verify them before using them in public-facing content.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Inventory the customer story and evidence.
2. Structure the narrative arc.
3. Write the case study with proof points.
4. Provide short derivatives if useful.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Context
- Challenge
- Solution and mechanism
- Outcome and proof
- Channel-ready draft or plan with hook, proof, CTA, and sequencing.
- Audience assumptions, risks, and the missing proof that would strengthen the asset.

## Failure modes to avoid
- Writing generic hype that is not anchored in proof or audience tension.
- Creating channel content before the narrative, hook, or CTA is actually sharp.
- Confusing attention with trust; the output should attract and hold scrutiny.
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/att_case_study_builder <task>`
- Natural language: "Use case Study Builder to shape a customer story into a credible case study with before, after, mechanism, and proof."
- Example: "Build an attention asset that feels specific, credible, and worth sharing."
- Example: "Turn this product reality into a sharper story, launch angle, or distribution plan."
- Often paired with: `att_message_house`, `att_launch_plan`, `att_proof_mining`

## Quality bar
- A credible case study sells by explaining, not boasting.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.
