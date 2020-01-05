# Datos Complejos en Python
"""
Tuplas
Diccionarios
Listas
Matrices....
"""
mi_tupla = ('Cadena de texto', 4.5, 15, True, 0o42, 0x45, (34, 45))
print("Esta es una tupla = " + str(mi_tupla))
print("El tamanio de la tupla es = " + str(len(mi_tupla)))

print("============================================")

mi_lista = [3, "una palabra", 56.4, 0o42, 0x45, [1, 52, "Cadena de nuevo"]]
print("Este es un ejemplo de listas en Python = " + str(mi_lista))
mi_lista[0] = "Una cadena de nuevo xd"

# Darle vuelta a una lista
mi_lista.reverse()

# Eliminar el cuarto numero
mi_lista.pop(4)

# Agregar elemento a mi lista con Python
mi_lista.append(45)

mi_lista1 = mi_lista.copy()

# Limpiar lista
mi_lista.clear()

print("La cantidad de elementos de la lista es = " + str(len(mi_lista1)))

print("Mi lista vaciada es = " + str(mi_lista))

print("============================================")

mi_diccionario = {
    "nombre": "Jose David",
    "apellido": "Briones Rosa",
    "edad": 19,
    "numerosFavoritos": (3, 4, 9),
    "alias": "DesktopL0rddit",
    "skills": ['Python', 'Java', 'JavaScript', 'TypeScript', 'R', 'SQL', 'MongoDB'],
    "correo": "david_briones@bytepl.com"
}

mi_diccionario["alias"] = "ByteCode"

print("Los datos del instructor son = " + str(mi_diccionario))
print("Mi nombre es = " + mi_diccionario.get("nombre"))
print("Mi apellido es = " + mi_diccionario['apellido'])
print("Mi numerosFavoritos es = " + str(mi_diccionario['numerosFavoritos'][0]))
print("Mi edad es = " + str(mi_diccionario['edad']))
print("Las llaves de mi diccionarios son " + str(mi_diccionario.keys()))
print("Tienes la cantidad de propiedades = "+ str(len(mi_diccionario)))
print("Las valores de mi diccionarios son " + str(mi_diccionario.items()))
print("Tienes la cantidad de valores = "+ str(len(mi_diccionario)))

# Creamos un diccionario con dict
diccionario = dict(nombre="David", apellido="Briones")
# Creamos un diccionario con zip
diccionario1 = dict(zip('abc',[1,2,3]))

print("Diccionario con dict " + str(diccionario))
print("Diccionario con dict y zip " + str(diccionario1))

# Limpiar diccionario
mi_diccionario.clear()

print("Diccionario limpio = " + str(mi_diccionario))

print("============================================")