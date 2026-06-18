# Assignment 4 — ILASP (Rocksample learning + planning)

**Slides:** `3. XAI_ILASP_Lab.pptx` — Lab 4

## Part A — Learn `good(R)` rules (`ilasp_task.las`)

**Goal:** Induce which rocks are good from `dist(R,D)` and `guess(R,V)` examples.

**Implemented:** Mode bias in `ilasp_lab/assignment/ilasp_task.las`:
- Head: `good(R)`
- Body: `dist`, `guess`, comparisons (`D < 1`, `V > 80`, …)

**Run (Linux / Docker):**
```bash
ILASP --version=4 ilasp_task.las
```

## Part B — Use rules in ASP planner (`rocksample_ilp.lp`)

**Goal:** Put learned rules in `#program base`, define `dist/3`, complete `step(t)`.

**Result:** Plans sample **good rock 2** (`guess(2,90) > 80`).

```powershell
conda activate causalai
python asp_lab/run_incmode.py ilasp_lab/assignment/rocksample_ilp.lp 3 --output-dir assignments/assignment_04_ilasp/results
```

**Status:** Done (planning verified; run ILASP in Docker for full learned hypothesis file)
