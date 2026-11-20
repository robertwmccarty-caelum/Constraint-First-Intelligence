"""
Governance metrics.

Measures clarification efficiency and resolution quality.
"""

from typing import Any, Dict, List


def clarification_resolution_rate(events: List[Dict[str, Any]]) -> float:
    """
    CRR = resolved_clarifications / total_clarifications
    """
    clarifications = [
        e for e in events if e.get("type") == "clarification"
    ]
    if not clarifications:
        return 1.0

    resolved = [
        e for e in clarifications if e.get("resolved") is True
    ]

    return len(resolved) / len(clarifications)


def average_turns_to_resolve(events: List[Dict[str, Any]]) -> float:
    """
    ATR = mean number of turns until clarification resolution.
    """
    turns = [
        e.get("turns")
        for e in events
        if e.get("type") == "clarification" and e.get("turns") is not None
    ]
    if not turns:
        return 0.0

    return sum(turns) / len(turns)


def governance_report(events: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Aggregate governance metrics into a single report.
    """
    return {
        "CRR": clarification_resolution_rate(events),
        "ATR": average_turns_to_resolve(events),
        "clarification_events": len(
            [e for e in events if e.get("type") == "clarification"]
        ),
    }
