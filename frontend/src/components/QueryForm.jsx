import { useState } from "react";
import axios from "axios";

export default function QueryForm({ setResult }) {
  const [question, setQuestion] = useState("");
  const [cloudLink, setCloudLink] = useState("");
  const [remarks, setRemarks] = useState("");

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
    <form onSubmit={handleSubmit} className="space-y-4 p-4 bg-white shadow-xl rounded-2xl max-w-2xl mx-auto mt-10">
      <h1 className="text-xl font-bold text-gray-800">Natural Language Query</h1>
      <input
        type="text"
        placeholder="Enter your question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        className="w-full p-2 border border-gray-300 rounded"
      />

      <input
        type="text"
        placeholder="Prototype Cloud Link (Optional)"
        value={cloudLink}
        onChange={(e) => setCloudLink(e.target.value)}
        className="w-full p-2 border border-gray-300 rounded"
      />

      <textarea
        placeholder="Remarks or extra notes (Optional)"
        value={remarks}
        onChange={(e) => setRemarks(e.target.value)}
        className="w-full p-2 border border-gray-300 rounded"
      ></textarea>

      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Submit
      </button>
    </form>
  );
}
