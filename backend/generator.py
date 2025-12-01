import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

def configure_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: Missing GEMINI_API_KEY")
        return False
    genai.configure(api_key=api_key)
    return True

def generate_report(topic: str, context: list):
    """
    Generates a research report using Google Gemini.
    
    Args:
        topic (str): The research topic.
        context (list): List of strings containing search results/snippets.
        
    Returns:
        dict: A structured JSON report.
    """
    if not configure_gemini():
        return {"error": "Gemini API key not configured"}

    context_str = "\n\n".join(context)
    
    prompt = f"""
    You are an advanced AI Research Assistant. Your goal is to generate a comprehensive, professional research report on the topic: "{topic}".
    
    Use the following gathered information as your primary source:
    {context_str}
    
    Your output MUST be a valid JSON object with the following structure:
    {{
        "topic": "{topic}",
        "insights": [
            "Insight 1",
            "Insight 2",
            "...",
            "Insight 6"
        ],
        "credibility_score": <integer between 0 and 100>,
        "report_content": "<A detailed 400-600 word research report in markdown format. Use headers, bullet points, and clear paragraphs.>",
        "sources": [
            "List of source URLs used"
        ]
    }}
    
    Ensure the "report_content" is high-quality, objective, and well-structured.
    Do not include any text outside the JSON object.
    """

    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        # Clean up response text to ensure it's valid JSON
        content = response.text.strip()
        if content.startswith("```json"):
            content = content[7:-3]
        elif content.startswith("```"):
            content = content[3:-3]
            
        return json.loads(content)

    except Exception as e:
        print(f"Error generating report: {e}")
        return {
            "error": "Failed to generate report",
            "details": str(e)
        }

if __name__ == "__main__":
    # Test the generator
    os.environ["GEMINI_API_KEY"] = "TEST_KEY" # Placeholder
    test_topic = "AI in Healthcare"
    test_context = ["AI is transforming healthcare."]
    # report = generate_report(test_topic, test_context)
    # print(report)
