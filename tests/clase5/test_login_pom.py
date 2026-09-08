import pytest 
import allure

@allure.title("Login válido con evidencia")
@allure.epic("E-commerce")
@allure.feature("Autenticación")
@allure.story("Login exitoso")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Pruebas UI") 
@pytest.mark.smoke 
def test_login_correcto_con_pom(login_page, inventory_page): 
    with allure.step("Inicio de pruebas"):
        login_page.abrir() 
    login_page.iniciar_sesion("standard_user", "secret_sauce") 

    with allure.step("Fin de pruebas"):
        assert inventory_page.obtener_titulo() == "Products" 


@allure.title("Agregar producto al carrito de compra")
@allure.epic("E-commerce")
@allure.feature("Selección de producto")
@allure.story("Validación de carrito de compra")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Pruebas UI") 
def test_agregar_producto_al_carrito(login_page, inventory_page): 
    with allure.step("Navegador al login"):
        login_page.abrir() 

    with allure.step("Autenticarse"):
        login_page.iniciar_sesion("standard_user", "secret_sauce") 

    with allure.step("Seleccionar producto"):
        inventory_page.agregar_mochila_al_carrito() 

    assert inventory_page.obtener_cantidad_carrito() == "1"