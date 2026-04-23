# Compatibility

This pack targets **Claude Code**.

## Assumptions

- Skills are discovered from `.claude/skills` and `~/.claude/skills`
- `SKILL.md` frontmatter supports `name`, `description`, `user-invocable`, and `disable-model-invocation`
- Project-wide standing guidance belongs in `CLAUDE.md`

## Port notes

This port removes OpenClaw-specific metadata and keeps Claude Code-compatible invocation controls in frontmatter.
