import express from "express";
import { WebSocketServer } from "ws";
import { computeDri } from "../src/core/dri.js";

const app = express();
app.use(express.json());

app.get("/api/v1/health", (_req, res) => {
  res.json({ status: "ok", service: "SOG-API v1.0" });
});

app.post("/api/v1/dri", (req, res) => {
  const result = computeDri(req.body);
  res.json(result);
});

const server = app.listen(8080, () => {
  console.log("SOG-API v1.0 listening on :8080");
});

const wss = new WebSocketServer({ server, path: "/ws/v1/telemetry" });

wss.on("connection", (socket) => {
  socket.send(JSON.stringify({ type: "hello", channel: "telemetry" }));
});
