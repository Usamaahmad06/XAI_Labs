# Assignment 1 — Causal forecasting

**Goal:** Predict building `cooling_demand` using Tigramite `Prediction` vs a TCN baseline.

**Source:** `code/forecast.py`

**Run from repo root:**

```powershell
conda activate causalai
python assignments/run_assignment.py 1
```

**Results:** `results/metrics.json`, `results/metrics_summary.csv`, `results/causal_predictors.csv`, `results/feature_importance.csv`, `results/predictions.png`, `results/feature_importance.png`

**Status:** Completed (run via Cursor terminal)

Latest run summary:
- Causal predictors: **6** (vs 32 TCN inputs)
- NMAE causal: **0.096** | NMAE TCN: **0.130**
