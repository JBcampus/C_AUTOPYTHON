import logging
from selenium import webdriver

logger = logging.getLogger(__name__)

class WebDriverHelper:
    @staticmethod
    def inicializar_driver():
        logger.info("Inicializando Google Chrome nativamente con Selenium 4...")
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        return driver
