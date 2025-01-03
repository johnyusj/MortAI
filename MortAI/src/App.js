// src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [message, setMessage] = useState("");

  useEffect(() => {
    // Make GET request to FastAPI
    axios.get("http://localhost:8000/api/greet")
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(error => {
        console.error("There was an error making the request!", error);
      });
  }, []);

  return (
    <div>
      <h1>FastAPI and React</h1>
      <p>{message}</p>
    </div>
  );
};

export default App;