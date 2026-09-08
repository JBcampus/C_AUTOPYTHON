import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_flujo_seleccion_y_compra(driver):
    wait = WebDriverWait(driver, 15)

    # Crear la carpeta de evidencias si no existe
    output_dir = os.path.join("artifacts", "tarea2")
    os.makedirs(output_dir, exist_ok=True)

    # 1. Navegar a la página
    driver.get("https://automationexercise.com/")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "features_items")))
    
    # 📸 CAPTURA 1: Inicio (Features Items)
    driver.save_screenshot(os.path.join(output_dir, "01_home.png"))

    # 2. Ubicar botón "POLO" y dar click
    polo_brand_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/brand_products/Polo')]"))
    )
    driver.execute_script("arguments[0].click();", polo_brand_btn)

    # Control por si aparece publicidad de Google
    if "#google_vignette" in driver.current_url or "Polo" not in driver.current_url:
        driver.get("https://automationexercise.com/brand_products/Polo")

    wait.until(EC.url_contains("Polo"))
    
    # 📸 CAPTURA 2: Sección de Productos Polo
    driver.save_screenshot(os.path.join(output_dir, "02_polo_products.png"))

    # 3. Dar click en "Add to cart" al primer elemento
    add_to_cart_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//a[contains(@class, 'add-to-cart')])[1]"))
    )
    driver.execute_script("arguments[0].click();", add_to_cart_btn)

    # 4. Esperar a que el pop up sea visible
    wait.until(EC.visibility_of_element_located((By.ID, "cartModal")))
    
    # 📸 CAPTURA 3: Pop-up / Modal "Added!"
    driver.save_screenshot(os.path.join(output_dir, "03_modal_added.png"))

    # 5. Dar click en "View Cart"
    view_cart_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//u[text()='View Cart']/parent::a"))
    )
    driver.execute_script("arguments[0].click();", view_cart_btn)

    # 6. Esperar que la url contenga "/view_cart"
    wait.until(EC.url_contains("/view_cart"))
    
    # 📸 CAPTURA 4: Vista del Carrito de Compras
    driver.save_screenshot(os.path.join(output_dir, "04_view_cart.png"))

    # 7. Dar click en "Proceed To Checkout"
    proceed_checkout_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'check_out')]"))
    )
    driver.execute_script("arguments[0].click();", proceed_checkout_btn)

    # 📸 CAPTURA 5: Evidencia Final en Checkout
    driver.save_screenshot(os.path.join(output_dir, "05_evidencia_checkout.png"))