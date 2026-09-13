from playground.clase2.app_web import ( 
    validar_login, 
    obtener_titulo_pagina, 
    buscar_producto, 
    agregar_al_carrito, 
    obtener_mensaje_carrito 
) 
 
def test_login_correcto_muestra_bienvenida(): 
    mensaje = validar_login("admin", "123456") 
 
    assert mensaje == "Bienvenido al panel principal" 
 
def test_login_vacio_muestra_mensaje_obligatorio(): 
    mensaje = validar_login("", "") 
 
    assert mensaje == "Debe completar usuario y contraseña" 
 
def test_ruta_login_muestra_titulo_correcto(): 
    titulo = obtener_titulo_pagina("/login") 
 
    assert titulo == "Iniciar sesión" 
 
def test_busqueda_producto_retorna_resultado(): 
    productos = ["Laptop Lenovo", "Mouse Logitech", "Teclado Redragon"] 
 
    resultados = buscar_producto(productos, "mouse") 
 
    assert len(resultados) == 1 
    assert resultados[0] == "Mouse Logitech" 
 

def test_agregar_producto_al_carrito(): 
    carrito = [] 
 
    carrito_actualizado = agregar_al_carrito(carrito, "Laptop Lenovo") 
 
    assert len(carrito_actualizado) == 1 
    assert obtener_mensaje_carrito(carrito_actualizado) == "El carrito tiene 1 producto" 