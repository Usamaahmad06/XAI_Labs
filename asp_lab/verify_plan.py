"""Verify rocksample plans against lab conditions."""
from clingo import Control, Number

LOC = {0: (2, 5), 1: (5, 2), 2: (8, 6), 3: (1, 9)}
GOOD = {0, 1}
HORIZON = 16


def validate_model(atoms: set[str], plan_id: int) -> dict:
    ats = {}
    for a in atoms:
        if a.startswith("at("):
            inner = a[3:-1]
            coords, t = inner.rsplit(",", 1)
            ats[int(t)] = eval(coords)

    moves = sorted(
        a for a in atoms if a.split("(")[0] in {"east", "west", "north", "south"}
    )
    samples = sorted(a for a in atoms if a.startswith("sample("))

    issues = []
    for s in samples:
        r, t = s[7:-1].split(",")
        r, t = int(r), int(t)
        if r in LOC:
            pos_before = ats.get(t - 1)
            pos_at = ats.get(t)
            if pos_at != LOC[r] and pos_before != LOC[r]:
                issues.append(f"{s}: agent not at rock cell (at t={pos_at}, rock at {LOC[r]})")

    good_ok = all(f"sampled({r},{HORIZON})" in atoms for r in GOOD)
    if not good_ok:
        issues.append("goal not met: good rocks 0 and 1 not both sampled by horizon")

    return {
        "plan_id": plan_id,
        "start": ats.get(1),
        "end": ats.get(HORIZON),
        "n_moves": len(moves),
        "samples": samples,
        "good_goal_ok": good_ok,
        "issues": issues,
    }


def main():
    ctl = Control(["5"])
    ctl.load("rocksample.lp")
    parts = [("base", []), ("check", [Number(HORIZON)])]
    parts += [("step", [Number(i)]) for i in range(1, HORIZON + 1)]
    ctl.add("base", [], f"query({HORIZON}).")
    ctl.ground(parts)

    print("=== Lab conditions check ===\n")
    with ctl.solve(yield_=True) as handle:
        for i, model in enumerate(handle, 1):
            atoms = {str(a) for a in model.symbols("atoms")}
            r = validate_model(atoms, i)
            status = "OK" if r["good_goal_ok"] and not r["issues"] else "ISSUES"
            print(f"Plan {i}: {status}")
            print(f"  Start {r['start']} -> End {r['end']}")
            print(f"  Samples: {', '.join(r['samples'])}")
            if r["issues"]:
                for issue in r["issues"]:
                    print(f"  ! {issue}")
            print()

    print("Rock positions (good=0,1):")
    for r, c in LOC.items():
        print(f"  rock {r} at {c} {'(GOOD)' if r in GOOD else '(bad)'}")


if __name__ == "__main__":
    main()
