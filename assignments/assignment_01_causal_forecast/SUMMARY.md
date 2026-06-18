# Lab 1 — Causal Forecasting

## Goal
Predict `cooling_demand` using causal features vs TCN baseline.

## Method
Tigramite `Prediction` + LinearRegression; compare to dilated TCN.

## Results
- Causal predictors: **6** (vs **32** TCN)
- NMAE causal: **0.096** | NMAE TCN: **0.130**

## Key files
- `results/predictions.png`
- `results/metrics.json`
- `results/feature_importance.png`

## Takeaway
Causal model is sparser and more accurate — interpretable predictors (humidity, past demand, pricing).
