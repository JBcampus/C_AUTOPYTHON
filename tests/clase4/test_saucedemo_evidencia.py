import pytest 
 
from datetime import datetime 
from pathlib import Path 
 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
 
from playground.clase4.fixtures_selenium import driver 

 
@pytest.mark.regression 
def test_login_usuario_bloqueado_con_evidencia_si_falla(driver): 
    wait = WebDriverWait(driver, 10) 
 
    try: 
        driver.get("https://www.saucedemo.com/") 
 
        # Espera explícita a elemento estratégico 
        wait.until( EC.visibility_of_element_located((By.CLASS_NAME, "login_logo")) ) 
 
        # Selectores 
        campo_usuario = driver.find_element(By.ID, "user-name") 
 
        campo_clave = driver.find_element(By.ID, "password") 
 
        boton_login = driver.find_element(By.ID, "login-button") 
 
        # Acciones 
        campo_usuario.send_keys("locked_out_user") 
        campo_clave.send_keys("secret_sauce") 
        boton_login.click() 
 
        # Espera explícita a elemento 
        mensaje_error = wait.until( 
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")) 
        ) 
 
        assert "locked_out" in mensaje_error.text 
 
    except Exception: 
        # Definición de carpeta, crea si no existe 
        carpeta_evidencias = Path("artifacts/clase4") 

        carpeta_evidencias.mkdir(parents=True, exist_ok=True) 
        # Fecha de fallo y nombre de la evidencia 

        fecha = datetime.now().strftime("%Y%m%d_%H%M%S") 
        ruta_evidencia = carpeta_evidencias / f"fallo_login_{fecha}.png" 

        # Captura de evidencia de fallo 
        driver.save_screenshot(str(ruta_evidencia)) 
        print(driver.current_url)
        print(f"Evidencia guardada en: {ruta_evidencia}") 
        raise 
    
    finally: 
        print("Finalizó la prueba de login bloqueado")