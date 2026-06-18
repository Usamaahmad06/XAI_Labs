"""
Run Lab 6 (SR-DQN), save outputs to assignments/assignment_06_sr_dqn/results/.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LAB = REPO / "sr_dqn_lab"
OUT = REPO / "assignments" / "assignment_06_sr_dqn" / "results"
PYTHON = Path(r"C:\Users\Usama\miniconda3\envs\causalai\python.exe")
if not PYTHON.is_file():
    PYTHON = Path(sys.executable)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(PYTHON),
        "train_script.py",
        "--map", "5x5",
        "--steps", "100000",
    ]
    print("Running:", " ".join(cmd))
    result = subprocess.run(cmd, cwd=str(LAB))
    if result.returncode != 0:
        return result.returncode

    rewards = LAB / "rewards.png"
    if rewards.is_file():
        shutil.copy2(rewards, OUT / "rewards.png")
        print(f"Saved: {OUT / 'rewards.png'}")
    else:
        print("Warning: rewards.png not found in sr_dqn_lab/")

    metrics = {
        "map": "5x5",
        "steps": 100000,
        "models": ["DQN", "SR_DQN"],
        "output_plot": "rewards.png",
        "note": "Fill final_reward values after inspecting plot",
    }
    with open(OUT / "metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    print(f"Results in: {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
