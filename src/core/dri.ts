import { DriInputs, DriResult } from "./types.js";

/**
 * Decay Risk Index (DRI) scaffold.
 * Example canonical form:
 * DRI = w1*F_decay + w2*F_margin + w3*F_drag + w4*F_solar
 */
export function computeDri(input: DriInputs): DriResult {
  const w1 = 0.45;
  const w2 = 0.25;
  const w3 = 0.2;
  const w4 = 0.1;

  const fDecay = clamp01(1 - input.projectedDecayDays / 30);
  const fMargin = clamp01(1 - input.targetMarginDays / 14);
  const fDrag = clamp01(input.dragLoadRatio);
  const fSolar = clamp01(input.solarFluxIndex / 300);

  const value = 100 * (w1 * fDecay + w2 * fMargin + w3 * fDrag + w4 * fSolar);

  return {
    value,
    severity:
      value >= 85 ? "CRITICAL" :
      value >= 65 ? "HIGH" :
      value >= 40 ? "MEDIUM" : "LOW"
  };
}

function clamp01(v: number): number {
  return Math.max(0, Math.min(1, v));
}
