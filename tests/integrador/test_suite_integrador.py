import pytest
import allure
import os
import logging

from pages.tarea3.login_page import LoginPage
from pages.tarea3.inventory_page import InventoryPage
from pages.tarea3.checkout_page import CheckoutPage

from helpers.tarea3.data_helper import leer_json
from helpers.tarea3.screenshot_helper import guardar_captura
from helpers.tarea3.text_helper import contiene_texto, textos_son_iguales

# Requerimiento: Trazabilidad obligatoria con logging
logger = logging.getLogger(__name__)

def obtener_casos_integrador():
    """Carga los datos dinámicamente con el helper nativo leer_json de la Tarea 3"""
    ruta_json = "data/tarea3/Data_cases.json"
    try:
        return leer_json(ruta_json)
    except Exception as e:
        logger.critical(f"Error al cargar el archivo data driven: {str(e)}")
        return []

casos_prueba = obtener_casos_integrador()
ids_casos = [caso["caso"] for caso in casos_prueba] if casos_prueba else []

# IMPLEMENTACIÓN DE 5 DECORADORES (@allure.step) PARA CADA PANTALLA TRABAJADA

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
    # Nota: Si tu método de la Tarea 3 retorna un Booleano, la aserción se ejecuta directo:
    resultado_validacion = checkout_page.validar_producto_en_carrito(producto_esperado)
    assert resultado_validacion, f"Error: No se encontró el producto esperado '{producto_esperado}' en el carrito."
    logger.info("Validación de consistencia completada con éxito.")

# SUITE: AUTENTIFICACIÓN Y ALMACENAMIENTO DE ESTADO (DATA DRIVEN)

@pytest.mark.data
@pytest.mark.parametrize("data", casos_prueba, ids=ids_casos)
def test_suite_autenticacion_y_estado(driver, data):
    """
    Suite Integradora: Implementa modularidad POM, Helpers, Logging,
    Manejo de Excepciones y paralelismo con 2 Workers distribuidos.
    """
    # Inicialización de las clases de página (POM)
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)
    
    # Requerimiento 1: Implementar try except para manejo de excepciones
    try:
        logger.info(f"=== INICIANDO CASO DATA DRIVEN: {data['caso']} ===")
        
      
        step_abrir_application(login_page)
        step_autenticar_usuario(login_page, "standard_user", "secret_sauce")
        step_ordenar_catalogo(inventory_page, data['orden'])
        step_agregar_producto_y_checkout(inventory_page, checkout_page, data['indice_producto'])
        step_validar_producto_en_carrito(checkout_page, data['producto_esperado'])
        
        logger.info(f"=== CASO FINALIZADO CON ÉXITO: {data['caso']} ===")
        
    except Exception as e:
        logger.error(f"Excepción capturada de forma controlada en [{data['caso']}]: {str(e)}")
        
       
        nombre_evidencia = f"fallo_{data['caso']}"
        ruta_imagen_guardada = guardar_captura(driver, nombre_evidencia)
        
        
        with allure.step("Adjuntando evidencia de fallo al reporte Allure"):
            allure.attach.file(
                source=ruta_imagen_guardada,
                name=f"Captura_Error_{data['caso']}",
                attachment_type=allure.attachment_type.PNG
            )
        
        logger.error(f"Prueba abortada. Evidencia física resguardada en: {ruta_imagen_guardada}")
        
     
        raise e
