export type Vector3 = [number, number, number];

export interface OrbitState {
  epochUnixSec: number;
  positionEciKm: Vector3;
  velocityEciKmS: Vector3;
  altitudeKm: number;
  semiMajorAxisKm: number;
  eccentricity: number;
  inclinationDeg: number;
}

export interface AtmosphereState {
  densityKgM3: number;
  exoTempK: number;
  f107: number;
  ap: number;
}

export interface SpacecraftConfig {
  massKg: number;
  dragAreaM2: number;
  dragCoefficient: number;
  liftToDrag: number;
  maxDeltaVPerBurnMS: number;
  minBurnIntervalSec: number;
}

export enum ScipMode {
  SAFE = "SAFE",
  STANDBY = "STANDBY",
  MONITOR = "MONITOR",
  GUIDANCE = "GUIDANCE",
  PROPULSION_EXEC = "PROPULSION_EXEC",
  CONTINGENCY = "CONTINGENCY"
}

export interface DriInputs {
  projectedDecayDays: number;
  targetMarginDays: number;
  dragLoadRatio: number;
  solarFluxIndex: number;
}

export interface DriResult {
  value: number;
  severity: "LOW" | "MEDIUM" | "HIGH" | "CRITICAL";
}
