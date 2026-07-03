import { AtmosphereState, OrbitState, SpacecraftConfig } from "./types.js";

export interface DecayPrediction {
  daysToThreshold: number;
  thresholdAltitudeKm: number;
  estimatedDailyAltitudeLossKm: number;
}

export function predictDecay(
  orbit: OrbitState,
  atm: AtmosphereState,
  sc: SpacecraftConfig,
  thresholdAltitudeKm = 300
): DecayPrediction {
  const ballisticCoeff = sc.massKg / (sc.dragCoefficient * sc.dragAreaM2);
  const dragFactor = atm.densityKgM3 * 1e9 / Math.max(ballisticCoeff, 1);
  const solarAmplifier = 1 + (atm.f107 - 70) / 300;
  const dailyLoss = Math.max(0.01, dragFactor * solarAmplifier * 0.6);

  const days = Math.max(0, (orbit.altitudeKm - thresholdAltitudeKm) / dailyLoss);

  return {
    daysToThreshold: days,
    thresholdAltitudeKm,
    estimatedDailyAltitudeLossKm: dailyLoss
  };
}
