peliculas = ["Batman", "Spiderman", "Shreck"]

# Ciclo for para enlistar las películas
for pelicula in peliculas:
    print(pelicula)

print("\n")

# Ciclo while para que el usuario agregue las películas
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    
    # Crerar una condicion para que "parar" no se agregue a la lista
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n==*== LISTADO PELICULAS ==*==")

# Ciclo for para enlistar y enumerar las películas
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1}. {pelicula}") # el metodo .index es para enumerar las peliculas
