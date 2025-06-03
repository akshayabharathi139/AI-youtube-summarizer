import streamlit as st
from youtube_api import get_video_metadata, extract_video_id
from ai_generator import generate_summary_hashtags_chapters
from utils import clean_description

st.set_page_config(page_title="YouTube AI Summarizer", layout="centered")

st.title("📼 YouTube AI Summarizer + Hashtag Generator")
video_url = st.text_input("Enter YouTube Video URL:")

if video_url:
    video_id = extract_video_id(video_url)
    
    if video_id:
        with st.spinner("Fetching video metadata..."):
            metadata = get_video_metadata(video_id)
        
        if metadata:
            st.subheader("🎬 Video Details")
            st.write(f"**Title:** {metadata['title']}")
            st.write(f"**Tags:** {', '.join(metadata.get('tags', []))}")
            
            with st.spinner("Generating AI content..."):
                cleaned_desc = clean_description(metadata['description'])
                result = generate_summary_hashtags_chapters(metadata['title'], cleaned_desc, metadata.get('tags', []))
                
            st.subheader("📄 AI Summary, Hashtags, and Chapters")
            st.text_area("Generated Content:", result, height=300)
        else:
            st.error("Video not found or invalid video ID.")
    else:
        st.warning("Could not extract video ID from the URL.")
