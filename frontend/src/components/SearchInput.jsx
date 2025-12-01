import React, { useState } from 'react';

const SearchInput = ({ onSearch, isLoading }) => {
  const [topic, setTopic] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (topic.trim()) {
      onSearch(topic);
    }
  };

  return (
    <div className="w-full max-w-2xl mx-auto p-6">
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <label htmlFor="topic" className="text-2xl font-bold text-gray-800 text-center">
          What do you want to research?
        </label>
        <div className="relative">
          <input
            type="text"
            id="topic"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            placeholder="e.g., Artificial Intelligence in Healthcare"
            className="w-full p-4 pr-12 text-lg border-2 border-gray-300 rounded-xl focus:border-blue-500 focus:outline-none shadow-sm transition-all"
            disabled={isLoading}
          />
          <button
            type="submit"
            disabled={isLoading || !topic.trim()}
            className="absolute right-2 top-2 bottom-2 bg-blue-600 text-white px-6 rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400 transition-colors"
          >
            {isLoading ? 'Searching...' : 'Go'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default SearchInput;
