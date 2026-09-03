import pytest 
 
@pytest.mark.smoke 
def test_login_correcto_con_pom(login_page, inventory_page): 
    login_page.abrir() 
    login_page.iniciar_sesion("standard_user", "secret_sauce") 
 
    assert inventory_page.obtener_titulo() == "Products" 

def test_agregar_producto_al_carrito(login_page, inventory_page): 
    login_page.abrir() 
    login_page.iniciar_sesion("standard_user", "secret_sauce") 
    inventory_page.agregar_mochila_al_carrito() 

    assert inventory_page.obtener_cantidad_carrito() == "1"   