import React from 'react';
import ReactMarkdown from 'react-markdown';
import { FileText, Link2 } from 'lucide-react';
import { motion } from 'framer-motion';

const ReportViewer = ({ reportContent = "", sources = [] }) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.2 }}
      className="bg-dark-800/50 backdrop-blur-xl border border-dark-700 rounded-2xl p-8 shadow-xl"
    >
      <div className="flex items-center gap-3 mb-8 pb-6 border-b border-dark-700">
        <div className="p-3 bg-violet-500/10 rounded-xl">
          <FileText className="w-6 h-6 text-violet-400" />
        </div>
        <h2 className="text-2xl font-bold text-gray-100">Research Report</h2>
      </div>

      <div className="prose prose-invert prose-lg max-w-none mb-12">
        <ReactMarkdown
          components={{
            h1: ({ node, ...props }) => <h1 className="text-3xl font-bold text-blue-400 mb-6" {...props} />,
            h2: ({ node, ...props }) => <h2 className="text-2xl font-semibold text-gray-100 mt-8 mb-4" {...props} />,
            h3: ({ node, ...props }) => <h3 className="text-xl font-medium text-violet-400 mt-6 mb-3" {...props} />,
            p: ({ node, ...props }) => <p className="text-gray-300 leading-relaxed mb-4" {...props} />,
            ul: ({ node, ...props }) => <ul className="list-disc list-inside space-y-2 text-gray-300 mb-4" {...props} />,
            li: ({ node, ...props }) => <li className="marker:text-blue-500" {...props} />,
            strong: ({ node, ...props }) => <strong className="text-gray-100 font-semibold" {...props} />,
          }}
        >
          {reportContent}
        </ReactMarkdown>
      </div>

      <div className="bg-dark-900/50 rounded-xl p-6 border border-dark-700">
        <h3 className="flex items-center gap-2 text-lg font-semibold text-gray-200 mb-4">
          <Link2 className="w-5 h-5 text-gray-400" />
          Sources
        </h3>
        <ul className="grid gap-2">
          {sources.map((source, index) => (
            <li key={index}>
              <a
                href={source}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-2 text-sm text-blue-400 hover:text-blue-300 hover:underline transition-colors truncate"
              >
                <span className="w-1.5 h-1.5 rounded-full bg-blue-500 flex-shrink-0"></span>
                {source}
              </a>
            </li>
          ))}
        </ul>
      </div>
    </motion.div>
  );
};

export default ReportViewer;
