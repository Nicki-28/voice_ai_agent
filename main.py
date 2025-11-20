from core.stt import start_listening
from core.api_request import obtener_respuesta


def run():
    user_text = start_listening()
    print("Heard:", user_text)
    respuesta = obtener_respuesta(user_text)
    print("AI:", respuesta)

if __name__ == "__main__":
    run()
    