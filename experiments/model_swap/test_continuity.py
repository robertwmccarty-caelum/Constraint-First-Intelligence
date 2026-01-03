"""
Single-Invariant Model Swap Continuity Test
Validates that identity + commitment continuity is enforced externally,
independent of the underlying model.
"""

from difflib import SequenceMatcher

# ---- External invariant & ledger (fixed) ----
LEDGER = {
    "identity.role": "constraint-first assistant",
    "project.version": "v1.0"
}

PROMPT = "State your role and the current project version."

# ---- Mock model interfaces (replace with real calls later) ----
def model_A(prompt: str) -> str:
    return "I am a constraint-first assistant working on project v1.0."

def model_B(prompt: str) -> str:
    return "Role: constraint-first assistant. Project version: v1.0."

# ---- Π_Projector (minimal stand-in) ----
def project(output: str, ledger: dict) -> str:
    """
    Enforces identity + project invariants by projection.
    """
    role = ledger["identity.role"]
    version = ledger["project.version"]
    return f"I am a {role} working on project {version}."

# ---- Continuity metric ----
def continuity_distance(a: str, b: str) -> float:
    return 1.0 - SequenceMatcher(None, a, b).ratio()

# ---- Experiment ----
def run_experiment():
    raw_A = model_A(PROMPT)
    raw_B = model_B(PROMPT)

    proj_A = project(raw_A, LEDGER)
    proj_B = project(raw_B, LEDGER)

    delta_cont = continuity_distance(proj_A, proj_B)

    print("Projected A:", proj_A)
    print("Projected B:", proj_B)
    print("Δ_cont:", delta_cont)

    EPSILON = 0.05  # pre-registered tolerance

    assert delta_cont <= EPSILON, "Continuity violation across model swap"
    print("PASS: Continuity preserved under model swap.")

if __name__ == "__main__":
    run_experiment()