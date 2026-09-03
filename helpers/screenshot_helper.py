from datetime import datetime
from pathlib import Path

def guardar_captura(driver, nombre_base, carpeta="artifacts"):
    carpeta_evidencias = Path(carpeta)
    carpeta_evidencias.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    ruta_archivo = carpeta_evidencias / f"{nombre_base}_{timestamp}.png"
    driver.save_screenshot(str(ruta_archivo))
    return ruta_archivo