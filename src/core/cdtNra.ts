import { OrbitState } from "./types.js";

export interface CdtNraResult {
  cdtSec: number; // Critical Decay Time
  nraKm: number;  // Nominal Recovery Altitude
}

export function computeCdtNra(state: OrbitState): CdtNraResult {
  // Placeholder logic; replace with mission-specific calibration.
  const cdtSec = Math.max(600, state.altitudeKm * 42);
  const nraKm = Math.max(250, state.altitudeKm + (1 - state.eccentricity) * 5);

  return { cdtSec, nraKm };
}
