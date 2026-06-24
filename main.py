from core.stt import start_listening
from core.api_request import obtener_respuesta
from core.tts import sintetizar_voz_inworld_stream as sintetizar_voz



def run():
    for user_text in start_listening():
        print("Heard:", user_text)
        if (user_text!=""):
            respuesta = obtener_respuesta(user_text)
            print("AI:", respuesta)
            sintetizar_voz(respuesta)
        else:
            exit

if __name__ == "__main__":
    run()
    