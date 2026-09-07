import pytest
import logging
from helpers.tarea3.data_helper import leer_json
from helpers.screenshot_helper import guardar_captura
from helpers.tarea3.text_helper import contiene_texto, textos_son_iguales

logger = logging.getLogger(__name__)

datos_productos = leer_json("data/tarea3/productos.json")

@pytest.mark.data
@pytest.mark.parametrize(
    "caso_agregar_producto",
    datos_productos["casos_agregar_producto"],
    ids=[caso["caso"] for caso in datos_productos["casos_agregar_producto"]]
)

def test_agregar_producto(inventory_page, caso_agregar_producto, login_page):

    login_page.abrir()
    logger.info("Página de login abierta")
    guardar_captura(
        inventory_page.driver,
        f"{caso_agregar_producto['caso']}_00_pantalla_login",
        "artifacts/tarea3",
    )
    
    login_page.iniciar_sesion( "standard_user", "secret_sauce")
    logger.info(f"Login ejecutado con usuario: standard_user")
    guardar_captura(
        inventory_page.driver,
        f"{caso_agregar_producto['caso']}_01_login",
        "artifacts/tarea3",
    )
    
    url = inventory_page.get_current_url()
    logger.info(f"URL: {url}")
    
    assert contiene_texto(url, "https://www.saucedemo.com/inventory.html")
    logger.info(f"Validacion de que URL contenga 'inventory' ")

    logger.info(f"Ejecutando caso agregar producto: {caso_agregar_producto['caso']}")

    inventory_page.ordenar_productos_por_valor(caso_agregar_producto['orden'])
    logger.info(f"Ordenando producto por: {caso_agregar_producto['orden']} ")

    inventory_page.obtener_producto_indice(caso_agregar_producto['indice_producto'])
    logger.info(f"Obtener producto por indice[ {caso_agregar_producto['indice_producto']} ]")

    assert textos_son_iguales(inventory_page.obtener_cantidad_carrito(), caso_agregar_producto['cantidad_esperada'])

    inventory_page.ingresar_carrito()
    logger.info(f"Ingresamos al carrito")

    assert textos_son_iguales(inventory_page.obtener_nombre_producto(), caso_agregar_producto['producto_esperado'])
    guardar_captura(
        inventory_page.driver,
        f"{caso_agregar_producto['caso']}_02_carrito",
        "artifacts/tarea3",
    )

    inventory_page.click_checkout()
    logger.info(f"Click en checkout")

    inventory_page.completar_formulario("Pedro","Perez","0051")
    logger.info(f"Completar formulario")

    inventory_page.click_boton_continue()

    inventory_page.click_boton_finish()
    logger.info(f"Finalizar la compra")

    assert textos_son_iguales(inventory_page.obtener_titulo(), "Checkout: Complete!")
    logger.info(f"Validamos que la compra se ha realizado correctamente")
    guardar_captura(
        inventory_page.driver,
        f"{caso_agregar_producto['caso']}_03_compra_finalizada",
        "artifacts/tarea3",
    )




