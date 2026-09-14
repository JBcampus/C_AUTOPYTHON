import json
import os
import pytest
import allure
from pages.tarea3.login_page import LoginPage
from helpers.tarea3.logger_helper import get_logger
from helpers.tarea3.screenshot_helper import capture_screenshot

logger = get_logger("Test_Auth_State")

def load_test_data():
    json_path = os.path.join(os.path.dirname(__file__), "data", "login_data.json")
    with open(json_path, "r", encoding="utf-8") as file:
        return json.load(file)

@allure.epic("Taller Integrador Final")
@allure.feature("Módulo de Autenticación")
@allure.story("Autentificación y almacenamiento de estado")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("data", load_test_data())
def test_autenticacion_y_estado(driver, data):
    logger.info(f"Iniciando prueba de autenticación para usuario: {data['user']}")
    login_page = LoginPage(driver)
    
    try:
        login_page.open_url("https://www.saucedemo.com/")
        login_page.login(data["user"], data["pass"])
        
        # Validación
        assert login_page.is_login_successful() == True, f"Error al autenticar usuario {data['user']}"
        logger.info(f"Prueba completada exitosamente para usuario: {data['user']}")
        
    except Exception as e:
        logger.error(f"Fallo detectado en el test para usuario {data['user']}: {str(e)}")
        # Captura pantalla y adjunta en Allure usando allure.attach.file
        capture_screenshot(driver, f"error_{data['user']}")
        # Retorna el error para fallar la prueba adecuadamente
        raise e