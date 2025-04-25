from typing import Any, Dict
import requests

GEMINI_API_URL = "https://api.gemini.com/v1/summarize"  # Replace with the actual Gemini API endpoint
API_KEY = "your_api_key"  # Replace with your actual API key

def summarize_document(file_content: str, file_type: str) -> Dict[str, Any]:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    payload = {
        "content": file_content,
        "type": file_type
    }
    
    response = requests.post(GEMINI_API_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()  # Raise an error for bad responses
