import axios from "axios";
import { useState, useEffect } from "react";

import Register from "./Register";

function App() {
  useEffect(() => {
    axios.get("http://localhost:3000/").then((response) => {
      console.log("Response from server:", response.data);
    });
  }, []);

  return (
    <div>
      <h1>Basic User Auth Test</h1>

      <Register />
    </div>
  );
}

export default App;
