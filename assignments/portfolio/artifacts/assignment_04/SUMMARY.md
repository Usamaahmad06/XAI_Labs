# Lab 4 — ILASP + ASP Planning

## Goal
Learn which rocks are good from `dist`/`guess`, then plan to sample them.

## Method
Mode bias in `ilasp_task.las`; rules in `rocksample_ilp.lp` + ASP `step(t)`.

## Results
- Plans sample **rock 2** (`guess(2,90) > 80`)
- 5 plans in `plans.txt`

## Key files
- `results/plans.txt`
- `results/learned_rules.txt`

## Takeaway
Logic learns goodness under uncertainty; ASP executes the policy.

## Note
Full ILASP learning run on Linux optional; planning verified on Windows.
