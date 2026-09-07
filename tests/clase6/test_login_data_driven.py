import pytest
import logging
from helpers.data_helper import leer_json
from helpers.screenshot_helper import guardar_captura
from helpers.text_helper import contiene_texto, textos_son_iguales

logger = logging.getLogger(__name__)
datos_login = leer_json("data/clase6/usuarios_login.json")

@pytest.mark.data
@pytest.mark.parametrize("caso_login", datos_login["usuarios_validos"],
        ids=[caso["caso"] for caso in datos_login["usuarios_validos"]]
    )
def test_login_valido_data_driven(login_page, inventory_page, caso_login):
    logger.info(f"Ejecutando caso válido: {caso_login['caso']}")
    login_page.abrir()

    logger.info("Página de login abierta")
    login_page.iniciar_sesion(caso_login["user"],caso_login["pass"])

    logger.info(f"Login ejecutado con usuario: {caso_login['user']}")
    titulo = inventory_page.obtener_titulo()

    logger.info(f"Título obtenido: {titulo}")
    assert textos_son_iguales(titulo, caso_login["resultado_esperado"])

@pytest.mark.data
@pytest.mark.parametrize("caso_login",datos_login["usuarios_invalidos"],
    ids=[caso["caso"] for caso in datos_login["usuarios_invalidos"]]
    )
def test_login_invalido_data_driven(driver, login_page, caso_login):
    logger.info(f"Ejecutando caso inválido: {caso_login['caso']}")
    try:
        login_page.abrir()
        logger.info("Página de login abierta")

        login_page.iniciar_sesion(caso_login["user"],caso_login["pass"])
        logger.info(f"Login ejecutado con usuario: {caso_login['user']}")

        mensaje_error = login_page.obtener_mensaje_error()
        logger.info(f"Mensaje de error obtenido: {mensaje_error}")

        assert contiene_texto(mensaje_error,caso_login["mensaje_esperado"]
                              )
    except Exception as e:
        ruta_captura = guardar_captura(driver, f"fallo_{caso_login['caso']}")
        logger.error(f"Prueba fallida. Captura guardada en: {ruta_captura}")
        logger.error(e)

        raise e