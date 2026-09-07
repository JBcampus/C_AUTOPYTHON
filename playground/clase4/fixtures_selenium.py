<<<<<<< HEAD
import pytest
from selenium import webdriver 
 
=======
import pytest 
from selenium import webdriver 

>>>>>>> 2e3c6b826b8a33f8fa39cb4d9ac3c75da3573a8a
@pytest.fixture 
def driver(): 
    navegador = webdriver.Edge() 
    navegador.maximize_window() 
<<<<<<< HEAD
 
    yield navegador 
 
    navegador.quit()
=======
    yield navegador 
    navegador.quit() 
>>>>>>> 2e3c6b826b8a33f8fa39cb4d9ac3c75da3573a8a
