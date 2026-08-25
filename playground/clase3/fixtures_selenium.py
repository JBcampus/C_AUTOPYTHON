import pytest 
from selenium import webdriver
from selenium.webdriver.edge.service import Service 
 
@pytest.fixture(scope='function') 
def driver(): 
    # 1. Definimos la ruta exacta al driver que ya descargaste
    ruta_driver = r"./drivers/msedgedriver.exe"

    # 2. Creamos el servicio con esa ruta
    servicio = Service(executable_path=ruta_driver)

    # 3. Le pasamos el servicio a webdriver.Edge
    navegador = webdriver.Edge(service=servicio)
    navegador.maximize_window() 
 
    yield navegador 
 
    navegador.quit()