import pytest 
from selenium import webdriver 
 
@pytest.fixture(scope='function') 
def driver(): 
    navegador = webdriver.Chrome()
    navegador.maximize_window() 
 
    yield navegador 
 
    navegador.quit()