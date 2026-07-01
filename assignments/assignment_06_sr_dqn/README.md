# Assignment 6 — NeSy DQN (SR-DQN)

**Slides:** `4. XAI_NeSy_Labs.pptx` — Lab 6  
**Source:** `code/` (`SR_DQN.py`, `train_script.py`)

## Goal

Symbolic-heuristic-guided exploration in DQN: when exploring, sample actions biased toward logically suggested actions (DoorKey domain).

## TODO

Implement `_get_random_action()` in `code/SR_DQN.py`.

## Run

```powershell
conda activate causalai
cd D:\XAI\XAI
.\assignments\run.ps1 6
```

Or directly:

```bash
cd assignments/assignment_06_sr_dqn/code
python train_script.py --map 5x5 --steps 100000
```

## Results (saved to `results/`)

| File | Description |
|------|-------------|
| `rewards.png` | DQN vs SR-DQN learning curves |
| `metrics.json` | Final episode rewards summary |
| `SUMMARY.md` | One-page report for portfolio |

**Status:** Done — SR-DQN beats DQN on DoorKey 5×5 (see `results/rewards.png`).
