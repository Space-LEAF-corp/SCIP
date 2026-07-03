import { AtmosphereState } from "../core/types.js";

export function estimateDensityKgM3(altitudeKm: number, atm: AtmosphereState): number {
  const base = 3e-11 * Math.exp(-(altitudeKm - 250) / 55);
  const solarBoost = 1 + (atm.f107 - 80) / 200 + atm.ap / 300;
  return Math.max(1e-13, base * solarBoost);
}
