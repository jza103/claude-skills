# claude-skills

My personal collection of [Claude skills](https://docs.claude.com). Each skill is a folder with a `SKILL.md` that tells Claude how to do one kind of job well.

## Skills

<!-- SKILLS-START -->
| Skill | Description |
| --- | --- |
| [interactive-course-builder](skills/interactive-course-builder/) | Build an interactive crash course on any topic as a published page: lessons, analogies, glossary, clickable labs, quizzes, an Ask Claude tutor, and a Docker-ready hands-on lab when it fits. |
<!-- SKILLS-END -->

## Layout

```
claude-skills/
├── README.md
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md          required: frontmatter + instructions
│       ├── references/       optional: longer docs the skill points to
│       ├── scripts/          optional: helper scripts the skill runs
│       └── assets/           optional: templates, fonts, images
├── template/
│   └── SKILL.md              copy this to start a new skill
└── scripts/
    └── update_index.py       regenerates the table above
```

## Adding a skill

1. Copy `template/` to `skills/<skill-name>/` (lowercase, hyphens).
2. Fill in the `name` and `description` in the frontmatter. The description decides when Claude uses the skill, so say when to use it.
3. Write the instructions. Put long reference material in `references/` and link to it from `SKILL.md`.
4. Run `python scripts/update_index.py` to refresh the table in this README.
5. Commit and push.

## Using a skill

Copy or zip the skill folder (the folder itself, with `SKILL.md` at its top level) and add it in Claude under Settings, Capabilities, Skills. For Claude Code, place the folder in `~/.claude/skills/` or a project's `.claude/skills/`.
