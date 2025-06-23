import { useEffect, useState } from "react";
import { useAuth } from "../AuthContext";
import { useNavigate } from "react-router";

import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  serverTimestamp,
  addDoc,
  query,
  orderBy,
} from "firebase/firestore";
import { useCollectionData } from "react-firebase-hooks/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyBUl4pwXJk6dVXJPpT0G5o3FJcfsYzLKTU",
  authDomain: "chat-app-98a70.firebaseapp.com",
  projectId: "chat-app-98a70",
  storageBucket: "chat-app-98a70.firebasestorage.app",
  messagingSenderId: "956268450678",
  appId: "1:956268450678:web:266e149abedeb21b5ae057",
  measurementId: "G-KV2KZXRYK5",
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

const messageConvertor = {
  toFirestore: (msg) => msg,

  fromFirestore: (snapshot, options) => {
    const data = snapshot.data(options);
    return {
      idx: snapshot.id,
      ...data,
    };
  },
};

const Chat = () => {
  const { userdata, logout } = useAuth();
  const navigate = useNavigate();

  const [newMessage, setNewMessage] = useState("");

  const messagesRef = collection(db, "messages").withConverter(
    messageConvertor
  );
  const [messages, loading, error] = useCollectionData(
    query(messagesRef, orderBy("createdAt"))
  );

  useEffect(() => {
    if (!userdata) {
      navigate("/login");
    }
  }, []);

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  const sendMessage = async (e) => {
    e.preventDefault();

    const trimmed = newMessage.trim();
    if (!trimmed) return;

    try {
      await addDoc(messagesRef, {
        message: trimmed,
        username: userdata.username,
        createdAt: serverTimestamp(),
      });
      setNewMessage("");
    } catch (err) {
      console.error("Error sending message: ", err);
      alert("Failed to send message. Please try again.");
    }
  };

  if (loading) return <div>Loading messages...</div>;
  if (error) return <div>Error loading messages: {error.message}</div>;

  return (
    userdata && (
      <div>
        <h1>Chat Page</h1>
        <p>Welcome, {userdata.username}!</p>

        <button onClick={handleLogout}>Logout</button>

        <ul>
          {messages.map((msg) => (
            <li key={msg.idx}>
              <strong>{msg.username || "Anon"}:</strong> {msg.message}
            </li>
          ))}
        </ul>

        <form onSubmit={sendMessage} style={{ marginTop: "1rem" }}>
          <input
            value={newMessage}
            onChange={(e) => setNewMessage(e.target.value)}
            placeholder="Type your message"
          />
          <button type="submit">Send</button>
        </form>
      </div>
    )
  );
};

export default Chat;
