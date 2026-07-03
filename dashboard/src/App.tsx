import React from "react";
import { CesiumView } from "./components/CesiumView";
import { ModePanel } from "./components/ModePanel";
import { TelemetryPanel } from "./components/TelemetryPanel";

export function App() {
  return (
    <div className="layout">
      <h1>SCIP-Orbit Mission Control</h1>
      <ModePanel />
      <TelemetryPanel />
      <CesiumView />
    </div>
  );
}
