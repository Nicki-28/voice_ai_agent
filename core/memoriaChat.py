import os
import json


def cargar_memoria():
    historial_completo = []
    
    # Cargamos el primer archivo (si existe)
    if os.path.exists("data/output.json"):
        with open("data/output.json", "r") as f:
            datos_output = json.load(f)
            historial_completo.extend(datos_output) # Añadimos los datos a la lista
            
    # Cargamos el segundo archivo (si existe)
    if os.path.exists("data/context.json"):
        with open("data/context.json", "r") as g:
            datos_context = json.load(g)
            historial_completo.extend(datos_context) # Sumamos estos datos a la misma lista
            
    # return último
    return historial_completo

def guardar_memoria(historial):
    print("Guardando historial...")
    with open("data/context.json", "w") as f:
        json.dump(historial, f, indent=2)