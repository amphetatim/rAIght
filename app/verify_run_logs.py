"""CLI verification for simulated run logs used in R1."""

from __future__ import annotations

from pathlib import Path
import sys

from run_log_analysis import (
    compute_same_path_share_per_agent,
    compute_total_tokens_per_agent,
    load_run_logs,
    validate_issue19_coverage,
    validate_run_logs,
)


def main() -> int:
    dataset = Path(__file__).with_name("simulated-run-logs.json")
    records = load_run_logs(dataset)

    errors = [
        *validate_run_logs(records),
        *validate_issue19_coverage(records),
    ]

    if errors:
        print("Run-log verification FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    totals = compute_total_tokens_per_agent(records)
    shares = compute_same_path_share_per_agent(records)

    print("Run-log verification passed")
    print("Total tokens per agent:")
    for agent, total in totals.items():
        print(f"- {agent}: {total}")

    print("Same-path share per agent:")
    for agent, share in shares.items():
        print(f"- {agent}: {share:.2f}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
