# Voice AI Agent 🤖

This project is an **experimental intelligent voice agent** that allows users to interact with a personal assistant called *Jarvis* via voice (can you tell i'm a marvel fan? ahah). The agent converts speech to text, processes the request through an AI backend, and responds using Text-to-Speech.

⚠️ **Super experimental:** this is a prototype to test ideas quickly. I used **Eleven Labs TTS** for voice output, **Sonar (Perplexity API)** for the chatbot backend, everything is **Dockerized**, and it's a **pure backend setup** (no Flask frontend). Highly improvable—just a sandbox of ideas that made sense in my head.

---

## 🔹 Features

- **Wake word activation**: the agent only listens when a wake word is spoken, e.g., `"Hey Jarvis!"`.
- **Real-time Speech-to-Text (STT)**: transcribes user speech as it happens.
- **Text-to-Speech (TTS) with Eleven Labs**: responds with natural-sounding voice.
- **Adaptive personality**: the agent adapts its tone and style based on the person talking.
- **Tone in responses**: each reply includes an emotional tone in brackets, e.g., `[calm]`, `[laughs nervously]`, `[excited]`.
- **Real-time processing using silences**: the agent detects pauses and uses them to process responses with timeouts.
- **Simple memory**: interactions are stored to maintain conversational context.
- **Direct backend integration**: the STT transcription is sent as text to the Sonar (Perplexity) API.

---

## 🔹 Technologies

- Python 3.10+
- [RealTimeSTT](https://github.com/OpenAI/RealTimeSTT) for STT, wake word, and TTS
- Eleven Labs TTS API
- Sonar (Perplexity API) for chatbot intelligence
- FastAPI for backend (pure API, no frontend)
- Docker for containerization
- JSON for data exchange

---
- To use the agent, clone the repository (`git clone https://github.com/Nicki-28/voice_ai_agent.git`)
- install dependencies (`pip install -r requirements.txt`), and run it with Docker (`docker compose up`). 
 
---
## 🔹 Technologies

Speak to the agent using the wake word, for example: "Hey Jarvis, what is the most famous singer in the world?" and it will respond in real-time, adapting to your personality, using silences to detec when you finish speaking, and maintaining conversation context.

 ---
## 🔹 Improvements
 Potential improvements include support for multiple wake words, advanced memory and context handling, external TTS voices, optimizing response time, and adding a proper frontend interface.


