# AI-youtube-summarizer


 Project Summary – AI-Powered YouTube Video Summarizer + Hashtag Generator
🔗 Takes a YouTube video URL as input and fetches metadata like title, description, and tags using the YouTube Data API v3.

🧠 Uses LLaMA 3 via Groq API to generate a short summary, relevant hashtags, and suggested video chapters from the metadata.

💻 Displays the results on a clean Streamlit UI for users to quickly view AI-generated content strategy.



🛠️ Technologies Used
Python

Streamlit – for web UI

YouTube Data API v3 – to fetch video metadata

Groq API + LLaMA 3 – for AI-powered text generation

Regex – to extract video IDs and clean text

Pandas – optional, for structured data handling

TextBlob – optional, for sentiment filtering or text cleaning





🧠 What is the Groq Model (LLaMA 3)?
Groq API provides blazing-fast inference using Meta's LLaMA 3 models.

LLaMA 3 is a state-of-the-art large language model capable of summarization, content generation, keyword extraction, and structured formatting.

With Groq's high-speed, low-latency infrastructure, responses are almost real-time, which is perfect for live web apps like Streamlit.
