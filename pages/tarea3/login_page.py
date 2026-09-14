from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.tarea3.base_page import BasePage
import allure

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    TITLE = (By.CLASS_NAME, "title")

    @allure.step("Paso: Iniciar sesión con usuario '{username}'")
    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Paso: Validar ingreso exitoso a la pantalla principal")
    def is_login_successful(self):
        element = self.wait.until(EC.visibility_of_element_located(self.TITLE))
        return element.is_displayed()