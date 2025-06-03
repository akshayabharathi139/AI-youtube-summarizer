from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_video_metadata(video_id):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()

    if not response['items']:
        return None

    video = response['items'][0]['snippet']
    return {
        'title': video['title'],
        'description': video['description'],
        'tags': video.get('tags', [])
    }

def extract_video_id(url):
    import re
    match = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url)
    return match.group(1) if match else None
