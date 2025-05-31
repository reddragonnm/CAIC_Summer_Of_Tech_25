import axios from "axios";
import { useState, useEffect } from "react";

function App() {
  useEffect(() => {
    axios
      .get("https://jsonplaceholder.typicode.com/posts")
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }, []);

  const [index, setIndex] = useState(0);

  return (
    <div className="App">
      <h1>Hello World!</h1>
      <p>Current Index: {index}</p>
      <button onClick={() => setIndex(index + 1)}>Increment Index</button>
    </div>
  );
}

export default App;
