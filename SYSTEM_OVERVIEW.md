# System Overview

## Design goal

This pack gives Claude Code a large, reusable workflow library without turning every session into a giant always-on prompt.

## Core design choices

- Each skill is a directory with `SKILL.md`
- The skill descriptions stay compact so the platform can discover them efficiently
- The skill bodies are deep playbooks that only matter once the skill is chosen
- Profiles exist to keep installs selective
- Safety, quality, and security skills sit beside domain skills rather than after the fact

## Library anatomy

- `skills/`: the reusable skill directories
- `profiles/`: curated skill sets
- `examples/`: sample repo guidance and setup snippets
- `scripts/`: validation and install helpers
- `CATALOG*.md`: skill indexes

## How to think about the system

- Put repo conventions in `CLAUDE.md`
- Put reusable methods in skills
- Use profiles to decide which skill surface a given user or repository should see
- Keep internal or high-risk workflows out of casual daily usage unless they are clearly needed
