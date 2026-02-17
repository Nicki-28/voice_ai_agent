from config import API_KEY_ELEVEN
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os

load_dotenv()

def sintetizar_voz(texto):
   
    elevenlabs = ElevenLabs(
    api_key=os.getenv(API_KEY_ELEVEN),
    )

    audio = elevenlabs.text_to_speech.convert(
        text=texto,
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )

    play(audio)

  

