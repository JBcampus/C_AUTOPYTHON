def validar_registro(correo, clave, confirmacion):

# 1. los parámetros de entrada No dene  ser vacios

    if correo == "" or clave == "" or confirmacion == "":
        return "Los campos no pueden estar vacíos"
    
# 2. el parámetro correo debe contener @
    if "@" not in correo:
        return "El correo debe contener @"
    
# 3. el parámetro clave debe tener más de 6 caracteres 
    if len(clave) <= 6:
        return "La clave debe tener más de 6 caracteres"

# 4. los parámetros clave y confirmación deben ser iguales 
    if clave != confirmacion:
        return "La clave y confirmación deben ser iguales"

    return "Registro exitoso"


def generar_correo(rol, nombre):

    if rol == "" or nombre == "":
        return "El rol y nombre no pueden estar vacíos"

    return f"{rol}.{nombre}@mail.com"