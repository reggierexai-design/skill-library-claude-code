---
name: att_changelog_story
description: "Turn product updates into clear stories that reinforce momentum, quality, and user trust."
user-invocable: true
disable-model-invocation: true
---


# Changelog Story

## Purpose
- Turn product updates into clear stories that reinforce momentum, quality, and user trust.
- This is an **attention specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use for release notes, product update posts, launch emails, or roadmap communication.
- The main bottleneck is best solved through attention work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not use when there is no meaningful user-facing change to communicate.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Audience, offer, proof, timing, channel mix, and the action you want people to take.
- Existing assets, customer language, constraints, and how bold or conservative the positioning can be.
- Whether the goal is launch attention, ongoing demand, activation, conversion, or reputation building.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Lead with what changed for the user.
- Explain why it matters, not just what shipped.
- Keep the tone grounded and specific.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Ground messaging in real proof, user language, and the current product truth before polishing copy.
- Read existing site copy, launch assets, notes, or research so the new output fits the system instead of floating beside it.
- When external facts or competitors matter, verify them before using them in public-facing content.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Identify the user-facing value of the update.
2. Organize the changes into a story arc.
3. Write the changelog or announcement in channel-appropriate form.
4. Return optional shorter derivatives if helpful.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Headline
- What changed
- Why it matters
- Next step or CTA
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
- Slash: `/att_changelog_story <task>`
- Natural language: "Use changelog Story to turn product updates into clear stories that reinforce momentum, quality, and user trust."
- Example: "Build an attention asset that feels specific, credible, and worth sharing."
- Example: "Turn this product reality into a sharper story, launch angle, or distribution plan."
- Often paired with: `att_message_house`, `att_launch_plan`, `att_proof_mining`

## Quality bar
- A changelog story should make shipping feel real and cumulative.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.
