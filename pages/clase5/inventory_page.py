from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
 
class InventoryPage: 
    TITLE = (By.CLASS_NAME, "title") 
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack") 
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge") 
 
    def __init__(self, driver): 
        self.driver = driver 
        self.wait = WebDriverWait(driver, 10) 
 
    def obtener_titulo(self): 
        titulo = self.wait.until( EC.visibility_of_element_located(self.TITLE) ) 
        return titulo.text 
 
    def agregar_mochila_al_carrito(self): 
        boton = self.wait.until(EC.element_to_be_clickable(self.ADD_BACKPACK_BUTTON)) 
        boton.click() 
 
    def obtener_cantidad_carrito(self): 
        badge = self.wait.until(EC.visibility_of_element_located(self.SHOPPING_CART_BADGE)) 
        return badge.text 