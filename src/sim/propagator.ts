import { OrbitState, Vector3 } from "../core/types.js";

const MU = 398600.4418; // km^3/s^2

export interface PropagatorStepInput {
  state: OrbitState;
  dtSec: number;
  accelPerturbKmS2?: Vector3;
}

export function stepOrbit(input: PropagatorStepInput): OrbitState {
  const a = input.accelPerturbKmS2 ?? [0, 0, 0];
  const r = input.state.positionEciKm;
  const v = input.state.velocityEciKmS;
  const rNorm = Math.sqrt(r[0] ** 2 + r[1] ** 2 + r[2] ** 2);

  const grav: Vector3 = [
    (-MU / rNorm ** 3) * r[0],
    (-MU / rNorm ** 3) * r[1],
    (-MU / rNorm ** 3) * r[2]
  ];

  const accel: Vector3 = [grav[0] + a[0], grav[1] + a[1], grav[2] + a[2]];

  const vNext: Vector3 = [
    v[0] + accel[0] * input.dtSec,
    v[1] + accel[1] * input.dtSec,
    v[2] + accel[2] * input.dtSec
  ];

  const rNext: Vector3 = [
    r[0] + vNext[0] * input.dtSec,
    r[1] + vNext[1] * input.dtSec,
    r[2] + vNext[2] * input.dtSec
  ];

  return {
    ...input.state,
    epochUnixSec: input.state.epochUnixSec + input.dtSec,
    positionEciKm: rNext,
    velocityEciKmS: vNext,
    altitudeKm: Math.sqrt(rNext[0] ** 2 + rNext[1] ** 2 + rNext[2] ** 2) - 6378.137
  };
}
