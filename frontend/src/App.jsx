import React, { useState, useRef } from 'react';
import { useReactToPrint } from 'react-to-print';
import SearchInput from './components/SearchInput';
import ResultsCard from './components/ResultsCard';
import ReportViewer from './components/ReportViewer';
import DownloadButtons from './components/DownloadButtons';

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const reportRef = useRef();

  const handleSearch = async (topic) => {
    setIsLoading(true);
    setError(null);
    setData(null);

    try {
      const response = await fetch('http://localhost:8000/research', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ topic }),
      });

      if (!response.ok) {
        throw new Error('Failed to fetch research data');
      }

      const result = await response.json();
      setData(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleDownloadJSON = () => {
    if (!data) return;
    const jsonString = `data:text/json;chatset=utf-8,${encodeURIComponent(
      JSON.stringify(data, null, 2)
    )}`;
    const link = document.createElement('a');
    link.href = jsonString;
    link.download = `research_report_${data.topic.replace(/\s+/g, '_')}.json`;
    link.click();
  };

  const handleDownloadPDF = useReactToPrint({
    content: () => reportRef.current,
    documentTitle: data ? `Research_Report_${data.topic}` : 'Research_Report',
  });

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto space-y-8">
        <header className="text-center space-y-4">
          <h1 className="text-4xl font-extrabold text-gray-900 tracking-tight">
            AI Research <span className="text-blue-600">Agent</span>
          </h1>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Autonomous deep research powered by Google Search & GPT-4.
          </p>
        </header>

        <SearchInput onSearch={handleSearch} isLoading={isLoading} />

        {error && (
          <div className="bg-red-50 border-l-4 border-red-500 p-4 rounded-md">
            <div className="flex">
              <div className="flex-shrink-0">
                <svg className="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                </svg>
              </div>
              <div className="ml-3">
                <p className="text-sm text-red-700">{error}</p>
              </div>
            </div>
          </div>
        )}

        {data && (
          <div className="space-y-8 animate-fade-in">
            <ResultsCard
              insights={data.insights}
              credibilityScore={data.credibility_score}
            />

            <div ref={reportRef}>
              <ReportViewer
                reportContent={data.report_content}
                sources={data.sources}
              />
            </div>

            <DownloadButtons
              onDownloadJSON={handleDownloadJSON}
              onDownloadPDF={handleDownloadPDF}
            />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
