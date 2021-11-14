cantantes = ["2pac", "Rudimental", "ACDC"]
numeros = [1, 2, 5, 8, 4]

"""Ordenar una lista"""
#print(numeros)
numeros.sort()
#print(numeros)

"""Añadir elementos a una lista"""
cantantes.append("El Binomio de Oro")
cantantes.insert(2, "Juan Luis Guerra")
#print(cantantes)

"""Eliminar elementos a una lista"""
cantantes.pop(0)
cantantes.remove("Rudimental")
#print(cantantes)

"""Dar la vuelta a los elementos de una lista"""
#print(numeros)
numeros.reverse()
#print(numeros)

"""Buscar dentro de una lista con el operador "in"""
print("Juan Luis Guerra" in cantantes)

"""Contar el numero de elemntos de una lista"""
print(cantantes)
print(len(cantantes))

"""Cuantas veces aparece un elemento en una lista"""
numeros.append(8) #Con el metodo append agregar otro 8 a la lista
print(numeros.count(8))

"""Conseguir indice"""
print(cantantes.index("Juan Luis Guerra"))

"""Unir listas"""
cantantes.extend(numeros)
print(cantantes)
