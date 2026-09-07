import pytest
from selenium import webdriver

from pages.tarea3.login_page import LoginPage
from pages.tarea3.inventory_page import InventoryPage


@pytest.fixture(scope="module")
def driver():
    navegador = webdriver.Edge()
    navegador.maximize_window()

    yield navegador

    navegador.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)
