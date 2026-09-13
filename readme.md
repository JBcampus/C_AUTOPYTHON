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