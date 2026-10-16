---
description: Start work on a GitHub issue – branch, context, plan
argument-hint: <issue-number>
---

Start work on issue #$ARGUMENTS.

1. Get the issue: run `gh issue view $ARGUMENTS` if the GitHub CLI is available. If not, ask me to paste the issue title, description and acceptance criteria.
2. Check `git status`. If there are uncommitted changes, stop and ask what to do with them.
3. Update `main` (`git checkout main && git pull`) and create a branch following CONTRIBUTING.md: `<type>/$ARGUMENTS-<short-name>` (type = feature, fix, docs or spike – pick from the issue).
4. Read only the context this issue needs: the relevant `CLAUDE.md` in `app/`, and from `docs/technical/` and `docs/concept/` only what the issue touches. Don't read `docs/handbook/`.
5. Give me a short plan:
   - what you'll change (files) and why
   - which acceptance criterion each step covers
   - which **structural files** (CLAUDE.md rule 1) would be touched, if any
   - how it will be tested
   - open questions
6. **Wait for my OK** before writing code.
