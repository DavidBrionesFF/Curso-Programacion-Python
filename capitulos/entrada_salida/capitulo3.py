# Entradas, salidas de datos, y casting
print("Hola me llamo xd dame tu nombre y tu dinero xd")
nombre = input()
print(f"Me alegro de conocerte {nombre}")
print(f"Ahora por favor {nombre}, dame tu dinero")
dinero = int(input())
print(f"Genial {nombre} que andas {dinero}$")
print(f"Pero te regalare mejor unos 40$ para que andes {(dinero + 40)}$ pinche pobre")
print("============================================")

print("Soy una calculadora")
print("Dame 2 numeros ")
num1 = float(input())
num2 = float(input())
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

print(f"Es resultado de la suma de 4 + 8 = {resultado_suma}" )
print(f"El resultado de la resta de 4 - 8 = {resultado_resta}")
print(f"El resultado de la multiplicacion de 4 * 8 = {resultado_multiplicacion}")
print(f"El resultado de la division de 4 / 8 = {resultado_division}")
print(f"El resultado de elevar 4 a la 8 es = {resultado_exponente}")
print(f"El resultado de el modulo es = {resultado_modulo}")
print(f"El resultado de la division entera es = {resultado_division_entera}")
print(f"El resultado de la raiz cuadrada es = {resultado_raiz_cuadrada}")