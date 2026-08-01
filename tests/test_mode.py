"""Screening-mode contract.

models/mode.py is deliberately dependency-free, but the models package
__init__ imports pydantic-dependent siblings, so this test loads the
module file directly — it must run even where pydantic is unavailable.
"""

import importlib.util
from pathlib import Path

_path = (
    Path(__file__).resolve().parent.parent
    / "src"
    / "deal_engine"
    / "models"
    / "mode.py"
)
_spec = importlib.util.spec_from_file_location("deal_engine_mode_standalone", _path)
mode = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mode)

ModeRequirement = mode.ModeRequirement
ScreeningMode = mode.ScreeningMode
mode_satisfied = mode.mode_satisfied


def test_two_modes_only():
    assert {m.value for m in ScreeningMode} == {"financial", "signal"}


def test_any_requirement_always_satisfied():
    assert mode_satisfied(ModeRequirement.ANY, set())
    assert mode_satisfied(ModeRequirement.ANY, {ScreeningMode.SIGNAL})


def test_specific_requirement_needs_its_mode():
    assert mode_satisfied(ModeRequirement.FINANCIAL, {ScreeningMode.FINANCIAL})
    assert not mode_satisfied(ModeRequirement.FINANCIAL, {ScreeningMode.SIGNAL})
    assert mode_satisfied(
        ModeRequirement.SIGNAL, {ScreeningMode.FINANCIAL, ScreeningMode.SIGNAL}
    )
    assert not mode_satisfied(ModeRequirement.SIGNAL, set())
