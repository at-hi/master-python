peliculas = ["Batman", "Spiderman", "Shreck"]
cantantes = list(("drake", "Juan Luis Guerra", "2-pac"))

print(peliculas[0]) #Acceder a los indices de las listas
print(peliculas[-2]) # Indice negativo (de adelante hacia atras)
print(cantantes[0:2]) # Sacar los elementos hasta el indice 2 
print(cantantes[1:]) # Sacar todos los elementos a partir del indice 1

peliculas[1] = "Nemo"
print(peliculas)