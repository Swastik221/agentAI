from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

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

class ResearchRequest(BaseModel):
    topic: str

@app.post("/research")
async def research(request: ResearchRequest):
    try:
        print(f"Received research request for: {request.topic}")
        
        # Check for API keys
        if not os.getenv("GOOGLE_API_KEY") or not os.getenv("OPENAI_API_KEY"):
            print("WARNING: Missing API keys. Returning MOCK DATA for demonstration.")
            import time
            time.sleep(2) # Simulate delay
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
        search_results = search_google(request.topic, num_results=7)
        if not search_results:
            return {"error": "No search results found."}
            
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
        print("Step 4: Generating Report...")
        report = generate_report(request.topic, context_docs)
        
        # 5. Quality Check (Basic)
        required_keys = ["topic", "insights", "credibility_score", "report_content", "sources"]
        if not citation_evaluator.validate_json_structure(report, required_keys):
             print("Warning: Generated report missing keys.")
        
        # Add source links from search results if not present or to ensure accuracy
        if "sources" not in report or not report["sources"]:
             report["sources"] = [m["source"] for m in metadatas[:5]]

        return report

    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "AI Research Agent Backend is running"}
