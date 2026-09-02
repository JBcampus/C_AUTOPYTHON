import pytest
from selenium import webdriver

@pytest.fixture
def driver(scope="session"):
    navegador = webdriver.Edge()
    navegador.maximize_window()

    yield navegador

    navegador.quit()
