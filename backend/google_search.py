import os
import requests
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

def search_google(query: str, num_results: int = 5):
    """
    Searches Google using the Custom Search JSON API.
    
    Args:
        query (str): The search topic.
        num_results (int): Number of results to return.
        
    Returns:
        list: A list of dictionaries containing title, snippet, and link.
    """
    if not GOOGLE_API_KEY or not GOOGLE_CSE_ID:
        print("Error: Missing Google API Key or CSE ID.")
        return []

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": query,
        "num": num_results
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        results = []
        if "items" in data:
            for item in data["items"]:
                results.append({
                    "title": item.get("title"),
                    "snippet": item.get("snippet"),
                    "link": item.get("link")
                })
        return results

    except requests.exceptions.RequestException as e:
        print(f"Google Search API Error: {e}")
        return []

if __name__ == "__main__":
    # Test the function
    test_topic = "Artificial Intelligence in Healthcare"
    print(f"Searching for: {test_topic}")
    results = search_google(test_topic, num_results=3)
    for i, res in enumerate(results, 1):
        print(f"{i}. {res['title']}\n   {res['link']}\n   {res['snippet']}\n")
