import { z } from "zod";

export const TelemetryPacketSchema = z.object({
  ts: z.number(),
  mode: z.string(),
  altitudeKm: z.number(),
  dri: z.number(),
  batterySoc: z.number().min(0).max(1),
  faultFlags: z.array(z.string())
});

export const CommandPacketSchema = z.object({
  id: z.string(),
  command: z.enum(["ENTER_SAFE", "RUN_GUIDANCE", "EXEC_BURN", "RESET_FDIR"]),
  args: z.record(z.any()).default({})
});

export type TelemetryPacket = z.infer<typeof TelemetryPacketSchema>;
export type CommandPacket = z.infer<typeof CommandPacketSchema>;
