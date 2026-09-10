import pytest
import allure
import logging

from pages.tarea3.login_page import LoginPage
from pages.tarea3.inventory_page import InventoryPage
from pages.tarea3.checkout_page import CheckoutPage

from helpers.data_helper import leer_json
from helpers.screenshot_helper import guardar_captura
from helpers.text_helper import contiene_texto


logger = logging.getLogger(__name__)

casos_prueba = leer_json("data/tarea3/data_cases.json")
ids_casos = [caso["caso"] for caso in casos_prueba]

@allure.step("Paso 1 [Login Page]: Inicializar navegador y cargar SauceDemo")
def step_abrir_aplicacion(login_page):
    login_page.navegar_a_login("https://www.saucedemo.com/")  
    logger.info("Página de login cargada exitosamente.")

@allure.step("Paso 2 [Login Page]: Ingresar credenciales y autenticar usuario")
def step_autenticar_usuario(login_page, username, password):
    login_page.autentificarse(username, password)
    logger.info(f"Intento de autenticación ejecutado para el usuario: {username}")

@allure.step("Paso 3 [Inventory Page]: Aplicar filtro de ordenamiento: {orden}")
def step_ordenar_catalogo(inventory_page, orden):
    inventory_page.ordenar_productos_por_valor(orden)
    logger.info(f"Filtro de ordenamiento por '{orden}' aplicado correctamente.")

@allure.step("Paso 4 [Inventory Page]: Añadir artículo por índice {indice} y proceder")
def step_agregar_producto_y_checkout(inventory_page, checkout_page, indice):
    inventory_page.agregar_al_carrito_por_indice(indice)
    inventory_page.ir_al_carrito() 
    logger.info(f"Producto con índice {indice} agregado. Redireccionando a la cesta.")

@allure.step("Paso 5 [Checkout Page]: Validar que figure el artículo esperado: {producto_esperado}")
def step_validar_producto_en_carrito(checkout_page, producto_esperado):
    producto_obtenido = checkout_page.validar_producto_en_carrito()
    assert contiene_texto(str(producto_obtenido), producto_esperado), (
        f"Error: Se esperaba '{producto_esperado}' pero se obtuvo '{producto_obtenido}'"
    )
    logger.info("Validación de consistencia completada con éxito.")


# SUITE: AUTENTIFICACIÓN Y ALMACENAMIENTO DE ESTADO (DATA DRIVEN)

@allure.title("Title: Autenticacion y Compra de Producto")
@allure.epic("Epic: EP01_E-commerce")
@allure.feature("Feature: Autenticación/Compra")
@allure.story("Story: HU001-Autenticación exitosa y compra de producto")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Test Suite: Login y Compra productos") 
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
        
        ruta_imagen_guardada = guardar_captura(
            driver,
            f"fallo_{data['caso']}",
            carpeta="artifacts/integrador",
        )
        logger.info(f"Evidencia guardada localmente en: {ruta_imagen_guardada}")
        
        with allure.step("Adjuntando evidencia de fallo al reporte Allure"):
            allure.attach.file(
                source=str(ruta_imagen_guardada),
                name=f"Captura_Error_{data['caso']}",
                attachment_type=allure.attachment_type.PNG
            )
        
        raise e