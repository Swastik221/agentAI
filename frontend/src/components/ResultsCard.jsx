import React from 'react';
import { motion } from 'framer-motion';
import { Lightbulb, CheckCircle, AlertTriangle } from 'lucide-react';

const ResultsCard = ({ insights = [], credibilityScore = 0 }) => {
  const container = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1
      }
    }
  };

  const item = {
    hidden: { opacity: 0, x: -20 },
    show: { opacity: 1, x: 0 }
  };

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      className="bg-dark-800/50 backdrop-blur-xl border border-dark-700 rounded-2xl p-8 shadow-xl"
    >
      <div className="flex justify-between items-center mb-8">
        <div className="flex items-center gap-3">
          <div className="p-3 bg-blue-500/10 rounded-xl">
            <Lightbulb className="w-6 h-6 text-blue-400" />
          </div>
          <h2 className="text-2xl font-bold text-gray-100">Key Insights</h2>
        </div>

        <div className="flex items-center gap-3 bg-dark-900/50 px-4 py-2 rounded-lg border border-dark-700">
          <span className="text-sm text-gray-400">Credibility Score</span>
          <div className={`flex items-center gap-2 font-bold ${credibilityScore >= 80 ? 'text-green-400' :
            credibilityScore >= 60 ? 'text-yellow-400' :
              'text-red-400'
            }`}>
            {credibilityScore >= 80 ? <CheckCircle className="w-4 h-4" /> : <AlertTriangle className="w-4 h-4" />}
            {credibilityScore}/100
          </div>
        </div>
      </div>

      <motion.ul
        variants={container}
        initial="hidden"
        animate="show"
        className="grid gap-4"
      >
        {insights.map((insight, index) => (
          <motion.li
            key={index}
            variants={item}
            className="group flex gap-4 p-4 rounded-xl bg-dark-700/30 hover:bg-dark-700/50 border border-transparent hover:border-dark-600 transition-all"
          >
            <span className="flex-shrink-0 w-8 h-8 bg-blue-500/20 text-blue-400 rounded-lg flex items-center justify-center text-sm font-bold group-hover:scale-110 transition-transform">
              {index + 1}
            </span>
            <p className="text-gray-300 leading-relaxed">{insight}</p>
          </motion.li>
        ))}
      </motion.ul>
    </motion.div>
  );
};

export default ResultsCard;
