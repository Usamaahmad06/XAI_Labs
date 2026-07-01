# 🧠 Causal AI Lab – Anomaly Detection & Forecasting

> **Assignment code** for Labs 1–2 lives in `assignments/assignment_01_causal_forecast/code/` and `assignments/assignment_02_causal_anomaly/code/`. This folder keeps **shared course data** (`citylearn/`, `pepper_csv/`).

This repository provides two hands-on tutorials demonstrating **Causal Discovery**, **Anomaly Detection**, and **Forecasting** in time-series data using Python.

## ⚙️ Environment Setup
```bash
conda create -n causalai python=3.10 -y
conda activate causalai
pip install -r requirements.txt
````

## 📂 Project Structure

```
.
├── anomaly_detection.py       # Causal discovery + anomaly detection using Tigramite
├── forecast_citylearn.py      # Forecasting with TCN and causal discovery
├── requirements.txt
├── README.md
├── pepper_csv/                # Data for anomaly detection (Pepper robot)
└── citylearn/                 # CityLearn dataset for forecasting
```

## 🚀 Run the Scripts



### ▶ Forecasting (CityLearn)

Forecast building energy demand using **Temporal Convolutional Networks (TCN)** and **causal feature selection**:

```bash
python forecast.py
```

Outputs:

* NMAE and NSTD metrics for prediction performance
* Feature importance plots
* Comparison with TCN

### ▶ Anomaly Detection (Pepper social robot)

**Detect and explain** anomalies in multivariate sensor data using **PCMCI** (causal discovery) and **coefficient deviation analysis**:

```bash
python anomaly_detection.py
```

Outputs:

* Anomaly detection metrics (Precision, Recall, F1)
* Bar plots of top anomalous variables per attack scenario