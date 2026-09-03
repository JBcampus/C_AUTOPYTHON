import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Clase base para el modelo POM utilizando tu fixture personalizado."""

    def __init__(self, driver):
        """Inicializa la página base con tu driver de Edge.
        Args:
            driver: Instancia de Microsoft Edge heredada del fixture.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 

    def wait_element_visible(self, locator):
        """Espera explícita hasta que un elemento sea visible."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_url_contains(self, text: str) -> bool:
        """Espera explícita hasta que la URL contenga un texto."""
        return self.wait.until(EC.url_contains(text))

    def click(self, locator):
        """Espera visibilidad y hace clic en el elemento."""
        self.wait_element_visible(locator).click()

    def take_screenshot(self, filename: str):
        """Guarda la evidencia en la ruta exacta solicitada en el taller."""
        directory = "artifacts/tarea2"
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        path = os.path.join(directory, filename)
        self.driver.save_screenshot(path)
        print(f"\n[EVIDENCIA] Captura guardada en: {path}")
