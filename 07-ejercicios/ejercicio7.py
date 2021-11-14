"""
Ejercicio 7: Hacer un programa que muestre todos los numeros impares
entre dos numeros que decida el usuario
"""

numero_1 = int(input("Número 1: "))
numero_2 = int(input("Número 2: "))

if numero_1 < numero_2:
    
    """Aquí "x" reemplaza a "contador" y al numero_2 le sumamos 1 para que considere el numero del usuario también"""
    for x in range(numero_1, numero_2 + 1): 
        if x%2 != 0:
            print(x)
else:
    print("El Número 1 debe ser menor que el Número 2")