import os
import json


def cargar_memoria():
    if not os.path.exists("data/output.json"):
        return []
    with open("data/output.json", "r") as f:
        return json.load(f)

def guardar_memoria(historial):
    with open("data/context.json", "w") as f:
        json.dump(historial, f, indent=2)