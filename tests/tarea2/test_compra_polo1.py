import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # Desactiva extensiones y bloquea popups para evitar interferencias
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_flujo_seleccion_y_compra(driver):
    wait = WebDriverWait(driver, 15)

    # 1. Navegar a la página
    driver.get("https://automationexercise.com/")

    # 2. Validar que "features_items" esté disponible
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "features_items"))
    )

    # 3. Ubicar botón "POLO" y dar click
    polo_brand_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/brand_products/Polo')]"))
    )
    driver.execute_script("arguments[0].click();", polo_brand_btn)

    # Si salta un anuncio de Google (redirección #google_vignette), forzamos la navegación
    if "#google_vignette" in driver.current_url or "Polo" not in driver.current_url:
        driver.get("https://automationexercise.com/brand_products/Polo")

    # 4. Esperar que la URL contenga "Polo"
    wait.until(EC.url_contains("Polo"))

    # 5. Dar click en "Add to cart" al primer elemento usando JavaScript para evitar superposiciones
    add_to_cart_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//a[contains(@class, 'add-to-cart')])[1]"))
    )
    driver.execute_script("arguments[0].click();", add_to_cart_btn)

    # 6. Esperar a que el pop up sea visible
    wait.until(
        EC.visibility_of_element_located((By.ID, "cartModal"))
    )

    # 7. Dar click en "View Cart" dentro del pop up
    view_cart_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//u[text()='View Cart']/parent::a"))
    )
    driver.execute_script("arguments[0].click();", view_cart_btn)

    # 8. Esperar que la URL contenga "/view_cart"
    wait.until(EC.url_contains("/view_cart"))

    # 9. Dar click en "Proceed To Checkout"
    proceed_checkout_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'check_out')]"))
    )
    driver.execute_script("arguments[0].click();", proceed_checkout_btn)

    # 10. Capturar evidencia en artifacts/tarea2
    output_dir = os.path.join("artifacts", "tarea2")
    os.makedirs(output_dir, exist_ok=True)
    
    screenshot_path = os.path.join(output_dir, "evidencia_checkout.png")
    driver.save_screenshot(screenshot_path)