def normalizar_texto(texto):
    return texto.strip().lower()

def contiene_texto(texto_completo, texto_esperado):
    texto_completo = normalizar_texto(texto_completo)
    texto_esperado = normalizar_texto(texto_esperado)
    return texto_esperado in texto_completo

def textos_son_iguales(texto_actual, texto_esperado):
    texto_actual = normalizar_texto(texto_actual)
    texto_esperado = normalizar_texto(texto_esperado)
    return texto_actual == texto_esperado