import pytest
import allure
import os
import logging
import json
from pages.tarea3.login_page import LoginPage
from pages.tarea3.inventory_page import InventoryPage
from pages.tarea3.checkout_page import CheckoutPage
from helpers.tarea3.webdriver_helper import WebDriverHelper

logger = logging.getLogger(__name__)

def cargar_casos_prueba():
    ruta_json = os.path.join("data", "tarea3", "data_cases.json")
    with open(ruta_json, "r", encoding="utf-8") as file:
        return json.load(file)

# Definición de Steps mediante decoradores (Cumple con los 5 requeridos)
@allure.step("Paso 1: Inicializar el navegador y navegar a la página")
def step_abrir_pagina(login_page):
    login_page.navegar_a_la_url()

@allure.step("Paso 2: Autenticar con el usuario {username}")
def step_autenticar_usuario(login_page, username, password):
    login_page.autenticar(username, password)

@allure.step("Paso 3: Ordenar productos por filtro {orden}")
def step_ordenar_productos(inventory_page, orden):
    inventory_page.ordenar_productos_por_valor(orden)

@allure.step("Paso 4: Agregar producto al carrito y proceder al Checkout")
def step_agregar_y_proceder(inventory_page, checkout_page, indice):
    inventory_page.agregar_al_carrito_por_indice(indice)
    inventory_page.proceder_al_checkout()

@allure.step("Paso 5: Validar que el producto correcto esté en el carrito")
def step_validar_producto(checkout_page, producto_esperado):
    assert checkout_page.validar_producto_en_carrito(producto_esperado), f"No se encontró el producto: {producto_esperado}"


@pytest.mark.parametrize("data", cargar_casos_prueba())
def test_suite_autenticacion_y_estado(driver, data):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)
    
    os.makedirs("artifacts", exist_ok=True)
    
    try:
        logger.info(f"Iniciando caso integrador: {data['caso']}")
        step_abrir_pagina(login_page)
        step_autenticar_usuario(login_page, "standard_user", "secret_sauce")
        step_ordenar_productos(inventory_page, data['orden'])
        step_agregar_y_proceder(inventory_page, checkout_page, data['indice_producto'])
        step_validar_producto(checkout_page, data['producto_esperado'])
        
        logger.info(f"Caso finalizado con ÉXITO: {data['caso']}")
        
    except Exception as e:
        logger.error(f"Error detectado en el caso {data['caso']}: {str(e)}")
        
        # Generar ruta de la captura dentro del directorio asegurado
        screenshot_path = os.path.join("artifacts", f"error_{data['caso']}.png")
        
        # Captura física de la pantalla
        driver.save_screenshot(screenshot_path)
        logger.info(f"Captura de pantalla guardada en: {screenshot_path}")
        
        # Adjunto obligatorio para Allure
        allure.attach.file(
            source=screenshot_path,
            name=f"Evidencia_Error_{data['caso']}",
            attachment_type=allure.attachment_type.PNG
        )
        raise e

