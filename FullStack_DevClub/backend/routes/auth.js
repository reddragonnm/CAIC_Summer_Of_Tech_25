import express from "express";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import dotenv from "dotenv";

import User from "../models/User.js";
import authenticateJWT from "../middleware/authenticateJWT.js";

dotenv.config();

const router = express.Router();

const numSalts = 10;

async function createUser(username, name, email, password) {
  const hashedPassword = await bcrypt.hash(password, numSalts);

  return User.create({
    username,
    name,
    email,
    password: hashedPassword,
  });
}

async function validateUser(username, password) {
  const user = await User.findOne({ username });
  const isPasswordValid = await bcrypt.compare(password, user.password);

  return user && isPasswordValid;
}

function generateJWT(username) {
  return jwt.sign({ username }, process.env.JWT_SECRET);
}

router.post("/register", async (req, res) => {
  try {
    const { username, name, email, password } = req.body;

    // verify username
    const existingUser = await User.exists({ username });
    if (existingUser) {
      return res.status(400).json({ message: "Username already exists" });
    }

    // verify email
    const existingEmail = await User.exists({ email });
    if (existingEmail) {
      return res.status(400).json({ message: "Email already exists" });
    }

    // TODO: validate password strength using joi

    const user = await createUser(username, name, email, password);

    res.status(201).json({
      message: "User registered successfully",
      token: generateJWT(user.username),
    });
  } catch (error) {
    console.error("Error registering user:", error);
    res.status(500).json({ message: "Internal server error" });
  }
});

router.post("/change-password", authenticateJWT, async (req, res) => {
  const { username } = req.payload;
  const { oldPassword, newPassword } = req.body;

  // verify old password
  if (!validateUser(username, oldPassword)) {
    return res.status(400).json({ message: "Invalid username or password" });
  }

  // TODO: validate new password strength using joi

  const hashedPassword = await bcrypt.hash(newPassword, numSalts);
  user.password = hashedPassword;
  await user.save();

  res.status(200).json({ message: "Password changed successfully" });
});

router.post("/delete-account", authenticateJWT, async (req, res) => {
  const { username } = req.payload;

  // verify user exists
  const user = await User.findOne({ username });
  if (!user) {
    return res.status(404).json({ message: "User not found" });
  }

  // delete user
  await User.deleteOne({ username });
  res.status(200).json({ message: "Account deleted successfully" });
});

router.post("/login", async (req, res) => {
  const { username, password } = req.body;

  // verify old password
  if (!validateUser(username, password)) {
    return res.status(400).json({ message: "Invalid username or password" });
  }

  res
    .status(200)
    .json({ message: "Login successful", token: generateJWT(user.username) });
});

router.get("/profile", authenticateJWT, async (req, res) => {
  const { username } = req.payload;

  const user = await User.findOne({ username });
  if (!user) {
    return res.status(404).json({ message: "User not found" }); // should never happen
  }

  const { name, email, createdAt } = user;
  res.status(200).json({ username, name, email, createdAt });
});

export default router;
