"""
Ejercicio 1:

Hacer una programa que tenga una lista
de 8 números enteros y haga los siguiente:

1) (hecho) Recorrer la lista y mostrarla
2) (hecho) Hacer una función que recorra listas de numeros y devuelva un string
3) (hecho) Ordenarla y mostrarla
4) (hecho) Mostrar su longitud
5) (hecho) Buscar un elemento que el usuario pida por teclado
"""

print("\n*********NUMEROS ENTEROS*********")

# Crear lista
numeros = [20, 12, 6, 8, 2, 60, 54, 22]

# 2) Hacer función
def mostrarLista(lista):
    resultado = ""

# Recorrer lista y devolver str
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    
    return resultado

# 1) Recorrer y mostrar
"""for numero in numeros:
    print(numero)"""

print(mostrarLista(numeros))

# 3) Ordenarda y mostrarla
numeros.sort()
print(mostrarLista(numeros))

# 4) Mostrar su longitud
print(len(numeros))

# 5) Busqueda en la lista

busqueda = int(input("Introduce un numero: "))
comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <= 0:
    busqueda = input("Introduce un numero: ") 
else:
    print(f"Has introducido el {busqueda}")

print(f"Buscar en la lista el numero {busqueda}")

search = numeros.index(busqueda)

print(f"El numero buscado existe en la lista, es el indice {search}")
