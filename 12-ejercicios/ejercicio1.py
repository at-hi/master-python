"""
Hacer una programa que tenga una lista
de 8 números enteros y haga los siguiente:
- Recorrer la lista y mostrarla
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar un elemento que el usuario pida por teclado
"""

print("\n*********NUMEROS ENTEROS*********")
numeros = [2, 5, 1, 3, 6, 8, 7, 4]

numero_usuario = ""
while numero_usuario <= 2:
    numero_usuario = input("Adivina los 8 números que tengo en una lista de 20 números: ")

    if numero_usuario == [2, 5, 1, 3, 6, 8, 7, 4]:
        print(f"Felicitaciones, el número {numero_usuario} ¡es correcto!")
        break
    else:
        print(f"El numero {numero_usuario} es incorrecto. Intenta de nuevo: ")


numeros.sort()
print(numeros)
print(len(numeros))
