# Anti-Rot

Chrome extension + Python backend that automatically blocks non valuable YouTube videos.

## How It Works

- You browse YouTube normally
- Extension detects when you open a video, extracts the URL
- Backend extracts the transcript via `yt-dlp`
- LLM classifies: educational or distraction
- non valuable? Page gets replaced with a "Time is valuable" screen
- Valuable? Nothing happens, keep watching

**Prerequisites:** Chromium Based Browsere

## How to install

1. Go to, "Chrome Webstore Link"
2. Install The extension
3. Sign-Up or Log-IN

## Project Structure

```
yt-focus/
├── extension/             #Deployed Client Side
│   ├── manifest.json
│   ├── content.js
│   └── background.js
├── server/                # Deployed on Google Cloud
│   ├── main.py            # Main Logic
|   ├── Server.py          # Logic Optimized for Docker & GCP
│   ├── requirements.txt   # Python deps
│   └── .env               # API key & System Prompt (gitignored)
├── Testing
│   ├── Logic.py           # basic logic i wrote while protyping
│   ├── testclient.py.     # For testing APIs, and troubleshooting (gitignored)
│   └── .env               # API key & System Prompt (gitignored)
|   README.md
└── .gitignore
```
## Skills Learned
- Creating APIs
- Deploying Docker on GCP
- Managing User Acounts
- Working With LLMs
- creating Simple and Usefull software

## Upcoming Features
- Custom Preferances to decide Valuable/non valuable videos
- Support for videos which aren't in english
- Hide Distracting UI elements, Like Unhook
- Support Extended to sites outside of youtube

## Development Info
- Version: Beta 0.2 
- Current Development Stage: Prototype 
- With Love, [@prshv1](https://linktr.ee/prshv1)