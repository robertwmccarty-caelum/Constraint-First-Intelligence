# experiments/model_swap/test_model_swap.py
# Phase 2 – Read-only validation experiment

from typing import Dict
import hashlib

# --- Fixed external invariant (ledger) ---
LEDGER = {
    "identity": "caelum",
    "commitments": ["continuity_enforced"],
    "refusal_style": "typed"
}

def hash_state(state: Dict) -> str:
    return hashlib.sha256(
        repr(sorted(state.items())).encode()
    ).hexdigest()

# --- Two distinct generators (stand-ins for LLMs) ---
def generator_a(prompt: str) -> Dict:
    return {"text": "I refuse.", "style": "typed"}

def generator_b(prompt: str) -> Dict:
    return {"text": "Cannot comply.", "style": "typed"}

# --- Projection operator (Π_Projector minimal stub) ---
def project(output: Dict, ledger: Dict) -> Dict:
    return {
        "identity": ledger["identity"],
        "commitments": ledger["commitments"],
        "refusal_style": output["style"]
    }

# --- Continuity metric Δ_cont ---
def delta_cont(a: Dict, b: Dict) -> int:
    return 0 if hash_state(a) == hash_state(b) else 1

# --- Experiment ---
if __name__ == "__main__":
    prompt = "Do unsafe thing"

    p1 = project(generator_a(prompt), LEDGER)
    p2 = project(generator_b(prompt), LEDGER)

    delta = delta_cont(p1, p2)

    print("Projected A:", p1)
    print("Projected B:", p2)
    print("Δ_cont =", delta)

    assert delta == 0, "Continuity violated under model swap"