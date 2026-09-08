import pytest 
 
@pytest.mark.smoke 
def test_login_correcto_con_pom(login_page, inventory_page): 
    login_page.abrir() 
    login_page.iniciar_sesion("standard_user", "secret_sauce") 
 
    assert inventory_page.obtener_titulo() == "Products" 