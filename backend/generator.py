from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_report(topic: str, context: list):
    """
    Generates a research report using OpenAI GPT.
    
    Args:
        topic (str): The research topic.
        context (list): List of strings containing search results/snippets.
        
    Returns:
        dict: A structured JSON report.
    """
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
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful and precise research assistant. You always output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content
        return json.loads(content)

    except Exception as e:
        print(f"Error generating report: {e}")
        return {
            "error": "Failed to generate report",
            "details": str(e)
        }

if __name__ == "__main__":
    # Test the generator
    test_topic = "AI in Healthcare"
    test_context = [
        "AI is used for early disease detection.",
        "Machine learning models predict patient outcomes.",
        "Robotic surgery is becoming more common."
    ]
    report = generate_report(test_topic, test_context)
    print(json.dumps(report, indent=2))
