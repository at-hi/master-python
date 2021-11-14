#Entrada de datos
nombre = input("¿Cuál es su nombre?: ")
edad = input("¿Cuál es tu edad?: ")
sexo = input("¿Hombre o mujer?: ")
comida = input("¿Comida favorita?: ")

#Salida de datos
print(f"¡Me alegro de conocerte {nombre}, Veo que tienes {edad} años y eres {sexo}")

if comida == "Hamburguesa":
    print(f"y tu comida favortita es {comida} ¡Felicitaciones, eres miembro de nuestro club!")

else:
    print(f"y tu comida favorita es {comida}, lastimosamente no podemos aceptarte en nuestro club, ¡Adios!")
