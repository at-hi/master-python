peliculas = ["Batman", "Spiderman", "El señor de los anillos"] 
cantantes = list(("2 pac", "Drake", "Jennifer López"))
years = list(range(2020, 2050))
variada = ["Annie", 30, 40.4, True, "Texto"]

#cambiar el valor de una variable
pelicula = "Back to the future"
peliculas [0] = "Terminator"
peliculas [1] = "Matrix"
peliculas [2] = "Halloween"
print(peliculas)

#Acceder a un indice/elemento de una lista
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[2:])

# Añadir un elemento a una lista
cantantes.append("Kase o")
cantantes.append("Diomedes Diaz")
print(cantantes)

# Recorrer lista: Un script para mostrar una pelicula debajo de la otra
print("\n*********LISTADO DE PELÍCULAS*********")

# Para ingresar nuevas peliculas por teclado y que las enliste 
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva película: ")
    peliculas.append(nueva_pelicula)

#recorrer la lista con un bucle
for pelicula in peliculas:
    """Y tambien se puede sacar en numero del indice de cada una de las peliculas que se van
    recorriendo en cada momento con el metodo .index (para sacar el numero del indice)"""
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")