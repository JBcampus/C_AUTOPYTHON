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

<<<<<<< HEAD
    assert inventory_page.obtener_cantidad_carrito() == "1"   
=======
    assert inventory_page.obtener_cantidad_carrito() == "1"
>>>>>>> 2e3c6b826b8a33f8fa39cb4d9ac3c75da3573a8a
