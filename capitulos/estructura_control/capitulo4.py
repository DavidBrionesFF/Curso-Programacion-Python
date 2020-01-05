# -*- coding: utf-8 -*-
"""
Estructuras de control, identacion, encodig, asignacion multiple
"""
# inicio_estructura_control:
#    expresiones
# La estructura if

mi_lista = [
    {
        "usuario": "admin",
        "contrasena": "admin"
    },
    {
        "usuario": "root",
        "contrasena": "root"
    }
]

# Por cada item se genere un ciclo

is_logged = False

while not is_logged:
    print("Bienvenido, puedes digitar tu usuario y su contrasena")
    usuario = input()
    contrasena = input()
    for item in mi_lista:
        if usuario == item["usuario"] and contrasena == item["contrasena"]:
            is_logged = True
            break
    mensaje = f"Bienvenido {usuario} a el sistema" if is_logged else f"Lo siento, intentelo con otro usuario y contrasena que no sea {usuario}, {contrasena}"
    print(mensaje)

while is_logged:
    print("Ingrese 1 numero")
    num = int(input())

    if num % 2 == 0:
        print("Este numero es par")
    else:
        print("Este numero es impar")

    print("Deseas seguir en tu sesion y/n")
    seguir = input()
    is_logged = seguir == "y"