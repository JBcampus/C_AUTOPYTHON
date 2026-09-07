import pytest 
 
from selenium.webdriver.common.by import By 
 
from playground.clase3.fixtures_selenium import driver 

<<<<<<< HEAD
@pytest.mark.custom
=======
@pytest.mark.custom  
>>>>>>> 2e3c6b826b8a33f8fa39cb4d9ac3c75da3573a8a
@pytest.mark.smoke 
def test_login_saucedemo_correcto(driver): 
    driver.get("https://www.saucedemo.com/") 
 
    campo_usuario = driver.find_element(By.ID, "user-name") 
<<<<<<< HEAD
    campo_clave = driver.find_element(By.ID, "password") 
    boton_login = driver.find_element(By.ID, "login-button") 
 
    campo_usuario.send_keys("standard_user") 
    campo_clave.send_keys("secret_sauce") 
    boton_login.click() 
=======
    campo_clave = driver.find_element(By.XPATH, "//input[@id='password']") 
 
    campo_usuario.send_keys("standard_user") 
    campo_clave.send_keys("secret_sauce") 
    driver.find_element(By.CSS_SELECTOR, "#login-button").click() 
>>>>>>> 2e3c6b826b8a33f8fa39cb4d9ac3c75da3573a8a
 
    titulo_productos = driver.find_element(By.CLASS_NAME, "title") 
 
    assert titulo_productos.text == "Products" 
<<<<<<< HEAD
    assert "inventory.html" in driver.current_url
=======
    assert "inventory.html" in driver.current_url 
>>>>>>> 2e3c6b826b8a33f8fa39cb4d9ac3c75da3573a8a
