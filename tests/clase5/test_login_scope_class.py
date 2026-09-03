import pytest 
 
@pytest.mark.regression 
class TestSauceDemoConScopeClass: 
 
    def test_login_muestra_inventario(self, login_page_class, inventory_page_class): 
        login_page_class.abrir() 
        login_page_class.iniciar_sesion("standard_user", "secret_sauce") 
 
        assert inventory_page_class.obtener_titulo() == "Products" 
 
    def test_agregar_producto_al_carrito(self, login_page_class, inventory_page_class): 
 
        login_page_class.abrir() 
        login_page_class.iniciar_sesion("standard_user", "secret_sauce") 
        inventory_page_class.agregar_mochila_al_carrito() 
 
        assert inventory_page_class.obtener_cantidad_carrito() == "1"