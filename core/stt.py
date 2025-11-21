from RealtimeSTT import AudioToTextRecorder
import numpy as np
import json
import time

palabra_detectada = False
query_list = []

# almacenar el último chunk recibido
ultimo_chunk = None

def is_silence(audio_chunk, threshold=0.08):
    """
    audio_chunk: numpy array en rango -1..1
    """
    if audio_chunk is None or len(audio_chunk) == 0:
        return True

    # bytearray-int16
    if isinstance(audio_chunk, (bytes, bytearray)):
        audio_chunk = np.frombuffer(audio_chunk, dtype=np.int16)
    print("RMS actual:", np.sqrt(np.mean((audio_chunk.astype(np.float32)/32768.0)**2)))

    # Normalizar a -1..1
    audio_chunk = audio_chunk.astype(np.float32) / 32768.0

    rms = np.sqrt(np.mean(np.square(audio_chunk)))
    return rms < threshold



def start_listening(timeout_silence=0.2, absolute_timeout=10.0):
    global palabra_detectada, query_list, ultimo_chunk

    last_heard_time = None
    start_time = None
    ultimo_chunk = None

    def on_chunk(audio_np):
        nonlocal last_heard_time
        global ultimo_chunk

        # el chunk para analizar silencio en el bucle principal
        ultimo_chunk = audio_np


    def text_detected(text):
        nonlocal last_heard_time, start_time
        global palabra_detectada, query_list

        texto = text.strip().lower()
        current_time = time.time()

        # wake word
        if not palabra_detectada:
            if "hey jarvis" in texto:
                print("Wake word detectada, empiezo a transcribir...")
                palabra_detectada = True
                last_heard_time = current_time
                start_time = current_time
            return

        
        if texto:
            query_list.append(texto)
            last_heard_time = current_time

        with open("query.json", "w", encoding="utf-8") as f:
            json.dump({"content": " ".join(query_list)}, f, indent=4, ensure_ascii=False)


    with AudioToTextRecorder(
            model="tiny",
            post_speech_silence_duration=0.2,
            silero_deactivity_detection=True,
            silero_sensitivity=0.7,
            webrtc_sensitivity=3,
            silero_use_onnx=False,
            language='en',
            on_recorded_chunk=on_chunk 
        ) as recorder:
        
        while True:
            recorder.text(text_detected)

            if palabra_detectada:
                current_time = time.time()

                
                chunk = ultimo_chunk

                if chunk is not None and not is_silence(chunk):
                    last_heard_time = current_time

                # Timeout por silencio
                if last_heard_time and (current_time - last_heard_time > timeout_silence):
                    print("Silencio detectado, terminando captura.")
                    break

                # Timeout absoluto
                if start_time and (current_time - start_time > absolute_timeout):
                    print("Timeout absoluto alcanzado, terminando captura.")
                    break

    return " ".join(query_list)
