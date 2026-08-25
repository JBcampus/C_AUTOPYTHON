def validar_login(usuario, clave): 
    if usuario == "" or clave == "": 
        return "Debe completar usuario y contraseña" 
 
    if usuario == "admin" and clave == "123456": 
        return "Bienvenido al panel principal" 
 
    return "Credenciales incorrectas" 

def obtener_titulo_pagina(ruta): 
    if ruta == "/login": 
        return "Iniciar sesión" 
 
    if ruta == "/productos": 
        return "Catálogo de productos" 
 
    if ruta == "/carrito": 
        return "Carrito de compras" 
 
    return "Página no encontrada" 
 
def buscar_producto(productos, texto_busqueda): 
    resultados = [] 
 
    for producto in productos: 
        if texto_busqueda.lower() in producto.lower(): 
            resultados.append(producto) 
 
    return resultados 
 
def agregar_al_carrito(carrito, producto): 
    carrito.append(producto) 
 
    return carrito 
 
def obtener_mensaje_carrito(carrito): 
    if len(carrito) == 0: 
        return "El carrito está vacío" 
 
    if len(carrito) == 1: 
        return "El carrito tiene 1 producto" 
 
    return f"El carrito tiene {len(carrito)} productos" 