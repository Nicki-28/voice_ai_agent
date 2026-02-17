import os
import json


def cargar_memoria():
    if not os.path.exists("output.json"):
        return []
    with open("output.json", "r") as f:
        return json.load(f)

def guardar_memoria(historial):
    with open("context.json", "w") as f:
        json.dump(historial, f, indent=2)