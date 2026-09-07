import pytest
from selenium import webdriver 
 
<<<<<<< HEAD
@pytest.fixture 
=======
@pytest.fixture (scope='package')
>>>>>>> 2e3c6b826b8a33f8fa39cb4d9ac3c75da3573a8a
def driver(): 
    navegador = webdriver.Edge() 
    navegador.maximize_window() 
 
    yield navegador 
 
<<<<<<< HEAD
    navegador.quit()
=======
    navegador.quit() 
>>>>>>> 2e3c6b826b8a33f8fa39cb4d9ac3c75da3573a8a
