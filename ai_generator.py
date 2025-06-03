import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_summary_hashtags_chapters(title, description, tags):
    prompt = f"""
Given the following YouTube video details:

Title: {title}
Description: {description}
Tags: {', '.join(tags)}

Generate:
1. A short and engaging video summary (2-3 sentences).
2. 5 relevant YouTube hashtags.
3. 3 suggested video chapters (timestamp format not required).

Format your response as:
Summary: ...
Hashtags: ...
Chapters:
- ...
- ...
- ...
"""
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']
