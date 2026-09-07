from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    """Mapea los elementos de la página de productos filtrados por la marca Polo."""

    
    # Localizador enfocado directamente en el primer botón interactuable del grid
    FIRST_ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".features_items .col-sm-4 .productinfo .add-to-cart")

    MODAL_POPUP = (By.CLASS_NAME, "modal-content")
    VIEW_CART_LINK = (By.XPATH, "//u[text()='View Cart']")

    def is_url_correct(self) -> bool:
        """Espera a que la URL del navegador contenga la palabra 'Polo'.

        Returns:
            bool: True si la URL se actualizó correctamente con el filtro de la marca.
        """
        return self.wait_url_contains("Polo")

    def add_first_item_to_cart(self):
        """Hace clic sobre el botón 'Add to cart' asignado al primer elemento visible."""
        self.click(self.FIRST_ADD_TO_CART_BTN)

    def is_popup_visible(self) -> bool:
        """Espera a que el modal emergente de éxito sea visible.

        Returns:
            bool: True si el modal emergente se encuentra desplegado en el DOM.
        """
        return self.wait_element_visible(self.MODAL_POPUP).is_displayed()

    def click_view_cart(self):
        """Hace clic sobre el enlace 'View Cart' del mensaje de confirmación."""
        self.click(self.VIEW_CART_LINK)
