import { describe, expect, it } from "vitest";
import { stepOrbit } from "../src/sim/propagator.js";

describe("propagator", () => {
  it("advances epoch", () => {
    const state = {
      epochUnixSec: 1000,
      positionEciKm: [6778.137, 0, 0] as [number, number, number],
      velocityEciKmS: [0, 7.67, 0] as [number, number, number],
      altitudeKm: 400,
      semiMajorAxisKm: 6778.137,
      eccentricity: 0.001,
      inclinationDeg: 51.6
    };
    const next = stepOrbit({ state, dtSec: 5 });
    expect(next.epochUnixSec).toBe(1005);
  });
});
