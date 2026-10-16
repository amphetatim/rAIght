# ADR 0003 – Shared Claude Code context and protected structural files

- **Status:** proposed
- **Date:** 2026-10-16

## Context

All six developers code with Claude Code. Without a shared setup, everyone's Claude works with different assumptions about the product, stack and rules, and context files can be changed by accident in a side task.

## Decision

- Project context lives in the repo: root `CLAUDE.md` (short, loaded every session), folder-level `CLAUDE.md` files, shared `.claude/settings.json`, slash commands and a reviewer subagent.
- Details live in `docs/technical/` and are read on demand. Explanations for humans live in `docs/handbook/`, which Claude doesn't load.
- A defined set of **structural files** is protected by three layers: an instruction in `CLAUDE.md`, a `PreToolUse` hook that forces a confirmation prompt, and `CODEOWNERS` review (enforced once branch protection is active).
- After a confirmed structural change, the matching handbook page is updated in the same PR.

## Consequences

- Same context and workflow for everyone; onboarding = clone + trust the project settings.
- Small friction: editing a protected file always needs a confirmation.
- The protected list is kept in three places (CLAUDE.md, hook, CODEOWNERS) and must stay in sync.
- Until GitHub Pro is active, review is enforced only by agreement.
