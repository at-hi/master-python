"""
Diccionario: Es parecido a una lista, es un tipo de dato que almacena un conjunto de datos
en formato clave > valor
Es parecido a un array asociativo o un objeto json.
y se define con llaves {}
"""

persona = {
    #Propiedad / clave ó indice
    "nombre": "Roman",
    "apellidos": "Popam",
    "web": "roman.com"
}

print(type(persona)) #Para ver el tipo de dato
print(persona["nombre"]) #Para acceder a las diferentes propiedades del dict


""""""