#!/usr/bin/env bash
# PreToolUse hook: asks for explicit confirmation before Claude changes a structural file.
# Explained in docs/handbook/03-protected-files.md – keep both in sync.
#
# Input:  hook JSON on stdin (tool_name, tool_input.file_path / tool_input.command)
# Output: JSON with permissionDecision "ask" for structural files; nothing otherwise.
# No jq/python needed – plain bash + sed, so it runs on macOS, Linux and Git Bash (Windows).

input="$(cat)"

# --- Protected paths (relative to repo root). Bash `case` globs: * also matches "/". ---
is_protected() {
  case "$1" in
    CLAUDE.md|*/CLAUDE.md) return 0 ;;
    .claude/*) return 0 ;;
    docs/technical/*|docs/decisions/*|docs/concept/*) return 0 ;;
    .github/*) return 0 ;;
    TEAM.md|CONTRIBUTING.md|README.md|.gitignore) return 0 ;;
    package.json|*/package.json|package-lock.json|*/package-lock.json) return 0 ;;
    pnpm-lock.yaml|*/pnpm-lock.yaml|yarn.lock|*/yarn.lock) return 0 ;;
    pyproject.toml|*/pyproject.toml|requirements*.txt|*/requirements*.txt) return 0 ;;
    poetry.lock|*/poetry.lock|uv.lock|*/uv.lock) return 0 ;;
    Dockerfile|*/Dockerfile|docker-compose*.yml|*/docker-compose*.yml) return 0 ;;
  esac
  return 1
}

ask() {
  # $1 = what is being changed
  local reason="STRUCTURAL CHANGE: ${1}. This file is protected (see CLAUDE.md, rule 1). Only confirm if you explicitly want this change. If it affects something docs/handbook/ describes, the matching handbook page must be updated too."
  reason="${reason//\\/\\\\}"; reason="${reason//\"/\\\"}"
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"%s"}}\n' "$reason"
  exit 0
}

tool="$(printf '%s' "$input" | sed -n 's/.*"tool_name"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n1)"
root="${CLAUDE_PROJECT_DIR:-$(pwd)}"

case "$tool" in
  Edit|Write|MultiEdit|NotebookEdit)
    path="$(printf '%s' "$input" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n1)"
    [ -z "$path" ] && path="$(printf '%s' "$input" | sed -n 's/.*"notebook_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n1)"
    [ -z "$path" ] && exit 0
    path="${path//\\\\//}"          # Windows: C:\\x\\y -> C:/x/y
    rootn="${root//\\//}"
    rel="${path#"$rootn"/}"
    rel="${rel#./}"
    is_protected "$rel" && ask "$tool on $rel"
    ;;
  Bash)
    cmd="$(printf '%s' "$input" | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\(.*\)".*/\1/p' | head -n1)"
    # Only commands that write/move/delete AND mention a protected location
    if printf '%s' "$cmd" | grep -Eq '(>|sed -i|tee |mv |rm |cp |git rm|git mv|npm (install|i |uninstall|add)|pnpm add|yarn add|pip install|uv add|poetry add)'; then
      if printf '%s' "$cmd" | grep -Eq '(CLAUDE\.md|\.claude/|docs/(technical|decisions|concept)/|\.github/|TEAM\.md|CONTRIBUTING\.md|README\.md|\.gitignore|package(-lock)?\.json|pnpm-lock|yarn\.lock|pyproject\.toml|requirements.*\.txt|poetry\.lock|uv\.lock|Dockerfile|docker-compose|npm (install|i |uninstall|add)|pnpm add|yarn add|pip install|uv add|poetry add)'; then
        ask "Bash command touching protected files or dependencies"
      fi
    fi
    ;;
esac
exit 0
