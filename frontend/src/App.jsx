import { useState } from "react";
import QueryForm from "./components/QueryForm";
import ResultDisplay from "./components/ResultDisplay";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-gray-50">
      <QueryForm setResult={setResult} />
      <ResultDisplay result={result} />
    </div>
  );
}

export default App;
