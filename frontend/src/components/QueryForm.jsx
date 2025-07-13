import { useState } from "react";
import axios from "axios";

export default function QueryForm({ setResult }) {
  const [question, setQuestion] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!question.trim()) return alert("Please enter a query");

    try {
      const res = await axios.post("http://localhost:8000/query", {
        question,
      });
      setResult(res.data);
    } catch (err) {
      setResult({ status: "error", message: err.message });
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="space-y-6 p-8 bg-gradient-to-r from-sky-100 via-white to-indigo-100 shadow-2xl rounded-3xl max-w-xl mx-auto mt-20 border border-indigo-300"
    >
      <h1 className="text-2xl font-extrabold text-indigo-800 text-center">
        💬 Ask Your Data
      </h1>

      <input
        type="text"
        placeholder="Type your natural language query..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        className="w-full p-3 border border-indigo-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent text-gray-800 text-md placeholder-gray-500"
      />

      <button
        type="submit"
        className="w-full bg-indigo-600 text-white font-semibold px-4 py-3 rounded-lg hover:bg-indigo-700 transition-all duration-200 shadow-md"
      >
        🚀 Submit Query
      </button>
    </form>
  );
}
