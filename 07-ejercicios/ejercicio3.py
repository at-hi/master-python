"""
Ejercicio 3. Escribir un programa que muestre los cuadrados
(un numero miltiplicado por si mismo) de los 60 primeros numeros naturales.
Resolverlo con for y con while
""" 

print("\n==*== Con while ==*==")

contador = 0
while contador <= 60:

    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    contador += 1


print("\n==*== Con for ==*==")

for numero in range(61):
    cuadrado = numero*numero
    print(f"El cuadrado de {numero} es {cuadrado}")

