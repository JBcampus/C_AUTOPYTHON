import json
from pathlib import Path

def leer_json(ruta_archivo):
    ruta = Path(ruta_archivo)
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)