# XAI Course Assignments (8 labs)

| # | Folder | Lab | Status |
|---|--------|-----|--------|
| 1 | `assignment_01_causal_forecast` | Causal forecasting | **Done** |
| 2 | `assignment_02_causal_anomaly` | Anomaly detection | **Done** |
| 3 | `assignment_03_asp` | ASP planning | **Done** |
| 4 | `assignment_04_ilasp` | ILASP + planning | **Done** |
| 5 | `assignment_05_activation_rate` | Activation rate | **Done** |
| 6 | `assignment_06_sr_dqn` | SR-DQN (NeSy) | **Done** |
| 7 | `assignment_07_nesy_distributional` | H-C51 | **Done** |
| 8 | `assignment_08_stl_rl` | STL RL | **Done** |

## Run a lab

```powershell
conda activate causalai
.\assignments\run.ps1 6
```

## Portfolio (final presentation)

After each lab:

```powershell
python assignments/collect_portfolio.py
```

- **Index:** `assignments/portfolio/INDEX.md`
- **All artifacts:** `assignments/portfolio/artifacts/`
- **Presentation outline:** `assignments/portfolio/PRESENTATION_OUTLINE.md`
- **Per-lab report:** `assignment_XX_.../SUMMARY.md`

## Structure (every assignment)

```
assignment_XX_name/
  code/          # your implementation (scripts, .lp, lab package)
  README.md      # what to do, how to run
  SUMMARY.md     # one-page results for portfolio
  results/       # plots, metrics.json, logs
  run.py         # labs 6–8 only (training + copy results)
```
