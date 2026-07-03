from dataclasses import dataclass
from math import inf

@dataclass
class DecayState:
    altitude_km: float        # Current altitude (km)
    velocity_kms: float       # Orbital velocity (km/s)
    drag_coeff: float         # Cd
    density_kg_m3: float      # Atmospheric density (kg/m^3)

@dataclass
class DecayParams:
    mass_kg: float            # Satellite mass
    area_m2: float            # Cross-sectional area
    a_d_ref: float            # Reference drag acceleration (m/s^2)
    k_decay: float            # Decay proportionality constant
    crit_altitude_km: float   # Critical altitude (km) for collapse

@dataclass
class DecayOutput:
    dri: float                # Decay Rate Index [0, 1]
    cdt_sec: float            # Collapse-Deadline Time (seconds)
    drag_accel_ms2: float     # Actual drag acceleration (m/s^2)

class DecayPredictionEngine:
    def __init__(self, params: DecayParams):
        self.params = params

    def _compute_drag_accel(self, state: DecayState) -> float:
        """
        a_d = 0.5 * (Cd * A / m) * rho * v^2
        v is converted from km/s to m/s.
        """
        v_ms = state.velocity_kms * 1000.0
        Cd = state.drag_coeff
        A = self.params.area_m2
        m = self.params.mass_kg
        rho = state.density_kg_m3

        return 0.5 * (Cd * A / m) * rho * v_ms**2

    def _compute_dri(self, drag_accel_ms2: float) -> float:
        """
        DRI = clip(a_d / a_d_ref, 0, 1)
        """
        if self.params.a_d_ref <= 0.0:
            return 0.0

        dri = drag_accel_ms2 / self.params.a_d_ref
        return max(0.0, min(1.0, dri))

    def _compute_cdt(self, state: DecayState, drag_accel_ms2: float) -> float:
        """
        Approximate collapse time:
        CDT ≈ (h - h_crit) / (k * a_d)

        h, h_crit in meters; k is a tuning constant.
        """
        if drag_accel_ms2 <= 0.0 or self.params.k_decay <= 0.0:
            return inf

        h_m = state.altitude_km * 1000.0
        h_crit_m = self.params.crit_altitude_km * 1000.0
        delta_h_m = max(0.0, h_m - h_crit_m)

        cdt_sec = delta_h_m / (self.params.k_decay * drag_accel_ms2)
        return max(0.0, cdt_sec)

    def step(self, state: DecayState) -> DecayOutput:
        drag_accel = self._compute_drag_accel(state)
        dri = self._compute_dri(drag_accel)
        cdt_sec = self._compute_cdt(state, drag_accel)

        return DecayOutput(
            dri=dri,
            cdt_sec=cdt_sec,
            drag_accel_ms2=drag_accel,
        )
