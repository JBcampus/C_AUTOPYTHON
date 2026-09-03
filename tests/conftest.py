import pytest 
from selenium import webdriver 
 
from pages.clase5.login_page import LoginPage 
from pages.clase5.inventory_page import InventoryPage 
# from pages.clase5.alerts_page import AlertsPage 
# from pages.clase5.upload_page import UploadPage 
 
@pytest.fixture()
def driver(): 
    navegador = webdriver.Edge() 
    navegador.maximize_window() 
 
    yield navegador 
 
    navegador.quit() 
 
@pytest.fixture(scope="class") 
def driver_class(): 
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
 
@pytest.fixture(scope="class") 
def login_page_class(driver_class): 
    return LoginPage(driver_class) 
 
@pytest.fixture(scope="class") 
def inventory_page_class(driver_class): 
    return InventoryPage(driver_class) 
 
# @pytest.fixture 
# def alerts_page(driver): 
#     return AlertsPage(driver) 
 
# @pytest.fixture 
# def upload_page(driver): 
#     return UploadPage(driver)