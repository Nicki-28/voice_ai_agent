from RealtimeSTT import AudioToTextRecorder
import json
import time

palabra_detectada = False
query_list = []

def start_listening(timeout_silence=0.5):
    global palabra_detectada, query_list

    last_heard_time = None

    def text_detected(text):
        nonlocal last_heard_time
        global palabra_detectada, query_list

        texto = text.strip().lower()
        current_time = time.time()

        # wake word
        if not palabra_detectada:
            if "hey jarvis" in texto:
                #DEBUGGING
                print("Wake word detectada, empiezo a transcribir...")
                palabra_detectada = True
                last_heard_time = current_time
            return

        # Guardar todo lo que diga
        if texto:
            query_list.append(texto)
            last_heard_time = current_time

        
        with open("query.json", "w", encoding="utf-8") as f:
            json.dump({"content": " ".join(query_list)}, f, indent=4, ensure_ascii=False)

    with AudioToTextRecorder(
            model="tiny",
            post_speech_silence_duration=0.2,
            silero_deactivity_detection= True
        ) as recorder:
            while True:
                recorder.text(text_detected)
                if palabra_detectada and last_heard_time:
                    if time.time() - last_heard_time > timeout_silence:
                        #DEBUGGING
                        print("Silencio detectado, terminando captura.")
                        break

    return " ".join(query_list)