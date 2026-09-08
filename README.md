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

## Comandos Tarea Integrador

-Ejecucion con 2 Workers + Cobertura + Allure
python -m pytest tests/integrador/test_suite1.py -v -n 2 --cov=helpers --cov=pages --cov-report=term-missing --cov-report=html:coverage-report --alluredir=reports/allure-results --clean-alluredir

-Ejecucion con Workers: (n 2 indica la cantidad de workers)
python -m pytest tests/integrador/test_suite1.py -v -n 2

-Comando ejecución de cobertura de proyecto
python -m pytest tests/integrador/test_suite1.py --cov=helpers --cov=pages --cov-report=term-missing --cov-report=html:coverage-report

-Levantar reporte de cobertura html
start coverage-report/index.html

-Generar Reporte Allure
python -m pytest tests/integrador/test_suite1.py --alluredir=reports/allure-results --clean-alluredir
python -m pytest tests/integrador/test_suite1.py --alluredir=reports/allure-results
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
