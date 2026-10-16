---
description: Bring docs/technical and docs/handbook in line with the current changes
---

Check whether the documentation still matches the code and setup on this branch.

1. Look at `git diff main...HEAD --stat` and the changed files.
2. For each change, decide which docs are affected:
   - API / data model / architecture / conventions → `docs/technical/`
   - Claude setup, protected files, git/GitHub workflow, repo structure, roles → `docs/handbook/` (use the mapping table at the top of `docs/handbook/README.md`; read only the pages it points to)
   - A decision with team-wide impact → propose a new ADR in `docs/decisions/`
3. Show me a list: doc → what's outdated → proposed change.
4. These are **structural changes** (except `docs/handbook/`): wait for my explicit yes per file before editing.
5. After editing, update the "Last updated" line on each handbook page you changed.
