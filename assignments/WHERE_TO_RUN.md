# Where to run each lab (honest guide)

The course README says labs are designed for **Ubuntu 22.04** (native, WSL, or VirtualBox).  
On **Windows + Cursor**, only some labs run fully. Others need a Linux environment.

---

## Always do this first (Windows / Cursor)

```powershell
conda activate causalai
```

Your terminal showed `(base)` — that env does **not** have `clingo`, `numpy`, etc.  
Labs 1–4 failed when you used `base`.

**Or use the wrapper (no need to remember activate):**

```powershell
cd D:\XAI\XAI
.\assignments\run.ps1 4
```

---

## What runs where

| Assignment | Runs in Cursor (Windows + causalai)? | Needs Ubuntu / VM? | Results folder |
|------------|-------------------------------------|--------------------|----------------|
| **1** Causal forecast | **Yes** | No | `assignment_01_causal_forecast/results/` |
| **2** Anomaly detection | **Yes** | No (need pepper CSVs) | `assignment_02_causal_anomaly/results/` |
| **3** ASP Rocksample | **Yes** | No | `assignment_03_asp/results/` |
| **4** ILASP | **Part B only** (ASP planning) | **Part A** (ILASP learn) | `assignment_04_ilasp/results/` |
| **5** Activation rate | Demo only on Windows | **Full lab** (MAPPO + models) | `assignment_05_activation_rate/results/` |

---

## Lab 4 — ILASP

### Part B (planning) — Windows OK

```powershell
conda activate causalai
cd D:\XAI\XAI
.\assignments\run.ps1 4
```

Output: `assignment_04_ilasp/results/plans.txt`

### Part A (learn `good(R)` rules) — **Linux only**

`ILASP` has **no Windows installer** in this course. Use one of:

**Option A — Ubuntu VM (recommended by course)**  
1. Install [VirtualBox](https://www.virtualbox.org/) + [Ubuntu 22.04](https://releases.ubuntu.com/jammy/)  
2. Clone repo inside VM  
3. Run:
   ```bash
   bash install_binaries.sh
   sudo mv clingo ILASP /usr/local/bin/
   cd ilasp_lab/assignment
   ILASP --version=4 ilasp_task.las
   ```
4. Copy learned rules into `rocksample_ilp.lp` if different from slides

**Option B — WSL Ubuntu** (if you install it: `wsl --install Ubuntu-22.04`)

```bash
cd /mnt/d/XAI/XAI
bash install_binaries.sh
# ... same as above
```

---

## Lab 5 — Activation rate

### Why `./run.sh` did nothing useful on Windows

- `run.sh` / `plot.sh` are **bash** scripts (for Linux)
- They use **`uv`** (not installed on your PC)
- They need **`activation_rate_lab/models/`** — pretrained MAPPO checkpoints (**not in git**)

### Full lab — Ubuntu VM

```bash
cd activation_rate_lab
curl -LsSf https://astral.sh/uv/install.sh | sh   # install uv
uv sync
# Obtain models/ from course instructors or train MAPPO first
./run.sh
./plot.sh
```

### Windows demo (logic test only)

```powershell
conda activate causalai
python assignments/test_activation_rate.py
```

This verifies `_does_rule_activate` works; it is **not** the full training plot from the slides.

---

## Quick verify Labs 1–4 on your machine

```powershell
conda activate causalai
cd D:\XAI\XAI
.\assignments\run.ps1 1
.\assignments\run.ps1 2
.\assignments\run.ps1 3
.\assignments\run.ps1 4
```

---

## Summary

| You want | Where |
|----------|--------|
| Labs 1–3 + Lab 4 planning | **Cursor terminal**, `conda activate causalai` |
| Lab 4 ILASP learning | **Ubuntu VM or WSL** |
| Lab 5 full plot | **Ubuntu VM** + models + uv |

Contact course staff if you need the **MAPPO checkpoint files** for Lab 5.
