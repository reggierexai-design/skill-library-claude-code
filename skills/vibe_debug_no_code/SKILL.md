---
name: vibe_debug_no_code
description: "Debug AI-generated code when you can't read the code yourself."
user-invocable: true
metadata: {"openclaw":{"emoji":"🔧"}}
---

# Debug No Code

## Purpose
Debug AI-generated code when you can't read the code yourself. Vibe coders don't need to understand every line — but they do need to know how to systematically identify and fix problems using AI assistance, error messages, and structured debugging.

## Use when
Use when your AI-generated app throws an error. Use when something works in development but breaks in production. Use when the output doesn't match what you asked for.

## Avoid when
Don't use when you can read and fix the code yourself — that's faster. Don't use for security vulnerabilities — get professional review for those.

## Inputs to gather
- Error message: the exact text of any error, warning, or unexpected behavior.
- What you expected vs what happened: be specific.
- Recent changes: what prompt or action caused the issue?
- Environment details: browser, Node version, framework version.
- Steps to reproduce: what do you click/type to trigger the problem?

## Operating rules
- Copy the exact error message. Don't paraphrase — the specific error text is the fastest path to the fix.
- Describe the expected behavior and the actual behavior separately. "It should show X but it shows Y."
- Check the console. Browser dev tools console and terminal output have the answers. Learn to find them.
- One issue at a time. Don't try to fix three bugs in one prompt. Fix one, test, then fix the next.
- If the AI can't fix it in 3 attempts, try a different approach. Rephrase the problem, search for the error message, or ask for a simplified version.

## Claude Code tool pattern
- Use `eng_debug_systematically` for structured debugging methodology.
- Use `vibe_ai_pair_program` for collaborative debugging with AI.
- Use `eng_bug_triage` for prioritizing multiple issues.

## Expanded workflow
1. **Capture the exact error.** Copy the error message verbatim. Screenshot if needed.
2. **Describe expected vs actual behavior.** "When I click Submit, the form should save and show a success message. Instead, I get a 500 error."
3. **Identify recent changes.** What was working before? What did you change? Revert if needed.
4. **Check the console output.** Browser F12 → Console tab. Or terminal output. Look for red text.
5. **Search for the error message.** Copy the error into your AI tool or web search. Others have likely seen it.
6. **Write a fix prompt.** Include the error, the code file, and what you expected. "In app.js line 42, I get [exact error]. The function should [expected behavior]. Fix it."
7. **Test the fix.** Does it solve the problem? Does it break anything else?
8. **If 3 attempts fail, restructure.** Ask for a minimal reproduction, a different approach, or a simplified version that avoids the issue.

## Output contract
- Issue description: exact error, expected behavior, actual behavior
- Debugging steps taken and results
- Fix applied (if resolved)
- Workaround (if unresolved)
- Prevention: what to do differently next time

## Failure modes to avoid
- Paraphrasing error messages — the exact text matters for diagnosis.
- Trying to fix multiple issues at once — fix one, test, then fix the next.
- Not checking the console — the answer is usually in the error output.
- Repeatedly asking the AI the same question — if it didn't work the first 3 times, rephrase.
- Making changes without testing — compounding errors.

## Handoff cues
- Issue status: resolved, workaround applied, or needs different approach.
- Fix description or workaround details.
- Prevention notes for similar issues.

## Example invocation
- Slash: `/vibe_debug_no_code <task>`
- Natural language: "Use vibe_debug_no_code to debug AI-generated code when you can't read the code yourself."

## Quality bar
Error messages are captured verbatim. Expected vs actual behavior is clearly described. Console output is checked. Fixes are tested before moving on. If 3 AI attempts fail, the approach is restructured.

## Related workflows
- **Debug flow:** `vibe_debug_no_code` → `eng_debug_systematically` → fix → test → `vibe_deploy_novice`
- **AI-assisted debugging:** `vibe_debug_no_code` → `vibe_ai_pair_program` → `eng_bug_triage`
- **Ship cycle:** `vibe_prompt_to_app` → `vibe_debug_no_code` → `solo_rapid_ship`
