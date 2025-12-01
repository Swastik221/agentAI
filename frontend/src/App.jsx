import React, { useState, useRef } from 'react';
import { useReactToPrint } from 'react-to-print';
import { BrainCircuit } from 'lucide-react';
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
      const response = await fetch('/api/research', {
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
    <div className="min-h-screen text-gray-100 selection:bg-blue-500/30">
      {/* Background Blobs */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none -z-10">
        <div className="absolute top-0 left-1/4 w-96 h-96 bg-blue-600/20 rounded-full blur-3xl animate-blob"></div>
        <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-violet-600/20 rounded-full blur-3xl animate-blob animation-delay-2000"></div>
      </div>

      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <header className="text-center mb-16 space-y-4">
          <div className="flex justify-center mb-6">
            <div className="p-4 bg-dark-800 rounded-2xl border border-dark-700 shadow-2xl">
              <BrainCircuit className="w-12 h-12 text-blue-500" />
            </div>
          </div>
          <h1 className="text-5xl font-extrabold tracking-tight">
            AI Research <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-violet-400">Agent</span>
          </h1>
          <p className="text-xl text-gray-400 max-w-2xl mx-auto">
            Autonomous deep research powered by Google Search & GPT-4.
          </p>
        </header>

        <SearchInput onSearch={handleSearch} isLoading={isLoading} />

        {error && (
          <div className="mt-8 bg-red-500/10 border border-red-500/20 p-4 rounded-xl text-red-400 text-center animate-fade-in">
            {error}
          </div>
        )}

        {data && (
          <div className="mt-16 space-y-12">
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
