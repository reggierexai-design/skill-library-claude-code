---
name: att_email_nurture_sequences
description: "Build concise email sequences for launches, onboarding, activation, and reactivation."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udce3"}}
---

## Purpose
- Build concise email sequences for launches, onboarding, activation, and reactivation.

## Use when
- Use when the user needs lifecycle emails for signups, waitlists, launches, onboarding, activation, or reactivation.

## Avoid when
- Do not use when the real problem is unclear positioning or weak proof. Fix the message first.

## Inputs to gather
- Audience segment: who's receiving this sequence and what do they already know?
- Entry trigger: what action puts someone in this sequence (signup, demo request, trial start)?
- The end goal: what action should the recipient take by the end?
- Available proof: case studies, metrics, testimonials, feature demos.
- Current email infrastructure: tool, sending domain, existing templates.

## Operating rules
- Each sequence should have one job, one audience, and one next step.
- Write with product truth, user relevance, and consistent timing.
- Prefer fewer stronger emails over long low-signal drips.

## Claude Code tool pattern
- Use `WebFetch` to research competitor content and current platform conventions.
- Read existing site copy, product pages, and proof assets before drafting so output fits the real product truth.
- When external claims appear, verify before publishing with `safe_external_claims`.
- After drafting, run `att_proof_mining` to verify every claim has backing.

## Expanded workflow
1. Define audience, trigger, and desired next action.
2. Choose the minimum effective sequence length and send timing.
3. Draft subject lines, bodies, and CTAs around one message arc.
4. Return the sequence with notes on why each email exists.
## Output contract
- Audience and trigger
- Sequence goal
- Email-by-email plan
- Draft copy and CTA notes
## Failure modes to avoid
- Every email is a pitch — no value given means no trust earned.
- Subject lines that oversell and underdeliver — high opens but high unsubscribes.
- No exit conditions — converted customers still getting nurture emails.
- Too many CTAs per email — the recipient doesn't know what to click.
- Generic content that could come from any brand.

## Handoff cues
- List all emails with subject lines, timing, and CTAs.
- Flag the exit conditions and where they're configured.
- Note any proof assets still needed.

## Example invocation
- Slash: `/att_email_nurture_sequences <task>`
- Natural language: "Use email Nurture Sequences to build concise email sequences for launches, onboarding, activation, and reactivation."
- Example: "Build a 5-email onboarding sequence for new signups who have not activated."
- Example: "Write a 3-email reactivation sequence for users who churned last month."
- Often paired with: `att_message_house`, `att_launch_plan`, `att_proof_mining`

## Quality bar

- Every email has one clear CTA and earns the next open.
- The first 2 emails deliver value before any pitch.
- Exit conditions defined for converted/disengaged recipients.
- Subject lines are specific, not clickbait.

## Related workflows
- Content system: `att_message_house` → `att_content_calendar` → `att_content_repurposing`
- Launch sequence: `att_launch_plan` → `att_proof_mining` → `att_thread_writer`
- Proof deployment: `att_proof_mining` → `att_case_study_builder` → `att_social_proof_pack`
