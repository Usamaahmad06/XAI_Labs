# Lab 5 — Activation Rate (Explain RL)

## Goal
Measure how often logical rules match MAPPO agent actions on RWARE warehouse.

## Method
`_does_rule_activate` in `parallel_runner.py`; compare obs atoms to rule bodies.

## Results (checkpoint 1M, theory index 0)
- Agent 0: forward ~4.5%, left ~8.6%, right ~9.9%
- Agent 1: load ~1.0%, right ~11.3%

## Key files
- `results/plot_activation_rate.pdf`
- `results/activation_rate_*.csv`

## Takeaway
Return alone doesn't explain policy — activation rate shows which rules drive which actions.

## Note
Run in WSL (`~/XAI/activation_rate_lab`).
