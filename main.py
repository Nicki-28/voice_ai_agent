from core.stt import start_listening
from core.api_request import obtener_respuesta

while True:
    user_text= start_listening()
    
    respuesta = obtener_respuesta(user_text)
    
    print (respuesta)
    