# Automatización E2E Web con Python, Selenium y Pytest

## Estructura

- tests/: casos de prueba
- pages/: Page Objects
- helpers/: utilidades reutilizables
- data/: datos de prueba
- artifacts/: evidencias generadas

## Validación de herramientas

pip --version

## Ejecución inicial

pytest

## Comandos Taller3

pytest tests/clase3/test_saucedemo_login.py -v
pytest tests/clase3/test_saucedemo_login.py -m smoke -v
pytest tests/clase3/test_saucedemo_login.py -k login -v
pytest -v -s tests/clase3/test_navegacion_basica.py #ejecutar todos test en un archivo
pytest -m smoke -v #ejecutar test con markador Smoke
pytest tests/clase3/test_saucedemo_login.py::test_login_saucedemo_correcto -v #ejecutar test especifico en un archivo
pytest tests/clase2/test_fixtures_marcadores.py::test_critical_carrito -v #ejecutar test especifico en un archivo
pytest -k "login" -v #ejecutar test que contengan nombre "login"
