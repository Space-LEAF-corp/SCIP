from src.sim.orbital_decay_simulator import (
    OrbitalDecaySimulator,
    OrbitState,
)
from src.flight.decay_prediction.engine import DecayParams

def main():
    params = DecayParams(
        mass_kg=500.0,
        area_m2=4.0,
        a_d_ref=1e-5,
        k_decay=1e5,
        crit_altitude_km=180.0,
    )

    sim = OrbitalDecaySimulator(decay_params=params, dt_sec=10.0)

    initial_orbit = OrbitState(
        altitude_km=300.0,
        velocity_kms=7.7,
        density_kg_m3=1e-11,
        drag_coeff=2.2,
    )

    results = sim.run(initial_orbit, max_time_sec=86400.0)

    print("=== Orbital Decay Simulation ===")
    for r in results[:20]:  # print first 20 steps
        print(
            f"t={r.time_sec:6.0f}s | alt={r.altitude_km:7.2f} km | "
            f"DRI={r.dri:.3f} | CDT={r.cdt_sec:.0f}s | drag={r.drag_accel_ms2:.3e}"
        )

if __name__ == "__main__":
    main()
