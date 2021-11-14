"""
Set: Es un tipo de dato, para tener una coleccion de valores,
pero no tiene ni indice ni dato y se define con llaves {}
"""

personas = {
    "Victor",
    "Manolo",
    "Francisco"
}

personas.add("Paco")
personas.remove("Victor")

print(type(personas))
print(personas)

