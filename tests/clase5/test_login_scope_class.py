import pytest 
 
@pytest.mark.regression 
class TestSauceDemoConScopeClass: 

#por cada test se usa la misma clase porque tiene "Scope=Class"
#y eso se refleja en que el navegador no se cierra y vuelve abrir , porque solo se invoca la clase 1 sola vez.
 
    def test_login_muestra_inventario(self, login_page_class, inventory_page_class): 
        login_page_class.abrir() 
        login_page_class.iniciar_sesion("standard_user", "secret_sauce") 
 
        assert inventory_page_class.obtener_titulo() == "Products" 
 
    def test_agregar_producto_al_carrito(self, login_page_class, inventory_page_class): 
 
        login_page_class.abrir() 
        login_page_class.iniciar_sesion("standard_user", "secret_sauce") 
        inventory_page_class.agregar_mochila_al_carrito() 
 
        assert inventory_page_class.obtener_cantidad_carrito() == "1"