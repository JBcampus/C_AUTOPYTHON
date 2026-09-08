from packaging.tags import logger
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Navegación headless sin interfaz grafica
@pytest.fixture
def driver():
    
    logger.info("Inicializando Google Chrome nativamente con Selenium 4 desde el 'conftest.py'")

    #Initialize Google Chrome with Selenium 4 - optimized for CI/CD environments
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Essential for headless environments
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--headless=new")
    
    # Additional stability options
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-sync")
    
    # For CI/CD environments
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-blink-features=AutomationControlled")

    navegador = webdriver.Chrome(options=options)

    yield navegador
    
    navegador.quit()