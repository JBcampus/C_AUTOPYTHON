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
