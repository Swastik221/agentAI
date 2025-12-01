
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import sys
import os

# Add current directory to sys.path to allow importing local modules on Vercel
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import google.generativeai as genai
import json

# Import our modules
from google_search import search_google
from memory import ResearchMemory
from generator import generate_report
from quality import CitationEvaluator

load_dotenv()

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with specific origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Memory
memory = ResearchMemory()
citation_evaluator = CitationEvaluator()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class ResearchRequest(BaseModel):
    topic: str

@app.post("/api/research")
async def research(request: ResearchRequest):
    try:
        print(f"Received research request for: {request.topic}")
        
        # Check for API keys
        has_search_keys = os.getenv("GOOGLE_API_KEY") and os.getenv("GOOGLE_CSE_ID")
        has_llm_key = os.getenv("GEMINI_API_KEY")

        if not has_search_keys:
            print("WARNING: Missing Search API keys. Using MOCK SEARCH RESULTS.")
            
        if not has_llm_key:
            print("WARNING: Missing LLM API keys. Returning FULL MOCK DATA.")
            import time
            time.sleep(2)
            return {
                "topic": request.topic,
                "insights": [
                    "AI improves diagnostic accuracy in medical imaging.",
                    "Predictive analytics helps in patient care and resource management.",
                    "Robotic surgery is becoming more precise and common.",
                    "Privacy concerns regarding patient data are a major challenge.",
                    "AI reduces administrative burden on healthcare professionals.",
                    "Personalized medicine is advancing through genomic data analysis."
                ],
                "credibility_score": 85,
                "report_content": f"# Research Report: {request.topic}\n\n## Executive Summary\nArtificial Intelligence (AI) is rapidly transforming the healthcare industry. From early disease detection to personalized treatment plans, AI algorithms are enhancing the capabilities of medical professionals.\n\n## Key Findings\n\n### 1. Diagnostic Accuracy\nAI models, particularly in radiology and pathology, have shown the ability to detect anomalies with high precision, often matching or exceeding human experts.\n\n### 2. Operational Efficiency\nHospitals are using AI to optimize patient flow, manage staffing, and reduce wait times.\n\n### 3. Challenges\nDespite the benefits, integration challenges, data privacy issues, and the need for regulatory frameworks remain significant hurdles.\n\n## Conclusion\nThe future of healthcare is increasingly digital and data-driven, with AI playing a central role in improving patient outcomes.",
                "sources": [
                    "https://www.who.int/health-topics/artificial-intelligence",
                    "https://www.nature.com/articles/s41591-021-01614-0",
                    "https://www.healthcareitnews.com/topic/artificial-intelligence"
                ]
            }
        
        # 1. Google Search
        print("Step 1: Searching Google...")
        if has_search_keys:
            search_results = search_google(request.topic, num_results=7)
        else:
            # Mock search results for Gemini to process
            print("Generating realistic mock search results using Gemini...")
            mock_search_prompt = f"""
            Generate 5 realistic Google Search results for the topic: "{request.topic}".
            Return a JSON list of objects, each with "title", "snippet", and "link".
            The snippets should contain specific, factual details relevant to the topic.
            """
            try:
                model = genai.GenerativeModel('gemini-flash-latest')
                response = model.generate_content(mock_search_prompt)
                content = response.text.strip()
                if content.startswith("```json"):
                    content = content[7:-3]
                elif content.startswith("```"):
                    content = content[3:-3]
                search_results = json.loads(content)
            except Exception as e:
                print(f"Failed to generate mock results: {e}")
                # Fallback to static mock data if generation fails
                search_results = [
                    {"title": f"{request.topic} - Comprehensive Guide", "snippet": f"A detailed guide covering the basics, history, and future of {request.topic}.", "link": f"https://www.techtarget.com/search/{request.topic.replace(' ', '-')}"},
                    {"title": f"The Future of {request.topic}", "snippet": f"Experts predict how {request.topic} will evolve over the next decade.", "link": f"https://www.forbes.com/sites/future-tech/{request.topic.replace(' ', '-')}"},
                    {"title": f"Top Trends in {request.topic} for 2024", "snippet": f"Analysis of the latest trends and innovations in the field of {request.topic}.", "link": f"https://www.wired.com/story/{request.topic.replace(' ', '-')}-trends"},
                    {"title": f"Benefits and Risks of {request.topic}", "snippet": f"Understanding the pros and cons of implementing {request.topic} in various industries.", "link": f"https://hbr.org/2024/01/{request.topic.replace(' ', '-')}-analysis"},
                    {"title": f"{request.topic}: What You Need to Know", "snippet": f"Key concepts, terminology, and real-world applications of {request.topic}.", "link": f"https://www.mit.edu/technology-review/{request.topic.replace(' ', '-')}"}
                ]

        if not search_results:
            print("Error: No search results found.")
            return {"error": "No search results found."}
            
        print(f"Found {len(search_results)} search results.")
            
        # 2. Store in Memory
        print("Step 2: Storing in Memory...")
        documents = [f"{res['title']}: {res['snippet']}" for res in search_results]
        metadatas = [{"source": res['link'], "title": res['title']} for res in search_results]
        memory.add_documents(documents, metadatas)
        
        # 3. Retrieve Context
        print("Step 3: Retrieving Context...")
        # We can query for the topic itself or sub-aspects. 
        # For simplicity, we query the main topic.
        context_results = memory.query_documents(request.topic, n_results=5)
        context_docs = context_results['documents'][0]
        
        # 4. Generate Report
        # 4. Generate Report
        print("Step 4: Generating Report...")
        try:
            report_data = generate_report(request.topic, context_docs)
            print(f"Report generated. Keys: {list(report_data.keys())}")
        except Exception as e:
            print(f"Generator Error: {e}")
            return {"error": str(e)}
        
        if "error" in report_data:
            return report_data
        
        # 5. Quality Check (Basic)
        required_keys = ["topic", "insights", "credibility_score", "report_content", "sources"]
        if not citation_evaluator.validate_json_structure(report_data, required_keys):
             pass # Removed print statement
        
        # Add source links from search results if not present or to ensure accuracy
        if "sources" not in report_data or not report_data["sources"]:
             report_data["sources"] = [m["source"] for m in metadatas[:5]]

        return report_data

    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
@app.get("/api")
@app.get("/api/")
async def root():
    return {"message": "AI Research Agent Backend is running"}
