import React from 'react';

const ResultsCard = ({ insights, credibilityScore }) => {
  return (
    <div className="bg-white rounded-xl shadow-lg p-6 mb-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-bold text-gray-800">Key Insights</h2>
        <div className="flex items-center gap-2">
          <span className="text-sm text-gray-500">Credibility Score:</span>
          <span className={`font-bold px-3 py-1 rounded-full ${credibilityScore >= 80 ? 'bg-green-100 text-green-700' :
              credibilityScore >= 60 ? 'bg-yellow-100 text-yellow-700' :
                'bg-red-100 text-red-700'
            }`}>
            {credibilityScore}/100
          </span>
        </div>
      </div>
      <ul className="space-y-3">
        {insights.map((insight, index) => (
          <li key={index} className="flex gap-3 items-start">
            <span className="flex-shrink-0 w-6 h-6 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center text-sm font-bold">
              {index + 1}
            </span>
            <p className="text-gray-700 leading-relaxed">{insight}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ResultsCard;
