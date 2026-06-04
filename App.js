import { useState } from "react";
import "./App.css";
import { FaShieldAlt } from "react-icons/fa";

function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const checkURL = async () => {
    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8001/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url }),
      });

      const data = await response.json();

      setTimeout(() => {
        setResult(data.prediction);
        setLoading(false);
      }, 1500);

    } catch (error) {
      console.log(error);
      setResult("Connection Error");
      setLoading(false);
    }
  };

  return (
    <div className="app">

      <div className="card">

        <FaShieldAlt className="icon" />

        <h1>AI Phishing URL Detector</h1>

        <p className="subtitle">
          Cloud-Based Cybersecurity Detection Platform
        </p>

        <input
          type="text"
          placeholder="Enter URL to scan..."
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />

        <button onClick={checkURL}>
          {loading ? "Scanning..." : "Scan URL"}
        </button>

        {result && (
          <div
            className={
              result === "phishing"
                ? "result phishing"
                : "result legitimate"
            }
          >
            {result.toUpperCase()}
          </div>
        )}

      </div>

    </div>
  );
}

export default App;