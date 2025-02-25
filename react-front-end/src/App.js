import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import Scene from "./components/Scene";
import Test from "./components/Test";

function App() {
  const [message, setMessage] = useState(0);

  // Proxy in  package.json is set to be 127.0.0.1 not localhost
  useEffect(() => {
    fetch('/message').then(res => res.json()).then(data => {
      setMessage(data.message);
    });
  }, []);

  return (
    <div className="App">
      <div>
        <Test />
      </div>
    </div>
  );
}

export default App;


