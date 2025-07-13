import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

export default function ResultDisplay({ result }) {
  if (!result) return null;

  if (result.status === "error") {
    return <p className="text-red-500 text-center mt-4">{result.message}</p>;
  }

  const data = result.data;

  if (!data || !data.data || data.data.length === 0) {
    return <p className="text-center text-gray-500 mt-4">No data found.</p>;
  }

  if (data.type === "text") {
    return <p className="text-lg p-4">{data.data}</p>;
  }

  if (data.type === "table") {
    const headers = Object.keys(data.data[0]);

    return (
      <div className="overflow-x-auto p-4">
        <table className="table-auto w-full border-collapse border border-gray-300">
          <thead>
            <tr>
              {headers.map((col, idx) => (
                <th key={idx} className="border p-2 bg-gray-100">{col}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.data.map((row, idx) => (
              <tr key={idx}>
                {headers.map((header, i) => (
                  <td key={i} className="border p-2">{row[header]}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }

    if (data.type === "graph") {
    const firstRow = data.data[0];
    const labelKey = Object.keys(firstRow)[0];
    const valueKey = Object.keys(firstRow)[1];

    const chartData = {
      labels: data.data.map((item) => item[labelKey]),
      datasets: [
        {
          label: valueKey,
          data: data.data.map((item) => item[valueKey]),
          backgroundColor: "rgba(59, 130, 246, 0.7)",
        },
      ],
    };

    return (
      <div className="p-4">
        <Bar data={chartData} />
      </div>
    );
  }

  return (
    <p className="text-center text-gray-500 mt-4">
      Unknown result type. Cannot render output.
    </p>
  );
}
