import math
import pytest
from src.flight.decay_prediction.engine import (
    DecayPredictionEngine,
    DecayState,
    DecayParams,
)

def test_decay_prediction_basic():
    params = DecayParams(
        mass_kg=500.0,
        area_m2=4.0,
        a_d_ref=1e-5,
        k_decay=1e5,
        crit_altitude_km=180.0,
    )

    engine = DecayPredictionEngine(params)

    state = DecayState(
        altitude_km=300.0,
        velocity_kms=7.7,
        drag_coeff=2.2,
        density_kg_m3=1e-11,
    )

    out = engine.step(state)

    assert out.dri >= 0.0
    assert out.dri <= 1.0
    assert out.drag_accel_ms2 > 0.0
    assert out.cdt_sec > 0.0

def test_cdt_infinite_when_no_drag():
    params = DecayParams(
        mass_kg=500.0,
        area_m2=4.0,
        a_d_ref=1e-5,
        k_decay=1e5,
        crit_altitude_km=180.0,
    )

    engine = DecayPredictionEngine(params)

    state = DecayState(
        altitude_km=300.0,
        velocity_kms=7.7,
        drag_coeff=0.0,
        density_kg_m3=0.0,
    )

    out = engine.step(state)
    assert math.isinf(out.cdt_sec)
