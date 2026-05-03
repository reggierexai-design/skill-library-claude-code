---
name: vibe_learning_path
description: "Build a structured learning path that teaches you what you need as you build, not before."
user-invocable: true
---

# Learning Path

## Purpose
Build a structured learning path that teaches you what you need as you build, not before. The biggest trap for new developers is trying to learn everything before building anything. You end up with tutorial knowledge and no products. Learn by doing, but do it with structure.

## Use when
Use when you're learning to code and building simultaneously. Use when you feel overwhelmed by how much there is to learn. Use when tutorial hell has you watching videos but never shipping.

## Avoid when
Don't use when you need formal CS education for a specific job requirement. Don't use as a substitute for actually building — the path supports building, it doesn't replace it.

## Inputs to gather
- Current skill level: what can you already do?
- Current project: what are you building right now?
- Knowledge gaps: what's blocking you from building what you want?
- Learning style: video, text, interactive, pair programming?
- Time available: how many hours per week for learning vs building?

## Operating rules
- Learn just enough to unblock yourself, then build. Don't study a topic for 5 hours when 30 minutes gets you building again.
- Build first, learn second. Start with what you want to make, then learn the skills it requires. This keeps motivation high.
- Document what you learn. A learning log turns scattered knowledge into retrievable reference.
- Revisit fundamentals at increasing depth. First pass: "what is a variable?" Second pass: "how does memory allocation work?" Each pass goes deeper.
- Teach what you learn. Explaining a concept to someone else (or a rubber duck) is the fastest way to find gaps in your understanding.

## Claude Code tool pattern
- Use `vibe_ai_pair_program` for learning through collaborative coding.
- Use `vibe_prompt_to_app` for project-based learning.
- Use `vibe_debug_no_code` for learning through debugging.

## Expanded workflow
1. **Identify your current project.** What are you building? This drives what you need to learn.
2. **Map the knowledge gaps.** What's blocking you right now? Not next month — right now.
3. **Prioritize by blocking level.** What prevents you from shipping? Learn that first. Everything else can wait.
4. **Choose one resource per gap.** Don't collect 10 tutorials. Pick one, finish it, move on.
5. **Learn the minimum, then build.** 30 minutes of focused learning > 3 hours of passive watching.
6. **Document what you learned.** Learning log: concept, explanation in your own words, code example, gotchas.
7. **Build with the new knowledge.** Apply it immediately in your project. If you can't apply it, you didn't learn it.
8. **Review and deepen.** Come back to fundamentals at increasing depth as your projects get more complex.

## Output contract
- Current project and its knowledge requirements
- Prioritized learning gaps: blocking now vs later
- One resource per gap (not ten)
- Learning log: concepts, explanations, examples
- Build-examples for each learned concept

## Failure modes to avoid
- Tutorial hell — watching endless tutorials without building anything.
- Learning everything before starting — you'll never feel ready. Start now.
- No learning log — you'll forget what you learned and re-learn it repeatedly.
- Too many resources — one good resource beats ten mediocre ones.
- Learning without applying — if you can't use it in your project within a week, it's not the right time.

## Handoff cues
- Current knowledge gaps and their priority.
- What you learned this week and how you applied it.
- Next learning priority and the resource you'll use.
- Learning log entries for reference.

## Example invocation
- Slash: `/vibe_learning_path <task>`
- Natural language: "Use vibe_learning_path to build a structured learning path that teaches you what you need as you build, not before."

## Quality bar
Learning is driven by current project needs. Each gap has one focused resource. Knowledge is applied within a week of learning. Learning log documents concepts in your own words. Tutorial consumption is balanced with building output.

## Related workflows
- **Learn-and-build cycle:** `vibe_learning_path` → `vibe_ai_pair_program` → build → `vibe_debug_no_code` → learn more
- **Project-driven learning:** `vibe_prompt_to_app` → `vibe_learning_path` → fill gaps → continue building
- **Skill development:** `vibe_learning_path` → `vibe_prototype_sprint` → apply new skills → assess gaps
