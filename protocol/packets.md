# Packet Specification

## Uplink Command Packet
```text
| Sync | Version | MsgType=CMD | Length | Payload | CRC16 |
```

## Downlink Telemetry Packet
```text
| Sync | Version | MsgType=TLM | Length | Payload | CRC16 |
```

## Notes
- Endianness: little-endian.
- CRC polynomial: CRC-16/CCITT-FALSE.
- Max payload size: 1024 bytes.
