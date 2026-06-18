# Lab 6 — SR-DQN (NeSy DQN)

## Goal
DoorKey task: guide DQN exploration with symbolic heuristics (SR-DQN).

## Method
Implemented `_get_random_action()` — weighted sampling: `conf_level` on suggested actions, rest uniform. Trained DQN vs SR-DQN on MiniGrid-DoorKey-5x5-v0 (100k steps).

## Results
- **SR-DQN** learns and reaches reward **~0.7** by end of training
- **DQN** baseline stays near **0** (sparse reward, random exploration fails)
- SR-DQN clearly outperforms standard DQN on this task

## Key files
- `results/rewards.png`
- `results/metrics.json`

## Takeaway
Symbolic heuristics during exploration help the agent discover the sparse +1 reward; explainable logic shapes learning, not just the final policy.

**Status:** Done
