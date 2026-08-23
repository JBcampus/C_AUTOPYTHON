import os 
import pytest 
 
from playground.clase2.app_web import validar_login
from playground.tarea1.app_web_registro import ( 
    validar_registro, 
    generar_correo 
) 
 
@pytest.fixture(scope="session") 
def casos_registro(): 
    return [
        {
            "correo": "",
            "clave": "1111111",
            "confirmacion": "1234567",
            "mensaje": "Debe completar todos los campos"
        },
        {
            "correo": "usuario@mail.com",
            "clave": "123",
            "confirmacion": "123",
            "mensaje": "La clave debe tener más de 6 caracteres"
        },
        {
            "correo": "usuario@mail.com",
            "clave": "1234567",
            "confirmacion": "1234567",
            "mensaje": "Registro exitoso"
        }
    ] 

def test_casos_registro_fixture(casos_registro):
    for caso in casos_registro:
        resultado = validar_registro(caso["correo"], caso["clave"], caso["confirmacion"])
        assert resultado == caso["mensaje"]

@pytest.mark.smoke
def test_generar_correo_smoke():
    resultado = generar_correo("admin", "adelina")
    print(resultado)
    assert "@mail.com" in resultado

