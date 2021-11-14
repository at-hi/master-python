"""
Asi como se pueden crear funciones, pyton tiene una
serie de funciones/metodos predefinidas, en la docu hay muchas
"""

nombre = "Franklyn Gothic"

print(nombre) # funciones generales

print(type(nombre)) # ver el tipo de dato

comprobar = isinstance(nombre, str) # detectar el tipado
if comprobar:
    print("Esa variale es un str")
else:
    print("No es una cadena")
if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

frase = "   mi contenido    " # Limpiar espacios
print(frase.strip()) # Si se pone un punto se acceden a los metodos/funciones predefinidas del lenguaje

year = 2022 # Eliminar variables
print(year)
del year
#print(year)

texto = [3,1,2,3,5,"d",41] # Comprobar cantidad de caracteres
if len(texto) <= 0:
    print("La var esta vacía")
else:
    print("La variable tiene contenido", len(texto))

frase = "La vida es bella" # Encontrar caracteres
print(frase.find("bella"))

nueva_frase = frase.replace("bella", "Jesus")  # Reemplazar caracteres en un str
print(nueva_frase)

print(nombre) # Mayúsculas y minúsculas
print(nombre.lower())
print(nombre.upper())