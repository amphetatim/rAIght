from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import unittest

from app.run_log_analysis import (
    EXPECTED_AGENT_IDS,
    compute_unused_agents,
    compute_same_path_share_per_agent,
    compute_total_tokens_per_agent,
    load_run_logs,
    validate_issue19_coverage,
    validate_run_logs,
)


class RunLogAnalysisTest(unittest.TestCase):
    def setUp(self) -> None:
        dataset = Path(__file__).with_name("simulated-run-logs.json")
        self.records = load_run_logs(dataset)

    def test_schema_validation_passes_for_current_dataset(self) -> None:
        self.assertEqual(validate_run_logs(self.records), [])

    def test_issue_19_coverage_passes(self) -> None:
        self.assertEqual(validate_issue19_coverage(self.records), [])

    def test_total_tokens_per_agent(self) -> None:
        self.assertEqual(
            compute_total_tokens_per_agent(self.records),
            {
                "agent_application_status": 5080,
                "agent_document_check": 8100,
                "agent_interview_scheduling": 11230,
                "agent_offer_letters": 10745,
            },
        )

    def test_same_path_share_per_agent(self) -> None:
        shares = compute_same_path_share_per_agent(self.records)
        self.assertEqual(shares["agent_application_status"], 0.8)
        self.assertEqual(shares["agent_offer_letters"], 0.8)
        self.assertEqual(shares["agent_document_check"], 0.6)
        self.assertEqual(shares["agent_interview_scheduling"], 0.6)

    def test_compute_unused_agents_without_period(self) -> None:
        self.assertEqual(compute_unused_agents(EXPECTED_AGENT_IDS, self.records), [])

    def test_compute_unused_agents_with_period(self) -> None:
        cutoff = datetime(2026, 10, 20, 10, 15, tzinfo=timezone.utc)
        self.assertEqual(
            compute_unused_agents(EXPECTED_AGENT_IDS, self.records, period_start=cutoff),
            ["agent_application_status"],
        )


if __name__ == "__main__":
    unittest.main()
