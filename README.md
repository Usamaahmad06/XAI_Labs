# XAI Labs — Complete Assignment Portfolio

**Author:** [Usama Ahmad](https://github.com/Usamaahmad06)  
**Repository:** [Usamaahmad06/XAI_Labs](https://github.com/Usamaahmad06/XAI_Labs)

This repository contains my completed work for the **Explainable Artificial Intelligence (XAI)** laboratory course. It extends the upstream course materials ([Isla-lab/XAI](https://github.com/Isla-lab/XAI)) with full implementations, experiment results, run scripts, and a presentation-ready portfolio for all **8 assignments**.

---

## Table of contents

1. [Overview](#overview)
2. [Environment setup](#environment-setup)
3. [Quick start — run any lab](#quick-start--run-any-lab)
4. [Assignment tracker](#assignment-tracker)
5. [Lab details (method, results, how to run)](#lab-details)
6. [Results folder map](#results-folder-map)
7. [Portfolio and presentation](#portfolio-and-presentation)
8. [Repository structure](#repository-structure)
9. [Platform notes (Windows vs Linux)](#platform-notes)
10. [Upstream attribution](#upstream-attribution)

---

## Overview

The course covers three families of explainable AI:

| Track | Labs | Core idea |
|-------|------|-----------|
| **Causal XAI** | 1–2 | Discover causal structure; explain forecasts and anomalies |
| **Symbolic AI** | 3–4 | Logic programming (ASP) and inductive learning (ILASP) |
| **Neuro-symbolic RL** | 5–8 | Rules + RL: activation rates, NeSy DQN/C51, STL constraints |

All assignment outputs are saved under `assignments/assignment_XX_*/results/`.

---

## Environment setup

### Recommended: Conda (`causalai`)

Most labs on **Windows** were run with:

```powershell
conda activate causalai
cd D:\XAI\XAI
```

Install extra packages as needed per lab:

```powershell
# Labs 6–7 (MiniGrid + RL)
pip install gymnasium stable-baselines3 minigrid tyro python-dotenv matplotlib tqdm rich

# Lab 8 (STL + TRPO)
pip install rtamt==0.2.8 scipy plotly kaleido pyyaml rich

# Lab 1–2 (causal)
pip install tigramite pandas scikit-learn

# Lab 3–4 (ASP)
pip install clingo
```

### Original course setup (Linux / WSL)

For ILASP learning (Lab 4 Part A) and full Activation Rate training (Lab 5):

```bash
bash install_binaries.sh
sudo mv clingo ILASP /usr/local/bin/
```

See `assignments/WHERE_TO_RUN.md` for a per-lab platform guide.

---

## Quick start — run any lab

From the repository root:

```powershell
conda activate causalai
.\assignments\run.ps1 1    # Lab 1 — causal forecast
.\assignments\run.ps1 6    # Lab 6 — SR-DQN
.\assignments\run.ps1 8    # Lab 8 — STL Pendulum
```

Or use the Python runner:

```powershell
python assignments/run_assignment.py 3
```

After completing or updating results:

```powershell
python assignments/collect_portfolio.py
python assignments/build_presentation.py   # regenerates PPTX
```

---

## Assignment tracker

| # | Topic | Folder | Status | Key metric |
|---|-------|--------|--------|------------|
| 1 | Causal forecasting | `assignments/assignment_01_causal_forecast` | Done | NMAE **0.096** (6 predictors) |
| 2 | Causal anomaly detection | `assignments/assignment_02_causal_anomaly` | Done | F1 **0.75**, Recall **0.89** |
| 3 | ASP Rocksample planning | `assignments/assignment_03_asp` | Done | **5** valid plans |
| 4 | ILASP + ASP planning | `assignments/assignment_04_ilasp` | Done | Learned `good(R)` + **5** plans |
| 5 | Activation rate (MAPPO) | `assignments/assignment_05_activation_rate` | Done | Per-rule activation CSV + plot |
| 6 | SR-DQN (NeSy DQN) | `assignments/assignment_06_sr_dqn` | Done | SR-DQN reward **~0.7** vs DQN **~0** |
| 7 | H-C51 (distributional NeSy) | `assignments/assignment_07_nesy_distributional` | Done | H-C51 **~0.5–0.8** vs C51 **~0** |
| 8 | STL-constrained RL | `assignments/assignment_08_stl_rl` | Done | STL TRPO return **~-18**, cost **→ 0** |

---

## Lab details

### Lab 1 — Causal forecasting

**Goal:** Predict `cooling_demand` using causal parents vs a TCN baseline.

**Method:**
- Tigramite `Prediction` + `LinearRegression` on causal features only
- Dilated TCN on all 32 input channels as baseline
- Metrics: NMAE, NSTD on held-out test split

**Results:**

| Model | Predictors | NMAE | NSTD |
|-------|------------|------|------|
| Causal | 6 | **0.096** | 0.127 |
| TCN | 32 | 0.130 | 0.156 |

**How to run:**
```powershell
.\assignments\run.ps1 1
# or
cd assignments/assignment_01_causal_forecast/code
python forecast.py --output-dir ../results
```

**Result files:** `predictions.png`, `feature_importance.png`, `metrics_summary.csv`, `causal_predictors.csv`

---

### Lab 2 — Explainable anomaly detection (Pepper robot)

**Goal:** Detect cyber-attacks online via causal coefficient drift.

**Method:**
- PCMCI offline causal discovery + structural coefficients
- Sliding-window monitoring; flag when coefficients deviate from baseline

**Results:**

| Metric | Value |
|--------|-------|
| Precision | 0.64 |
| Recall | **0.89** |
| F1 | **0.75** |
| False positives (normal) | 56 |

**How to run:**
```powershell
.\assignments\run.ps1 2
```
Requires Pepper CSV data in `causal_lab/pepper_csv/` (see course data link in lab README).

**Result files:** `feature_importance.png`, `metrics_summary.csv`, `per_attack.csv`

---

### Lab 3 — ASP Rocksample planning

**Goal:** Find action sequences that sample all **good** rocks on a grid.

**Method:**
- Answer Set Programming in `assignments/assignment_03_asp/code/rocksample.lp`
- Implemented `#program step(t).` — preconditions, effects, constraints
- Clingo incremental search via `code/run_incmode.py`

**Results:**
- **5** valid plans found (`models_found=5`, horizon 16 steps)
- Plans sample good rocks 0 and 1

**How to run:**
```powershell
.\assignments\run.ps1 3
```

**Result files:** `plans.txt`, `summary.txt`

---

### Lab 4 — ILASP learning + ASP planning

**Goal:** Learn which rocks are good from `dist`/`guess`, then plan to sample them.

**Method:**
- Mode bias in `assignments/assignment_04_ilasp/code/ilasp_task.las`
- Learned rules in `code/rocksample_ilp.lp` + ASP `step(t)` for planning
- **Part A** (ILASP learn): Linux/WSL only — `ILASP --version=4 ilasp_task.las`
- **Part B** (planning): Windows via `run_incmode.py`

**Results:**
- Plans target rock 2 when `guess(2,90) > 80`
- **5** plans, horizon 8 steps

**How to run:**
```powershell
.\assignments\run.ps1 4
```

**Result files:** `plans.txt`, `learned_rules.txt`, `summary.txt`

---

### Lab 5 — Activation rate (explain MAPPO policy)

**Goal:** Measure how often logical rules match MAPPO agent actions on RWARE warehouse.

**Method:**
- Implemented `_does_rule_activate()` in `assignments/assignment_05_activation_rate/code/helpers.py`
- Compare observation atoms to rule bodies per agent/action
- Evaluated on checkpoint at 1M steps (theory index 0)

**Results (activation rates):**

| Agent | Action | Activation rate |
|-------|--------|-----------------|
| 0 | forward | ~4.5% |
| 0 | left | ~8.6% |
| 0 | right | ~9.9% |
| 1 | load | ~1.0% |
| 1 | right | ~11.3% |

**How to run:**
- **Full experiment (WSL/Linux):** `cd activation_rate_lab && ./run_quick.sh && ./plot.sh`
- **Windows logic test:** `python assignments/test_activation_rate.py`

**Result files:** `plot_activation_rate.pdf`, `plot_activation_rate.png`, `activation_rate_*.csv`

---

### Lab 6 — SR-DQN (Neuro-symbolic DQN)

**Goal:** Guide DQN exploration with symbolic heuristics on MiniGrid DoorKey.

**Method:**
- Implemented `_get_random_action()` in `assignments/assignment_06_sr_dqn/code/SR_DQN.py`
- Weighted sampling: `conf_level` on rule-suggested actions, uniform on others
- Trained DQN vs SR-DQN on `MiniGrid-DoorKey-5x5-v0`, **100k** steps

**Results:**
- **SR-DQN:** learns to **~0.7** reward
- **DQN:** stays near **0** (sparse reward, random exploration fails)

**How to run:**
```powershell
.\assignments\run.ps1 6
```

**Result files:** `rewards.png`, `metrics.json`

---

### Lab 7 — H-C51 (Distributional NeSy RL)

**Goal:** Combine C51 (distributional DQN) with logical heuristics via PMF product.

**Method:**
- In `assignments/assignment_07_nesy_distributional/code/h_c51_product.py` → `get_action()`:
  1. Multiply PMFs of rule-suggested actions by `1 + ε · rule_pmf`
  2. Renormalize over atoms
  3. Compute Q-values from combined distribution
- Trained C51 baseline vs H-C51, **50k** steps each

**Results:**
- **H-C51:** sustains returns **~0.5–0.8**
- **C51:** drops to **~0** after early episodes

**How to run:**
```powershell
.\assignments\run.ps1 7
```

**Result files:** `c51_vs_hc51_returns.png`, `metrics.json`, `metrics_summary.csv`

---

### Lab 8 — STL-constrained RL (Pendulum)

**Goal:** Use STL robustness as cost in Lagrangian TRPO; constrain |θ̇| and |τ|.

**Method:**
- Implemented `step()` in `assignments/assignment_08_stl_rl/code/env/Pendulum.py`:
  - Build τ-horizon `[thetadot, torque]` trajectory
  - STL robustness ρ via RTAMT (`eventually always |thetadot| ≤ 0.5`, `|torque| ≤ 0.3`)
  - Costs: `tanh(-β · ρ)` per constraint (β = 100)
- Compared **Our** (Lagrangian TRPO + STL costs) vs **Reward shaping** (STL mixed into reward)
- **50 episodes**, seed 47

**Results:**

| Method | Return (end) | Total STL cost (end) | Interpretation |
|--------|--------------|----------------------|----------------|
| **Our (STL TRPO)** | **~-18** | **→ 0** | Constraints satisfied |
| Reward shaping | ~-65 | ~-180 | Weak constraint satisfaction |

**How to run:**
```powershell
.\assignments\run.ps1 8
# Full 200 episodes:
$env:STL_MAX_EPISODES="200"; .\assignments\run.ps1 8
```

**Result files:** `pendulum_reward.png`, `pendulum_cost.png`, `pendulum_theta.png`, `pendulum_thetadot_subplots.png`, `pendulum_torque_subplots.png`, `pendulum_rho_thetadot_subplots.png`, `pendulum_rho_torque_subplots.png`, `metrics.json`

---

## Results folder map

```
assignments/
├── assignment_01_causal_forecast/results/   # plots, CSV, metrics.json
├── assignment_02_causal_anomaly/results/
├── assignment_03_asp/results/               # plans.txt
├── assignment_04_ilasp/results/
├── assignment_05_activation_rate/results/   # PDF, PNG, CSV
├── assignment_06_sr_dqn/results/            # rewards.png
├── assignment_07_nesy_distributional/results/
├── assignment_08_stl_rl/results/            # 7 pendulum plots
└── portfolio/
    ├── artifacts/                           # copy of all results
    ├── INDEX.md
    └── XAI_Assignments_1_to_8_Report_v2.pptx
```

Each assignment also has `SUMMARY.md` (one-page report) and `README.md` (lab-specific instructions).

---

## Portfolio and presentation

| Artifact | Path |
|----------|------|
| Master tracker | `assignments/README.md` |
| Portfolio index | `assignments/portfolio/INDEX.md` |
| Presentation (detailed) | `assignments/portfolio/XAI_Assignments_1_to_8_Report_v2.pptx` |
| Regenerate portfolio | `python assignments/collect_portfolio.py` |
| Regenerate PPTX | `python assignments/build_presentation.py` |
| Export CSV tables | `python assignments/export_metrics_tables.py 1` |

---

## Repository structure

```
XAI_Labs/
├── assignments/
│   ├── assignment_01_causal_forecast/code/   # forecast.py
│   ├── assignment_02_causal_anomaly/code/    # anomaly_detection.py
│   ├── assignment_03_asp/code/               # rocksample.lp, run_incmode.py
│   ├── assignment_04_ilasp/code/             # ilasp_task.las, rocksample_ilp.lp
│   ├── assignment_05_activation_rate/code/     # helpers.py (_does_rule_activate)
│   ├── assignment_06_sr_dqn/code/            # SR-DQN lab package
│   ├── assignment_07_nesy_distributional/code/  # H-C51 lab package
│   ├── assignment_08_stl_rl/code/            # STL Pendulum lab package
│   └── portfolio/                            # PPTX + collected artifacts
├── causal_lab/           # Shared course data (citylearn/, pepper_csv/)
├── asp_lab/              # Upstream ASP examples (toh.lp, verify_plan.py)
├── ilasp_lab/            # Upstream ILASP course materials
├── activation_rate_lab/  # Lab 5 training infrastructure (imports code/helpers.py)
└── README.md
```

---

## Platform notes

| Lab | Windows (`causalai`) | Linux / WSL |
|-----|----------------------|-------------|
| 1–3 | Yes | Yes |
| 4 planning | Yes | Yes |
| 4 ILASP learn | No | Yes |
| 5 full MAPPO run | No | Yes (needs `models/`) |
| 6–8 | Yes | Yes |

Details: `assignments/WHERE_TO_RUN.md`

---

## Upstream attribution

Course lab materials originate from the [Isla-lab XAI Laboratory](https://github.com/Isla-lab/XAI) (University of Verona). This repository contains my **completed implementations, experiment results, and portfolio** built on top of those materials.

---

## Contact

**Usama Ahmad** — [github.com/Usamaahmad06](https://github.com/Usamaahmad06)
