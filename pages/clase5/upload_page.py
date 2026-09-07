from pathlib import Path 
 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
 
class UploadPage: 
    URL = "https://the-internet.herokuapp.com/upload" 
 
    FILE_INPUT = (By.ID, "file-upload") 
    SUBMIT_BUTTON = (By.ID, "file-submit") 
    UPLOADED_FILE = (By.ID, "uploaded-files") 
 
    def __init__(self, driver): 
        self.driver = driver 
        self.wait = WebDriverWait(driver, 10) 
 
    def abrir(self): 
        self.driver.get(self.URL) 
 
    def cargar_archivo(self, ruta_archivo): 
 
        ruta_absoluta = Path(ruta_archivo).resolve() 
 
        input_file = self.wait.until( EC.presence_of_element_located(self.FILE_INPUT) ) 
 
        input_file.send_keys(str(ruta_absoluta)) 
 
    def enviar_archivo(self): 
        boton = self.wait.until( EC.element_to_be_clickable(self.SUBMIT_BUTTON) ) 
 
        boton.click() 
 
    def obtener_nombre_archivo_cargado(self): 
        archivo = self.wait.until( EC.visibility_of_element_located(self.UPLOADED_FILE) ) 
 
        return archivo.text 