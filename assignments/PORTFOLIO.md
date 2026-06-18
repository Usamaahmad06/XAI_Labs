# XAI Course — Assignment Portfolio

Master index for all 8 labs. Use this to build your final presentation/report.

## Progress

| # | Lab | Folder | Status | Key result |
|---|-----|--------|--------|------------|
| 1 | Causal forecasting | `assignment_01_causal_forecast` | Done | NMAE causal 0.096, 6 predictors |
| 2 | Anomaly detection | `assignment_02_causal_anomaly` | Done | Recall 0.89, F1 0.75 |
| 3 | ASP planning | `assignment_03_asp` | Done | Valid Rocksample plans |
| 4 | ILASP + planning | `assignment_04_ilasp` | Done | Learned good(R) + plans |
| 5 | Activation rate | `assignment_05_activation_rate` | Done | MAPPO rule activation plot |
| 6 | SR-DQN (NeSy) | `assignment_06_sr_dqn` | Pending | — |
| 7 | H-C51 (NeSy dist.) | `assignment_07_nesy_distributional` | Pending | — |
| 8 | STL RL Pendulum | `assignment_08_stl_rl` | Pending | — |

## Refresh portfolio after each lab

```powershell
conda activate causalai
cd D:\XAI\XAI
python assignments/collect_portfolio.py
```

This copies all `results/` into `assignments/portfolio/artifacts/` and updates `assignments/portfolio/INDEX.md`.

## Per-assignment report

Each folder has `SUMMARY.md` — fill after completing the lab (goal, method, results, one figure).

## Final presentation outline

See `assignments/portfolio/PRESENTATION_OUTLINE.md`.

## Run any lab

```powershell
.\assignments\run.ps1 1
.\assignments\run.ps1 6
```
