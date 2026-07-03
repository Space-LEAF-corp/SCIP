from dataclasses import dataclass
from src.flight.decay_prediction.engine import DecayOutput

@dataclass
class SkipCommand:
    mode: str          # "NONE", "LIFT", "LOW_DRAG"
    reason: str

class SkipLogicController:
    DRI_EMERGENCY = 0.8
    CDT_CRITICAL_SEC = 1800.0  # 30 minutes

    def decide(self, decay: DecayOutput) -> SkipCommand:
        if decay.dri >= self.DRI_EMERGENCY or decay.cdt_sec <= self.CDT_CRITICAL_SEC:
            return SkipCommand(mode="LIFT", reason="Emergency skip due to high DRI/CDT")
        elif decay.dri >= 0.4:
            return SkipCommand(mode="LOW_DRAG", reason="Moderate decay, reduce drag")
        else:
            return SkipCommand(mode="NONE", reason="Orbit stable")
