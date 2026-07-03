from src.flight.skip_logic.controller import SkipLogicController
from src.flight.decay_prediction.engine import DecayOutput

def test_skip_logic_none():
    logic = SkipLogicController()
    decay = DecayOutput(dri=0.1, cdt_sec=50000, drag_accel_ms2=1e-7)
    cmd = logic.decide(decay)
    assert cmd.mode == "NONE"

def test_skip_logic_low_drag():
    logic = SkipLogicController()
    decay = DecayOutput(dri=0.5, cdt_sec=50000, drag_accel_ms2=1e-7)
    cmd = logic.decide(decay)
    assert cmd.mode == "LOW_DRAG"

def test_skip_logic_emergency_dri():
    logic = SkipLogicController()
    decay = DecayOutput(dri=0.9, cdt_sec=50000, drag_accel_ms2=1e-7)
    cmd = logic.decide(decay)
    assert cmd.mode == "LIFT"

def test_skip_logic_emergency_cdt():
    logic = SkipLogicController()
    decay = DecayOutput(dri=0.2, cdt_sec=1000, drag_accel_ms2=1e-7)
    cmd = logic.decide(decay)
    assert cmd.mode == "LIFT"
