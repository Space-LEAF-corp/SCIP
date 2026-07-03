from src.flight.decay_prediction.engine import DecayPredictionEngine, DecayState
from src.flight.mode_control.supervisor import ModeSupervisor

def main():
    decay_engine = DecayPredictionEngine()
    supervisor = ModeSupervisor()

    # Fake sample state – later this comes from sensors/orbit propagator
    sample_state = DecayState(
        altitude_km=300.0,
        velocity_kms=7.7,
        drag_coeff=2.2,
        density_kg_m3=1e-11,
    )

    decay_output = decay_engine.step(sample_state)
    mode_state = supervisor.step(decay_output)

    print("DRI:", decay_output.dri)
    print("CDT (sec):", decay_output.cdt_sec)
    print("Mode:", mode_state.mode.value)
    print("Reason:", mode_state.last_reason)

if __name__ == "__main__":
    main()
