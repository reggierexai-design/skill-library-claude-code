#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
PROFILES_DIR = ROOT / "profiles"

def parse_profile(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return re.findall(r'"([a-z0-9_]+)"', text)

def install_skill(src: Path, dst: Path, mode: str) -> None:
    if dst.exists() or dst.is_symlink():
        if dst.is_symlink() or dst.is_file():
            dst.unlink()
        else:
            shutil.rmtree(dst)
    if mode == "copy":
        shutil.copytree(src, dst)
    else:
        dst.symlink_to(src, target_is_directory=True)

def main() -> int:
    parser = argparse.ArgumentParser(description="Install a RexBot Claude Code skill profile.")
    parser.add_argument("profile", help="Profile name without extension, e.g. minimal_core")
    parser.add_argument("--dest", default=".claude/skills", help="Destination skills directory")
    parser.add_argument("--mode", choices=["symlink","copy"], default="symlink")
    args = parser.parse_args()

    profile_path = PROFILES_DIR / f"{args.profile}.json5"
    if not profile_path.exists():
        raise SystemExit(f"Unknown profile: {args.profile}")
    skills = parse_profile(profile_path)
    dest = Path(args.dest).expanduser()
    dest.mkdir(parents=True, exist_ok=True)

    for name in skills:
        src = SKILLS_DIR / name
        if src.is_dir():
            install_skill(src, dest / name, args.mode)

    print({"profile": args.profile, "count": len(skills), "dest": str(dest), "mode": args.mode})
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
