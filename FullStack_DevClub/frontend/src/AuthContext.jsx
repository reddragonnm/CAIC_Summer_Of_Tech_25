import { useContext, createContext, useState, useEffect } from "react";

import authAPI from "./services/api";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [userdata, setUserdata] = useState(null);
  const [loading, setLoading] = useState(true);

  const getUserdata = async () => {
    setLoading(true);
    const token = localStorage.getItem("token");
    if (!token) {
      setUserdata(null);
      return;
    }

    try {
      const response = await authAPI.getProfile();
      setUserdata(response.data);
      console.log("User data fetched:", response.data);
    } catch (error) {
      console.error("Failed to fetch user data:", error);
      setUserdata(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    getUserdata();
  }, []);

  const login = async (userData) => {
    try {
      const response = await authAPI.login(userData);
      localStorage.setItem("token", response.data.token);

      await getUserdata();
      console.log("Login successful:", response.data);
      return true;
    } catch (error) {
      console.error("Login failed:", error);
      return false;
    }
  };

  const register = async (userData) => {
    try {
      const response = await authAPI.register(userData);
      localStorage.setItem("token", response.data.token);

      await getUserdata();
      console.log("Registration successful:", response.data);
      return [true, ""];
    } catch (error) {
      console.error("Registration failed:", error);
      return [false, error.response.data.message || "Registration failed"];
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUserdata(null);
  };

  return (
    <AuthContext.Provider value={{ userdata, login, logout, register }}>
      {loading ? <div>Loading...</div> : <>{children}</>}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};
