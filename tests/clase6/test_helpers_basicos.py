import pytest
from helpers.data_helper import leer_json
from helpers.text_helper import contiene_texto, textos_son_iguales

@pytest.mark.smoke
def test_leer_json_usuarios_login():
    datos = leer_json("data/clase6/usuarios_login.json")

    assert "usuarios_validos" in datos
    assert "usuarios_invalidos" in datos

@pytest.mark.smoke
def test_helper_contiene_texto():
    mensaje = " Error: Username and password do not match "

    assert contiene_texto(mensaje, "username and password")

@pytest.mark.smoke
def test_helper_textos_son_iguales():
    texto_actual = " Products "
    texto_esperado = "products"
    
    assert textos_son_iguales(texto_actual, texto_esperado)