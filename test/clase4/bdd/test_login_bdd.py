from selenium.webdriver.common.by import By
from pytest_bdd import scenarios, given, when, then

from playground.clase3.fixtures_selenium import driver


scenarios("features/login.feature")


@given("el usuario accede a SauceDemo")
def abrir_saucedemo(driver):
    driver.get("https://www.saucedemo.com/")


@when("ingresa credenciales válidas")
def ingresar_credenciales_validas(driver):
    campo_usuario = driver.find_element(By.ID, "user-name")
    campo_clave = driver.find_element(By.CSS_SELECTOR, "#password")

    campo_usuario.send_keys("standard_user")
    campo_clave.send_keys("secret_sauce")


@when("ingresa credenciales inválidas")
def ingresar_credenciales_invalidas(driver):
    campo_usuario = driver.find_element(By.ID, "user-name")
    campo_clave = driver.find_element(By.CSS_SELECTOR, "#password")

    campo_usuario.send_keys("standard_user")
    campo_clave.send_keys("clave_incorrecta")


@when("presiona el botón Login")
def presionar_login(driver):
    boton_login = driver.find_element(By.ID, "login-button")
    boton_login.click()


@then("debe visualizar la página de productos")
def validar_productos(driver):
    titulo_productos = driver.find_element(By.CLASS_NAME, "title")

    assert titulo_productos.text == "Products"
    assert "inventory.html" in driver.current_url


@then("debe visualizar un mensaje de error")
def validar_error_login(driver):
    mensaje_error = driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    assert "Username and password do not match" in mensaje_error.text