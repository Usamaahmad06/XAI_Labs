# Final Presentation Outline — XAI Labs 1–8

Use this structure for your professor / report. Fill sections as you complete each lab.

---

## 1. Introduction (1 slide)

- Course: Explainable AI (XAI)
- Repo: `D:\XAI\XAI`
- Environment: Windows + WSL Ubuntu, conda `causalai`
- 8 labs: causal ML → logic → ILASP → RL explainability → neuro-symbolic RL

---

## 2. Lab 1 — Causal Forecasting

- **Problem:** Predict building cooling demand
- **Method:** Tigramite Prediction vs TCN
- **Result:** Fewer features (6 vs 32), better NMAE
- **Figure:** `assignment_01_.../results/predictions.png`
- **XAI angle:** Interpretable causal predictors

---

## 3. Lab 2 — Explainable Anomaly Detection

- **Problem:** Pepper robot attack detection
- **Method:** PCMCI + coefficient monitoring
- **Result:** High recall (0.89), mid precision (0.64)
- **Figure:** `feature_importance.png` — broken causal links
- **XAI angle:** Root cause via broken coefficients

---

## 4. Lab 3 — ASP Planning

- **Problem:** Sample all good rocks on a grid
- **Method:** Clingo incremental mode, `step(t)` rules
- **Result:** Valid action plans
- **Figure:** Example plan from `plans.txt`
- **XAI angle:** Symbolic plans, no training

---

## 5. Lab 4 — ILASP

- **Problem:** Which rocks are good under uncertainty?
- **Method:** ILASP learns `good(R)`; ASP plans
- **Result:** Plans sample learned good rocks
- **XAI angle:** Logic learned from examples + planning

---

## 6. Lab 5 — Activation Rate

- **Problem:** Explain MAPPO warehouse policy
- **Method:** Logical rules + `_does_rule_activate`
- **Result:** Per-action activation rates
- **Figure:** `plot_activation_rate.pdf`
- **XAI angle:** Neural policy vs symbolic rule agreement

---

## 7. Lab 6 — SR-DQN

- **Problem:** DoorKey with sparse reward
- **Method:** DQN + symbolic heuristic exploration
- **Result:** [FILL: DQN vs SR-DQN curves]
- **Figure:** `rewards.png`
- **XAI angle:** Logic guides exploration

---

## 8. Lab 7 — H-C51

- **Problem:** Distributional RL + logic bias
- **Method:** C51 product with heuristic distribution
- **Result:** [FILL: C51 vs H-C51]
- **Figure:** `c51_vs_hc51_returns.png`
- **XAI angle:** Logic shapes return distribution

---

## 9. Lab 8 — STL RL

- **Problem:** Pendulum with safety constraints
- **Method:** STL robustness as Lagrangian cost
- **Result:** [FILL: STL vs reward shaping]
- **Figure:** Pendulum learning curves
- **XAI angle:** Formal specs as interpretable costs

---

## 10. Conclusion (1 slide)

- Theme: **explainability** across forecasting, causality, logic, and RL
- Labs 1–2: data-driven XAI
- Labs 3–4: symbolic AI + learning
- Lab 5: explaining neural policies
- Labs 6–8: neuro-symbolic RL

---

## Appendix

- All artifacts: `assignments/portfolio/artifacts/`
- Run guide: `assignments/WHERE_TO_RUN.md`
