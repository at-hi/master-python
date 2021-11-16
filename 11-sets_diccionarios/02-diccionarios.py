"""
Diccionario: Es una forma diferente de agrupar un conjunto de datos dentro de una variable.
- Es parecido a una lista, es un tipo de dato que almacena un conjunto de datos alfanumericos
- Es parecido a un array asociativo o un objeto json. (Tipo de dato que almacena clave y valor)
- Se define con llaves {}
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