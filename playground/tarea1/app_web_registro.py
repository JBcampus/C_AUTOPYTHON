# playground/tarea1/app_web_registro.py

def validar_registro(correo, clave, confirmacion):
   
    # 1. Los parámetros de entrada NO deben ser vacíos
    if not correo or not clave or not confirmacion:
        return "Debe completar todos los campos"
    
    # 2. El parámetro correo debe contener @
    if "@" not in correo:
        return "El correo electrónico no es válido"
    
    # 3. El parámetro clave debe tener más de 6 caracteres
    if len(clave) <= 6:
        return "La contraseña debe tener más de 6 caracteres"
    
    # 4. Los parámetros clave y confirmación deben ser iguales
    if clave != confirmacion:
        return "Las contraseñas no coinciden"
    
    # Si cumple todas las condiciones
    return "Registro exitoso"


def generar_correo(rol, nombre):
   
    # 1. Validar que los parámetros de entrada NO sean vacíos
    if not rol or not nombre:
        return "El rol y el nombre son obligatorios"
    
    # 2. Retornar el correo formateado
    return f"{rol.lower()}.{nombre.lower()}@mail.com"