import pytest 
 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
 
from playground.clase4.fixtures_selenium import driver 
 
class UsuarioLogin: 
    def __init__(self, usuario, clave): 
        self.usuario = usuario 
        self.clave = clave 
 
@pytest.mark.smoke 
def test_login_correcto_con_esperas(driver): 
    # Crear objeto 
    usuario = UsuarioLogin("standard_user", "secret_sauce") 
 
    wait = WebDriverWait(driver, 10) 
 
    # Navegar a la pagina 
    driver.get("https://www.saucedemo.com/") 
 
    # Esperar hasta que el elemento exista y sea visible 
    campo_usuario = wait.until( 
        EC.visibility_of_element_located((By.ID, "user-name")) 
    ) 
 
    # Esperar hasta que el elemento exista y sea visible 
    campo_clave = wait.until( 
        EC.visibility_of_element_located((By.ID, "password")) 
    ) 
 
    # Esperar hasta que el botón esté visible y habilitado 
    boton_login = wait.until( 
        EC.element_to_be_clickable((By.ID, "login-button")) 
    ) 
 
    # Realizar acciones en los objetos almacenados 
    campo_usuario.send_keys(usuario.usuario) 
    campo_clave.send_keys(usuario.clave) 
    boton_login.click() 
 
    # Esperar hasta que el elemento exista y sea visible 
    titulo_productos = wait.until( 
        EC.visibility_of_element_located((By.CLASS_NAME, "title")) 
    ) 
 
    # Validaciones finales 
    assert titulo_productos.text == "Products" 
    assert "inventory.html" in driver.current_url
     