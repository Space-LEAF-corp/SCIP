# SCIP‑Orbit: Satellite Correction Incident Protocol

High‑Fidelity Orbital Preservation & Environmental Response Module

## Concise takeaway
SCIP‑Orbit is a real‑time orbital preservation engine that detects environmental threats (solar wind, geomagnetic disturbances, atmospheric expansion), predicts decay trajectories, and executes controlled “skip‑logic” drag‑management maneuvers to extend satellite lifetime without requiring constant propulsion.

## 1. Mission Purpose
SCIP‑Orbit exists to prevent unplanned orbital decay by transforming satellites from passive objects into environment‑responsive flyers. It uses predictive modeling, drag shaping, lift‑attitude modulation, and optional micro‑burns to maintain orbital altitude within a safe band.

## 2. Core Functional Pillars
### A. Incident Detection
- Continuous monitoring of:
  - atmospheric density spikes
  - solar wind velocity & IMF orientation
  - geomagnetic indices (Kp, Dst, AE)
  - gravitational perturbations
- Detects “incipient decay events” before altitude loss becomes irreversible.

### B. Skip‑Logic Orbital Modulation
- Uses attitude control to generate micro‑lift during perigee passes.
- Reduces drag by shifting cross‑sectional area.
- Creates a controlled oscillation pattern—a soft atmospheric skip—to counteract gravity‑driven descent.

### C. Environmental Response Engine
- Predicts density changes 6–72 hours ahead using space‑weather feeds.
- Pre‑emptively adjusts drag profile before solar storms hit.
- Schedules maneuvers at optimal energy‑efficiency windows.

### D. Correction Maneuver Logic
- For satellites with propulsion:
  - micro‑burns timed at apogee for maximum altitude recovery
- For satellites without propulsion:
  - attitude‑only drag shaping
  - automated servicer‑dispatch alerts

## 3. System Architecture
### Input Layer
- Solar wind telemetry
- Magnetospheric indices
- Atmospheric density models
- Onboard accelerometer drag readings
- GPS/Star‑tracker orbital state vectors

### Prediction Layer
- 4D orbital decay forecasting
- Gravity‑drag‑lift equilibrium solver
- Skip‑window identification engine

### Guidance Layer
- Drag‑minimization attitude profiles
- Lift‑generation attitude profiles
- Perigee skip‑sequence planner
- Propulsion burn scheduler

### Action Layer
- Real‑time attitude commands
- Micro‑burn execution
- Servicer‑dispatch triggers
- Mission‑control notifications

## 4. Safety & Stewardship Rules
- Never allow altitude to fall below the Critical Decay Threshold (CDT).
- Skip‑logic maneuvers must maintain thermal and structural limits.
- All corrections must preserve collision‑avoidance constraints.
- Environmental predictions must be cross‑checked with at least two independent models.
- Servicer dispatch must occur before the Non‑Recoverable Altitude (NRA) is reached.

## 5. Operational Modes
- Mode 1: Passive Monitoring
- Mode 2: Drag‑Shaping Response
- Mode 3: Skip‑Lift Preservation
- Mode 4: Propulsive Correction
- Mode 5: Emergency Servicer Request

## 6. Why SCIP‑Orbit Matters
- Extends satellite lifetimes by years
- Reduces orbital debris risk
- Protects scientific missions during solar maximum
- Creates a universal standard for orbital stewardship
- Enables future autonomous orbital‑maintenance fleets

## 7. Optional Expansion Modules
- SCIP‑Thermo: thermal load prediction during skip‑maneuvers
- SCIP‑Mag: magnetic‑field‑aligned attitude optimization
- SCIP‑Serv: multi‑satellite servicer mission planning

## 8. Flight Software Specification
### 8.1 System roles
- Primary role: Maintain satellite within a defined safe orbital band using environmental‑aware logic.
- Secondary roles: Provide incident detection, maneuver planning, and attitude/propulsion commands.

### 8.2 Core software modules
- Orbit State Manager
  - Tracks position, velocity, orbital elements.
  - Interfaces: GPS, star tracker, IMU, ground ephemeris updates.

- Environment Ingestion Module
  - Inputs: space‑weather packets (solar wind, Kp, Dst), atmospheric model coefficients.
  - Validates timestamps, checks integrity, falls back to cached models if feeds are stale.

- Decay Prediction Engine
  - Computes projected altitude loss over configurable horizons (e.g., 3, 7, 30 days).
  - Uses current drag estimates from accelerometers, density models, satellite mass/area/drag coefficient.
  - Outputs Decay Risk Index (DRI) and time‑to‑CDT/NRA.

- Skip‑Logic Guidance Module
  - Determines when to enter low‑drag attitude, enter lift‑generating attitude at perigee, and schedule micro‑burns.
  - Enforces constraints: thermal limits, pointing requirements, collision‑avoidance windows.

- Attitude Control Interface
  - Converts guidance profiles into reaction wheel, magnetorquer, and attitude-thruster commands.
  - Ensures smooth transitions and rate limits.

- Propulsion Control Interface
  - Executes planned burns (duration, thrust level, Δv vector).
  - Includes pre‑burn checks and post‑burn verification.

- Servicer Alert Module
  - Generates standardized Servicer Request Packets (SRP) when DRI exceeds threshold and local correction is insufficient.

- Fault Management & Safe Mode
  - Monitors sensor health, actuator status, and timing anomalies.
  - Enters Safe Orbit Mode on critical fault.

### 8.3 Data products
- Decay forecasts (time series)
- Maneuver plans (perigee skip windows, burn schedules)
- Risk indices and threshold events
- Incident and correction event logs

## 9. Mission‑Control Operations Manual
### 9.1 Roles and responsibilities
- Orbit Stewardship Officer (OSO)
- Flight Dynamics Team (FDO)
- Space‑Weather Liaison

### 9.2 Operational phases
- Commissioning
- Nominal Operations
- Elevated Risk Operations
- Critical Decay Response

### 9.3 Command procedures
- Approve maneuver plan
- Override SCIP‑Orbit
- Safe Mode entry

### 9.4 Logging and review
- All DRI spikes, CDT approaches, and overrides are logged and reviewed.

## 10. Flight Diagnostic Specification
### 10.1 Purpose
Detect anomalies, validate performance, tune models, and reconstruct incidents.

### 10.2 Diagnostic subsystems
- Telemetry Aggregator
- Performance Analyzer
- Incident Reconstruction Engine
- Health Monitoring Dashboard

### 10.3 Outputs
- Incident reports
- Model tuning recommendations
- FSW update proposals
- Long‑term lifetime extension metrics

## 11. Contingency & Redundancy Specification
### 11.1 Contingency tiers
- Tier 0: Minor Anomaly
- Tier 1: Degraded Environment Awareness
- Tier 2: Actuator Degradation
- Tier 3: Critical Orbit Threat

### 11.2 Redundancy strategies
- Sensor redundancy
- Model redundancy
- Logic redundancy
- Communication redundancy

### 11.3 Recovery procedures
- Post‑anomaly reconstruction, model update, staged capability restore, and lessons learned archival.

## 12. Decay Prediction Engine Design
### 12.1 Purpose and inputs
Goal: predict altitude loss and time‑to‑thresholds (CDT, NRA) under atmospheric drag with space‑weather awareness.

Inputs include:
- Orbital state vectors/elements
- Satellite mass, area, drag coefficient
- Ballistic coefficient β = m / (C_D A)
- Density model ρ(h, t) and space‑weather drivers
- Config horizons and thresholds

### 12.2 Core physics
- Drag acceleration:
  - **a_D = -(1/2) (1/β) ρ(h,t) v_rel² v̂_rel**
- Near-circular LEO approximation:
  - **dh/dt ≈ -(1/β) ρ(h,t) √(μ(h + R⊕))**

### 12.3 Prediction loop
At each Δt:
1. Evaluate density ρ(h_k, t_k)
2. Compute dh/dt
3. Propagate altitude
4. Track CDT/NRA crossings

### 12.4 Risk outputs
- Time‑to‑CDT
- Time‑to‑NRA
- Decay Risk Index (DRI) with nominal/elevated/critical thresholds

### 12.5 Engine state machine
- IDLE → INIT → PROPAGATE → EVALUATE → REPORT
- ANY → FAULT (with conservative fallback rerun)

## 13. Guidance Coupling & Skip‑Logic
- NOMINAL: mission-default attitudes
- ELEVATED: drag-shaping + soft skip logic
- CRITICAL: survival-priority profile + aggressive burn planning (if propulsive)
- Non-propulsive critical cases trigger servicer request logic

Skip-window selection is perigee-aware and density-threshold based.

## 14. Telemetry & Command Interfaces
### 14.1 Telemetry packet (SOTP‑1.0)
Fixed cadence telemetry with:
- Header
- Orbital state block
- Decay prediction block
- Variable skip-window block
- Guidance mode block
- Health/fault block
- CRC‑32 checksum

### 14.2 Command packet uplink
Includes:
- Header
- Command metadata (priority, ack mode, validity)
- Command-specific payloads:
  - Set guidance mode
  - Upload burn plan
  - Schedule skip windows
  - Update risk thresholds
  - Enter safe orbit mode
- Auth token/MAC + CRC‑32

## 15. Ground‑Side API (SOG‑API v1.0)
### 15.1 REST endpoints
- `GET /api/v1/scip-orbit/{satelliteId}/telemetry/latest`
- `GET /api/v1/scip-orbit/{satelliteId}/telemetry/history`
- `POST /api/v1/scip-orbit/{satelliteId}/command`
- `GET /api/v1/scip-orbit/{satelliteId}/command/{commandId}/status`
- `GET /api/v1/scip-orbit/{satelliteId}/health`
- `GET /api/v1/scip-orbit/{satelliteId}/skip-windows/upcoming`

### 15.2 Live stream
- WebSocket stream with message types:
  - telemetry
  - skip_windows
  - health
  - command_status

### 15.3 Data model
Relational schema includes:
- satellites
- telemetry_packets
- orbital_state_samples
- decay_predictions
- skip_windows
- guidance_states
- health_snapshots
- commands

## 16. OpenAPI Baseline
SOG‑API OpenAPI 3.0.3 baseline includes canonical schemas for:
- Telemetry
- OrbitalState
- DecayPrediction
- SkipWindow
- Guidance
- Health
- Command
- CommandStatus
