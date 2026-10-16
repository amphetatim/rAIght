# 03 – Protected ("structural") files

**Goal:** everyone may edit the project's context and config files, but **never by accident**. Claude must say *"this is a structural change"* and get an explicit yes first.

## Three layers

| Layer | Where | How strong |
|---|---|---|
| 1. Instruction | `CLAUDE.md`, rule 1 | Soft – Claude follows it, but it's text |
| 2. Hook | `.claude/hooks/protect-structure.sh`, registered in `.claude/settings.json` | Enforced locally – Claude Code shows a confirmation prompt with the warning |
| 3. Review | `.github/CODEOWNERS` + ruleset "Require review from Code Owners" | Enforced on GitHub – the change can't reach `main` without Tim's or Wenxuan's approval. ⚠️ Needs branch protection, see [04](04-git-and-github.md) |

## Which files are protected

| Group | Paths |
|---|---|
| Claude context | every `CLAUDE.md`, everything in `.claude/` |
| Docs that define the product/tech | `docs/technical/**`, `docs/decisions/**`, `docs/concept/**` |
| Repo rules | `.github/**`, `TEAM.md`, `CONTRIBUTING.md`, `README.md`, `.gitignore` |
| Dependencies & build | `package.json`, lockfiles, `pyproject.toml`, `requirements*.txt`, `poetry.lock`, `uv.lock`, `Dockerfile`, `docker-compose*.yml` |

**Not protected:** application code, tests, `docs/handbook/` (so Claude can keep it in sync after a confirmed change), `app/README.md`.

## How the hook works

1. Before Claude runs `Edit`, `Write`, `MultiEdit`, `NotebookEdit` or `Bash`, Claude Code passes the tool call (as JSON) to the hook.
2. The hook works out the file path relative to the repo and checks it against the list.
3. For `Bash`, it checks whether the command **writes/moves/deletes** (`>`, `sed -i`, `tee`, `mv`, `rm`, `cp`, `git rm/mv`) **and** mentions a protected path – or installs a dependency (`npm install`, `pip install`, …).
4. If so, it returns `permissionDecision: "ask"` with a warning text. Claude Code then shows a confirmation prompt with that text.
5. Otherwise it returns nothing and the tool runs normally.

Written in plain bash + `sed` (no `jq`/Python), so it works on macOS, Linux and Windows (Git Bash).

## Limits – be honest about them

- The Bash check is pattern-based. A deliberately obscure command could slip past. That's what layer 1 and layer 3 are for.
- `ls`, `cat`, `grep` on protected files are fine – reading isn't a change.
- If someone starts Claude Code with all permission checks disabled, local layers can be skipped. **Layer 3 (review) is the real safety net.**

## Changing the protected list

The list exists in **three places** – keep them identical:

1. `CLAUDE.md` → rule 1
2. `.claude/hooks/protect-structure.sh` → `is_protected()` and the Bash pattern
3. `.github/CODEOWNERS`

…and update the table above. (Changing any of them is itself a structural change.)

## Testing the hook

In Claude Code: *"Add a comment to CLAUDE.md"* → you should get a confirmation prompt starting with **STRUCTURAL CHANGE**. Answer no.

From a terminal (no Claude needed):

```bash
echo '{"tool_name":"Edit","tool_input":{"file_path":"'"$PWD"'/CLAUDE.md"}}' \
  | CLAUDE_PROJECT_DIR="$PWD" bash .claude/hooks/protect-structure.sh
# → prints JSON with "permissionDecision":"ask"
```

_Last updated: 2026-10-16_
