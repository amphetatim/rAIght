# 02 – Claude setup

We all code with **Claude Code**. The goal: every developer's Claude gets **the same project context and rules**, without anyone copying prompts around.

## How it works: everything is in the repo

Claude Code reads certain files automatically. Because they're committed, everyone who pulls `main` has the same setup.

| File | Loaded | Purpose |
|---|---|---|
| `CLAUDE.md` (root) | **Every session** in this repo | Project summary, stack, commands, map of the repo, rules for Claude |
| `app/CLAUDE.md` (and later `app/frontend/CLAUDE.md` etc.) | Only when Claude works in that folder | Rules specific to that part of the code |
| `.claude/settings.json` | Every session | Shared permissions (e.g. never read `.env`, never force-push) and the protection hook |
| `.claude/commands/*.md` | When you type the command | Shared slash commands |
| `.claude/agents/reviewer.md` | When used (e.g. by `/pr-ready`) | Review subagent with our checklist |
| `CLAUDE.local.md`, `.claude/settings.local.json` | Only for you | Personal notes/overrides – **git-ignored**, never shared |

Everything else (`docs/`) is **not** loaded automatically. `CLAUDE.md` tells Claude *where* to look, and Claude reads those files only when the task needs them. That keeps every chat lean.

### Why `CLAUDE.md` is short

It's loaded into every session. The longer it gets, the less reliably Claude follows each rule, and the more context it uses. Rule of thumb: **under ~150 lines**. Details belong in `docs/technical/` with a pointer from `CLAUDE.md`.

### Why the handbook is separate

This handbook explains *why* things are set up the way they are – useful for us, noise for Claude. So `CLAUDE.md` tells Claude not to read it, except the mapping table in [README.md](README.md) when a structural change needs a handbook update.

## Shared slash commands

| Command | What it does |
|---|---|
| `/start-issue 12` | Fetches issue #12 (via `gh` or you paste it), creates the branch, reads only the relevant docs, proposes a plan and **waits for your OK** |
| `/pr-ready` | Runs lint and tests, runs the reviewer subagent on your diff, checks docs and commit messages, drafts the PR text, asks before pushing, opens a **draft** PR |
| `/update-docs` | Compares your branch with `docs/technical/` and `docs/handbook/` and proposes updates |

`gh` (GitHub CLI) is optional but makes these smoother: `brew install gh` then `gh auth login`.

## Reviewer subagent

`.claude/agents/reviewer.md` reviews a diff against [conventions.md](../technical/conventions.md) – correctness, scope, project rules (e.g. no AI in metrics), security, tests, maintainability, docs. It reports; it doesn't edit. It's a pre-check, **not a replacement** for the human review on the PR.

## Shared permissions (`.claude/settings.json`)

- **Denied:** reading `.env` files; `git push --force`; pushing directly to `main`.
- **Hook:** `protect-structure.sh` runs before every edit and asks for confirmation on structural files – see [03](03-protected-files.md).

Personal permission tweaks (e.g. always allowing `npm test`) go in `.claude/settings.local.json`, not the shared file.

## Good habits

- **One task per session.** Use `/clear` when switching to an unrelated task.
- **Plan first** for anything bigger than a small fix (`/start-issue` does this; or press Shift+Tab for plan mode).
- **Read what Claude wrote** before committing. You own the code.
- If Claude keeps making the same mistake, the fix belongs in `CLAUDE.md` – propose it (it's a structural change, so it goes through review).

## First-time setup per developer

1. Install Claude Code and log in.
2. `git clone` the repo, open it in a terminal, run `claude`.
3. On first start, Claude Code asks whether to trust the project's settings/hooks → **yes**.
4. Test once: ask Claude to *"add a line to CLAUDE.md"* → it must warn about a structural change and ask. Say no.

_Last updated: 2026-10-16_
