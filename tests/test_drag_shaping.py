from src.flight.drag_shaping.guidance import DragShapingGuidance
from src.flight.skip_logic.controller import SkipCommand

def test_guidance_none():
    g = DragShapingGuidance()
    cmd = SkipCommand(mode="NONE", reason="Stable")
    out = g.execute(cmd)
    assert out.attitude_target_deg == 0.0
    assert out.thrust_profile == "OFF"

def test_guidance_low_drag():
    g = DragShapingGuidance()
    cmd = SkipCommand(mode="LOW_DRAG", reason="Moderate decay")
    out = g.execute(cmd)
    assert out.attitude_target_deg == -5.0
    assert out.thrust_profile == "OFF"

def test_guidance_lift():
    g = DragShapingGuidance()
    cmd = SkipCommand(mode="LIFT", reason="Emergency")
    out = g.execute(cmd)
    assert out.attitude_target_deg == 10.0
    assert out.thrust_profile == "BOOST"
