def validar_registro(correo, clave, confirmacion): 
    if correo == "" or clave == "" or confirmacion == "": 
        return "Debe completar todos los campos" 
 
    if "@" not in correo:
        return "Correo inválido: falta '@'" 

    if len(clave) <= 6:
        return "La clave debe tener más de 6 caracteres"

    if clave == confirmacion:
        return "Registro exitoso"

    return "No se puede registrar: la clave y la confirmación no coinciden" 


def generar_correo(rol, nombre):
    if rol == "" or nombre == "":
        return "Debe completar ambos campos"

    return f"{rol.lower()}.{nombre.lower()}@mail.com"
