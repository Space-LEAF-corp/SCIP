from dataclasses import dataclass
from src.flight.decay_prediction.engine import DecayOutput

@dataclass
class SkipCommand:
    mode: str      # "NONE", "LIFT", "LOW_DRAG"
    reason: str

class SkipLogicController:
    """
    Decides when to trigger skip maneuvers based on DRI and CDT.
    """

    def __init__(
        self,
        dri_emergency: float = 0.8,
        dri_moderate: float = 0.4,
        cdt_critical_sec: float = 1800.0,  # 30 minutes
    ):
        self.dri_emergency = dri_emergency
        self.dri_moderate = dri_moderate
        self.cdt_critical_sec = cdt_critical_sec

    def decide(self, decay: DecayOutput) -> SkipCommand:
        if decay.dri >= self.dri_emergency or decay.cdt_sec <= self.cdt_critical_sec:
            return SkipCommand(
                mode="LIFT",
                reason=f"Emergency skip: DRI={decay.dri:.2f}, CDT={decay.cdt_sec:.0f}s",
            )
        elif decay.dri >= self.dri_moderate:
            return SkipCommand(
                mode="LOW_DRAG",
                reason=f"Moderate decay: DRI={decay.dri:.2f}",
            )
        else:
            return SkipCommand(
                mode="NONE",
                reason=f"Orbit stable: DRI={decay.dri:.2f}",
            )
