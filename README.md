<<<<<<< HEAD
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

## Comandos Taller6
-Ejecutar ejemplo de helpers basicos
pytest tests/clase6/test_login_data_driven.py -v

-Ejecutar ejemplo de data driven
pytest tests/clase6/test_login_data_driven.py -v

-Comando ejecución de cobertura de proyecto
pytest tests/clase6/test_helpers_basicos.py --cov=helpers --cov=pages --cov-report=term-missing --cov-report=html:coverage-report

-Levantar reporte de cobertura html
start coverage-report/index.html

## Comandos Tarea3
-Comando ejecución de cobertura de proyecto
pytest tests/tarea3/test_suite1.py --cov=helpers --cov=pages --cov-report=term-missing --cov-report=html:coverage-report

-Levantar reporte de cobertura html
start coverage-report/index.html

=======
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
pytest tests/tarea2/test_saucedemo_compra.py -v
python -m pytest tests/clase5/test_login_pom.py -v
python -m pytest tests/clase5/test_login_scope_class.py -v
>>>>>>> 2e3c6b826b8a33f8fa39cb4d9ac3c75da3573a8a
