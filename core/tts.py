import requests
import json
import base64
import io
import wave
import pyaudio
import threading
import queue
from config import INWORLD_API_KEY


def _extraer_pcm(chunk_wav: bytes) -> bytes:
    #extraemos la cabecera datos iworld
    with wave.open(io.BytesIO(chunk_wav), "rb") as wf:
        return wf.readframes(wf.getnframes())


def sintetizar_voz_inworld_stream(texto):
    url = "https://api.inworld.ai/tts/v1/voice:stream"

    headers = {
        "Authorization": f"Basic {INWORLD_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "text": texto,
        "voiceId": "Felix",
        "modelId": "inworld-tts-2",
        "audioConfig": {
            "audioEncoding": "LINEAR16",
            "sampleRateHertz": 48000
        }
    }

    response = requests.post(url, headers=headers, json=payload, stream=True)
    response.raise_for_status()  
    
    # hilo 1 tira audio
    cesta_audio = queue.Queue()

    # hilo 2 reproduce
    def trabajador_reproductor():
        p = pyaudio.PyAudio()
        stream = p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=48000,
            output=True,
            frames_per_buffer=2048, 
        )

        buffer_interno = b""

        while True:
            chunk = cesta_audio.get()

            if chunk is None:  
                break

            buffer_interno += chunk

            if len(buffer_interno) >= 8192:
                bytes_pares = (len(buffer_interno) // 2) * 2
                chunk_perfecto = buffer_interno[:bytes_pares]
                stream.write(chunk_perfecto)
                buffer_interno = buffer_interno[bytes_pares:]

        if len(buffer_interno) > 1:
            bytes_finales = (len(buffer_interno) // 2) * 2
            stream.write(buffer_interno[:bytes_finales])

        stream.stop_stream()
        stream.close()
        p.terminate()

    # hilo 2
    hilo_audio = threading.Thread(target=trabajador_reproductor)
    hilo_audio.start()

    print("Jarvis está hablando (Multihilo)...")

    #hilo 1 desempaqueta los chunks
    for linea in response.iter_lines():
        if not linea:
            continue

        datos = json.loads(linea)

        if "error" in datos:
            print("ERROR DE INWORLD:", datos)
            break

        audio_b64 = datos.get("result", {}).get("audioContent")
        if not audio_b64:
            continue

        chunk_wav = base64.b64decode(audio_b64)

        try:
            pcm = _extraer_pcm(chunk_wav)
        except wave.Error:
            # fallback de seguridad: si algún chunk llegara sin cabecera válida
            pcm = chunk_wav

        cesta_audio.put(pcm)


    cesta_audio.put(None)
    hilo_audio.join()

    print("Jarvis ha terminado de hablar.")