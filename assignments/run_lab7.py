"""
Run Lab 7 (H-C51), save outputs to assignments/assignment_07_nesy_distributional/results/.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LAB = REPO / "nesy_distributional"
OUT = REPO / "assignments" / "assignment_07_nesy_distributional" / "results"
PYTHON = Path(r"C:\Users\Usama\miniconda3\envs\causalai\python.exe")
if not PYTHON.is_file():
    PYTHON = Path(sys.executable)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    cmd = [str(PYTHON), "run_experiments.py"]
    print("Running:", " ".join(cmd))
    result = subprocess.run(cmd, cwd=str(LAB))
    if result.returncode != 0:
        return result.returncode

    plot = LAB / "c51_vs_hc51_returns.png"
    if plot.is_file():
        shutil.copy2(plot, OUT / "c51_vs_hc51_returns.png")
        print(f"Saved: {OUT / 'c51_vs_hc51_returns.png'}")

    metrics = {
        "models": ["C51", "H-C51"],
        "output_plot": "c51_vs_hc51_returns.png",
    }
    with open(OUT / "metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    print(f"Results in: {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
