from typing import ChainMap

cantantes = ["2pac", "Rudimental", "Justice", "U2"]
numeros = [1, 2, 5, 8, 3, 4,]
peliculas = ["Batman", "Spiderman", "Avengers", "Hulk"]
libros = ["LOS", "Ratón Perez", "Zoom", "PawPatrol"]

# tenemos disponible una serie de motodos para procesar, manipular y trabajar una lista

# ordenar elementos
numeros.sort()
print("\n", numeros)

# añadir elementos
cantantes.append("Oasis")
print("\n", cantantes)

# añadir elementos y ubicarlos en donde yo quiera
cantantes.insert(1, "Blur")
print("\n", cantantes)

# eliminar elementos
peliculas.pop(2)
print("\n", peliculas)

# eliminar un elemento por su nombre o valor
libros.remove("Zoom")
print("\n", libros)

# dar la vuelta
numeros.reverse()
print("\n", numeros)

# buscar dentro de una lista
print("\n", "U2" in cantantes)

# contar elementos
print("\n", len(libros))

# cuántas veces aparece un elemento
print("\n", numeros.count(8))

# conseguir indece
print("\n", cantantes.index("U2"))

# unir listas
cantantes.extend(numeros)
print("\n", cantantes)