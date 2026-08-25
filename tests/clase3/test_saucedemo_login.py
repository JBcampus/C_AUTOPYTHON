import pytest

from selenium.webdriver.common.by import By

from playground.clase3.fixtures_selenium import driver

@pytest.mark.custom
@pytest.mark.smoke
def test_login_saucedemo_correcto(driver):
    driver.get("https://www.saucedemo.com/")

    campo_usuario = driver.find_element(By.ID, "user-name")
    campo_clave = driver.find_element(By.ID,"password")
    boton_login = driver.find_element(By.ID, "login-button")

    #se ingresa textos en los campos
    campo_usuario.send_keys("standard_user")
    campo_clave.send_keys("secret_sauce")

    #se da click en el botón
    boton_login.click()

    #e extrae un titulo de la pagina
    titulo_productos = driver.find_element(By.CLASS_NAME, "title")

    assert titulo_productos.text == "Products"
    assert "inventory.html" in driver.current_url 