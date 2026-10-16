# Team handbook

**For humans.** Explains *how and why* our repo, Claude setup and workflow are organised. Read it when something is unclear.

Claude does **not** load this folder automatically, so it doesn't cost context in every chat. Claude reads only the mapping table below, and only when it makes a structural change, to know which page to update.

## Keeping it up to date

**Rule:** when you change something in the left column, update the page on the right **in the same PR**. Claude does this automatically after a confirmed structural change (CLAUDE.md rule 2), and the PR template asks about it.

<!-- MAPPING TABLE – Claude reads this. Keep it accurate. -->
| If you change … | … update |
|---|---|
| `TEAM.md` (roles, people, pairs) | [01-team-and-roles.md](01-team-and-roles.md) |
| Where we keep what (GitHub / Excel / OneDrive) | [01-team-and-roles.md](01-team-and-roles.md) |
| `CLAUDE.md` (any), `.claude/commands/`, `.claude/agents/` | [02-claude-setup.md](02-claude-setup.md) |
| `.claude/settings.json` (permissions, hooks) | [02-claude-setup.md](02-claude-setup.md), [03-protected-files.md](03-protected-files.md) |
| `.claude/hooks/protect-structure.sh` or the protected-file list in `CLAUDE.md` | [03-protected-files.md](03-protected-files.md) |
| `CONTRIBUTING.md`, `.github/` (templates, CODEOWNERS, workflows), branch rules, rulesets | [04-git-and-github.md](04-git-and-github.md) |
| Folder structure (new top-level folder, new `app/` sub-folder) | [05-repo-structure.md](05-repo-structure.md) |
| `docs/technical/conventions.md` | nothing – it's self-explaining; just keep it correct |
<!-- END MAPPING TABLE -->

## Pages

| Page | Read it if you're wondering … |
|---|---|
| [01 – Team and roles](01-team-and-roles.md) | Who does what? Why GitHub and not Excel? |
| [02 – Claude setup](02-claude-setup.md) | How does Claude get the same context for everyone? What are `/start-issue` and `/pr-ready`? |
| [03 – Protected files](03-protected-files.md) | Why does Claude ask "structural change – confirm?" and how does it work? |
| [04 – Git and GitHub](04-git-and-github.md) | Branches, PRs, CODEOWNERS, protecting `main`, permissions |
| [05 – Repo structure](05-repo-structure.md) | What's in which folder and why? |

_Last updated: 2026-10-16_
