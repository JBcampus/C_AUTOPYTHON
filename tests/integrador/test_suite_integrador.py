import pytest
import allure
import os
import logging
import json

# IMPORTACIONES POM DE LA TAREA 3
from pages.tarea3.login_page import LoginPage
from pages.tarea3.inventory_page import InventoryPage
from pages.tarea3.checkout_page import CheckoutPage

# HELPER DE CAPTURA (Este sí existe y se valida en tu estructura de la Tarea 3)
from helpers.tarea3.webdriver_helper import WebDriverHelper

# Requerimiento: Trazabilidad obligatoria con logging
logger = logging.getLogger(__name__)

def obtener_casos_integrador():
    """Carga los datos de forma nativa e independiente para evitar fallos de módulos"""
    ruta_json = os.path.join("data", "tarea3", "Data_cases.json")
    if not os.path.exists(ruta_json):
        logger.error(f"No se encontró el archivo JSON en la ruta: {ruta_json}")
        return []
    try:
        with open(ruta_json, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        logger.critical(f"Error al cargar el archivo Data_cases.json de forma nativa: {str(e)}")
        return []

casos_prueba = obtener_casos_integrador()
ids_casos = [caso["caso"] for caso in casos_prueba] if casos_prueba else []

# ==============================================================================
# IMPLEMENTACIÓN DE 5 DECORADORES (@allure.step) PARA CADA PANTALLA TRABAJADA
# ==============================================================================

@allure.step("Paso 1 [Login Page]: Inicializar navegador y cargar SauceDemo")
def step_abrir_aplicacion(login_page):
    login_page.navegar_a_la_url()
    logger.info("Navegación inicial hacia SauceDemo exitosa.")

@allure.step("Paso 2 [Login Page]: Ingresar credenciales y autenticar usuario")
def step_autenticar_usuario(login_page, username, password):
    login_page.autenticar(username, password)
    logger.info(f"Intento de autenticación ejecutado para el usuario: {username}")

@allure.step("Paso 3 [Inventory Page]: Aplicar filtro de ordenamiento: {orden}")
def step_ordenar_catalogo(inventory_page, orden):
    inventory_page.ordenar_productos_por_valor(orden)
    logger.info(f"Filtro de ordenamiento por '{orden}' aplicado correctamente.")

@allure.step("Paso 4 [Inventory Page]: Añadir artículo por índice {indice} y proceder")
def step_agregar_producto_y_checkout(inventory_page, checkout_page, indice):
    inventory_page.agregar_al_carrito_por_indice(indice)
    inventory_page.proceder_al_checkout()
    logger.info(f"Producto con índice {indice} agregado. Redireccionando a Checkout.")

@allure.step("Paso 5 [Checkout Page]: Validar que figure el artículo esperado: {producto_esperado}")
def step_validar_producto_en_carrito(checkout_page, producto_esperado):
    # Usamos la validación del POM que ya verifica internamente el texto o estado
    resultado_validacion = checkout_page.validar_producto_en_carrito(producto_esperado)
    assert resultado_validacion, f"Error: No se encontró el producto esperado '{producto_esperado}' en el carrito."
    logger.info("Validación de consistencia completada con éxito.")

# ==============================================================================
# SUITE: AUTENTIFICACIÓN Y ALMACENAMIENTO DE ESTADO (DATA DRIVEN)
# ==============================================================================

@pytest.mark.data
@pytest.mark.parametrize("data", casos_prueba, ids=ids_casos)
def test_suite_autenticacion_y_estado(driver, data):
    """
    Suite Integradora: Implementa modularidad POM, Helpers, Logging,
    Manejo de Excepciones y paralelismo con 2 Workers distribuidos.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)
    
    # Requerimiento 1: Implementar try except para manejo de excepciones
    try:
        logger.info(f"=== INICIANDO CASO DATA DRIVEN: {data['caso']} ===")
        
        # Ejecución secuencial de los 5 Pasos Decorados obligatorios
        step_abrir_aplicacion(login_page)
        step_autenticar_usuario(login_page, "standard_user", "secret_sauce")
        step_ordenar_catalogo(inventory_page, data['orden'])
        step_agregar_producto_y_checkout(inventory_page, checkout_page, data['indice_producto'])
        step_validar_producto_en_carrito(checkout_page, data['producto_esperado'])
        
        logger.info(f"=== CASO FINALIZADO CON ÉXITO: {data['caso']} ===")
        
    except Exception as e:
        logger.error(f"Excepción capturada de forma controlada en [{data['caso']}]: {str(e)}")
        
        # Requerimiento: Capturar imagen en error y guardarla en la carpeta artifacts
        os.makedirs("artifacts", exist_ok=True)
        nombre_evidencia = f"fallo_{data['caso']}.png"
        ruta_imagen_guardada = os.path.join("artifacts", nombre_evidencia)
        
        # Captura usando el driver nativo de Selenium
        driver.save_screenshot(ruta_imagen_guardada)
        logger.info(f"Evidencia guardada localmente en: {ruta_imagen_guardada}")
        
        # Requerimiento: Incluir attach del error con la ruta de la imagen en artifacts usando allure.attach.file
        with allure.step("Adjuntando evidencia de fallo al reporte Allure"):
            allure.attach.file(
                source=ruta_imagen_guardada,
                name=f"Captura_Error_{data['caso']}",
                attachment_type=allure.attachment_type.PNG
            )
        
        # Requerimiento: Retornar/lanzar el error para la correcta trazabilidad del pipeline
        raise e
