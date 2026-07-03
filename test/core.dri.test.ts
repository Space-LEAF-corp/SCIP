import { describe, expect, it } from "vitest";
import { computeDri } from "../src/core/dri.js";

describe("computeDri", () => {
  it("returns bounded DRI", () => {
    const result = computeDri({
      projectedDecayDays: 4,
      targetMarginDays: 2,
      dragLoadRatio: 0.8,
      solarFluxIndex: 180
    });
    expect(result.value).toBeGreaterThanOrEqual(0);
    expect(result.value).toBeLessThanOrEqual(100);
  });
});
