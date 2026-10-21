"""Run-log validation and R1 metrics utilities."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json
from typing import Any

ALLOWED_OUTCOMES = {"success", "escalated", "failed"}
EXPECTED_AGENT_IDS = {
    "agent_application_status",
    "agent_document_check",
    "agent_offer_letters",
    "agent_interview_scheduling",
}


def load_run_logs(path: str | Path) -> list[dict[str, Any]]:
    with Path(path).open(encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, list):
        raise ValueError("Run-log dataset must be a JSON array")

    return data


def validate_run_logs(records: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []

    for index, record in enumerate(records):
        prefix = f"run[{index}]"
        if not isinstance(record, dict):
            errors.append(f"{prefix}: record must be an object")
            continue

        for field in ("id", "agent_id", "started_at", "tokens_in", "tokens_out", "outcome", "steps"):
            if field not in record:
                errors.append(f"{prefix}: missing field '{field}'")

        if not isinstance(record.get("id"), str) or not record.get("id"):
            errors.append(f"{prefix}: 'id' must be a non-empty string")

        if not isinstance(record.get("agent_id"), str) or not record.get("agent_id"):
            errors.append(f"{prefix}: 'agent_id' must be a non-empty string")

        if not isinstance(record.get("started_at"), str) or not record.get("started_at"):
            errors.append(f"{prefix}: 'started_at' must be a non-empty ISO-8601 string")

        for token_field in ("tokens_in", "tokens_out"):
            value = record.get(token_field)
            if not isinstance(value, int) or value < 0:
                errors.append(f"{prefix}: '{token_field}' must be a non-negative integer")

        if record.get("outcome") not in ALLOWED_OUTCOMES:
            errors.append(f"{prefix}: 'outcome' must be one of {sorted(ALLOWED_OUTCOMES)}")

        steps = record.get("steps")
        if not isinstance(steps, list) or not steps:
            errors.append(f"{prefix}: 'steps' must be a non-empty array")
            continue

        for step_index, step in enumerate(steps):
            step_prefix = f"{prefix}.steps[{step_index}]"
            if not isinstance(step, dict):
                errors.append(f"{step_prefix}: step must be an object")
                continue

            if not isinstance(step.get("order"), int) or step.get("order") <= 0:
                errors.append(f"{step_prefix}: 'order' must be a positive integer")

            if not isinstance(step.get("tool"), str) or not step.get("tool"):
                errors.append(f"{step_prefix}: 'tool' must be a non-empty string")

    return errors


def compute_total_tokens_per_agent(records: list[dict[str, Any]]) -> dict[str, int]:
    totals: dict[str, int] = defaultdict(int)
    for record in records:
        totals[record["agent_id"]] += int(record["tokens_in"]) + int(record["tokens_out"])
    return dict(sorted(totals.items()))


def compute_same_path_share_per_agent(records: list[dict[str, Any]]) -> dict[str, float]:
    paths_by_agent: dict[str, list[tuple[str, ...]]] = defaultdict(list)

    for record in records:
        path = tuple(step["tool"] for step in record["steps"])
        paths_by_agent[record["agent_id"]].append(path)

    result: dict[str, float] = {}
    for agent_id, paths in sorted(paths_by_agent.items()):
        most_common_count = Counter(paths).most_common(1)[0][1]
        result[agent_id] = most_common_count / len(paths)

    return result


def validate_issue19_coverage(
    records: list[dict[str, Any]],
    expected_agents: set[str] | None = None,
    uniform_threshold: float = 0.8,
) -> list[str]:
    errors: list[str] = []
    expected = expected_agents or EXPECTED_AGENT_IDS

    seen_agents = {record["agent_id"] for record in records if isinstance(record, dict) and "agent_id" in record}
    missing_agents = sorted(expected - seen_agents)
    if missing_agents:
        errors.append(f"Missing expected agent_id values: {', '.join(missing_agents)}")

    shares = compute_same_path_share_per_agent(records)
    expected_shares = {agent: shares[agent] for agent in shares if agent in expected}

    if not expected_shares:
        errors.append("No same-path-share data available for expected agents")
        return errors

    has_uniform = any(share >= uniform_threshold for share in expected_shares.values())
    has_non_uniform = any(share < uniform_threshold for share in expected_shares.values())

    if not has_uniform:
        errors.append(
            f"Coverage lacks a uniform agent (same_path_share >= {uniform_threshold})"
        )

    if not has_non_uniform:
        errors.append(
            f"Coverage lacks a non-uniform agent (same_path_share < {uniform_threshold})"
        )

    return errors
