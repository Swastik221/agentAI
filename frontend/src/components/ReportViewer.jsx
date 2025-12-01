import React from 'react';
import ReactMarkdown from 'react-markdown';

const ReportViewer = ({ reportContent, sources }) => {
  return (
    <div className="bg-white rounded-xl shadow-lg p-8">
      <h2 className="text-2xl font-bold text-gray-800 mb-6 border-b pb-4">Research Report</h2>
      <div className="prose prose-blue max-w-none mb-8">
        <ReactMarkdown>{reportContent}</ReactMarkdown>
      </div>

      <div className="mt-8 pt-6 border-t border-gray-200">
        <h3 className="text-lg font-semibold text-gray-700 mb-3">Sources</h3>
        <ul className="list-disc pl-5 space-y-1">
          {sources.map((source, index) => (
            <li key={index}>
              <a
                href={source}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-600 hover:underline break-all"
              >
                {source}
              </a>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default ReportViewer;
