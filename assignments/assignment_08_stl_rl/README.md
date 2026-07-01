# Assignment 8 — STL-constrained RL (Pendulum)

**Slides:** `4. XAI_NeSy_Labs.pptx` — Lab 8  
**Source:** `code/` (`env/Pendulum.py`, training scripts)

## Goal

Use **Signal Temporal Logic (STL)** robustness as cost in **Lagrangian TRPO** on the Pendulum — constrain angular velocity and torque.

## TODO

Implement STL cost on torque in `code/env/Pendulum.py` (`step` function).

## Run

```powershell
conda activate causalai
cd D:\XAI\XAI
.\assignments\run.ps1 8
```

Or WSL/Linux:

```bash
cd assignments/assignment_08_stl_rl/code
./pendulum_experiments.sh
python plot.py
```

## Results (saved to `results/`)

| File | Description |
|------|-------------|
| `*.png` / `*.pdf` | Learning curves, cost satisfaction |
| `metrics.json` | STL vs reward-shaping comparison |
| `SUMMARY.md` | Portfolio entry |

**Status:** Done — STL TRPO beats reward shaping (see `results/pendulum_reward.png`, `pendulum_cost.png`).
