import { describe, expect, it } from "vitest";
import { decodeTelemetry, encodeTelemetry } from "../src/telemetry/packetCodec.js";

describe("packet codec", () => {
  it("encodes and decodes telemetry", () => {
    const input = {
      ts: 1,
      mode: "MONITOR",
      altitudeKm: 401,
      dri: 44.2,
      batterySoc: 0.82,
      faultFlags: []
    };
    const encoded = encodeTelemetry(input);
    const decoded = decodeTelemetry(encoded);
    expect(decoded.mode).toBe("MONITOR");
  });
});
