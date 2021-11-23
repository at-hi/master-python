from typing import Collection

"""
Escribir un programa que añada valores a una lista 
mientras que su longitud sea menos a 120 y luego mostrar la listra.
Plus: Usar while y for
"""

coleccion = []

x = 0

while x < 120:
    coleccion.append(f"elemento-{x}")
    print("Mostrando el: " + coleccion[x])
    x += 1

print(coleccion[77])