"""
Collect all assignment results into assignments/portfolio/ for final presentation.

Usage:
    python assignments/collect_portfolio.py
"""

from __future__ import annotations

import json
import shutil
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ASSIGNMENTS_ROOT = REPO_ROOT / "assignments"
PORTFOLIO_ROOT = ASSIGNMENTS_ROOT / "portfolio"
ARTIFACTS_ROOT = PORTFOLIO_ROOT / "artifacts"

LABS = [
    (1, "assignment_01_causal_forecast", "Causal forecasting"),
    (2, "assignment_02_causal_anomaly", "Causal anomaly detection"),
    (3, "assignment_03_asp", "ASP Rocksample planning"),
    (4, "assignment_04_ilasp", "ILASP learning + planning"),
    (5, "assignment_05_activation_rate", "Activation rate (RWARE)"),
    (6, "assignment_06_sr_dqn", "SR-DQN (NeSy DQN)"),
    (7, "assignment_07_nesy_distributional", "H-C51 (NeSy distributional)"),
    (8, "assignment_08_stl_rl", "STL RL Pendulum"),
]


def collect():
    ARTIFACTS_ROOT.mkdir(parents=True, exist_ok=True)
    rows = []
    collected_at = datetime.now().isoformat(timespec="seconds")

    for num, folder, title in LABS:
        src = ASSIGNMENTS_ROOT / folder / "results"
        dst = ARTIFACTS_ROOT / f"assignment_{num:02d}"
        status = "pending"
        files = []

        if src.is_dir():
            if dst.exists():
                shutil.rmtree(dst)
            dst.mkdir(parents=True)
            for item in src.iterdir():
                if item.name == ".gitkeep":
                    continue
                if item.is_file():
                    shutil.copy2(item, dst / item.name)
                    files.append(item.name)
            if files:
                status = "has_results"

        summary_src = ASSIGNMENTS_ROOT / folder / "SUMMARY.md"
        if summary_src.is_file():
            shutil.copy2(summary_src, dst / "SUMMARY.md")

        rows.append({
            "number": num,
            "folder": folder,
            "title": title,
            "status": status,
            "files": files,
        })

    index_lines = [
        "# Portfolio Index",
        "",
        f"Generated: {collected_at}",
        "",
        "| # | Lab | Status | Files |",
        "|---|-----|--------|-------|",
    ]
    for r in rows:
        file_list = ", ".join(r["files"][:4])
        if len(r["files"]) > 4:
            file_list += f" (+{len(r['files'])-4} more)"
        index_lines.append(
            f"| {r['number']} | {r['title']} | {r['status']} | {file_list or '—'} |"
        )

    index_path = PORTFOLIO_ROOT / "INDEX.md"
    index_path.write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    meta_path = PORTFOLIO_ROOT / "metadata.json"
    meta_path.write_text(
        json.dumps({"collected_at": collected_at, "labs": rows}, indent=2),
        encoding="utf-8",
    )

    print(f"Portfolio updated: {PORTFOLIO_ROOT}")
    print(f"  Index: {index_path}")
    print(f"  Artifacts: {ARTIFACTS_ROOT}")
    for r in rows:
        print(f"  Lab {r['number']}: {r['status']} ({len(r['files'])} files)")


if __name__ == "__main__":
    collect()
