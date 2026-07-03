import { AtmosphereState } from "../core/types.js";

export interface SolarWeatherFeed {
  getCurrent(): Promise<Pick<AtmosphereState, "f107" | "ap">>;
}

export class MockSolarWeatherFeed implements SolarWeatherFeed {
  async getCurrent() {
    return { f107: 120, ap: 14 };
  }
}
