import React from 'react';
import { Download, FileJson } from 'lucide-react';
import { motion } from 'framer-motion';

const DownloadButtons = ({ onDownloadJSON, onDownloadPDF }) => {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay: 0.4 }}
      className="flex gap-4 justify-end mt-8"
    >
      <button
        onClick={onDownloadJSON}
        className="flex items-center gap-2 px-6 py-3 bg-dark-800 hover:bg-dark-700 text-gray-300 rounded-xl font-medium transition-all border border-dark-700 hover:border-gray-600"
      >
        <FileJson className="w-5 h-5" />
        Download JSON
      </button>
      <button
        onClick={onDownloadPDF}
        className="flex items-center gap-2 px-6 py-3 bg-blue-600 hover:bg-blue-500 text-white rounded-xl font-medium transition-all shadow-lg shadow-blue-900/20 hover:shadow-blue-900/40 hover:-translate-y-0.5"
      >
        <Download className="w-5 h-5" />
        Download PDF
      </button>
    </motion.div>
  );
};

export default DownloadButtons;
