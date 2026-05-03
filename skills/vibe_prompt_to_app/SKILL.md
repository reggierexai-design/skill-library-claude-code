---
name: vibe_prompt_to_app
description: "Turn a natural language prompt into a working app prototype using AI code generation tools."
user-invocable: true
---

# Prompt To App

## Purpose
Turn a natural language prompt into a working app prototype using AI code generation tools. This is the vibe coder's core workflow — describe what you want, get something running, then iterate. The key is knowing how to prompt effectively, evaluate the output, and iterate toward a real product.

## Use when
Use when you have an app idea but no code yet. Use when you want to quickly test a concept. Use when you need a prototype to show users or investors.

## Avoid when
Don't use for production-ready code on the first pass — this is a prototype workflow, not a deployment workflow. Don't use when the idea is so vague that you can't describe it in specific terms.

## Inputs to gather
- App concept: what does it do and for whom?
- Core user flow: what's the primary action a user takes?
- Technical constraints: platform (web, mobile, desktop), frameworks, hosting.
- Design preferences: look and feel, reference apps.
- Data requirements: what data does the app need and where does it come from?

## Operating rules
- Start with the core user flow, not the full feature set. One path through the app, working end to end.
- Be specific in your prompts. "Build a todo app" gives you a generic todo app. "Build a todo app for construction foremen that tracks tasks by job site with photo attachments" gives you something useful.
- Iterate, don't regenerate. When the output isn't right, describe what to change specifically. Don't start over from scratch.
- Test immediately. Don't write 50 prompts before running the code. Write one, test it, fix it, then add.
- Save working versions before making changes. AI code gen can break things that were working.

## Claude Code tool pattern
- Use `vibe_ai_pair_program` for collaborative coding with AI assistance.
- Use `vibe_debug_no_code` when the generated code has issues.
- Use `vibe_prototype_sprint` for structured rapid prototyping.

## Expanded workflow
1. **Define the core user flow.** What's the one thing a user does in this app? Describe it step by step.
2. **Write the initial prompt.** Include: purpose, core flow, tech stack, key screens, data model.
3. **Generate the first version.** Run the prompt through your AI code generation tool.
4. **Test immediately.** Does it run? Does the core flow work? Note what's broken.
5. **Write fix prompts.** Describe each issue specifically. "The login button doesn't redirect to the dashboard" not "fix the login."
6. **Iterate on design.** Once the core flow works, improve the look and feel with specific design prompts.
7. **Add secondary features.** One at a time, testing after each addition.

## Output contract
- Working prototype with core user flow functional
- Prompt history: every prompt used and the result
- Known issues list: what's broken and what's missing
- Next iteration priorities

## Failure modes to avoid
- Vague prompts — the more specific you are, the better the output.
- Regenerating instead of iterating — small targeted fixes beat starting over.
- Not testing between prompts — compounding errors that become impossible to debug.
- No version saving — AI can break working code while adding features.
- Building too much before testing the core flow.

## Handoff cues
- Working prototype URL or local path.
- Core flow status: working, partially working, broken.
- Prompt history for the current session.
- Next features to add or issues to fix.

## Example invocation
- Slash: `/vibe_prompt_to_app <task>`
- Natural language: "Use vibe_prompt_to_app to turn a natural language prompt into a working app prototype using AI code generation tools."

## Quality bar
Core user flow works end to end. Every prompt is specific and actionable. Code is tested after each change. Working versions are saved before new additions. The prototype demonstrates the concept clearly.

## Related workflows
- **App creation flow:** `vibe_prompt_to_app` → `vibe_debug_no_code` → `vibe_deploy_novice` → `vibe_prototype_sprint`
- **AI-assisted development:** `vibe_prompt_to_app` → `vibe_ai_pair_program` → `vibe_learning_path`
- **Rapid prototyping:** `vibe_prototype_sprint` → `vibe_prompt_to_app` → `solo_rapid_ship`
