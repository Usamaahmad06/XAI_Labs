# Assignment 2 — Explainable anomaly detection (Pepper robot)

**Goal:** Unsupervised online anomaly detection using PCMCI + coefficient monitoring.

**Source:** `causal_lab/anomaly_detection.py`

## 1. Download data

Get Pepper CSVs from https://sites.google.com/diag.uniroma1.it/robsec-data and copy into:

`causal_lab/pepper_csv/`

Required: `normal.csv`, `WheelsControl.csv`, `JointControl.csv`, `LedsControl.csv`

## 2. Run (Cursor terminal)

```powershell
conda activate causalai
cd D:\XAI\XAI
python assignments/run_assignment.py 2
```

## 3. Results

Saved to `results/`:

- `metrics.json` — raw metrics
- `metrics_summary.csv` — precision, recall, F1 (readable table)
- `per_attack.csv` — TP/FN per attack type
- `feature_importance.png` — top broken causal variables per attack

Re-export CSV tables anytime:

```powershell
python assignments/export_metrics_tables.py 2
```

**Status:** Done — Precision 0.64, Recall 0.89, F1 0.75 (see `results/metrics.json`).
