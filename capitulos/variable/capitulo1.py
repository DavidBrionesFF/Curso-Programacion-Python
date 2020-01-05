# Variables y Comentarios
# Cadena de caracteres String
"""
Este es un comentario de muchas lineas que describe este programa escrito en python
TODO Debemos de limpiar este codigo mas, es decir separarlo por funciones
FIXME Debemos de corregir el codigo que a veces da errores en la linea 4
"""
palabra = "esta es una palabra"
# Numerico
numero_decimal = 3.4  # Numerico decimal
numero_entero = -2  # Numerico entero
numero_octal = 0o43  # Numero en base octal
numero_hexadecimal = 0x23  # Numero en base hexadecimal

# Imprimir tipos de variables
print("Esta es una palabra - " + palabra)
print("Este es un valor numerico decimal " + str(numero_decimal))
print("Este es un valor numerico entero " + str(numero_entero))
print("Estes es un valor hexadecimal " + str(numero_hexadecimal))
print("Este es un numero en base octal " + str(numero_octal))

# Booleano
logico = False
# Nulo
nula = None
print("Este es un tipo de valor booleano " + str(logico))
print("Este es un tipo de valor nulo " + str(nula))

print("============================================")
# Operadores Aritmeticos
# Declaracion de variables
num1 = 4
num2 = 8
# Operador de Suma
resultado_suma = num1 + num2
# Operador de Resta
resultado_resta = num1 - num2
# Operador de multiplicacion
resultado_multiplicacion = num1 * num2
# Operador de division
resultado_division = num1 / num2
# Operador
resultado_exponente = num1 ** num2
# Modulo
resultado_modulo = num1 % num2
# Division entera
resultado_division_entera = num1 // num2
# Raiz cuadrada
resultado_raiz_cuadrada = num1 ** (1/2)

print("Es resultado de la suma de 4 + 8 = " + str(resultado_suma))
print("El resultado de la resta de 4 - 8 = " + str(resultado_resta))
print("El resultado de la multiplicacion de 4 * 8 = " + str(resultado_multiplicacion))
print("El resultado de la division de 4 / 8 = " + str(resultado_division))
print("El resultado de elevar 4 a la 8 es = " + str(resultado_exponente))
print("El resultado de el modulo es = " + str(resultado_modulo))
print("El resultado de la division entera es = " + str(resultado_division_entera))
print("El resultado de la raiz cuadrada es = " + str(resultado_raiz_cuadrada))

print("============================================")
"""
Este es el tipo de operadores logicos, consultar en la documentacion oficial 
https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion4/operadores_logicos.html
"""
valor_a = True
valor_b = True
resultado_or = valor_a or valor_b
resultado_and = valor_a and valor_b
resultado_not = not valor_a

print("El valor de el resultado or de " + str(valor_a) + " y " + str(valor_b) + " = " + str(resultado_or))
print("El valor de el resultado and de " + str(valor_a) + " y " + str(valor_b) + " = " + str(resultado_and))
print("El valor de el resultado not de " + str(valor_a) + " = " + str(resultado_not))

# Logicas entre numeros
print("El valor de la comparacion entre 4 == 5 es " + str(4==5))
print("El valor de la comparacion entre 4 < 5 es " + str(4<5))
print("El valor de la comparacion entre 4 > 5 es " + str(4>5))
print("El valor de la comparacion entre 4 != 5 es " + str(4!=5))
print("El valor de la comparacion entre 4 <= 5 es " + str(4<=5))
print("El valor de la comparacion entre 4 >= 5 es " + str(4>=5))

