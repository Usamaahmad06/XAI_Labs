"""
Export metrics.json to readable CSV tables in the same results folder.

Usage (from repo root):
    python assignments/export_metrics_tables.py 1
    python assignments/export_metrics_tables.py 2
    python assignments/export_metrics_tables.py --all
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[1]

RESULTS_DIRS = {
    1: REPO_ROOT / "assignments" / "assignment_01_causal_forecast" / "results",
    2: REPO_ROOT / "assignments" / "assignment_02_causal_anomaly" / "results",
}


def export_lab1(results_dir: Path) -> list[Path]:
    metrics_path = results_dir / "metrics.json"
    with metrics_path.open(encoding="utf-8") as f:
        m = json.load(f)

    written: list[Path] = []

    summary = {k: v for k, v in m.items() if not isinstance(v, (list, dict))}
    p = results_dir / "metrics_summary.csv"
    pd.DataFrame([summary]).to_csv(p, index=False)
    written.append(p)

    p = results_dir / "causal_predictors.csv"
    pd.DataFrame(m["causal_predictors"]).to_csv(p, index=False)
    written.append(p)

    p = results_dir / "feature_importance.csv"
    pd.DataFrame(
        list(m["causal_feature_importance"].items()),
        columns=["feature", "importance"],
    ).to_csv(p, index=False)
    written.append(p)

    return written


def export_lab2(results_dir: Path) -> list[Path]:
    metrics_path = results_dir / "metrics.json"
    with metrics_path.open(encoding="utf-8") as f:
        m = json.load(f)

    written: list[Path] = []

    p = results_dir / "metrics_summary.csv"
    pd.DataFrame(
        {
            "precision": [m["precision"]],
            "recall": [m["recall"]],
            "f1": [m["f1"]],
            "false_positives_normal": [m["false_positives"][0]],
        }
    ).to_csv(p, index=False)
    written.append(p)

    p = results_dir / "per_attack.csv"
    pd.DataFrame(
        {
            "attack": m["attack_names"],
            "true_positives": m["true_positives"],
            "false_negatives": m["false_negatives"],
        }
    ).to_csv(p, index=False)
    written.append(p)

    return written


EXPORTERS = {
    1: export_lab1,
    2: export_lab2,
}


def export_tables(assignment: int, results_dir: Path | None = None) -> list[Path]:
    if assignment not in EXPORTERS:
        raise ValueError(f"No table exporter for assignment {assignment}")

    out_dir = results_dir or RESULTS_DIRS[assignment]
    metrics_path = out_dir / "metrics.json"
    if not metrics_path.is_file():
        raise FileNotFoundError(f"Missing {metrics_path}")

    written = EXPORTERS[assignment](out_dir)
    print(f"Assignment {assignment}: exported {len(written)} CSV file(s) to {out_dir}")
    for path in written:
        print(f"  - {path.name}")
    return written


def main() -> None:
    parser = argparse.ArgumentParser(description="Export metrics.json to CSV tables")
    parser.add_argument("number", type=int, nargs="?", help="Assignment number (1, 2, …)")
    parser.add_argument("--all", action="store_true", help="Export all supported assignments")
    args = parser.parse_args()

    if args.all:
        for n in sorted(EXPORTERS):
            export_tables(n)
        return

    if args.number is None:
        parser.error("Provide assignment number or use --all")

    export_tables(args.number)


if __name__ == "__main__":
    main()
