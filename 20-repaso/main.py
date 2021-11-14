#Condicionales

from typing import List

print("==*== EJEMPLO: CONDICIONAL IF ==*==")

color = "rojo"
#color = input("¿De qué color es la bandera de china? ")

if color == "rojo": #Si el color es igual a "rojo"
    print("El color es rojo") #Se ejecutará esto
else: #Si no
    print("Color incorrecto") #se ejecutará esto

print("\n==*== EJEMPLO 2: CONDICIONAL IF ==*==")

year = "2020"
#year = input("¿En qué año estamos? ")

if year >= "2021": 
    print("Estamos en el 2021")
else: 
    print("Es un año anterior a 2021")

print("\n==*== EJEMPLO 3: IF ANINADOS ==*==")

edad = 18
nombre = "Victor Robles"
ciudad = "Barcelona"
continente = "Oceania"
edad = 18
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente != "Europa":
        print("El usuario NO es Europeo")
    else:
        print("Es Europeo oriundo de {ciudad}")

else:
    print(f"{nombre} no es mayor de edad")

#Se pueden hacer muchas instrucciones y lógicas de programación dentro de un IF,
#siempre y cuando el código este bien tabulado para que todo este jerarquicamente organizado.

print("\n==*== EJEMPLO 4: ELIF ==*==")

dia = 1
#dia = int(input("Introduce el número del día de la semana: "))

"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miércoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es fin de semana")

No se recomienda hacerlo de esta manera debido a la cantidad de if anidados,
se vuelve muy ilegible y complicado de mantener. La manera mas limpia es usando la
condición elif
"""

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")


print("\n==*== EJEMPLO 5: ELIF ==*==")

edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad: "))
edad_oficial = 17

if edad_oficial >= 18 and edad_oficial <= 65: #Esto se hizo usando el operador lógico "and"
    print("Esta en edad para trabajar")
else:
    print("No esta en edad para trabajar")

print("\n==*== EJEMPLO 6: OPERADORES DE COMPARACIÓN Y LÓGICOS ==*==")

#===*=== or
pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colomia": #Si el país es igual a los paises dentro del operadore lógico "or"
    print(f"{pais} es un pais de habla hispana !!") #Se cumple esta condición
else:
    print(f"{pais} no es un pais de habla hispana !!") #Sino se cumple esta condición

#===*=== not, or
pais = "Canada"

if not (pais == "Mexico" or pais == "España" or pais == "Colomia"): #Encerramos todo en () y anteponemos la condición "not" para que NO se cumpla la condición.
    print(f"{pais} No es un pais de habla hispana !!") #Se cumple esta condición
else:
    print(f"{pais} SI es un pais de habla hispana !!") #Sino, se cumple esta condición

#===*=== !=, and
pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia": #Si pais es diferente != a los paises dentro del if
    print(f"{pais} No es un pais de habla hispana !!") #Se cumple esta condición
else:
    print(f"{pais} SI es un pais de habla hispana !!") #Sino, se cumple esta condición

print("\n==*== EJEMPLO 7: BUCLE for ==*==")
contador = 0

for contador in range(0, 5):
    print("Voy por el " + str(contador))

print("\nEjemplo con una variable que guarda la suma de todos los numeros que hay dentro del rango")

contador = 0
resultado = 0

for contador in range(0, 5):
    print("Voy por el " + str(contador))

    resultado += contador

print(f"El resultado es {resultado}")

print("\nTabla de multiplicar con BUCLE for")

#numero_usuario = int(input("¿De qué número quieres la tabla? "))
numero_usuario = 2

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n=== Tabla de multiplicar del número {numero_usuario} ===")

for numero_tabla in range(1, 11):
    print(f"{numero_usuario} X {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada")

print("\n==*== EJEMPLO 8: BUCLE while ==*==")

contador = 1

while contador <= 100:
    print(f"Estoy en el Nº: {contador}")
    contador += 1

print("\nMostrar todos los números del 1 al 100 separados por comas")

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)

print("\n==*== EJEMPLO 9: REPASO FUNCIONES ==*==")

#Aquí defino la función
def muestraNumero():
    print(10)
    print(20)
    print(30)

#Invonvar la función
muestraNumero()

print("\n==*== EJEMPLO 10: Motrar tu nombre ==*==")

def mostrarNombre(nombre, edad, ocupacion):
    print(f"Tu nombre es: {nombre}")
    print(f"Eres {ocupación}")

    if edad >= 18:
        print("Y eres mayor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
ocupación = input("¿A qué te dedicas?: ")
mostrarNombre(nombre, edad, ocupación)

print("\n==*== EJEMPLO 11: Tabla de multiplicar ==*==")

#Aquí creo la función para que el usuario introduzca el numero de la tabla que desea
def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    #Con este bucle hago la operación
    for contador in range (0, 11):
        operacion = numero*contador
        print(f"{numero} X {contador} = {operacion}")

    print("\n")

#Para invocar la función y pasarle el número por parámetro que uno quiere.
tabla(2)

print("\n------MOSTRAR TODAS LAS TABLAS DE MULTIPLICAR CON UN BUCLE------")
#  creo un bucle / Hago un rango hasta la tabla del 10          
for numero_tabla in range (1, 11):
    #Utilizo la funcion tabla
    tabla(numero_tabla)


