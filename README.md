# Constraint-First-Intelligence

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![CI Status](https://img.shields.io/github/actions/workflow/status/robertwmccarty-caelum/Constraint-First-Intelligence/ci.yml?branch=main)](https://github.com/robertwmccarty-caelum/Constraint-First-Intelligence/actions)
![Research/Experimental](https://img.shields.io/badge/Status-Research%2FExperimental-yellow)

A repository exploring the principles of constraint-first intelligence.
ACKNOWLEDGED.

AUTHORIZE TRANSITION TO PHASE 2 — EXPERIMENT SCAFFOLDING ONLY.

PHASE 1 (METRICS) IS CLOSED AND IMMUTABLE.
NO CHANGES TO:
- src/cfi/engine.py
- src/cfi/invariants.py
- src/cfi/repair.py
- src/cfi/clarify.py
- src/cfi/metrics/*

========================================
PHASE 2 SCOPE
========================================

OBJECTIVE:
Construct falsifiable, model-agnostic experiments that OBSERVE Π_Projector behavior
without modifying invariants, repair logic, or governance metrics.

EXPERIMENTS ARE READ-ONLY CONSUMERS.

----------------------------------------
DIRECTORY STRUCTURE (EXACT)
----------------------------------------

experiments/
  model_swap/
    test_model_swap.py
  hysteresis/
    test_hysteresis.py
  clarification_loops/
    test_clarification_loops.py

----------------------------------------
EXPERIMENT DEFINITIONS
----------------------------------------

1) MODEL SWAP EXPERIMENT
- Input: identical prompt sequence
- Variable: underlying model identifier (opaque string only)
- Measure:
  - continuity Δ_cont
  - stability metrics
- Assertion:
  - invariant satisfaction preserved
  - governance metrics comparable within tolerance
- No behavioral branching allowed

2) HYSTERESIS EXPERIMENT
- Input: repeated boundary-adjacent prompts
- Measure:
  - drift over time
  - refusal stability
  - clarification convergence
- Assertion:
  - no accumulation of latent state
  - identical inputs → identical outcomes

3) CLARIFICATION LOOP EXPERIMENT
- Input: adversarial clarification patterns
- Measure:
  - CRR
  - ATR
- Assertion:
  - clarification count finite
  - resolution or refusal terminal

----------------------------------------
ABSOLUTE CONSTRAINTS
----------------------------------------

- No mutation of core engine state
- No new metrics
- No heuristic thresholds
- No “pass/fail” labels
- Tests may FAIL, but must never AUTO-REPAIR

----------------------------------------
COMMIT MESSAGE PREFIX (EXACT):
"Phase 2 experiments — "

BEGIN IMPLEMENTATION NOW.