# Assignment 3 — ASP (Answer Set Programming) — Rocksample

**Source:** `asp_lab/rocksample.lp`  
**Slides:** Lab 3 in `2. XAI_ASP_labs.pptx`

## What you do (no ML training)

This lab is **logic programming**, not machine learning. You write **Clingo/ASP rules** that describe:

- when actions are allowed (preconditions)
- what changes after each action (transition / effects)
- constraints so every plan stays valid

Clingo then **searches** for action sequences (plans) that reach the goal.

## Goal

Sample **all good rocks** on a grid. Rocks 0 and 1 are good; rocks 2–4 are bad (not required).

- Start at `(0,0)` at time step 1
- Actions: `north`, `south`, `east`, `west`, `sample(R)`

## Your TODO

Complete `#program step(t).` in `asp_lab/rocksample.lp`:

1. **Preconditions** — e.g. can only `sample(R,t)` when agent is at rock R’s cell
2. **Effects** — e.g. `east(t)` moves `at/2` one cell right
3. **Constraints** — exactly one action per step; cannot sample twice; stay on grid

Use `asp_lab/toh.lp` (Towers of Hanoi) as a template for `#program step(t)` structure.

## Run (Cursor terminal)

```powershell
conda activate causalai
cd D:\XAI\XAI
python assignments/run_assignment.py 3
```

Or directly:

```powershell
cd asp_lab
python run_incmode.py rocksample.lp 0 --output-dir ../assignments/assignment_03_asp/results
```

On Linux with native Clingo you can also use: `clingo rocksample.lp 0`

## Results

Saved to `results/`:

- `plans.txt` — answer sets (action plans)
- `summary.txt` — run summary

**Status:** Done — `step(t)` implemented in `rocksample.lp`
