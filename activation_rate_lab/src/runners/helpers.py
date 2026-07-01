"""Re-export assignment implementation from assignments/assignment_05_activation_rate/code/."""
from __future__ import annotations

import importlib.util
from pathlib import Path

_SUBMISSION = (
    Path(__file__).resolve().parents[4]
    / "assignments"
    / "assignment_05_activation_rate"
    / "code"
    / "helpers.py"
)
_spec = importlib.util.spec_from_file_location("_assignment_helpers", _SUBMISSION)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)

_does_rule_activate = _mod._does_rule_activate
rware_obs_to_atoms = _mod.rware_obs_to_atoms
get_theory_dict = _mod.get_theory_dict
_RWARE_ACTION_MAP = _mod._RWARE_ACTION_MAP
_RWARE_LAYERS = _mod._RWARE_LAYERS
ROOT = _mod.ROOT

__all__ = [
    "_does_rule_activate",
    "rware_obs_to_atoms",
    "get_theory_dict",
    "_RWARE_ACTION_MAP",
    "_RWARE_LAYERS",
    "ROOT",
]
