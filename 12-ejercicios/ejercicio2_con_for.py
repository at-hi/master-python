"""
Escribir un programa que añada valores a una lista 
mientras que su longitud sea menos a 120 y luego mostrar la listra.
Plus: Usar while y for
"""

coleccion = []

for contador in range (0, 120):
    coleccion.append(f"Elemento-{contador}")
    print("Mostrando el: " + coleccion[contador])

print(coleccion[112])