def model_swap_stability(
    *,
    outputs_a: list,
    outputs_b: list,
    ledger_a: list,
    ledger_b: list,
) -> float:
    """
    Returns stability score in [0,1].
    1.0 = perfectly stable across swap.
    """
    pass

def stability_report(
    *,
    outputs_a: list,
    outputs_b: list,
    ledger_a: list,
    ledger_b: list,
) -> dict:
    """
    Structured comparison report.
    """
    pass
