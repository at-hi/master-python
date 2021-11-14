"""
Ejercicio 2. Escribir un script que nos muestre por pantalla
todos los números pares del 1 al 120
"""
print("===MI SOLUCIÓN (NO SALIÓ)===") #Cada número se esta multiplicando por si mismo (el cuadrado de cada uno)
contador = 1

for contador in range(1, 121):
    contador += contador
    print("Voy por el " + str(contador))

print("\n===2do INTENTO===") #
contador = 1

for contador in range(1, 121):
    if contador %2 == 0: #En cada vuelta que da el buble se divide entre 2 y con el porcentaje se saca el resto, si ese resto es igual a 0 es numero par
        print(contador)