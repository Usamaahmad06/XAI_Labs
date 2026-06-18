# Lab 7 — H-C51 (Distributional NeSy RL)

## Goal
Combine **C51** (distributional DQN) with logical heuristics by modulating return distributions for rule-suggested actions (DoorKey 5×5).

## Method
Implemented the product in `h_c51_product.py` `get_action()`:
1. Multiply PMFs of rule-suggested actions by `1 + ε · rule_pmf`
2. Renormalize over atoms
3. Compute Q-values as the weighted sum over the combined distribution

Trained C51 baseline vs H-C51 for 50k steps each (`params.env`).

## Results
- **H-C51** learns quickly and sustains returns **~0.5–0.8**
- **C51 baseline** drops to **~0** after early episodes (sparse reward)
- H-C51 clearly outperforms standard C51 on DoorKey

## Key files
- `results/c51_vs_hc51_returns.png`
- `results/metrics.json`

## Takeaway
Distributional RL + symbolic heuristics shifts probability mass toward high-return atoms for suggested actions, improving learning under sparse rewards.

**Status:** Done
