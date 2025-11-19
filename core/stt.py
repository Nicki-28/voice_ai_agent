from RealtimeSTT import AudioToTextRecorder
import json

palabra_detectada = False
query_list = []

def start_listening():

    def text_detected(text):
        global palabra_detectada, query_list

        texto = text.strip().lower()

        #Detectamos la wakeup word
        if not palabra_detectada:
            if "hey jarvis" in texto:
                print("he detectado la palabra, debo escribir lo que dices")
                palabra_detectada = True
            return  

       #guardar todo lo que diga
        query_list.append(texto)

        
        with open("query.json", "w", encoding="utf-8") as f:
            json.dump({"content": " ".join(query_list)}, f, indent=4, ensure_ascii=False)

    with AudioToTextRecorder(model="tiny") as recorder:
        print("Escuchando wake word...")
        while True:
            recorder.text(text_detected)

    return " ".join(query_list)
