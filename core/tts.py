import subprocess
import requests
import json
import base64
from config import INWORLD_API_KEY

def sintetizar_voz_inworld_stream(texto):
    url = "https://api.inworld.ai/tts/v1/voice:stream"
    headers = {
        "Authorization": f"Basic {INWORLD_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": texto,
        "voiceId": "Ashley", 
        "modelId": "inworld-tts-1.5-mini" 
    }
    

    reproductor = subprocess.Popen(
        ["mpv", "--no-cache", "--no-terminal", "--", "-"],
        stdin=subprocess.PIPE
    )
    
    # petición iworld
    response = requests.post(url, headers=headers, json=payload, stream=True)
    
    # procesamos 
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line)
            if "result" in chunk and "audioContent" in chunk["result"]:
                audio_data = base64.b64decode(chunk["result"]["audioContent"])
                
                reproductor.stdin.write(audio_data)
                reproductor.stdin.flush() 
                print(f"Reproduciendo fragmento MP3: {len(audio_data)} bytes")
    
    reproductor.stdin.close()
    reproductor.wait()
    print("Jarvis ha terminado de hablar.")