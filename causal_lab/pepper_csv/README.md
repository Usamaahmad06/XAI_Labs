# Pepper robot dataset (Lab 2)

Download the **Pepper** CSV files from the official page:

https://sites.google.com/diag.uniroma1.it/robsec-data

Place these four files in **this folder**:

- `normal.csv`
- `WheelsControl.csv`
- `JointControl.csv`
- `LedsControl.csv`

Then run from repo root:

```powershell
conda activate causalai
python assignments/run_assignment.py 2
```

First run learns the causal model (`pepper_normal.npz`) and can take several minutes.
