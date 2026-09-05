import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class CheckoutPage:
    CART_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")
    FIRST_NAME = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "[data-test='lastName']")
    POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")
    FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")
    SUCCESS_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def validar_producto_en_carrito(self):
        logger.info("Validando el nombre del producto dentro del carrito.")
        elemento = self.wait.until(EC.visibility_of_element_located(self.CART_ITEM_NAME))
        return elemento.text

    def proceder_a_checkout(self):
        logger.info("Haciendo clic en el botón 'Checkout'.")
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def llenar_formulario_y_continuar(self, nombre, apellido, zip_code):
        logger.info(f"Llenando formulario de envío con: {nombre} {apellido}, CP: {zip_code}")
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(nombre)
        self.driver.find_element(*self.LAST_NAME).send_keys(apellido)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(zip_code)
        
        logger.info("Presionando el botón 'Continue' para ir al resumen.")
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def finalizar_compra(self):
        logger.info("Confirmando y finalizando la orden de compra.")
        self.wait.until(EC.visibility_of_element_located(self.FINISH_BUTTON)).click()

    def obtener_mensaje_exito(self):
        logger.info("Obteniendo mensaje de confirmación de orden exitosa.")
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_HEADER)).text
