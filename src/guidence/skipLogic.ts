import { OrbitState } from "../core/types.js";

export interface SkipLogicInput {
  orbit: OrbitState;
  dri: number;
  heatingProxy: number;
  dynamicPressurePa: number;
}

export interface SkipDecision {
  execute: boolean;
  reason: string;
  targetLiftBias: number;
}

/**
 * Skip-logic drag-shaping pseudocode encoded as executable scaffold.
 */
export function evaluateSkipLogic(input: SkipLogicInput): SkipDecision {
  // Pseudocode concept:
  // IF qdot > qdot_limit OR dynP > P_limit => SKIP
  // ELSE IF DRI > threshold AND altitude in control corridor => EXECUTE
  // ELSE HOLD
  const qLimit = 1200;
  const pLimit = 80;
  const inCorridor = input.orbit.altitudeKm > 320 && input.orbit.altitudeKm < 520;

  if (input.heatingProxy > qLimit || input.dynamicPressurePa > pLimit) {
    return { execute: false, reason: "THERMAL_OR_PRESSURE_CONSTRAINT", targetLiftBias: 0 };
  }

  if (input.dri > 65 && inCorridor) {
    return { execute: true, reason: "DECAY_RISK_MITIGATION", targetLiftBias: 0.35 };
  }

  return { execute: false, reason: "NO_ACTION_GATE", targetLiftBias: 0.1 };
}
