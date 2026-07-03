from dataclasses import dataclass
from src.flight.skip_logic.controller import SkipCommand

@dataclass
class GuidanceOutput:
    attitude_target_deg: float
    thrust_profile: str  # e.g. "OFF", "PULSE", "BOOST"

class DragShapingGuidance:
    def execute(self, cmd: SkipCommand) -> GuidanceOutput:
        if cmd.mode == "LIFT":
            return GuidanceOutput(attitude_target_deg=10.0, thrust_profile="BOOST")
        elif cmd.mode == "LOW_DRAG":
            return GuidanceOutput(attitude_target_deg=-5.0, thrust_profile="OFF")
        else:
            return GuidanceOutput(attitude_target_deg=0.0, thrust_profile="OFF")
