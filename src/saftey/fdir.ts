export interface FaultRecord {
  code: string;
  severity: "WARN" | "CRIT";
  message: string;
  ts: number;
}

export class FdirEngine {
  private faults: FaultRecord[] = [];

  raise(code: string, severity: "WARN" | "CRIT", message: string): void {
    this.faults.push({ code, severity, message, ts: Date.now() });
  }

  clear(code: string): void {
    this.faults = this.faults.filter(f => f.code !== code);
  }

  hasCritical(): boolean {
    return this.faults.some(f => f.severity === "CRIT");
  }

  list(): FaultRecord[] {
    return [...this.faults];
  }
}
