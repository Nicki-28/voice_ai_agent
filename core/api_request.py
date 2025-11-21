import requests
import json
from config import API_KEY_SONAR
from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import os
from core.memoriaChat import cargar_memoria, guardar_memoria

app = Flask(__name__)
CORS(app)

url = "https://api.perplexity.ai/chat/completions" 

headers = {
    "Authorization": f"Bearer {API_KEY_SONAR}",
    "Content-Type": "application/json"
}

def guardar_respuesta(respuesta):
    file_path = "query.json"
    
    # Inicializar data como lista
    data = []
    
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                # Si el JSON no es una lista, lo convertimos a lista
                if not isinstance(data, list):
                    data = [data]
            except json.JSONDecodeError:
                data = []

    # Añadir la nueva respuesta como dict
    data.append({"content": respuesta})

    output= "output.json"
    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

        

def obtener_respuesta(query_str):
    historial = cargar_memoria()

    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI assistant named Jarvis, and the user will ask questions or ask for advice. "
                "Your job is to reply in a useful and clear way, with a tone that reflects personality and emotions. "
                "Your answers should be medium length and written in a colloquial manner. "
                "If you cannot find reliable sources for this information, please say so explicitly. "
                "Include the tone you are using in BRACKETS at the end of sentences."
                "Make a clean paragraf, no tables, not pictures"
            )
        }
    ]

    # Añadir historial
    for mensaje in historial[-6:]:
        if "user" in mensaje:
            messages.append({"role": "user", "content": mensaje["user"]})
        elif "bot" in mensaje:
            messages.append({"role": "assistant", "content": mensaje["bot"]})

    messages.append({"role": "user", "content": query_str})

    data = {
        "model": "sonar",
        "messages": messages
    }

    try:
        response = requests.post(url, json=data, headers=headers)  #Envio petición a la api y me guardo la respuesta

        if response.status_code == 200: #si no hay ningun problema recibiendo la respuesta
            parcial = response.json()
            contenido = parcial["choices"][0]["message"]["content"]

            # Limpieza básica
            c1 = re.sub(r'([a-zA-Z])\d+(?=[\s.,;:]|$)', r'\1', contenido)
            c2 = re.sub(r'(?<=[\s.,;:])\d+([a-zA-Z])', r'\1', c1)
            result = re.sub(r"[\[\]\*\#]", "", c2)

            guardar_respuesta(result)
            return result

        else:
            # Error de API
            error_mssg = "It seems like I can´t answer your question right now, ohh sugar! [jokingly angry]"
            guardar_respuesta(error_mssg)
            print("Error API:", response.status_code, response.text)
            return error_mssg

    except requests.exceptions.RequestException as e:
        error_conection = (
            "Oops [laughs nervously], I think there's no connection. "
            "Do you mind checking your internet? Him and I are in very dependant relationship right now [jokingly]"
        )
        guardar_respuesta(error_conection)
        print("Error de conexión:", e)
        return error_conection

    except Exception as e:
        error_random = "Well, I don’t know what happened but I can't answer that, sorry [apologizing]"
        guardar_respuesta(error_random)
        print("Error inesperado:", e)
        return error_random

def gestionar_respuesta():
    data = request.get_json()
    query_str = data.get('query', '') #obtenemos la peticioón

    if not query_str:
        return jsonify({"error": "Consulta no proporcionada"}), 400

    historial = cargar_memoria ()

    #guardo también el historial de consulta del usuario
    historial.append ({"user": query_str})

    #guardamos también la respuesta
    respuesta = obtener_respuesta(query_str) 

    historial.append({"bot": respuesta})
    guardar_memoria(historial)
    return jsonify({"reply": respuesta})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
