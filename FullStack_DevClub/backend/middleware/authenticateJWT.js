import jwt from "jsonwebtoken";
import dotenv from "dotenv";

dotenv.config();

function authenticateJWT(req, res, next) {
  const token = req.headers["authorization"]?.split(" ")[1];

  if (!token) {
    return res
      .status(401)
      .json({ message: "Access denied. No token provided." });
  }

  jwt.verify(token, process.env.JWT_SECRET, (err, payload) => {
    if (err) {
      return res.status(403).json({ message: "Invalid token." });
    }

    req.payload = payload;
    next();
  });
}

export default authenticateJWT;
