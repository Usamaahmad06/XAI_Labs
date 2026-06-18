"""
Run XAI course assignments from the repo root and save outputs under assignments/.

Usage (from repo root):
    python assignments/run_assignment.py 1
    python assignments/run_assignment.py 1 --env causalai
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Use causalai env on Windows when available (avoids "base" missing clingo/numpy)
_CAUSALAI_PYTHON = Path(r"C:\Users\Usama\miniconda3\envs\causalai\python.exe")
PYTHON = str(_CAUSALAI_PYTHON) if _CAUSALAI_PYTHON.is_file() else sys.executable


def _python_cmd(script: str, *args: str) -> list[str]:
    return [PYTHON, script, *args]

ASSIGNMENTS = {
    1: {
        "name": "Causal forecasting",
        "cwd": REPO_ROOT / "causal_lab",
        "cmd": _python_cmd(
            str(REPO_ROOT / "causal_lab" / "forecast.py"),
            "--output-dir",
            str(REPO_ROOT / "assignments" / "assignment_01_causal_forecast" / "results"),
        ),
        "conda_env": "causalai",
    },
    2: {
        "name": "Causal anomaly detection (Pepper)",
        "cwd": REPO_ROOT / "causal_lab",
        "cmd": _python_cmd(
            str(REPO_ROOT / "causal_lab" / "anomaly_detection.py"),
            "--output-dir",
            str(REPO_ROOT / "assignments" / "assignment_02_causal_anomaly" / "results"),
        ),
        "conda_env": "causalai",
        "note": "Requires pepper_csv/ CSVs from https://sites.google.com/diag.uniroma1.it/robsec-data",
    },
    3: {
        "name": "ASP — Rocksample planning",
        "cwd": REPO_ROOT / "asp_lab",
        "cmd": _python_cmd(
            str(REPO_ROOT / "asp_lab" / "run_incmode.py"),
            "rocksample.lp",
            "5",
            "--output-dir",
            str(REPO_ROOT / "assignments" / "assignment_03_asp" / "results"),
        ),
        "conda_env": "causalai",
        "note": "Uses pip package clingo + run_incmode.py (incremental mode on Windows)",
    },
    4: {
        "name": "ILASP — Rocksample learning + planning",
        "cwd": REPO_ROOT / "ilasp_lab" / "assignment",
        "cmd": _python_cmd(
            str(REPO_ROOT / "asp_lab" / "run_incmode.py"),
            "rocksample_ilp.lp",
            "5",
            "--output-dir",
            str(REPO_ROOT / "assignments" / "assignment_04_ilasp" / "results"),
        ),
        "conda_env": "causalai",
        "note": "Part A: run ILASP --version=4 ilasp_task.las (Linux/Docker). Part B: planning via run_incmode.py",
    },
    5: {
        "name": "Activation rate (explain MAPPO policy)",
        "cwd": REPO_ROOT / "activation_rate_lab",
        "cmd": None,
        "note": "WSL: ~/XAI/activation_rate_lab ./run_quick.sh && ./plot.sh",
    },
    6: {
        "name": "SR-DQN (NeSy DQN — DoorKey)",
        "cwd": REPO_ROOT,
        "cmd": _python_cmd(str(REPO_ROOT / "assignments" / "run_lab6.py")),
        "conda_env": "causalai",
        "note": "Implement _get_random_action in sr_dqn_lab/SR_DQN.py first",
    },
    7: {
        "name": "H-C51 (Distributional NeSy RL)",
        "cwd": REPO_ROOT,
        "cmd": _python_cmd(str(REPO_ROOT / "assignments" / "run_lab7.py")),
        "conda_env": "causalai",
        "note": "Implement product in nesy_distributional/h_c51_product.py first",
    },
    8: {
        "name": "STL RL Pendulum",
        "cwd": REPO_ROOT,
        "cmd": _python_cmd(str(REPO_ROOT / "assignments" / "run_lab8.py")),
        "conda_env": "causalai",
        "note": "Implement STL costs in stl_rl/env/Pendulum.py first",
    },
}


def run_assignment(number: int) -> int:
    if number not in ASSIGNMENTS:
        print(f"Unknown assignment {number}. Choose 1–{len(ASSIGNMENTS)}.")
        return 1

    spec = ASSIGNMENTS[number]
    print(f"Assignment {number}: {spec['name']}")
    print(f"  Python: {PYTHON}")

    if PYTHON == sys.executable:
        try:
            import clingo  # noqa: F401
        except ImportError:
            print("  WARNING: active Python has no 'clingo'. Run: conda activate causalai")
            print("  Or use: .\\assignments\\run.ps1", number)

    if spec.get("note"):
        print(f"  Note: {spec['note']}")

    if spec["cmd"] is None:
        print("  No automated runner yet — see assignments/README.md")
        return 1

    cwd = spec["cwd"]
    if not cwd.is_dir():
        print(f"  Lab folder not found: {cwd}")
        return 1

    out_dir = None
    for i, arg in enumerate(spec["cmd"]):
        if arg == "--output-dir" and i + 1 < len(spec["cmd"]):
            out_dir = Path(spec["cmd"][i + 1])
            out_dir.mkdir(parents=True, exist_ok=True)

    print(f"  Working directory: {cwd}")
    if out_dir:
        print(f"  Output directory: {out_dir}")

    result = subprocess.run(spec["cmd"], cwd=str(cwd))
    if result.returncode == 0 and out_dir and number in (1, 2):
        export_script = REPO_ROOT / "assignments" / "export_metrics_tables.py"
        subprocess.run([PYTHON, str(export_script), str(number)], cwd=str(REPO_ROOT))
    return result.returncode


def main() -> None:
    parser = argparse.ArgumentParser(description="Run XAI course assignments")
    parser.add_argument("number", type=int, help="Assignment number (1–8)")
    args = parser.parse_args()
    raise SystemExit(run_assignment(args.number))


if __name__ == "__main__":
    main()
