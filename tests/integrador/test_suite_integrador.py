import json
import logging
import pytest
from helpers.screenshot_helper import guardar_captura
from helpers.tarea3.webdriver_helper import WebDriverHelper
from pages.tarea3.login_page import LoginPage
from pages.tarea3.inventory_page import InventoryPage
from pages.tarea3.checkout_page import CheckoutPage
import allure

logger = logging.getLogger(__name__)

def cargar_casos_prueba():
    with open("data/tarea3/data_cases.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["casos_agregar_producto"]

@pytest.fixture
def driver():
    # Llamada exacta a tu método estático
    driver = WebDriverHelper.inicializar_driver() 
    yield driver
    logger.info("Cerrando la instancia del navegador mediante la fixture.")
    driver.quit()

@allure.title("Autenticacion y Compra de Producto")
@allure.epic("E-commerce")
@allure.feature("Autenticación")
@allure.story("HU001-Autenticación exitosa y compra de producto")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Pruebas de Integración") 
@pytest.mark.smoke 
@pytest.mark.parametrize("data", cargar_casos_prueba())

def test_suite1_autentificacion_y_compra(driver, data):
    logger.info(f"=== INICIANDO CASO DE PRUEBA: {data['caso']} ===")

    try:
        with allure.step("Inicio de pruebas"):
            logger.info("Iniciando el flujo de autenticación y compra de producto.")
            # Inicialización de clases POM
            login_page = LoginPage(driver)
            inventory_page = InventoryPage(driver)
            checkout_page = CheckoutPage(driver)

        # Paso 1: Navegar a la página
        with allure.step("Navegando a la página de login"):
            login_page.navegar_a_login("https://www.saucedemo.com/")

        # Paso 2: Autentificarse con usuario estándar
        with allure.step("Autenticándose con usuario estándar"):
            login_page.autentificarse("standard_user", "secret_sauce")

        # Paso 3: Validar que el login fue exitoso (URL contiene inventory)
        with allure.step("Validar que el login fue exitoso (URL contiene inventory)"):
            assert "inventory" in driver.current_url, "Error: El login no redirigió a la página de inventario."
            logger.info("Login verificado con éxito vía URL.")

        # Paso 4: Ordenar el filtro según el data-driven
        with allure.step("Ordenando productos según el criterio definido en el caso de prueba"):
            inventory_page.ordenar_productos_por_valor(data['orden'])
            # Guardamos el nombre esperado que está en la posición/índice antes de hacer clic
            nombre_real_tienda = inventory_page.obtener_nombre_producto_por_indice(data['indice_producto'])

        # Paso 5: Agregar al carrito según los índices definidos
        with allure.step("Agregando producto al carrito"):
            inventory_page.agregar_al_carrito_por_indice(data['indice_producto'])

        # Paso 6: Validar número de productos en carrito ("cantidad_esperada")
        with allure.step("Validando cantidad de productos en carrito"):
            cantidad_actual = inventory_page.obtener_cantidad_carrito()
            assert cantidad_actual == data['cantidad_esperada'], "Error: La cantidad de productos difiere de la esperada."

        # Ir a la sección del carrito
        with allure.step("Navegando al carrito"):
            inventory_page.ir_al_carrito()

        # Paso 7: Validar que exista el elemento que coincida con "producto_esperado"
        with allure.step("Validando producto en carrito"):
            producto_en_carrito = checkout_page.validar_producto_en_carrito()
            assert producto_en_carrito == data['producto_esperado'], f"Error: Se esperaba '{data['producto_esperado']}' pero se encontró '{producto_en_carrito}'."
            logger.info("Validación de consistencia de producto en carrito completada.")

        # Paso 8 y 9: Continuar flujo de checkout y rellenar formulario ficticio
        with allure.step("Procediendo a checkout y llenando formulario"):
            checkout_page.proceder_a_checkout()
            checkout_page.llenar_formulario_y_continuar("Usuario", "Prueba", "LI-15011")

        # Paso 10: Finalizar compra y validar éxito
        with allure.step("Finalizando compra y validando éxito"):
            checkout_page.finalizar_compra()
            mensaje_final = checkout_page.obtener_mensaje_exito()
            assert mensaje_final == "Thank you for your order!", "Error: No se visualizó la pantalla final de éxito."
            logger.info(f"=== FINALIZADO CON ÉXITO: {data['caso']} ===")

    except Exception as e:
        ruta_captura = guardar_captura(driver, f"fallo_{data['caso']}")

        with allure.step("Capturando evidencia en allure"):
            allure.attach.file(
                ruta_captura,
                name="Error identificado",
                attachment_type=allure.attachment_type.PNG
                )

        logger.error(f"Prueba fallida. Captura guardada en: {ruta_captura}")
        logger.error(e)

        raise e