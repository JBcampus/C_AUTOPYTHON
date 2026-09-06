from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
 
class AlertsPage: 
    URL = "https://the-internet.herokuapp.com/javascript_alerts" 
 
    JS_ALERT_BUTTON = (By.XPATH, "//button[text()='Click for JS Alert']") 
    JS_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Click for JS Confirm']") 
    JS_PROMPT_BUTTON = (By.XPATH, "//button[text()='Click for JS Prompt']") 
    RESULT_TEXT = (By.ID, "result") 
 
    def __init__(self, driver): 
        self.driver = driver 
        self.wait = WebDriverWait(driver, 10) 
 
    def abrir(self): 
        self.driver.get(self.URL) 
 
    def abrir_alerta_simple(self): 
        boton = self.wait.until( EC.element_to_be_clickable(self.JS_ALERT_BUTTON) ) 
 
        boton.click() 
 
    def abrir_confirmacion(self): 
        boton = self.wait.until( EC.element_to_be_clickable(self.JS_CONFIRM_BUTTON) ) 
 
        boton.click() 
 
    def abrir_prompt(self): 
        boton = self.wait.until( EC.element_to_be_clickable(self.JS_PROMPT_BUTTON) ) 
 
        boton.click() 
 
    def aceptar_alerta(self): 
        alerta = self.wait.until(EC.alert_is_present()) 
 
        alerta.accept() 
 
    def cancelar_alerta(self): 
        alerta = self.wait.until(EC.alert_is_present()) 
 
        alerta.dismiss() 

 
    def escribir_en_prompt(self, texto): 
        alerta = self.wait.until(EC.alert_is_present()) 
 
        alerta.send_keys(texto) 
        alerta.accept() 
 
    def obtener_resultado(self): 
        resultado = self.wait.until( EC.visibility_of_element_located(self.RESULT_TEXT) ) 
 
        return resultado.text