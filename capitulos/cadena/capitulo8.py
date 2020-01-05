# -*- coding: utf-8 -*-
que_es_python ="""python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional"""

print("Count -- Contar coinciencias")
print(que_es_python.count("python"))

print("Find -- Encontrar una subcadena")
print(que_es_python.find("lenguaje"))

print("StartWith -- Encontrar una subcadena al inicio")
print(que_es_python.startswith("python"))

print("EndWith -- Encontrar una subcadena")
print(que_es_python.endswith("funcional al final"))

print("isalnum -- Verificar si una cadena es alfanumerica")
print(que_es_python.isalnum())

print("isdigit -- Verificar si una cadena tiene digitos")
print("3".isdigit())

print("islower -- Contiene solo minusculas")
print(que_es_python.lower().islower())

print("isupper -- Contiene solo mayusculas")
print(que_es_python.isupper())

print("isspace -- Contiene solo espacios en blanco")
print("    ".isspace())

print("cadenas de ejemplo {david}".format(david="Nombre"))

print("Trabajando con Strings o Cadenas de carateres...")
print(que_es_python)

print("Capitalzar -- La primera mayuscula")
print(que_es_python.capitalize())

print("Lower -- Todas en minusculas")
print(que_es_python.lower())

print("Upper -- Todas en mayusculas")
print(que_es_python.upper())

print("Swapcase -- Todas en mayusculas, minusculas y vicerversa")
print(que_es_python.swapcase())

print("Title -- Formato de titulo")
print("bienvenido a byte".title())

print("Center -- centrar")
print("bienvenido a byte".title().center(50, "="))

print("LJust -- Alinear a la izquierda")
print("bienvenido a byte".title().ljust(50, "="))

print("RJust -- Alinear a la derecha")
print("bienvenido a byte".title().rjust(50, "="))

print("zfill -- Anteponer 0")
print("bienvenido a byte".title().zfill(50))