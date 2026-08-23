def validar_registro(correo, clave, confirmacion):

    if correo == "" or clave == "" or confirmacion == "":
        return "Los campos no pueden estar vacíos"

    if "@" not in correo:
        return "El correo debe contener @"

    if len(clave) <= 6:
        return "La clave debe tener más de 6 caracteres"

    if clave != confirmacion:
        return "La clave y confirmación deben ser iguales"

    return "Registro exitoso"


def generar_correo(rol, nombre):

    if rol == "" or nombre == "":
        return "El rol y nombre no pueden estar vacíos"

    return f"{rol}.{nombre}@mail.com"