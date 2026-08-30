
from playground.clase4.fixtures_selenium import driver
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_suite_seleccion_y_compra(driver):
    """Test 1: Flujo completo analizando estabilidad de carga."""
    home = HomePage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)

    print("\n[PASO 1] Navegando a la plataforma...")
    home.navigate()

    print("[PASO 2] Validando sección features_items...")
    assert home.is_features_items_displayed(), "La sección de ítems destacados no cargó."

    print("[PASO 3] Haciendo clic en la marca POLO...")
    home.click_polo_brand()

    print("[PASO 4] Verificando cambio de URL de la marca...")
    assert products.is_url_correct(), "La URL no se actualizó con la palabra 'Polo'."

    print("[PASO 5] Agregando el primer ítem al carrito...")
    products.add_first_item_to_cart()

    print("[PASO 6] Esperando visibilidad del Pop-up emergente...")
    assert products.is_popup_visible(), "El pop-up de confirmación no se mostró."

    print("[PASO 7] Accediendo a la vista del carrito...")
    products.click_view_cart()

    print("[PASO 8] Validando URL interna del carrito...")
    assert cart.is_url_correct(), "No se redirigió correctamente al carrito."

    print("[PASO 9] Confirmando el Checkout y guardando evidencia...")
    cart.proceed_to_checkout_and_screenshot("evidencia_checkout.png")
