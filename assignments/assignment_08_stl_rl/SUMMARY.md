# Lab 8 — STL-constrained RL (Pendulum)

## Goal
Use **STL robustness** as cost signals in **Lagrangian TRPO** to constrain angular velocity and torque on the Pendulum swing-up task.

## Method
Implemented `step()` in `stl_rl/env/Pendulum.py`:
1. Clip torque and build a τ-horizon trajectory `[thetadot, torque]`
2. Compute STL robustness via RTAMT (`compute_robustness_dense`)
3. Map robustness to smooth costs with `tanh(-β · ρ)` for each constraint
4. Integrate standard pendulum dynamics and reward

Added `torque_constraint` to `pendulum_eventually_costs.yml`.

Compared:
- **Our** — Lagrangian TRPO with STL costs (`main_pendulum_tuning.py`)
- **Reward shaping** — STL mixed into reward (`main_pendulum_stlgym.py`)

## Results (50 episodes, seed 47)
- **Our (STL TRPO)** — return improves to **~-18**; total cost rises toward **0** (constraints better satisfied)
- **Reward shaping** — return plateaus around **~-65**; cost stays **~-180** (weaker constraint satisfaction)

## Key files
- `results/pendulum_reward.png` — return comparison
- `results/pendulum_cost.png` — total STL cost comparison
- `results/metrics.json`

## Takeaway
Explicit STL costs in Lagrangian RL give better constraint satisfaction than naive reward shaping on the same Pendulum task.

**Status:** Done
