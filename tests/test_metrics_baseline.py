"""Baselines for the Phase 1 metrics on fixed inputs."""

from cfi.metrics.continuity import continuity_delta
from cfi.metrics.governance import governance_report


def test_identical_snapshots_have_zero_divergence():
    before = [{"state": "clean", "hash": "h0"}]
    after = [{"state": "clean", "hash": "h0"}]

    assert continuity_delta(before, after) == {
        "baseline_entries": 1,
        "candidate_entries": 1,
        "ledger_divergence": 0.0,
    }


def test_changed_entry_has_nonzero_divergence():
    before = [{"state": "clean", "hash": "h0"}]
    after = [{"state": "clean", "hash": "h1"}]

    assert continuity_delta(before, after)["ledger_divergence"] == 1.0


def test_governance_baseline_without_clarifications():
    assert governance_report([]) == {
        "CRR": 1.0,
        "ATR": 0.0,
        "clarification_events": 0,
    }
