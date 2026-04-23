# RexBot Claude Code Skill Library v0.6

**RexBot / Rex Hub community release for Claude Code.**

This is the Claude Code-specific port of the RexBot generalist skill library. It keeps the same deep playbooks, profiles, and category coverage as the OpenClaw release, but the docs, install paths, examples, and packaging are rewritten for Claude Code.

## What is in this pack

- **185 skills**
- **22 curated profiles**
- **21 internal orchestration or safety skills**
- **76 skills intended for model-side discovery**
- **109 slash-first specialist skills**
- **619.4 average words per skill**

## Platform fit

- Claude Code reads skills from `.claude/skills` in a project or `~/.claude/skills` for personal use.
- Claude Code can invoke skills implicitly from descriptions or explicitly via `/skill-name`.
- Claude Code supports `user-invocable`, `disable-model-invocation`, and `allowed-tools` in skill frontmatter.
- Project-wide standing guidance belongs in `CLAUDE.md`; skills are better for reusable workflows that should load on demand.

## Quick start

1. Put this library somewhere stable on disk.
2. Install a profile with `python scripts/install_profile.py minimal_core`.
3. Start with a narrow profile before you install the whole catalog.
4. Keep repo-wide standing guidance in `CLAUDE.md` or an equivalent workspace note, and use skills for repeatable workflows.

## Invocation

- Explicit use: `/skill-name`
- Discovery: Type `/` and choose a skill, or ask Claude directly.

## Recommended rollout

- Start with `minimal_core`
- Add one domain profile such as `builder_engineering`, `docs_support`, `research_operator`, or `security_quality`
- Treat `full_library` as a power-user profile, not a default

## Important files

- `START_HERE.md`
- `TRAINING_MANUAL.md`
- `SYSTEM_OVERVIEW.md`
- `DEPLOYMENT_GUIDE.md`
- `AGENT_INTEGRATION_GUIDE.md`
- `PROFILE_SELECTION_GUIDE.md`
- `SKILL_ROUTING_GUIDE.md`
- `AUTHORING_GUIDE.md`
- `CATALOG.md`
- `CATALOG_DETAILED.md`

## Attribution

- Publisher: **RexBot / Rex Hub**
- Homepage: `https://reggierexai-design.github.io/rexhub/`
- Status: community-maintained, not an official Claude Code bundle
