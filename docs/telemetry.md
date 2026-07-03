# Telemetry

Telemetry and command schemas are defined in `/protocol`.

## Packet Structure

```text
SYNC | VERSION | TYPE | LENGTH | PAYLOAD | CRC
```

## Validation

`src/telemetry/schemas.ts` validates packet payloads with Zod before encode/decode.
