#Se recomienda que las funciones definidas esten todas juntas arriba del fichero"""
def mi_funcion(nombre):
    return "Hola que tal " + nombre #Lo recomendable es que una función devuelva un dato en lugar de hacer el print

def mi_segunda_funcion(apellidos):
    return "Hola que tal 2 " + apellidos

#Siempre definir las variablers antes de invocarlas
nombre = "Felipe"
apellidos = "Calderon" 

print(mi_funcion(nombre))
print(mi_segunda_funcion(apellidos))
