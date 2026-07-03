from math import inf
from src.flight.decay_prediction.engine import (
    DecayPredictionEngine,
    DecayState,
    DecayParams,
)
from src.flight.mode_control.supervisor import ModeSupervisor
from src.flight.drag_shaping.guidance import DragShapingGuidance

def main():
    # Example satellite parameters – tune these for your mission
    params = DecayParams(
        mass_kg=500.0,
        area_m2=4.0,
        a_d_ref=1e-5,          # reference drag acceleration (m/s^2)
        k_decay=1e5,           # decay proportionality constant
        crit_altitude_km=180.0,
    )

    decay_engine = DecayPredictionEngine(params=params)
    supervisor = ModeSupervisor()
    guidance = DragShapingGuidance()

    # Example state – later this comes from sensors / propagator
    state = DecayState(
        altitude_km=300.0,
        velocity_kms=7.7,
        drag_coeff=2.2,
        density_kg_m3=1e-11,
    )

    decay_output = decay_engine.step(state)
    mode_state = supervisor.step(decay_output)
    guidance_output = guidance.execute(
        supervisor.skip_logic.decide(decay_output)
    )

    print("=== SCIP Flight Loop Demo ===")
    print(f"Altitude: {state.altitude_km} km")
    print(f"Drag accel: {decay_output.drag_accel_ms2:.3e} m/s^2")
    print(f"DRI: {decay_output.dri:.3f}")
    print(f"CDT: {decay_output.cdt_sec if decay_output.cdt_sec != inf else 'inf'} s")
    print(f"Mode: {mode_state.mode.value}")
    print(f"Reason: {mode_state.last_reason}")
    print(f"Guidance attitude target: {guidance_output.attitude_target_deg} deg")
    print(f"Guidance thrust profile: {guidance_output.thrust_profile}")
    print(f"Guidance note: {guidance_output.note}")

if __name__ == "__main__":
    main()
