import { ScipMode } from "./types.js";

export interface StateMachineContext {
  faultActive: boolean;
  driValue: number;
  burnWindowOpen: boolean;
  commandedSafe: boolean;
}

export function transitionMode(current: ScipMode, ctx: StateMachineContext): ScipMode {
  if (ctx.commandedSafe || ctx.faultActive) return ScipMode.SAFE;

  switch (current) {
    case ScipMode.SAFE:
      return ScipMode.STANDBY;
    case ScipMode.STANDBY:
      return ScipMode.MONITOR;
    case ScipMode.MONITOR:
      return ctx.driValue >= 60 ? ScipMode.GUIDANCE : ScipMode.MONITOR;
    case ScipMode.GUIDANCE:
      return ctx.burnWindowOpen ? ScipMode.PROPULSION_EXEC : ScipMode.GUIDANCE;
    case ScipMode.PROPULSION_EXEC:
      return ScipMode.MONITOR;
    default:
      return ScipMode.CONTINGENCY;
  }
}
