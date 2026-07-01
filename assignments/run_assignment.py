"""
Run XAI course assignments from the repo root and save outputs under assignments/.

Usage (from repo root):
    python assignments/run_assignment.py 1
    python assignments/run_assignment.py 1 --env causalai
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ASSIGNMENTS_ROOT = REPO_ROOT / "assignments"

# Use causalai env on Windows when available (avoids "base" missing clingo/numpy)
_CAUSALAI_PYTHON = Path(r"C:\Users\Usama\miniconda3\envs\causalai\python.exe")
PYTHON = str(_CAUSALAI_PYTHON) if _CAUSALAI_PYTHON.is_file() else sys.executable


def _assignment_dir(number: int, folder: str) -> Path:
    return ASSIGNMENTS_ROOT / folder


def _python_cmd(script: str, *args: str) -> list[str]:
    return [PYTHON, script, *args]


ASSIGNMENTS = {
    1: {
        "name": "Causal forecasting",
        "folder": "assignment_01_causal_forecast",
        "cwd": None,  # set below
        "cmd": None,
        "conda_env": "causalai",
    },
    2: {
        "name": "Causal anomaly detection (Pepper)",
        "folder": "assignment_02_causal_anomaly",
        "cwd": None,
        "cmd": None,
        "conda_env": "causalai",
        "note": "Requires pepper_csv/ in causal_lab/ from https://sites.google.com/diag.uniroma1.it/robsec-data",
    },
    3: {
        "name": "ASP — Rocksample planning",
        "folder": "assignment_03_asp",
        "cwd": None,
        "cmd": None,
        "conda_env": "causalai",
    },
    4: {
        "name": "ILASP — Rocksample learning + planning",
        "folder": "assignment_04_ilasp",
        "cwd": None,
        "cmd": None,
        "conda_env": "causalai",
        "note": "Part A: run ILASP --version=4 code/ilasp_task.las (Linux/Docker). Part B: planning via code/run_incmode.py",
    },
    5: {
        "name": "Activation rate (explain MAPPO policy)",
        "folder": "assignment_05_activation_rate",
        "cwd": REPO_ROOT / "activation_rate_lab",
        "cmd": None,
        "note": "WSL: ~/XAI/activation_rate_lab ./run_quick.sh && ./plot.sh (implementation in assignment_05_activation_rate/code/)",
    },
    6: {
        "name": "SR-DQN (NeSy DQN — DoorKey)",
        "folder": "assignment_06_sr_dqn",
        "cwd": REPO_ROOT,
        "cmd": None,
        "conda_env": "causalai",
    },
    7: {
        "name": "H-C51 (Distributional NeSy RL)",
        "folder": "assignment_07_nesy_distributional",
        "cwd": REPO_ROOT,
        "cmd": None,
        "conda_env": "causalai",
    },
    8: {
        "name": "STL RL Pendulum",
        "folder": "assignment_08_stl_rl",
        "cwd": REPO_ROOT,
        "cmd": None,
        "conda_env": "causalai",
    },
}

# Build commands after folder paths are known
for n, spec in ASSIGNMENTS.items():
    adir = _assignment_dir(n, spec["folder"])
    code = adir / "code"
    results = adir / "results"
    if n == 1:
        spec["cwd"] = code
        spec["cmd"] = _python_cmd(
            str(code / "forecast.py"),
            "--output-dir",
            str(results),
        )
    elif n == 2:
        spec["cwd"] = code
        spec["cmd"] = _python_cmd(
            str(code / "anomaly_detection.py"),
            "--output-dir",
            str(results),
        )
    elif n == 3:
        spec["cwd"] = code
        spec["cmd"] = _python_cmd(
            str(code / "run_incmode.py"),
            "rocksample.lp",
            "5",
            "--output-dir",
            str(results),
        )
    elif n == 4:
        spec["cwd"] = code
        spec["cmd"] = _python_cmd(
            str(code / "run_incmode.py"),
            "rocksample_ilp.lp",
            "5",
            "--output-dir",
            str(results),
        )
    elif n == 6:
        spec["cmd"] = _python_cmd(str(adir / "run.py"))
    elif n == 7:
        spec["cmd"] = _python_cmd(str(adir / "run.py"))
    elif n == 8:
        spec["cmd"] = _python_cmd(str(adir / "run.py"))


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
    if cwd and not cwd.is_dir():
        print(f"  Assignment code folder not found: {cwd}")
        return 1

    out_dir = None
    for i, arg in enumerate(spec["cmd"]):
        if arg == "--output-dir" and i + 1 < len(spec["cmd"]):
            out_dir = Path(spec["cmd"][i + 1])
            out_dir.mkdir(parents=True, exist_ok=True)

    if cwd:
        print(f"  Working directory: {cwd}")
    if out_dir:
        print(f"  Output directory: {out_dir}")

    result = subprocess.run(spec["cmd"], cwd=str(cwd) if cwd else None)
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
