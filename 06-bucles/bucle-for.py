"""

FOR (es una estructura iterativa que se va a repetir x cantidad de veces)
for variable in elemento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES

"""

#Ejemplo 1 
print("########## EJEMPLO 1 ##########")

contador = 0
resultado = 0

for contador in range(0, 10):
    print("Voy por el "+ str(contador))

    #resultado = resultado + contador
    resultado += contador #usando operador de asignación

print(f"El resultado es: {resultado}")


"""
EJEMPLO 1 CON COMENTARIOS

contador = 0
resultado = 0

for contador in range(0, 10): #Funcion "range" para crear un rango
    print("Voy por el "+ str(contador)) #Bloque de instrucciones / usando concatenaciones

    resultado = resultado + contador # Al final se suma el resultado con el contador y se imprime
    resultado += contador #usando operador de asignación #Con el tipo de operador de asignación += se puede abreviar 

print(f"El resultado es: {resultado}")
"""

#Ejemplo 2
print("\n########## EJEMPLO 2 ##########")

numero_usuario = int(input("¿De qué número quieres la tabla? "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### Tabla de multiplicar del número {numero_usuario} ###")

for numero_tabla in range(1, 11):

    if numero_usuario >= 10:
        print("¡Número prohibido !")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}") 

else:
    print("Tabla finalizada.")

#Ejemplo 3
print("\n########## EJEMPLO 3 ##########")

numero_usuario = int(input("¿De qué número quieres la visión? "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### División del número {numero_usuario} ###")

for division in range(11, 21):

    if numero_usuario <= 10:
        print("¡Las divisiones de un digito dan el mismo resultado (incluido el 10) !")
        break 

    print(f"{numero_usuario} ÷ {division} = {numero_usuario/division}") 

else:
    print("Listo.")