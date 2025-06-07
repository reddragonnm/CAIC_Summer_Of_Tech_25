import express from "express";
import mongoose from "mongoose";
import cors from "cors";

import authRouter from "./routes/auth.js";

const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

app.use("/auth", authRouter);

app.get("/", (req, res) => {
  res.status(200).json({
    message: "Welcome to the Chat App API",
  });
});

mongoose
  .connect("mongodb://localhost:27017/Chat-App")
  .then(() =>
    app.listen(port, () =>
      console.log(`Server is running at http://localhost:${port}`)
    )
  )
  .catch((err) => {
    console.error("Database connection error:", err);
  });
