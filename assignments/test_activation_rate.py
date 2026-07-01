"""Standalone test for Lab 5 rule activation (no torch import)."""
import importlib.util
from pathlib import Path
import numpy as np

helpers_path = (
    Path(__file__).resolve().parent
    / "assignment_05_activation_rate"
    / "code"
    / "helpers.py"
)
spec = importlib.util.spec_from_file_location("helpers", helpers_path)
helpers = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(helpers)

obs = np.zeros((5, 7, 7))
obs[2, 3, 3] = 1.0
obs[2, 6, 3] = 1.0
atoms = set(helpers.rware_obs_to_atoms(obs, sensor_range=3))
rule = {"V1 >= 3", "ego(n)", "agent(south, V1)"}
print("Rule activates:", helpers._does_rule_activate(atoms, rule))
