---
description: Check the branch is ready for a pull request and draft the PR text
---

Prepare the current branch for a pull request.

1. Confirm we're not on `main`. If we are, stop.
2. Run lint/format (commands in the root `CLAUDE.md`, once defined) and remind me to click through the affected demo-script steps. Report failures and stop – don't open a PR with failing checks.
3. Review the diff against `main` (`git diff main...HEAD`) using the **reviewer** subagent (`.claude/agents/reviewer.md`). Summarise its findings and fix what I approve.
4. Docs check:
   - Did the sample-data format or page structure change? → `docs/technical/` must be updated.
   - Were structural files changed? → list them; check that the matching `docs/handbook/` page is updated (mapping table in `docs/handbook/README.md`).
5. Check commit messages follow `docs/technical/conventions.md` (Conventional Commits).
6. Draft the PR description using `.github/pull_request_template.md`, including `Closes #<issue>`, how to test, and the filled checklist.
7. Ask me before pushing. Then push the branch and, if `gh` is available, open the PR as **draft** (`gh pr create --draft`). Otherwise give me the text to paste.
