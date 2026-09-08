import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Navegación headless sin interfaz grafica
@pytest.fixture
def driver():
    logger.info("Inicializando Google Chrome nativamente con Selenium 4 desde Helpers/webdriver_helper.py...")
    options = webdriver.ChromeOptions()
    
    # Arguments for CI/CD environments (GitHub Actions)
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    #options.add_argument("--disable-extensions")
    #options.add_argument("--disable-software-rasterizer")
    
    navegador = webdriver.Chrome(options=options)

    yield navegador

    navegador.quit()
