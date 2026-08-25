# tests/tarea1/test_registro.py

import pytest
from playground.tarea1.app_web_registro import validar_registro, generar_correo

@pytest.fixture(scope="session")
def casos_registro():
    
    return [
        {
            "correo": "usuario@correo.com",
            "clave": "admin123",
            "confirmacion": "admin123",
            "mensaje": "Registro exitoso"
        },
        {
            "correo": "testmail.com", # Sin @
            "clave": "1234567",
            "confirmacion": "1234567",
            "mensaje": "El correo electrónico no es válido"
        },
        {
            "correo": "admin@correo.com",
            "clave": "123", # Menos de 6 caracteres
            "confirmacion": "123",
            "mensaje": "La contraseña debe tener más de 6 caracteres"
        }
    ]


def test_casos_registro_fixture(casos_registro):
   
    for caso in casos_registro:
        resultado = validar_registro(
            correo=caso["correo"],
            clave=caso["clave"],
            confirmacion=caso["confirmacion"]
        )
        assert resultado == caso["mensaje"], f"Falló para el caso: {caso}"


@pytest.mark.smoke
def test_generar_correo_admin():
    
    # Reemplaza 'tu_nombre' con tu nombre real si es necesario para el entregable
    resultado = generar_correo("admin", "wilfredop")
    
    assert "@mail.com" in resultado
    assert resultado == "admin.wilfredop@mail.com"