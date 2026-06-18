"""
Run Lab 8 (STL RL Pendulum), save outputs to assignments/assignment_08_stl_rl/results/.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LAB = REPO / "stl_rl"
OUT = REPO / "assignments" / "assignment_08_stl_rl" / "results"
PYTHON = Path(r"C:\Users\Usama\miniconda3\envs\causalai\python.exe")
if not PYTHON.is_file():
    PYTHON = Path(sys.executable)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    media_src = LAB / "results" / "pendulum" / "media"
    media_src.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    env["STL_MAX_EPISODES"] = env.get("STL_MAX_EPISODES", "50")

    for script in ("main_pendulum_tuning.py", "main_pendulum_stlgym.py"):
        cmd = [str(PYTHON), script]
        print("Running:", " ".join(cmd), f"(STL_MAX_EPISODES={env['STL_MAX_EPISODES']})")
        result = subprocess.run(cmd, cwd=str(LAB), env=env)
        if result.returncode != 0:
            return result.returncode

    plot_cmd = [str(PYTHON), "plot.py"]
    print("Running:", " ".join(plot_cmd))
    result = subprocess.run(plot_cmd, cwd=str(LAB))
    if result.returncode != 0:
        return result.returncode

    copied = []
    if media_src.is_dir():
        for item in media_src.iterdir():
            if item.is_file() and item.suffix.lower() in {".png", ".pdf", ".html"}:
                shutil.copy2(item, OUT / item.name)
                copied.append(item.name)

    metrics = {
        "env": "Pendulum-vBerga",
        "episodes": int(env.get("STL_MAX_EPISODES", "50")),
        "methods": ["stlgym (reward shaping)", "our (Lagrangian TRPO + STL)"],
        "constraints": ["|thetadot| <= 0.5", "|torque| <= 0.3"],
        "output_plots": copied,
    }
    with open(OUT / "metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    print(f"Copied {len(copied)} plot(s) to {OUT}")
    print(f"Results in: {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
