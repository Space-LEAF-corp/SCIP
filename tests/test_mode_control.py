from src.flight.mode_control.supervisor import ModeSupervisor, FlightMode
from src.flight.decay_prediction.engine import DecayOutput

def test_mode_nominal():
    sup = ModeSupervisor()
    decay = DecayOutput(dri=0.1, cdt_sec=50000, drag_accel_ms2=1e-7)
    state = sup.step(decay)
    assert state.mode == FlightMode.NOMINAL

def test_mode_correction():
    sup = ModeSupervisor()
    decay = DecayOutput(dri=0.5, cdt_sec=50000, drag_accel_ms2=1e-7)
    state = sup.step(decay)
    assert state.mode == FlightMode.CORRECTION

def test_mode_emergency_dri():
    sup = ModeSupervisor()
    decay = DecayOutput(dri=0.9, cdt_sec=50000, drag_accel_ms2=1e-7)
    state = sup.step(decay)
    assert state.mode == FlightMode.EMERGENCY

def test_mode_emergency_cdt():
    sup = ModeSupervisor()
    decay = DecayOutput(dri=0.2, cdt_sec=1000, drag_accel_ms2=1e-7)
    state = sup.step(decay)
    assert state.mode == FlightMode.EMERGENCY
