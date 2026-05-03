---
name: legal_cookie_consent
description: "Implement cookie consent and tracking compliance that meets GDPR, CCPA, and ePrivacy requirements."
user-invocable: true
metadata: {"openclaw":{"emoji":"🍪"}}
---

# Cookie Consent

## Purpose
Implement cookie consent and tracking compliance. Cookie consent isn't just a banner — it's a system that must respect user choices across every tracking technology. A consent banner that doesn't honor choices is a compliance violation, not a compliance solution.

## Use when
Use when adding new tracking, analytics, or advertising scripts. Use when expanding to EU/UK markets. Use when your current consent implementation was "set up and forgotten."

## Avoid when
Don't use a "consent wallpaper" that auto-accepts all cookies — that's not consent. Don't implement consent without honoring the choices technically.

## Inputs to gather
- Current tracking technologies: analytics, advertising pixels, session cookies, third-party embeds.
- Consent management platform: what tool manages consent? Or do you need one?
- Jurisdiction requirements: GDPR (opt-in), CCPA (opt-out), ePrivacy Directive.
- Cookie categories: strictly necessary, performance, functionality, targeting/advertising.
- Existing consent rates: accept vs reject percentages?

## Operating rules
- Consent must be freely given, specific, informed, and unambiguous. Pre-ticked boxes don't count under GDPR.
- Reject must be as easy as accept. Same number of clicks, same visual prominence. A tiny "reject" link doesn't pass.
- Cookie categories must be granular. Users should be able to accept/reject per category, not just all-or-nothing.
- Consent choices must be honored technically. Rejected scripts must not fire. Period.
- Document consent choices with timestamps. If you can't prove you had consent, you didn't have consent.

## Claude Code tool pattern
- Use `legal_privacy_policy` to ensure the policy reflects cookie practices.
- Use `safe_pii_minimization` to reduce tracking to what's truly necessary.
- Use `sec_logging_exposure_check` to verify consent choices are logged properly.

## Expanded workflow
1. **Inventory all tracking technologies.** Every cookie, pixel, script, and embed. If it tracks, it goes in the inventory.
2. **Categorize each tracker.** Strictly necessary, performance, functionality, targeting. Each category gets a different consent treatment.
3. **Choose a consent management platform.** Or audit the current one. Does it support granular consent and technical enforcement?
4. **Implement granular consent.** Users can accept/reject per category. Not just "accept all" or "reject all."
5. **Make reject as easy as accept.** Same clicks, same prominence. If accept is one button, reject is one button.
6. **Wire consent choices to tracking scripts.** Rejected categories must not fire. This is technical, not visual.
7. **Log consent choices with timestamps.** User ID, choice, timestamp, version of consent banner.
8. **Test the full flow.** Accept, reject, partial — verify each choice is respected technically, not just visually.

## Output contract
- Cookie/tracker inventory with categories
- Consent management platform configuration
- Consent flow: accept, reject, partial — all functional
- Technical enforcement: rejected scripts don't fire
- Consent logging: timestamps and choices recorded

## Failure modes to avoid
- Auto-accepting all cookies — that's a dark pattern, not consent.
- Making reject harder than accept — not compliant under GDPR.
- No granular categories — all-or-nothing isn't specific enough for GDPR.
- Consent not honored technically — rejected scripts still fire behind the banner.
- No consent logging — you can't prove compliance if challenged.

## Handoff cues
- Cookie inventory with categories and consent status.
- Consent flow verified: accept, reject, partial all work.
- Technical enforcement confirmed: rejected scripts don't fire.
- Consent logging operational with timestamps.

## Example invocation
- Slash: `/legal_cookie_consent <task>`
- Natural language: "Use legal_cookie_consent to implement cookie consent and tracking compliance that meets GDPR, CCPA, and ePrivacy requirements."

## Quality bar
Consent banner honors all choices technically, not just visually. Reject is as easy as accept. Cookie categories are granular and independently controllable. Consent choices are logged with timestamps. No tracking fires before consent is given.

## Related workflows
- **Tracking compliance:** `legal_cookie_consent` → `legal_privacy_policy` → `safe_pii_minimization`
- **Consent implementation:** `legal_cookie_consent` → `sec_logging_exposure_check` → `eng_release_readiness`
- **Privacy audit:** `safe_pii_minimization` → `legal_cookie_consent` → `legal_terms_review`
