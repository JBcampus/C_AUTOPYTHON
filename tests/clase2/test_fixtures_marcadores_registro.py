import pytest

from playground.clase2.app_web_registro import (
    validar_registro,
    generar_correo
)


@pytest.fixture(scope="session")
def casos_registro():
    return [
        {
            "correo": "daniel@gmail.com",
            "clave": "1234567",
            "confirmacion": "1234567",
            "mensaje": "Registro exitoso"
        },
        {
            "correo": "danielgmail.com",
            "clave": "1234567",
            "confirmacion": "1234567",
            "mensaje": "El correo debe contener @"
        },
        {
            "correo": "daniel@gmail.com",
            "clave": "123",
            "confirmacion": "133",
            "mensaje": "La clave debe tener más de 6 caracteres"
        }
    ]


def test_casos_registro_fixture(casos_registro):

    for caso in casos_registro:

        mensaje = validar_registro(
            caso["correo"],
            caso["clave"],
            caso["confirmacion"]
        )

        assert mensaje == caso["mensaje"]


@pytest.mark.smoke
def test_generar_correo():

    correo = generar_correo(
        "admin",
        "danielquintanilla"
    )

    assert "danielquintanilla" in correo
    assert "@mail.com" in correo