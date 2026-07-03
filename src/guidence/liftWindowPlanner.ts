import { OrbitState } from "../core/types.js";

export interface LiftWindowPlan {
  startEpoch: number;
  endEpoch: number;
  commandedLiftToDrag: number;
}

export function planLiftWindow(state: OrbitState, now = Math.floor(Date.now() / 1000)): LiftWindowPlan {
  const orbitalPeriodSec = 2 * Math.PI * Math.sqrt(Math.pow(state.semiMajorAxisKm, 3) / 398600.4418);
  const startEpoch = now + Math.floor(0.25 * orbitalPeriodSec);
  const endEpoch = startEpoch + Math.floor(0.08 * orbitalPeriodSec);

  return {
    startEpoch,
    endEpoch,
    commandedLiftToDrag: 0.28
  };
}
