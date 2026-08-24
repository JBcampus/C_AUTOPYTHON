def validar_registro(correo, clave, confirmacion):
    if correo == "" or clave == "" or confirmacion == "":
        return "Debe completar todos los campos"

    if "@" not in correo:
        return "El correo debe contener @"

    if len(clave) <= 6:
        return "La clave debe tener más de 6 caracteres"

    if clave != confirmacion:
        return "La contraseña y la confirmación no coinciden"

    return "Registro exitoso"

def generar_correo(rol, nombre):
    if rol == "" or nombre == "":
        return "Debe completar todos los campos"

    return f"{rol.lower()}.{nombre.lower()}@mail.com"
