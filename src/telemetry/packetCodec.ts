import { CommandPacket, CommandPacketSchema, TelemetryPacket, TelemetryPacketSchema } from "./schemas.js";

export function encodeTelemetry(pkt: TelemetryPacket): Uint8Array {
  const valid = TelemetryPacketSchema.parse(pkt);
  return new TextEncoder().encode(JSON.stringify(valid));
}

export function decodeTelemetry(payload: Uint8Array): TelemetryPacket {
  const obj = JSON.parse(new TextDecoder().decode(payload));
  return TelemetryPacketSchema.parse(obj);
}

export function encodeCommand(pkt: CommandPacket): Uint8Array {
  const valid = CommandPacketSchema.parse(pkt);
  return new TextEncoder().encode(JSON.stringify(valid));
}

export function decodeCommand(payload: Uint8Array): CommandPacket {
  const obj = JSON.parse(new TextDecoder().decode(payload));
  return CommandPacketSchema.parse(obj);
}
