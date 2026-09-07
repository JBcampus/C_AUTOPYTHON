import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class LoginPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "[data-test='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test='login-button']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navegar_a_login(self, url):
        """Navega hacia el portal web de SauceDemo"""
        logger.info(f"Navegando a la URL: {url}")
        self.driver.get(url)

    def autentificarse(self, username, password):
        """Ingresa credenciales y hace click en ingresar"""
        logger.info(f"Intentando autenticar al usuario estándar: {username}")
        
        # Esperar e interactuar con el campo de usuario
        txt_username = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        txt_username.clear()
        txt_username.send_keys(username)
        
        # Ingresar contraseña
        txt_password = self.driver.find_element(*self.PASSWORD_INPUT)
        txt_password.clear()
        txt_password.send_keys(password)
        
        # Hacer click en el botón de login
        logger.info("Presionando el botón de inicio de sesión.")
        self.driver.find_element(*self.LOGIN_BUTTON).click()
