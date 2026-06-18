"""
Incremental-mode runner for ASP lab programs (#include <incmode>).

Usage:
    python run_incmode.py rocksample.lp 0
    python run_incmode.py rocksample.lp --output-dir ../assignments/assignment_03_asp/results
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from clingo import Control, Number


def run_incmode(program: Path, max_models: int = 1, max_horizon: int = 50) -> list[str]:
    """Increase horizon until check(k) + query(k) is satisfiable."""
    ctl = Control([str(max_models)] if max_models else ["0"])
    ctl.load(str(program))

    for k in range(1, max_horizon + 1):
        parts = [("base", []), ("check", [Number(k)])]
        parts += [("step", [Number(i)]) for i in range(1, k + 1)]
        ctl.add("base", [], f"query({k}).")
        ctl.ground(parts)

        models: list[str] = []
        with ctl.solve(yield_=True) as handle:
            for model in handle:
                models.append(str(model))

        if models:
            return models

        # Reset for next horizon (fresh control each iteration is simplest)
        ctl = Control([str(max_models)] if max_models else ["0"])
        ctl.load(str(program))

    raise RuntimeError(f"No plan found within horizon {max_horizon}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run ASP programs in incremental mode")
    parser.add_argument("program", type=Path, help="Path to .lp file")
    parser.add_argument(
        "models",
        nargs="?",
        default="1",
        help='Number of models (use "0" for all)',
    )
    parser.add_argument("--max-horizon", type=int, default=50)
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()

    max_models = 0 if args.models == "0" else int(args.models)
    found = run_incmode(args.program, max_models=max_models, max_horizon=args.max_horizon)

    output_lines = []
    for i, model in enumerate(found, 1):
        header = f"Answer: {i}\n{model}\n"
        print(header, end="")
        output_lines.append(header)

    print("SATISFIABLE")
    output_lines.append("SATISFIABLE\n")

    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        out_file = args.output_dir / "plans.txt"
        out_file.write_text("".join(output_lines), encoding="utf-8")
        summary = args.output_dir / "summary.txt"
        summary.write_text(
            f"program={args.program.name}\n"
            f"models_found={len(found)}\n"
            f"horizon_steps={len(found[0].split()) if found else 0}\n",
            encoding="utf-8",
        )
        print(f"Results saved to: {args.output_dir}")


if __name__ == "__main__":
    main()
