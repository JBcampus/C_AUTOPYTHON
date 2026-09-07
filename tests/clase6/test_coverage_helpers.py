import pytest
from helpers.data_helper import leer_json
from helpers.text_helper import contiene_texto, normalizar_texto, textos_son_iguales

@pytest.mark.coverage
def test_coverage_data_helper():
    datos = leer_json("data/clase6/usuarios_login.json")
    assert len(datos["usuarios_validos"]) == 3
    assert len(datos["usuarios_invalidos"]) == 3

@pytest.mark.coverage
def test_coverage_text_helper():
    texto = " Selenium con Pytest "
    assert normalizar_texto(texto) == "selenium con pytest"
    assert contiene_texto(texto, "pytest")
    assert textos_son_iguales(texto, "selenium con pytest")