from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
 
class LoginPage: 
    URL = "https://www.saucedemo.com/" 
 
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password") 
    LOGIN_BUTTON = (By.ID, "login-button") 
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
 
    def __init__(self, driver): 
        self.driver = driver 
        self.wait = WebDriverWait(driver, 10) 
 
    def abrir(self): 
        self.driver.get(self.URL) 
 
    def escribir_usuario(self, usuario): 
        #campo_usuario = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT)) 
        campo_usuario = self.driver.find_element(*self.USERNAME_INPUT)
        campo_usuario.send_keys(usuario) 
 
    def escribir_clave(self, clave): 
        campo_clave = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT)) 
        campo_clave.send_keys(clave) 
 
    def click_login(self): 
        boton_login = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)) 
        boton_login.click() 
 
    def iniciar_sesion(self, usuario, clave): 
        self.escribir_usuario(usuario) 
        self.escribir_clave(clave) 
        self.click_login() 

    def obtener_mensaje_error(self):
        mensaje_error = self.driver.find_element(*self.ERROR_MESSAGE)
        return mensaje_error.text