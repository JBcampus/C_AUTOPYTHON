import pytest 
 
from datetime import datetime 
from pathlib import Path 
 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

from playground.clase4.fixtures_selenium import driver 

@pytest.mark.regression
def test_seleccion_compra_exitosa(driver):
    wait = WebDriverWait(driver, 10)

    try:
        # Paso 1: Navegar a la pagina
        driver.get("https://automationexercise.com/")

        # Paso 2: Validar que la sección de productos esté disponible
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "features_items")))

        # Paso 3: Ubicar botón "Polo" y hacer clic
        boton_polo = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@href, '/brand_products/Polo') and contains(normalize-space(.), 'Polo')]")
            )
        )
        boton_polo.click()


        #Paso 4: Esperar que url contenga “Polo”.
        wait.until(EC.url_contains("/brand_products/Polo"))

        #Paso 5: Dar click en “Add to cart” al primer elemento
        producto_polo = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[data-product-id="1"].add-to-cart')))
        producto_polo.click()                               

        #Paso 6: Esperar a que pop up sea visible
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"modal-content")))

        #Paso 7: Dar click en “View Cart”
        boton_view_cart = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"View Cart")))
        boton_view_cart.click()

        #Paso 8: Esperar que url contenga “/view_cart”.
        wait.until(EC.url_contains("/view_cart"))

        #Paso 9: Dar click en “Proceed to Checkout” y capturar evidencia
        btn_check_out = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-default.check_out")))
        btn_check_out.click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog.modal-confirm")))
        
        
    except Exception: 
        # Definición de carpeta, crea si no existe 
        carpeta_evidencias = Path("artifacts/tarea2") 

        carpeta_evidencias.mkdir(parents=True, exist_ok=True) 
        # Fecha de fallo y nombre de la evidencia 

        fecha = datetime.now().strftime("%Y%m%d_%H%M%S") 
        ruta_evidencia = carpeta_evidencias / f"fallo_compra_{fecha}.png" 

        # Captura de evidencia de fallo 
        driver.save_screenshot(str(ruta_evidencia)) 
        print(driver.current_url)
        print(f"Evidencia guardada en: {ruta_evidencia}") 
        raise 
    
    finally: 
        print("Finalizó la prueba")

#pasos:


