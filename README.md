# SCIP
A redundancy program to save decaying satellites.

## SCIP‑Orbit: Satellite Correction Incident Protocol
SCIP‑Orbit is a high‑fidelity orbital preservation and environmental response module for proactive satellite lifetime extension.

It detects environmental threats (solar wind, geomagnetic disturbances, atmospheric expansion), predicts orbital decay trajectories, and applies controlled skip‑logic drag‑management maneuvers with optional micro‑burn support.

### Mission focus
- Prevent unplanned orbital decay
- Maintain altitude within safe operational bands
- Use environment‑responsive guidance for long‑term stewardship

### Core capabilities
- Incident detection from space‑weather and drag telemetry
- Decay prediction with DRI (Decay Risk Index) and CDT/NRA timing
- Skip‑logic guidance (drag shaping + perigee lift windows)
- Propulsive and non‑propulsive correction strategies
- Safety/contingency logic with servicer dispatch escalation

### Operational modes
1. Passive Monitoring
2. Drag‑Shaping Response
3. Skip‑Lift Preservation
4. Propulsive Correction
5. Emergency Servicer Request

### Documentation
- Full SCIP‑Orbit specification: [`docs/SCIP-Orbit.md`](docs/SCIP-Orbit.md)
