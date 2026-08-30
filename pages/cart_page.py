from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    """Mapea las acciones dentro del carrito de compras de la aplicación."""

    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, ".check_out")

    def is_url_correct(self) -> bool:
        """Espera a que la URL del navegador contenga '/view_cart'.

        Returns:
            bool: True si la URL de navegación es la correcta.
        """
        return self.wait_url_contains("/view_cart")

    def proceed_to_checkout_and_screenshot(self, image_name="evidencia_final.png"):
        """Hace clic en 'Proceed to Checkout' y toma la captura requerida por el taller.

        Args:
            image_name (str): Nombre del archivo de imagen para la evidencia.
        """
        self.click(self.PROCEED_TO_CHECKOUT_BTN)
        self.take_screenshot(image_name) 
