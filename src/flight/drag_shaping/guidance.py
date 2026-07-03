from dataclasses import dataclass
from src.flight.skip_logic.controller import SkipCommand

@dataclass
class GuidanceOutput:
    attitude_target_deg: float
    thrust_profile: str   # "OFF", "PULSE", "BOOST"
    note: str

class DragShapingGuidance:
    """
    Converts skip commands into attitude and thrust profiles.
    """

    def execute(self, cmd: SkipCommand) -> GuidanceOutput:
        if cmd.mode == "LIFT":
            return GuidanceOutput(
                attitude_target_deg=10.0,
                thrust_profile="BOOST",
                note=f"LIFT maneuver: {cmd.reason}",
            )
        elif cmd.mode == "LOW_DRAG":
            return GuidanceOutput(
                attitude_target_deg=-5.0,
                thrust_profile="OFF",
                note=f"LOW_DRAG trim: {cmd.reason}",
            )
        else:
            return GuidanceOutput(
                attitude_target_deg=0.0,
                thrust_profile="OFF",
                note=f"No maneuver: {cmd.reason}",
            )
