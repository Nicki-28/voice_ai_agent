from RealtimeSTT import AudioToTextRecorder
import pyautogui
import json
#quiero que empiece a escuchar cuando escuche la wakeup word

palabra_detectada = False
query_list=[]

def start_listening ():

    def text_detected(text):
        global palabra_detectada
        global query_list
        
        texto = text.strip().lower()
        if not palabra_detectada:
                if "hey jarvis" in texto:
                    palabra_detectada = True
                    query_list.append(texto)    
                return
        query_list.append(texto)
                
    #guardamos en un json 
        with open("query.json", "w", encoding="utf-8") as f:
            json.dump({"content": " ".join(query_list)}, f, indent=4, ensure_ascii=False)
            
        with AudioToTextRecorder(model="tiny") as recorder:
            while not palabra_detectada:
                recorder.text(text_detected)
            print("Wake word detectada, empieza a transcribir!")
    return " ".join(query_list)
            

    