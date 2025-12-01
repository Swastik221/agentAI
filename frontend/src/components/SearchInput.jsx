import React, { useState } from 'react';
import { Search, Loader2 } from 'lucide-react';
import { motion } from 'framer-motion';

const SearchInput = ({ onSearch, isLoading }) => {
  const [topic, setTopic] = useState('');
  const [isFocused, setIsFocused] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (topic.trim()) {
      onSearch(topic);
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="w-full max-w-3xl mx-auto p-6"
    >
      <form onSubmit={handleSubmit} className="flex flex-col gap-6">
        <div className="text-center space-y-2">
          <h2 className="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-violet-400">
            What do you want to research?
          </h2>
          <p className="text-gray-400">Enter a topic and let AI do the deep dive.</p>
        </div>

        <div className={`relative group transition-all duration-300 ${isFocused ? 'scale-105' : ''}`}>
          <div className="absolute -inset-1 bg-gradient-to-r from-blue-600 to-violet-600 rounded-2xl blur opacity-25 group-hover:opacity-75 transition duration-1000 group-hover:duration-200"></div>
          <div className="relative flex items-center bg-dark-800 rounded-xl border border-dark-700 shadow-2xl overflow-hidden">
            <Search className={`ml-4 w-6 h-6 ${isFocused ? 'text-blue-500' : 'text-gray-500'} transition-colors`} />
            <input
              type="text"
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              onFocus={() => setIsFocused(true)}
              onBlur={() => setIsFocused(false)}
              placeholder="e.g., Quantum Computing in 2025"
              className="w-full p-4 bg-transparent text-lg text-gray-100 placeholder-gray-500 focus:outline-none"
              disabled={isLoading}
            />
            <button
              type="submit"
              disabled={isLoading || !topic.trim()}
              className="m-2 px-6 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-lg font-semibold transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
            >
              {isLoading ? <Loader2 className="w-5 h-5 animate-spin" /> : 'Go'}
            </button>
          </div>
        </div>
      </form>
    </motion.div>
  );
};

export default SearchInput;
