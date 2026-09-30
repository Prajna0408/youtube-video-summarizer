# YouTube Video Summarizer

A simple Streamlit application that extracts a YouTube video's transcript and uses a Google Gemini model to generate a concise summary of the video's key points.

## How it works

1. Enter a YouTube video URL.
2. The application extracts the video ID.
3. YouTube Transcript API retrieves the transcript.
4. The transcript is sent to a Gemini generative model.
5. The generated summary is displayed in the Streamlit interface.

## Tech stack

- Python
- Streamlit
- Google Gemini / Generative AI
- YouTube Transcript API
- python-dotenv

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Prajna0408/youtube-video-summarizer.git
cd youtube-video-summarizer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Copy `.env.example` to `.env`:

```powershell
Copy-Item .env.example .env
```

Then replace the placeholder with your own Google Gemini API key.

**Never commit `.env` or an API key to GitHub.**

### 5. Run the application

```bash
streamlit run app.py
```

The app opens in your browser and lets you enter a YouTube URL and generate a short summary.

## Project structure

```text
youtube-video-summarizer/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Notes

This is intentionally a small demonstration project showing a practical LLM workflow: retrieve external text, provide it as context to a generative model, and present the generated result through a simple UI.
