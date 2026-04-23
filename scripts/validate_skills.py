#!/usr/bin/env python3
from __future__ import annotations
import json, re, statistics
from collections import Counter
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
PROFILES_DIR = ROOT / "profiles"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
NAME_RE = re.compile(r"^[a-z0-9_]+$")
CATEGORY_BY_PREFIX = {
    "att":"attention","core":"core","eng":"engineering","ops":"operations","prod":"product","res":"research",
    "safe":"safety","ai":"ai","data":"data","doc":"documentation","des":"design","pm":"program","sales":"sales",
    "qa":"quality","sec":"security"
}
PLATFORM = "Claude Code"
REQUIRED_FRONTMATTER = [('name', 'str'), ('description', 'str'), ('user-invocable', 'bool'), ('disable-model-invocation', 'bool')]
REQUIRED_SECTIONS = ['## Purpose', '## Use when', '## Avoid when', '## Inputs to gather', '## Operating rules', '## Claude Code tool pattern', '## Expanded workflow', '## Output contract', '## Failure modes to avoid', '## Handoff cues', '## Example invocation', '## Quality bar']
TYPE_MAP = {"str": str, "bool": bool, "int": int, "float": float}

def parse_skill(path: Path):
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing frontmatter")
    fm = yaml.safe_load(match.group(1))
    if not isinstance(fm, dict):
        raise ValueError("frontmatter must be a mapping")
    return fm, text[match.end():]

def main() -> int:
    errors = []
    stats = Counter()
    word_counts = []
    for skill_dir in sorted([p for p in SKILLS_DIR.iterdir() if p.is_dir()]):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{skill_md}: missing")
            continue
        try:
            fm, body = parse_skill(skill_md)
        except Exception as exc:
            errors.append(f"{skill_md}: {exc}")
            continue
        for key, typ_name in REQUIRED_FRONTMATTER:
            typ = TYPE_MAP[typ_name]
            if key not in fm:
                errors.append(f"{skill_md}: missing {key}")
            elif not isinstance(fm[key], typ):
                errors.append(f"{skill_md}: {key} must be {typ_name}")
        name = fm.get("name", "")
        if isinstance(name, str):
            if not NAME_RE.fullmatch(name):
                errors.append(f"{skill_md}: invalid skill name {name!r}")
            if name != skill_dir.name:
                errors.append(f"{skill_md}: frontmatter name does not match directory name")
        for section in REQUIRED_SECTIONS:
            if section not in body:
                errors.append(f"{skill_md}: missing section {section}")
        stats["skills"] += 1
        if fm.get("user-invocable", True):
            stats["slash_visible"] += 1
        if not fm.get("disable-model-invocation", False):
            stats["model_visible"] += 1
        if fm.get("disable-model-invocation", False):
            stats["slash_first"] += 1
        if fm.get("user-invocable") is False:
            stats["internal_only"] += 1
        word_counts.append(len(body.split()))
        if PLATFORM == "Codex":
            oy = skill_dir / "agents" / "openai.yaml"
            if not oy.exists():
                errors.append(f"{skill_md}: missing agents/openai.yaml")
        # profile refs validated later
    for profile_path in sorted(PROFILES_DIR.glob("*.json5")):
        text = profile_path.read_text(encoding="utf-8")
        for skill_name in re.findall(r'"([a-z0-9_]+)"', text):
            if not (SKILLS_DIR / skill_name).exists():
                errors.append(f"{profile_path}: references missing skill {skill_name}")
    payload = {
        "platform": PLATFORM,
        "skills": stats["skills"],
        "slash_visible": stats["slash_visible"],
        "model_visible": stats["model_visible"],
        "slash_first": stats["slash_first"],
        "internal_only": stats["internal_only"],
        "avg_skill_words": round(statistics.mean(word_counts), 1) if word_counts else 0,
    }
    if errors:
        print("FAIL")
        for item in errors[:100]:
            print(f"- {item}")
        return 1
    print("PASS")
    print(json.dumps(payload, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
