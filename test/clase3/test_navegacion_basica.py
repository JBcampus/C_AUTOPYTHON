import pytest
from playground.clase3.fixtures_selenium import driver

@pytest.mark.smoke
def test_navegar_youtube_validar_titulo(driver):
    driver.get("https://www.youtube.com/")

    titulo = driver.title

    assert "YouTube" in titulo