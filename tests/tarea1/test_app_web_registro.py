import os 
import pytest 

from playground.tarea1.app_web_registro import ( 
    validar_registro,
    generar_correo
) 

@pytest.fixture(scope="session")
def casos_registro():
    return [
        { 
            "correo": "", 
            "clave": "Admin123",
            "confirmacion": "Admin123",
            "mensaje": "Debe completar todos los campos"
        },
        { 
            "correo": "admin.sergio@mail.com", 
            "clave": "Admin123",
            "confirmacion": "Admin456",
            "mensaje": "La contraseña y la confirmación no coinciden"
        },
        { 
            "correo": "admin.sergio@mail.com", 
            "clave": "Admin123",
            "confirmacion": "Admin123",
            "mensaje": "Registro exitoso"
        },
    ]

def test_casos_registro_fixture(casos_registro):
    for caso in casos_registro:
        resultado = validar_registro(caso["correo"], caso["clave"], caso["confirmacion"])
        assert resultado == caso["mensaje"], f"Fallo en el caso: {caso}, resultado: {resultado}"
        print(f"Resultado del caso {caso}: {resultado}")

@pytest.mark.smoke
def test_generar_correo():
    correo = generar_correo("admin", "sergio")
    assert "@mail.com" in correo