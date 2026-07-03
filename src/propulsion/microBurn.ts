import { SpacecraftConfig } from "../core/types.js";

export interface BurnCommand {
  deltaVms: number;
  thrustVectorBody: [number, number, number];
  durationSec: number;
}

export function buildMicroBurnCommand(
  desiredDeltaVms: number,
  cfg: SpacecraftConfig
): BurnCommand {
  const deltaV = Math.min(desiredDeltaVms, cfg.maxDeltaVPerBurnMS);
  const effectiveAccel = 0.0025; // m/s² placeholder
  const durationSec = deltaV / effectiveAccel;

  return {
    deltaVms: deltaV,
    thrustVectorBody: [1, 0, 0],
    durationSec
  };
}
