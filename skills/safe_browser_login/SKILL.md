---
name: safe_browser_login
description: "Handle authenticated browsing without taking custody of user credentials or live account secrets."
user-invocable: false
disable-model-invocation: false
---


# Browser Login Safety

## Purpose
- Handle authenticated browsing without taking custody of user credentials or live account secrets.
- This is a **safety specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when a task requires logging into a site, attaching to an existing user browser session, or working inside an authenticated web app.
- The main bottleneck is best solved through safety work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not use for public web pages that do not require sign-in.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- What sensitive asset, account, production system, or public claim is in scope.
- Who could be impacted if the action is wrong, leaked, or partially completed.
- What approvals, redactions, or safer alternatives exist before proceeding.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Manual user login is the default safe path.
- Do not ask the user to paste passwords, TOTP codes, session cookies, or recovery codes into chat.
- Stay inside the managed agent browser unless there is a clear reason to attach to a user profile.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Prefer observation, redaction, and user-mediated actions over direct handling of secrets or live credentials.
- Use the browser or shell only after the risk boundary is explicit and the action is reversible or approved.
- When a task crosses into high-impact territory, slow the workflow down and state the approval gate clearly.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Identify whether login is actually required.
2. Pick the safest browser profile and login path.
3. Proceed with the task after the user completes any manual auth step.
4. Avoid storing or repeating any auth material.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Login requirement
- Safe browser path
- Any manual user step
- Post-login execution note
- Risk summary with the protected surface named plainly.
- Approved handling path, redaction path, or stop-condition.

## Failure modes to avoid
- Treating convenience as a reason to bypass secret hygiene or approval paths.
- Repeating sensitive values in chat, logs, artifacts, or examples.
- Conflating 'possible' with 'safe enough to do now'.
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Primary use: internal or autonomous routing when the task pattern matches.
- Natural language: "Use browser Login Safety to handle authenticated browsing without taking custody of user credentials or live account secrets."
- Example: "Check the risky parts before we publish, deploy, or log in."
- Example: "Tell me the safest way to continue without exposing credentials or personal data."
- Often paired with: `core_risk_gate`, `safe_secret_hygiene`, `safe_high_impact_changes`

## Quality bar
- The agent should never become the storage layer for account credentials.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.
