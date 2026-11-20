"""
Continuity metrics.

Measures identity drift and ledger divergence across runs.
"""

from typing import Any, Dict, List
import hashlib
import json


def _hash(obj: Any) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True).encode("utf-8")
    ).hexdigest()


def ledger_divergence(
    baseline_ledger: List[Dict[str, Any]],
    candidate_ledger: List[Dict[str, Any]],
) -> float:
    """
    Fraction of ledger entries that differ.
    """
    shared = min(len(baseline_ledger), len(candidate_ledger))
    if shared == 0:
        return 0.0

    diffs = sum(
        1
        for i in range(shared)
        if _hash(baseline_ledger[i]) != _hash(candidate_ledger[i])
    )

    return diffs / shared


def continuity_delta(
    baseline_ledger: List[Dict[str, Any]],
    candidate_ledger: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    High-level continuity summary.
    """
    return {
        "baseline_entries": len(baseline_ledger),
        "candidate_entries": len(candidate_ledger),
        "ledger_divergence": ledger_divergence(
            baseline_ledger, candidate_ledger
        ),
    }
