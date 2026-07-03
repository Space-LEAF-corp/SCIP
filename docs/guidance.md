# Guidance Subsystem

## Skip-Logic Drag Shaping

Decision gates:
- Thermal proxy limit
- Dynamic pressure limit
- Decay risk threshold
- Orbital corridor eligibility

## Lift Window Planner

Planner computes per-orbit windows for aerodynamic shaping and burn opportunities.

```text
[orbit state] -> [window estimator] -> [candidate windows] -> [selected command window]
```
