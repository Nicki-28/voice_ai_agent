# 🎙️ Voice AI Agent (a.k.a. Budget Jarvis)

Because typing is so 2022. 

A modular, ultra-fast voice assistant designed to maintain fluid, natural, and real-time conversations. This project integrates speech-to-text (STT), ultra-low latency natural language processing (LLM), and bidirectional streaming text-to-speech (TTS) so you can finally feel like Tony Stark.


## ✨ Key Features

* **Active Listening (It actually listens):** Uses `RealtimeSTT` to detect when you speak, transcribe your voice instantly, and elegantly cut the recording as soon as you finish your sentence. 
* **Big Brain Energy:** Powered by **Groq** to generate coherent, personality-driven responses at a fast speed.
* **Memory:** Saves the conversation context in a local file (`context.json`) so it actually remembers what you talked about 5 minutes ago (unlike most humans).
* **Real-Time Voice (Zero Latency):** We ditched the slow engines and hooked up **Inworld AI**. It injects audio chunks directly into the `mpv` player via command line, meaning Jarvis starts speaking practically before he finishes thinking.

---

## 🛠️ Tech Stack

* **Language:** Python 3.11+ 
* **Ears (STT):** RealtimeSTT
* **Brain (LLM):** Groq API
* **Mouth (TTS):** Inworld AI API (HTTP Streaming)
* **Vocal Cords (Audio Player):** `mpv` (for real-time raw audio decoding without blowing out your speakers)

---

## 🚀 Prerequisites

Before waking up the AI on your local machine (Mac/Linux), make sure you have the following tools installed so it doesn't sound like a broken dial-up modem:

1. Install the background audio player:
   `brew install mpv`
2. Install Node.js and the Inworld CLI (optional, but highly recommended for debugging voices like a pro):
   `sudo npm install -g @inworld/cli`

---

## 📦 Installation & Setup

1. Clone this repository and bring it to your local machine:
   `git clone https://github.com/Nicki-28/voice_ai_agent.git`
2. Navigate to the base:
   `cd voice_ai_agent`
3. Create and activate a virtual environment:
   `python3 -m venv .venv`
   `source .venv/bin/activate`
4. Install dependencies:
   `pip install -r requirements.txt`
5. Configure your credentials by creating a `.env` file or setting up `config.py` with your keys. (Please, do not upload this to GitHub):
   `INWORLD_API_KEY="your_base64_key_with_write_permissions"`
   `GROQ_API_KEY="your_groq_api_key"`

---

## 💻 Usage

Put on your Iron Man suit and run the main module from the root of the project. Jarvis will automatically start listening to your microphone:

`python3 main.py`

---

## 🗺️ Roadmap / Next Steps

* Create a simple visual interface (Frontend) using Streamlit or Gradio (so we have something pretty to look at).
* Implement concurrency (async/threading) to allow interrupting Jarvis while he speaks (because sometimes AI talks too much).
* Containerize the final version using Docker.
