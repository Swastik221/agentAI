# AI Research & Intelligence Agent

An autonomous AI-powered research system that gathers information from Google Search, processes it using ChromaDB and GPT-4, and generates comprehensive research reports.

## Features

- **Deep Research**: Automated gathering of information from Google Search.
- **Vector Memory**: Uses ChromaDB to store and retrieve relevant context.
- **AI Analysis**: GPT-4 generates insights, credibility scores, and full reports.
- **Interactive UI**: React-based interface for easy interaction.
- **Export**: Download reports as PDF or JSON.

## System Architecture

![Architecture](docs/system_architecture.md)

## Setup

### Prerequisites

- Python 3.9+
- Node.js 16+
- OpenAI API Key
- Google Custom Search API Key & CSE ID

### Backend Setup

1. Navigate to `backend/`:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure `.env`:
   ```env
   OPENAI_API_KEY=your_key
   GOOGLE_API_KEY=your_key
   GOOGLE_CSE_ID=your_id
   ```
4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to `frontend/`:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```

## Usage

1. Open the frontend URL (usually `http://localhost:5173`).
2. Enter a research topic (e.g., "Future of Quantum Computing").
3. Wait for the agent to gather data and generate the report.
4. View insights and download the report.

## Tech Stack

- **Backend**: FastAPI, Python, ChromaDB, OpenAI SDK
- **Frontend**: React, Vite, Tailwind CSS
- **External APIs**: Google Custom Search, OpenAI API