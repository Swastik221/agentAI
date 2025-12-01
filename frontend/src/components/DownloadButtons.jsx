import React from 'react';

const DownloadButtons = ({ onDownloadJSON, onDownloadPDF }) => {
  return (
    <div className="flex gap-4 justify-end mt-6">
      <button
        onClick={onDownloadJSON}
        className="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 font-medium transition-colors flex items-center gap-2"
      >
        <span>{ }</span> Download JSON
      </button>
      <button
        onClick={onDownloadPDF}
        className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium transition-colors flex items-center gap-2"
      >
        <span>{ }</span> Download PDF
      </button>
    </div>
  );
};

export default DownloadButtons;
