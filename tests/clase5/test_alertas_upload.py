from pathlib import Path 
 
import pytest 
 
@pytest.mark.special 
def test_alerta_simple(alerts_page): 
    alerts_page.abrir() 
    alerts_page.abrir_alerta_simple() 
    alerts_page.aceptar_alerta() 
 
    assert alerts_page.obtener_resultado() == "You successfully clicked an alert" 

@pytest.mark.special 
def test_confirmacion_cancelada(alerts_page): 
    alerts_page.abrir() 
    alerts_page.abrir_confirmacion() 
    alerts_page.cancelar_alerta() 
 
    assert alerts_page.obtener_resultado() == "You clicked: Cancel" 
 
@pytest.mark.special 
def test_prompt_con_texto(alerts_page): 
    alerts_page.abrir() 
    alerts_page.abrir_prompt() 
    alerts_page.escribir_en_prompt("Curso Selenium") 
 
    assert alerts_page.obtener_resultado() == "You entered: Curso Selenium" 
 
@pytest.mark.special 
def test_carga_archivo(upload_page): 
    ruta_archivo = Path("data/clase5/archivo_demo.txt") 
 
    upload_page.abrir() 
    upload_page.cargar_archivo(ruta_archivo) 
    upload_page.enviar_archivo() 
 
    assert upload_page.obtener_nombre_archivo_cargado() == "archivo_demo.txt" 