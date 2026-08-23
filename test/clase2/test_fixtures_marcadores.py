import os 
import pytest 
 
from playground.clase2.app_web import ( 
    validar_login, 
    buscar_producto, 
    agregar_al_carrito, 
    obtener_mensaje_carrito 
) 
 
@pytest.fixture 
def usuario_valido(): 
    return { 
        "usuario": "admin", 
        "clave": "123456" 
    } 
 
@pytest.fixture 
def productos_demo(): 
    return [ 
        "Laptop Lenovo", 
        "Mouse Logitech", 
        "Teclado Redragon" 
    ] 
 
 
@pytest.fixture 
def carrito_vacio(): 
    return [] 
 
def test_login_usando_fixture(usuario_valido): 
    mensaje = validar_login( 
        usuario_valido["usuario"], 
        usuario_valido["clave"] 
    ) 
 
    assert mensaje == "Bienvenido al panel principal" 
 
def test_busqueda_usando_fixture(productos_demo): 
    resultados = buscar_producto(productos_demo, "mouse") 
 
    assert resultados[0] == "Mouse Logitech" 
 
def test_carrito_usando_fixture(carrito_vacio): 
    carrito = agregar_al_carrito(carrito_vacio, "Laptop Lenovo") 
 
    assert obtener_mensaje_carrito(carrito) == "El carrito tiene 1 producto" 
 
@pytest.fixture 
def archivo_evidencia(): 
    nombre_archivo = "evidencia_login.txt" 
 
    archivo = open(nombre_archivo, "w", encoding="utf8") 
 
    archivo.write("Evidencia simulada de prueba de login") 
    archivo.close() 
 
    yield nombre_archivo 
 
    if os.path.exists(nombre_archivo): 
        os.remove(nombre_archivo) 
 
def test_archivo_evidencia_se_crea(archivo_evidencia): 
    assert os.path.exists(archivo_evidencia) is True 
 
@pytest.fixture(scope="function") 
def datos_login_function(): 
    print("Fixture function ejecutada") 
 
    return { 
        "usuario": "admin", 
        "clave": "123456" 
    } 
 
def test_scope_function(datos_login_function): 
    mensaje = validar_login( 
        datos_login_function["usuario"], 
        datos_login_function["clave"] 
    ) 
 
    assert mensaje == "Bienvenido al panel principal" 
 
@pytest.fixture(scope="class") 
def datos_login_class(): 
    print("Fixture class ejecutada") 
 
    return { 
        "usuario": "admin", 
        "clave": "123456" 
    } 
 
class TestLogin: 
 
    def test_usuario_es_admin(self, datos_login_class): 
        assert datos_login_class["usuario"] == "admin" 
 
    def test_login_es_correcto(self, datos_login_class): 
        mensaje = validar_login( 
            datos_login_class["usuario"], 
            datos_login_class["clave"] 
        ) 
 
        assert mensaje == "Bienvenido al panel principal" 
 
@pytest.fixture(scope="module") 
def datos_modulo(): 
    print("Fixture module ejecutada") 
 
    return "Datos compartidos en este archivo" 
 
def test_scope_module(datos_modulo): 
    assert datos_modulo == "Datos compartidos en este archivo" 
 
@pytest.fixture(scope="session") 
def datos_session(): 
    print("Fixture session ejecutada") 
 
    return "Curso Selenium con Pytest" 

 
def test_scope_session(datos_session): 
    assert "Pytest" in datos_session 
 
@pytest.mark.smoke 
def test_smoke_login(usuario_valido): 
    mensaje = validar_login( 
        usuario_valido["usuario"], 
        usuario_valido["clave"] 
    ) 
 
    assert mensaje == "Bienvenido al panel principal" 
 
@pytest.mark.regression 
def test_regression_busqueda(productos_demo): 
    resultados = buscar_producto(productos_demo, "teclado") 
 
    assert resultados[0] == "Teclado Redragon" 
 
@pytest.mark.critical 
def test_critical_carrito(carrito_vacio): 
    carrito = agregar_al_carrito(carrito_vacio, "Mouse Logitech") 
 
    assert obtener_mensaje_carrito(carrito) == "El carrito tiene 1 producto" 
    