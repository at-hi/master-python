"""
Ejercicio 8.
Cuánto es el X por ciento de X numero
"""

numero = int(input("Numero: "))
porcentaje = int(input("%: "))

for x in range(numero):
    print(f"El {porcentaje} de {numero} = {numero*porcentaje/100}")
    break