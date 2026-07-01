# Assignment 7 — Distributional NeSy RL (H-C51)

**Slides:** `4. XAI_NeSy_Labs.pptx` — Lab 7  
**Source:** `code/` (`h_c51_product.py`, `run_experiments.py`)

## Goal

Combine **C51** (distributional DQN) with **logical heuristics** via a product on return distributions (H-C51).

## TODO

Implement the product in `code/h_c51_product.py` (see TODO comments).

## Run

```powershell
conda activate causalai
cd D:\XAI\XAI
.\assignments\run.ps1 7
```

## Results (saved to `results/`)

| File | Description |
|------|-------------|
| `c51_vs_hc51_returns.png` | C51 vs H-C51 returns |
| `metrics.json` | Comparison summary |
| `SUMMARY.md` | Portfolio entry |

**Status:** Done — H-C51 beats C51 on DoorKey 5×5 (see `results/c51_vs_hc51_returns.png`).
