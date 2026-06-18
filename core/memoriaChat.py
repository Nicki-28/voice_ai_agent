import os
import json

RUTA_CONTEXTO = "data/context.json"

def cargar_memoria():
    if not os.path.exists(RUTA_CONTEXTO):
        return []

    with open(RUTA_CONTEXTO, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def guardar_memoria(historial):
    with open(RUTA_CONTEXTO, "w", encoding="utf-8") as f:
        json.dump(historial, f, indent=2, ensure_ascii=False)


def borrar_memoria():
    guardar_memoria([])