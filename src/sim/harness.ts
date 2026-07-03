import { computeDri } from "../core/dri.js";
import { predictDecay } from "../core/decayPredictor.js";
import { estimateDensityKgM3 } from "./dragModel.js";
import { stepOrbit } from "./propagator.js";
import { OrbitState, SpacecraftConfig } from "../core/types.js";

export async function runSimulation(steps = 100): Promise<void> {
  const sc: SpacecraftConfig = {
    massKg: 220,
    dragAreaM2: 1.8,
    dragCoefficient: 2.2,
    liftToDrag: 0.3,
    maxDeltaVPerBurnMS: 0.08,
    minBurnIntervalSec: 1800
  };

  let state: OrbitState = {
    epochUnixSec: Math.floor(Date.now() / 1000),
    positionEciKm: [6778.137, 0, 0],
    velocityEciKmS: [0, 7.67, 0],
    altitudeKm: 400,
    semiMajorAxisKm: 6778.137,
    eccentricity: 0.001,
    inclinationDeg: 51.6
  };

  for (let k = 0; k < steps; k++) {
    const density = estimateDensityKgM3(state.altitudeKm, {
      densityKgM3: 0,
      exoTempK: 900,
      f107: 130,
      ap: 12
    });

    const decay = predictDecay(
      state,
      { densityKgM3: density, exoTempK: 900, f107: 130, ap: 12 },
      sc
    );

    const dri = computeDri({
      projectedDecayDays: decay.daysToThreshold,
      targetMarginDays: 7,
      dragLoadRatio: Math.min(1, density * 1e11),
      solarFluxIndex: 130
    });

    console.log(
      `[t+${k}] alt=${state.altitudeKm.toFixed(2)}km density=${density.toExponential(2)} DRI=${dri.value.toFixed(1)}`
    );

    const dragAccelKmS2: [number, number, number] = [0, -1.2e-8, 0];
    state = stepOrbit({ state, dtSec: 10, accelPerturbKmS2: dragAccelKmS2 });
  }
}

if (import.meta.url === `file://${process.argv[1]}`) {
  runSimulation(30);
}
