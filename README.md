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






📦 requirements.txt
txt
Copy
Edit
streamlit==1.35.0
requests==2.31.0
google-api-python-client==2.127.0
textblob==0.18.0
python-dotenv==1.0.1









📘 Commands to Add in README.md
md
Copy
Edit
## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/youtube-summarizer-groq.git
cd youtube-summarizer-groq
2. Create and Activate a Virtual Environment
bash
Copy
Edit
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the root directory and add:

env
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
YOUTUBE_API_KEY=your_youtube_data_api_key_here
🛡️ Never share your .env or commit it to version control!

5. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
