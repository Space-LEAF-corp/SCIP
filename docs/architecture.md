
````markdown name=docs/architecture.md
# Architecture

SCIP-Orbit follows a layered flight-software design:

1. **Core Layer**: analytical estimators and risk indices.
2. **Guidance Layer**: decision logic and maneuver planning.
3. **Execution Layer**: propulsion command generation.
4. **Safety Layer**: fault detection, isolation, and contingencies.
5. **Telemetry Layer**: packet normalization and transport codecs.
6. **Simulation Layer**: truth-model approximation and Monte Carlo-ready hooks.

## Module Interaction

```text
core -> guidance -> propulsion
  |         |          |
  +-----> telemetry <--+
            ^
            |
          safety
            ^
            |
            sim
```
