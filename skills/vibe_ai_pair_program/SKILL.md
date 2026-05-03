---
name: vibe_ai_pair_program
description: "Use AI as a pair programming partner to build, review, and improve code collaboratively."
user-invocable: true
metadata: {"openclaw":{"emoji":"🤖"}}
---

# AI Pair Program

## Purpose
Use AI as a pair programming partner to build, review, and improve code collaboratively. AI pair programming isn't about replacing the developer — it's about having a knowledgeable partner who never gets tired, never judges bad questions, and can explain any concept at your level.

## Use when
Use when you're stuck on a coding problem. Use when you want to understand existing code. Use when you need to add a feature you're not sure how to implement. Use when you want code reviewed.

## Avoid when
Don't blindly copy AI-generated code you don't understand at all. Don't use for security-critical code without review. Don't use when you already know exactly what to write.

## Inputs to gather
- Current code: what are you working on?
- Goal: what do you want to build, fix, or understand?
- Skill level: what do you already know? The AI should explain at your level.
- Constraints: language, framework, performance requirements.
- Specific questions: what exactly are you unsure about?

## Operating rules
- Explain what you want, not how to code it. "I need a function that validates email addresses" not "Write a regex for email."
- Ask for explanations, not just code. "Explain what this function does and why" builds understanding.
- Review the output before using it. AI generates plausible code that may be wrong. Read it, test it, understand it.
- Iterate on the solution. First answer is rarely the best. Refine with follow-up questions.
- Keep a learning log. Write down what you learned from each session. Patterns emerge over time.

## Claude Code tool pattern
- Use `vibe_prompt_to_app` for full app generation.
- Use `vibe_debug_no_code` when AI-generated code has issues.
- Use `eng_code_review_pass` for code review standards.
- Use `vibe_learning_path` for structured learning alongside building.

## Expanded workflow
1. **Describe the task clearly.** What are you building or fixing? What's the context?
2. **Share the relevant code.** Paste the file or function you're working on. Include error messages if applicable.
3. **Ask specific questions.** "How do I add authentication?" gets a generic answer. "How do I add JWT authentication to this Express.js route?" gets useful code.
4. **Review the AI's response.** Does it make sense? Does it work? Test it.
5. **Ask follow-up questions.** "Why did you use that approach?" "What are the edge cases?" "How would I test this?"
6. **Iterate.** Refine the solution. Add error handling. Improve the naming. Add tests.
7. **Document what you learned.** Write a note about the approach, the gotchas, the reasoning.

## Output contract
- Working code solution for the task
- Explanation of the approach and reasoning
- Edge cases and limitations identified
- Learning notes: what you learned and why
- Follow-up improvements to make

## Failure modes to avoid
- Blindly copying code without understanding it — you'll be helpless when it breaks.
- Asking vague questions — specific questions get specific answers.
- Not testing the AI's output — AI generates plausible code that may be subtly wrong.
- No follow-up questions — first answer is rarely optimal.
- No learning log — you'll ask the same questions again next week.

## Handoff cues
- Code solution and explanation.
- Understanding gained: what did you learn?
- Remaining questions or improvements.
- Learning log entry.

## Example invocation
- Slash: `/vibe_ai_pair_program <task>`
- Natural language: "Use vibe_ai_pair_program to use AI as a pair programming partner to build, review, and improve code collaboratively."

## Quality bar
Code is understood, not just copied. Specific questions get specific answers. AI output is tested before use. Follow-up questions improve the solution. Learning is documented for future reference.

## Related workflows
- **AI-assisted development:** `vibe_ai_pair_program` → `vibe_prompt_to_app` → `vibe_debug_no_code` → `vibe_deploy_novice`
- **Learning while building:** `vibe_ai_pair_program` → `vibe_learning_path` → build → review
- **Code review:** `vibe_ai_pair_program` → `eng_code_review_pass` → `solo_rapid_ship`
