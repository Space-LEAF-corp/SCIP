import math
from dataclasses import dataclass
from typing import List

from src.flight.decay_prediction.engine import (
    DecayPredictionEngine,
    DecayState,
    DecayParams,
)

@dataclass
class OrbitState:
    altitude_km: float
    velocity_kms: float
    density_kg_m3: float
    drag_coeff: float

@dataclass
class SimulationResult:
    time_sec: float
    altitude_km: float
    dri: float
    cdt_sec: float
    drag_accel_ms2: float

class OrbitalDecaySimulator:
    """
    Physics-backed orbital decay simulator using drag acceleration.
    """

    def __init__(
        self,
        decay_params: DecayParams,
        dt_sec: float = 10.0,
        crit_altitude_km: float = 180.0,
    ):
        self.dt = dt_sec
        self.crit_altitude_km = crit_altitude_km
        self.engine = DecayPredictionEngine(decay_params)

    def propagate(self, orbit: OrbitState) -> OrbitState:
        """
        Propagate altitude using simplified drag-based decay:
        dh/dt ≈ -k * a_d
        """
        decay_state = DecayState(
            altitude_km=orbit.altitude_km,
            velocity_kms=orbit.velocity_kms,
            drag_coeff=orbit.drag_coeff,
            density_kg_m3=orbit.density_kg_m3,
        )

        decay_output = self.engine.step(decay_state)

        # altitude decay model
        dh_dt_m = -self.engine.params.k_decay * decay_output.drag_accel_ms2
        dh_dt_km = dh_dt_m / 1000.0

        new_altitude = orbit.altitude_km + dh_dt_km * self.dt

        # velocity update (very small change, optional)
        new_velocity = orbit.velocity_kms  # keep constant for simplicity

        return OrbitState(
            altitude_km=new_altitude,
            velocity_kms=new_velocity,
            density_kg_m3=orbit.density_kg_m3,
            drag_coeff=orbit.drag_coeff,
        )

    def run(self, initial_orbit: OrbitState, max_time_sec: float = 86400.0):
        """
        Run the simulation until:
        - critical altitude reached
        - max time reached
        """
        t = 0.0
        orbit = initial_orbit
        results: List[SimulationResult] = []

        while t <= max_time_sec and orbit.altitude_km > self.crit_altitude_km:
            decay_state = DecayState(
                altitude_km=orbit.altitude_km,
                velocity_kms=orbit.velocity_kms,
                drag_coeff=orbit.drag_coeff,
                density_kg_m3=orbit.density_kg_m3,
            )

            decay_output = self.engine.step(decay_state)

            results.append(
                SimulationResult(
                    time_sec=t,
                    altitude_km=orbit.altitude_km,
                    dri=decay_output.dri,
                    cdt_sec=decay_output.cdt_sec,
                    drag_accel_ms2=decay_output.drag_accel_ms2,
                )
            )

            orbit = self.propagate(orbit)
            t += self.dt

        return results
