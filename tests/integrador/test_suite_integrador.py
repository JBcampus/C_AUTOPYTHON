import pytest
import allure
import os
import logging
import json
from pages.tarea3.login_page import LoginPage
from pages.tarea3.inventory_page import InventoryPage
from pages.tarea3.checkout_page import CheckoutPage

# Configuración del registrador de trazas (Logging) obligatorio
logger = logging.getLogger(__name__)

def cargar_casos_prueba():
    """
    Lee de manera segura el archivo JSON de datos respetando las mayúsculas
    y minúsculas (Case-Sensitive) esenciales para entornos Linux en GitHub Actions.
    """
    ruta_json = os.path.join("data", "tarea3", "Data_cases.json")
    if not os.path.exists(ruta_json):
        logger.error(f"No se encontró el archivo de datos en la ruta: {ruta_json}")
        raise FileNotFoundError(f"Archivo ausente: {ruta_json}")
        
    with open(ruta_json, "r", encoding="utf-8") as file:
        datos = json.load(file)
        if isinstance(datos, dict) and "usuarios_validos" in datos:
            return datos["usuarios_validos"]
        return datos

try:
    casos_prueba = cargar_casos_prueba()
    ids_casos = [caso["caso"] for caso in casos_prueba]
except Exception as e:
    logger.critical(f"Fallo crítico al pre-cargar el archivo Data_cases.json: {str(e)}")
    casos_prueba = []
    ids_casos = []


# DEFINICIÓN DE STEPS MEDIANTE DECORADORES (Cumple estrictamente los 5 requeridos)

@allure.step("Paso 1: Inicializar el navegador y navegar a SauceDemo")
def step_abrir_pagina(login_page):
    login_page.navegar_a_la_url()

@allure.step("Paso 2: Autenticar en la plataforma con el usuario {username}")
def step_autenticar_usuario(login_page, username, password):
    login_page.autenticar(username, password)

@allure.step("Paso 3: Ordenar catálogo de productos por el filtro: {orden}")
def step_ordenar_productos(inventory_page, orden):
    inventory_page.ordenar_productos_por_valor(orden)

@allure.step("Paso 4: Agregar producto al carrito según índice e ir al Checkout")
def step_agregar_y_proceder(inventory_page, checkout_page, indice):
    inventory_page.agregar_al_carrito_por_indice(indice)
    inventory_page.proceder_al_checkout()

@allure.step("Paso 5: Validar la presencia del producto esperado: {producto_esperado}")
def step_validar_producto(checkout_page, producto_esperado):
    assert checkout_page.validar_producto_en_carrito(producto_esperado), f"Validación fallida: No se encontró '{producto_esperado}'"


# SUITE DE PRUEBAS PRINCIPAL

@pytest.mark.data
@pytest.mark.parametrize("data", casos_prueba, ids=ids_casos)
def test_suite_autenticacion_y_estado(driver, data):
    """
    Suite de prueba integrada con inyección Data-Driven. Ejecuta los pasos del flujo,
    captura excepciones y empaqueta evidencias físicas en caso de error.
    """
    
    os.makedirs("artifacts", exist_ok=True)
    
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)
    
    try:
        logger.info(f"--- INICIANDO CASO INTEGRADOR: {data['caso']} ---")
        
        # Ejecución controlada y secuencial de los 5 pasos decorados
        step_abrir_pagina(login_page)
        step_autenticar_usuario(login_page, "standard_user", "secret_sauce")
        step_ordenar_productos(inventory_page, data['orden'])
        step_agregar_y_proceder(inventory_page, checkout_page, data['indice_producto'])
        step_validar_producto(checkout_page, data['producto_esperado'])
        
        logger.info(f"--- CASO FINALIZADO CON ÉXITO: {data['caso']} ---")
        
    except Exception as e:
        logger.error(f"Error detectado en el caso [{data['caso']}]: {str(e)}")
        
        
        nombre_captura = f"fallo_{data['caso']}.png"
        screenshot_path = os.path.join("artifacts", nombre_captura)
        
       
        driver.save_screenshot(screenshot_path)
        logger.info(f"Evidencia de pantalla resguardada en: {screenshot_path}")
        
        
        allure.attach.file(
            source=screenshot_path,
            name=f"Evidencia_Error_{data['caso']}",
            attachment_type=allure.attachment_type.PNG
        )
        
        raise e
