# Lab 2 — Explainable Anomaly Detection

## Goal
Detect Pepper robot attacks online using causal coefficient drift.

## Method
PCMCI offline model + sliding-window coefficient monitoring.

## Results
- Precision: **0.64** | Recall: **0.89** | F1: **0.75**

## Key files
- `results/feature_importance.png`
- `results/metrics.json`
- `results/per_attack.csv`

## Takeaway
Broken causal coefficients explain which sensors/actuators changed during each attack type.
