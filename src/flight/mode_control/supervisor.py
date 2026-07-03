from enum import Enum
from dataclasses import dataclass
from src.flight.decay_prediction.engine import DecayOutput
from src.flight.skip_logic.controller import SkipLogicController, SkipCommand

class FlightMode(Enum):
    NOMINAL = "NOMINAL"
    CORRECTION = "CORRECTION"
    SKIP = "SKIP"
    EMERGENCY = "EMERGENCY"
    SAFE = "SAFE"

@dataclass
class ModeState:
    mode: FlightMode
    last_reason: str

class ModeSupervisor:
    """
    Top-level flight mode state machine driven by DRI/CDT via SkipLogic.
    """

    def __init__(self):
        self.skip_logic = SkipLogicController()
        self.state = ModeState(mode=FlightMode.NOMINAL, last_reason="Init")

    def step(self, decay: DecayOutput) -> ModeState:
        cmd: SkipCommand = self.skip_logic.decide(decay)

        if cmd.mode == "LIFT":
            self.state.mode = FlightMode.EMERGENCY
        elif cmd.mode == "LOW_DRAG":
            self.state.mode = FlightMode.CORRECTION
        else:
            self.state.mode = FlightMode.NOMINAL

        self.state.last_reason = cmd.reason
        return self.state
