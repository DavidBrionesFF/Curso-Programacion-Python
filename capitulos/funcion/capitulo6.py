from capitulos.modulo.capitulo5 import MIS_DATOS
import statistics as st

def pedir_datos():
    print("Digite dos numeros")
    num1 = float(input())
    num2 = float(input())
    return [num1, num2]

def mi_primer_funcion():
    print("Bienvenido al programa")
    print("Esta es una funcion de ejemplo")

def mi_segunda_funcion():
    print(f"Hola!! {MIS_DATOS['nombre']}")

def mi_tercera_funcion_con_parametros(nombre, apellido):
    print(f"Hola!! {nombre} {apellido}".upper())

def mi_cuarta_funcion_con_parametros_de_distinto_tipo(nombre, apellido, numeros):
    mi_tercera_funcion_con_parametros(nombre, apellido)
    print("La media de los numero es = " + str(st.mean(numeros)))
    print("La suma de los numero es = " + str(sum(numeros)))
    print(numeros)

def mi_quinta_funcion_por_omision(nombre=MIS_DATOS['nombre'], edad=MIS_DATOS['edad']):
    print("Hola Mi nombre es = " + nombre + " y mi edad es " + str(edad))

def mi_sexta_funcion_arbitrarios(paramatero, *arbitrarios):
    print("Este es un parametro = "+ paramatero)
    for argumento in arbitrarios:
        print(argumento)

def mi_septima_funcion(parametro_fijo, *abitrarios, **kwords):
    mi_sexta_funcion_arbitrarios(parametro_fijo, abitrarios)

    for clave in kwords:
        print("El valor de ", clave, " es ", kwords[clave])

def mi_octava_funcion_con_retorno(num1, num2):
    return num1 + num2

def formateo(parametro):
    return f"El resultado es = {parametro}"

# Recursividad
def jugar(intento=1):
    print("¿De que color es la naranja?")
    respuesta = input()

    if respuesta != "naranja":
        if intento < 3:
            print("Fallaste, intentalo de nuevo")
            intento += 1
            jugar(intento)  # llamada recursiva
        else:
            print("Perdiste!!")
    else:
        print("Ganaste!!")

from capitulos.modulo.capitulo5 import MIS_DATOS

mi_cuarta_funcion_con_parametros_de_distinto_tipo("Jose", "Briones", list(range(1, 5)))
mi_quinta_funcion_por_omision(nombre="David", edad=20)
mi_sexta_funcion_arbitrarios("David", "Briones", 34, "...", ["David", "Briones"], list(range(3,10)))
mi_septima_funcion("David", "Briones", "Rosa", clave1="1234", clave2="12345")

datos = pedir_datos()
print(formateo(mi_octava_funcion_con_retorno(datos[0], datos[1])))
jugar()