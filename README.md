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
Anti_Rot/
├── Client Side/            # Chrome Extension (runs on user’s browser)
│   ├── icons/              # Extension icons used by Chrome UI
│   │   ├── icon16.png
│   │   ├── icon48.png
│   │   └── icon128.png
│   ├── manifest.json       # Core config file that defines permissions, scripts, and extension metadata
│   ├── background.js       # Background service worker; handles events, messaging, and persistent logic
│   ├── content.js          # Injected into YouTube pages; extracts URL/transcript + manipulates DOM
│   ├── content.css         # Styles applied directly to the YouTube page by content.js
│   ├── popup.html          # UI layout for extension popup
│   ├── popup.css           # Styling for popup interface
│   └── popup.js            # Logic for popup interactions and user actions
│
├── Server/                 # Backend API (Dockerized for cloud deployment)
│   ├── server.py           # Main backend entrypoint
│   ├── requirements.txt
│   ├── Dockerfile          # Container build instructions for GCP deployment (gitignored)
│   └── .env                # API keys + system prompts (gitignored)
│
├── Testing/
│   ├── Logic.py            # Early prototype logic
│   ├── testclient.py       # (gitignored)
│   └── .env                # API keys + system prompts (gitignored)
│
├── README.md               # Project overview, setup steps, architecture notes
├── todo.md                 # Task tracking, feature ideas, roadmap notes
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
- Version: Beta 0.4
- Current Development Stage: Prototype 
- With Love, [@prshv1](https://linktr.ee/prshv1)