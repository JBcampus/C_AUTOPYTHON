#Textos, números y valores booleanos 
url = "https://www.saucedemo.com" 
username = "standard_user" 
attempts = 3 
is_valid = True 
<<<<<<< HEAD
 
#Impresión de mensajes en terminal 
print("Hola mundo "+ username) 
print(f"Ejecutando login con usuario: {username}") # f-strings 
 
#Listas 
users = ["standard_user", "locked_out_user", "problem_user"] 
 
print(users[0]) 
print(users[1]) 
 
=======

#Impresión de mensajes en terminal 
print("Hola mundo "+ username) 
print(f"Ejecutando login con usuario: {username} ") # f-strings 

#Listas 
users = ["standard_user", "locked_out_user", "problem_user"] 
print(users[0]) 
print(users[1]) 

>>>>>>> 2e3c6b826b8a33f8fa39cb4d9ac3c75da3573a8a
#Diccionarios 
user = { 
    "username": "standard_user", 
    "password": "secret_sauce" 
} 
<<<<<<< HEAD
 
print(user["username"]) 
print(user["password"]) 
 
#Condicionales 
expected = "locked" 
 
if expected == "success": 
    print("El usuario debe ingresar correctamente") 
elif expected == "locked": 
    print("El sistema debe mostrar usuario bloqueado") 
else: 
    print("El sistema debe mostrar error de credenciales") 
 
#Ciclos 
for user in users: 
    print(f"Usuario disponible: {user}") 
 
=======
print(user["username"]) 
print(user["password"]) 

#Condicionales 
expected = "locked" 
if expected == "success": 
    print("El usuario debe ingresar correctamente") 
elif expected == "locked":
    print("El sistema debe mostrar usuario bloqueado") 
else: 
    print("El sistema debe mostrar error de credenciales") 

#Ciclos 
for user in users: 
    print(f"Usuario disponible: {user}") 
    
>>>>>>> 2e3c6b826b8a33f8fa39cb4d9ac3c75da3573a8a
#Funciones 
def build_user(username, password): 
    return { 
        "username": username, 
        "password": password 
    } 
<<<<<<< HEAD
 
=======
>>>>>>> 2e3c6b826b8a33f8fa39cb4d9ac3c75da3573a8a
user = build_user("standard_user", "secret_sauce") 
print(user)