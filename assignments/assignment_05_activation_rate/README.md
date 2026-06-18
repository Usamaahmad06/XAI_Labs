# Assignment 5 — Activation rate (explain RL policy)

**Slides:** `3. XAI_ILASP_Lab.pptx` — Lab 5

## Goal

Measure **how often** a logical rule’s body matches the state when the RL agent takes that action (MAPPO on RWARE warehouse).

**Implemented:** `_does_rule_activate` wired from `activation_rate_lab/src/runners/helpers.py` into `parallel_runner.py`.

Logic:
1. For each rule body atom, check if grounded atom is in state atoms
2. For variables (`V1`, …), find bound (`V1 >= 3`) and match any satisfying grounding

## Run (needs `uv sync` + checkpoint models)

```bash
cd activation_rate_lab
uv sync
./run.sh
./plot.sh
```

Outputs: `plots/activation_rate_*.csv` and PDF plot.

**Status:** Code done — full run needs `activation_rate_lab/models/` checkpoints
