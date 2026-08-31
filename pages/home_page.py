from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    """Mapea los elementos y acciones de la página principal (Home)."""

    # Localizadores utilizando selectores XPATH y CSS válidos
    FEATURES_ITEMS = (By.CLASS_NAME, "features_items")
    POLO_BRAND_BTN = (By.XPATH, "//a[@href='/brand_products/Polo']")

    def __init__(self, driver):
        """Inicializa la página Home."""
        super().__init__(driver)
        self.url = "https://automationexercise.com"

    def navigate(self):
        """Navega hacia la URL principal de Automation Exercise."""
        self.driver.get(self.url)

    def is_features_items_displayed(self) -> bool:
        """Valida mediante espera explícita si la sección 'features_items' está disponible.

        Returns:
            bool: True si el contenedor de ítems destacados es visible.
        """
        return self.wait_element_visible(self.FEATURES_ITEMS).is_displayed()

    def click_polo_brand(self):
        """Busca el botón de la categoría de marca 'POLO' y hace clic robusto."""
    # Selector alternativo insensible a mayúsculas si aplica
        locator = (By.XPATH, "//a[contains(@href, '/brand_products/Polo')]")
        element = self.wait_element_visible(locator)
    # Forzar clic por JS en caso de interferencia de anuncios flotantes
        self.driver.execute_script("arguments[0].click();", element)

