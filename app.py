import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# header for the Streamlit app
st.title("YouTube Video Summarizer")

# Display youtube thumbnail if a valid link is provided
youtube_video_url = st.text_input("Enter YouTube Video URL:")
if youtube_video_url:
    try:
        video_id = youtube_video_url.split("=")[1]
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/0.jpg"
        st.image(thumbnail_url, caption="YouTube Video Thumbnail", use_container_width=True)
    except Exception as e:
        st.error(f"Error fetching thumbnail: {e}")



prompt = """
You are a helpful assistant that summarizes the YouTube video into 250 words or less, highlighting the key points.
"""

# Function to extract transcript details from a YouTube video URL
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id)

        transcript_text = " ".join(
            item.text for item in transcript
        )
        return transcript_text

    except Exception as e:
        st.error(f"Error extracting transcript: {e}")
        return None

# Function to generate summary using Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-3.8-flash")
    response = model.generate_content([prompt, transcript_text])
    return response.text

# Button to fetch and display the detailed notes
if st.button("Get Detailed Notes"):
        transcript_text = extract_transcript_details(youtube_video_url)
        if transcript_text:
            summary = generate_gemini_content(transcript_text, prompt)
            st.markdown("Summary of the Video:")
            st.write(summary)

# Footer for the Streamlit app
st.markdown("""
---
""")