"""
Set: Es un tipo de dato, para tener una coleccion de valores,
pero no tiene ni indice ni orden y se define con llaves {}
"""

personas = {
    "Victor",
    "Manolo",
    "Francisco"
}

# diferentes metodos para usar
personas.add("Paco")
personas.remove("Victor")

print(type(personas))
print(personas)

