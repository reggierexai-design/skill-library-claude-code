---
name: att_email_nurture_sequences
description: "Build concise email sequences for launches, onboarding, activation, and reactivation."
user-invocable: true
disable-model-invocation: true
---


# Email Nurture Sequences

## Purpose
- Build concise email sequences for launches, onboarding, activation, and reactivation.
- This is an **attention specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when the user needs lifecycle emails for signups, waitlists, launches, onboarding, activation, or reactivation.
- The main bottleneck is best solved through attention work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not use when the real problem is unclear positioning or weak proof. Fix the message first.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Audience, offer, proof, timing, channel mix, and the action you want people to take.
- Existing assets, customer language, constraints, and how bold or conservative the positioning can be.
- Whether the goal is launch attention, ongoing demand, activation, conversion, or reputation building.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Each sequence should have one job, one audience, and one next step.
- Write with product truth, user relevance, and consistent timing.
- Prefer fewer stronger emails over long low-signal drips.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Ground messaging in real proof, user language, and the current product truth before polishing copy.
- Read existing site copy, launch assets, notes, or research so the new output fits the system instead of floating beside it.
- When external facts or competitors matter, verify them before using them in public-facing content.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define audience, trigger, and desired next action.
2. Choose the minimum effective sequence length and send timing.
3. Draft subject lines, bodies, and CTAs around one message arc.
4. Return the sequence with notes on why each email exists.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Audience and trigger
- Sequence goal
- Email-by-email plan
- Draft copy and CTA notes
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
- Slash: `/att_email_nurture_sequences <task>`
- Natural language: "Use email Nurture Sequences to build concise email sequences for launches, onboarding, activation, and reactivation."
- Example: "Build an attention asset that feels specific, credible, and worth sharing."
- Example: "Turn this product reality into a sharper story, launch angle, or distribution plan."
- Often paired with: `att_message_house`, `att_launch_plan`, `att_proof_mining`

## Quality bar
- A strong sequence feels like helpful momentum, not automated nagging.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.
