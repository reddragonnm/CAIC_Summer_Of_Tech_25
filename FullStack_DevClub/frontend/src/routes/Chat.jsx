import { useEffect } from "react";
import { useAuth } from "../AuthContext";
import { useNavigate } from "react-router";

const Chat = () => {
  const { userdata, logout } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (!userdata) {
      navigate("/login");
    }
  }, [userdata]);

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    userdata && (
      <div>
        <h1>Chat Page</h1>
        <p>Welcome, {userdata.username}!</p>

        <button onClick={handleLogout}>Logout</button>
      </div>
    )
  );
};

export default Chat;
