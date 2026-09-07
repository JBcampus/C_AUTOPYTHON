import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class InventoryPage:
    SORT_SELECT = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    LISTA_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    CARRITO_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CARRITO_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def ordenar_productos_por_valor(self, valor_orden):
        
        logger.info(f"Cambiando filtro de ordenamiento a: {valor_orden}")
        select_element = self.wait.until(EC.element_to_be_clickable(self.SORT_SELECT))
        select = Select(select_element)
        select.select_by_value(valor_orden)

    def obtener_producto_indice(self, indice):
        
        productos = self.driver.find_elements(*self.LISTA_ITEMS)
        producto = productos[indice]
        return producto

    def obtener_nombre_producto_por_indice(self, indice):
        
        producto_target = self.obtener_producto_indice(indice)
        return producto_target.find_element(By.CSS_SELECTOR, ".inventory_item_name").text

    def agregar_al_carrito_por_indice(self, indice):
        
        logger.info(f"Intentando añadir producto en el índice de lista: {indice}")
        
        # Esperamos a que los elementos estén presentes primero
        self.wait.until(EC.presence_of_all_elements_located(self.LISTA_ITEMS))
        
        try:
           
            producto_target = self.obtener_producto_indice(indice)
            
            boton_agregar = producto_target.find_element(By.CSS_SELECTOR, "button[id^='add-to-cart']")
            boton_agregar.click()
            logger.info(f"Producto en índice {indice} añadido correctamente.")
        except IndexError:
            raise IndexError(f"El índice solicitado ({indice}) no existe en la tienda.")

    def obtener_cantidad_carrito(self):
        try:
            cantidad = self.driver.find_element(*self.CARRITO_BADGE).text
            logger.info(f"Productos en el carrito detectados: {cantidad}")
            return cantidad
        except:
            return "0"

    def ir_al_carrito(self):
        logger.info("Navegando hacia la pantalla del carrito.")
        self.driver.find_element(*self.CARRITO_LINK).click()
