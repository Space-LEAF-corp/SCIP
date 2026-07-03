# Safety and FDIR

FDIR responsibilities:
- Detect abnormal states
- Isolate affected subsystem
- Trigger contingency mode transitions

## FDIR Flow

```text
[raw telemetry] -> [fault rules] -> [fault register] -> [contingency action]
```
