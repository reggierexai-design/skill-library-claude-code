# Training Manual

## Goal

Teach an operator or setup how to use the RexBot skill library well inside Claude Code.

## Operating principles

- Keep always-on instructions in `CLAUDE.md`
- Keep reusable workflows in skills
- Start with a narrow profile
- Prefer explicit invocation for new or high-risk workflows
- Expand the installed surface only after the current setup proves useful

## First-week routine

1. Install `minimal_core`
2. Add one specialist profile
3. Invoke skills explicitly and inspect whether the output shape matches the intended workflow
4. Remove skills that never trigger or create confusion
5. Add repo guidance only for facts or rules that should apply to every task

## How to train a team setup

- Pick one baseline profile for everyone
- Add one or two role-specific profiles
- Commit the selected skills or symlink instructions into repo docs
- Store team rules in `CLAUDE.md`
- Keep release, QA, security, and deployment workflows explicit

## Common mistake

Do not dump the whole library into every environment just because it exists. The point of the library is reusable depth with selective loading, not permanent prompt inflation.
