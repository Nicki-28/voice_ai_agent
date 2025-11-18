from RealtimeSTT import AudioToTextRecorder
import pyautogui
import json
#quiero que empiece a escuchar cuando escuche la wakeup word

palabra_detectada = False
query_list=[]

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
        
if __name__ == "__main__":
    print("*Escuchando...*")
    
    with AudioToTextRecorder(model="tiny") as recorder:
        while True:
            recorder.text(text_detected)
           

   