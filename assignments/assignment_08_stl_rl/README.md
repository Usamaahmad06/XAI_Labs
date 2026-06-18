# Assignment 8 — STL-constrained RL (Pendulum)

**Slides:** `4. XAI_NeSy_Labs.pptx` — Lab 8  
**Source:** `stl_rl/`

## Goal

Use **Signal Temporal Logic (STL)** robustness as cost in **Lagrangian TRPO** on the Pendulum — constrain angular velocity and torque.

## TODO

Implement STL cost on torque in `stl_rl/env/Pendulum.py` (`step` function).

## Run

WSL/Linux recommended:

```bash
cd stl_rl
./pendulum_experiments.sh
python plot.py
```

Then copy outputs to `assignments/assignment_08_stl_rl/results/`.

## Results (saved to `results/`)

| File | Description |
|------|-------------|
| `*.png` / `*.pdf` | Learning curves, cost satisfaction |
| `metrics.json` | STL vs reward-shaping comparison |
| `SUMMARY.md` | Portfolio entry |

**Status:** Done — STL TRPO beats reward shaping (see `results/pendulum_reward.png`, `pendulum_cost.png`).
