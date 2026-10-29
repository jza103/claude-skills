#!/usr/bin/env python3
"""Regenerate the skills table in README.md from each skill's SKILL.md frontmatter."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"
START, END = "<!-- SKILLS-START -->", "<!-- SKILLS-END -->"


def read_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip().strip("\"'")
    return fields


def main():
    rows = []
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        meta = read_frontmatter(skill_md)
        folder = skill_md.parent.name
        name = meta.get("name") or folder
        desc = meta.get("description", "").replace("|", "\\|")
        if not desc:
            print(f"warning: {folder} has no description", file=sys.stderr)
        rows.append(f"| [{name}](skills/{folder}/) | {desc} |")

    table = "| Skill | Description |\n| --- | --- |\n" + "\n".join(rows)
    readme = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(readme):
        sys.exit(f"README.md is missing the {START} / {END} markers")
    README.write_text(pattern.sub(f"{START}\n{table}\n{END}", readme), encoding="utf-8")
    print(f"Indexed {len(rows)} skill(s).")


if __name__ == "__main__":
    main()
