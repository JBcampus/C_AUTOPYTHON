from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")

    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    SORT_SELECT = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    LISTA_ITEMS = (By.CSS_SELECTOR, ".inventory_item")

    BUTTON = (By.CSS_SELECTOR, "button")

    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    CKECKOUT = (By.ID, "checkout")

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    BUTTON_CONTINUE = (By.ID, "continue")
    BUTTON_FINISH = (By.ID, "finish")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_current_url(self):
        return self.driver.current_url

    def obtener_titulo(self):
        titulo = self.wait.until(
            EC.visibility_of_element_located(self.TITLE)
        )
        return titulo.text
    
    def ordenar_productos_por_valor(self, valor_orden):
        select_element = self.driver.find_element(*self.SORT_SELECT)
        select = Select(select_element)
        select.select_by_value(valor_orden)

    def obtener_producto_indice(self, indice):
        productos = self.driver.find_elements(*self.LISTA_ITEMS)
        producto = productos[indice]
        boton = producto.find_element(*self.BUTTON)
        boton.click()
    
    def obtener_cantidad_carrito(self):
        badge = self.wait.until(
            EC.visibility_of_element_located(self.SHOPPING_CART_BADGE)
        )
        return badge.text

    def ingresar_carrito(self):
        carrito = self.wait.until(EC.visibility_of_element_located(self.SHOPPING_CART_LINK))
        carrito.click()

    def obtener_nombre_producto(self):
        nombre_producto = self.wait.until(EC.visibility_of_element_located(self.INVENTORY_ITEM_NAME))
        return nombre_producto.text

    def click_checkout(self):
        carrito = self.wait.until(EC.visibility_of_element_located(self.CKECKOUT))
        carrito.click()

    def completar_formulario(self, first_name, last_name, postal_code):
        nombre = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        nombre.send_keys(first_name)

        apellido = self.wait.until(EC.visibility_of_element_located(self.LAST_NAME))
        apellido.send_keys(last_name)

        apellido = self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE))
        apellido.send_keys(postal_code)

    def click_boton_continue(self):
        boton_continue = self.wait.until(EC.visibility_of_element_located(self.BUTTON_CONTINUE))
        boton_continue.click()

    def click_boton_finish(self):
        boton_continue = self.wait.until(EC.visibility_of_element_located(self.BUTTON_FINISH))
        boton_continue.click()

