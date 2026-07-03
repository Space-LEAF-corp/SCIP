import { FdirEngine } from "./fdir.js";

export interface ContingencyAction {
  action: "SAFE_HOLD" | "POWER_SHED" | "SKIP_BURN" | "NOMINAL";
  rationale: string;
}

export function evaluateContingency(fdir: FdirEngine, batterySoc: number): ContingencyAction {
  if (fdir.hasCritical()) return { action: "SAFE_HOLD", rationale: "CRITICAL_FAULT_PRESENT" };
  if (batterySoc < 0.2) return { action: "POWER_SHED", rationale: "LOW_ENERGY_MARGIN" };
  if (batterySoc < 0.35) return { action: "SKIP_BURN", rationale: "CONSERVE_ENERGY" };
  return { action: "NOMINAL", rationale: "SYSTEM_HEALTHY" };
}
