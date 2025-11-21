from core.stt import start_listening
from core.api_request import obtener_respuesta


def run():
    for user_text in start_listening():
        print("Heard:", user_text)
        respuesta = obtener_respuesta(user_text)
        print("AI:", respuesta)

if __name__ == "__main__":
    run()
    