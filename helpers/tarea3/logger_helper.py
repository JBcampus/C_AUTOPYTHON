import logging
import os

def get_logger(name="Test_Auth_State"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s - %(message)s')
        
        # Consola
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        
        # Archivo
        os.makedirs("logs", exist_ok=True)
        fh = logging.FileHandler("logs/pytest.log", encoding="utf-8")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        
    return logger