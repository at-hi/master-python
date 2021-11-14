"""
Los condicionales son una estructura de control que me permite controlar el flujo del programa
Dependiento de la entrada de datos podemos evaluar una condicion y
dependiendo si la condicion se cumple o no, sucede una cosa u otra.

# Condicional IF (Si sucede una cosa, va a pasar otra cosa)

if: se_cumple_esta_condicón: 
    Ejecutar grupo de instrucciones
else:
    Se Ejecuta otro grupo de instrucciones

if condicion:
    instrucciones

else:
    otras instrucciones

OPERADORES DE COMPARACION:
==  Igual
!=  Diferente
<   menor que
<   mayor que
<=  mayor o igual que
<=  menor o igual que



"""

#Ejemplo 1
from typing import ClassVar, List


print("########## EJEMPLO 1 ##########")

color = "verde"
#color = input("Adivina cual es mi color favorito: ") #Si color es igual a esto

if color == "rojo":                                  #Se ejecuta esto
    print("¡Adivinaste!")
    print("El color es ROJO")

else:                                                #Si no
    print("Ese no es, intenta de nuevo")             #Se ejecuta esto  


#Ejemplo 2
print("\n########## EJEMPLO 2 ##########")

year = int("2020")
#year = int(input("¿En qué año estamos?"))

if year >= 2021:
    print("Estamos en 2021 en adelante")
else:
    print("Es un año anterior a 2021 ")

print("\n########## Practica ###########")

forma = "Cuadrado"
#forma = input("Comienzo con uno, prosigo con uno, terminó con uno. ¿Me conoce alguno?")
if forma == "Cuadrado":
    print("¡CORRECTO!")
else: 
    print("¡INCORRECTO!")

moscas = 30
#moscas = int(input("Tres niños cazan tres moscas en tres minutos. ¿Cuánto tardan 30 niños en cazar 30 moscas?"))
if moscas == int("30"):
    print("¡CORRECTO!")

else: 
    print("¡INCORRECTO!")

#Ejemplo 3
print("\n########## EJEMPLO 3 ##########")


nombre = "Victor Robles"
ciudad = "Barcelona"
continente = "Europa"
edad = 23
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente != "Europa":
        print("el usuario No es Europeo")
    else:
        print(f"Es Europeo oriundo de Barcelona")

else:
    print(f"{nombre} No es mayor de edad")

#Ejemplo 4
print("\n########## EJEMPLO 4 ##########")

#dia = int(input("Introduce el día de la semana: "))
dia = 2

"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia ==3:
            print("Es miércoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    if dia > 5:
                        print("No es un dia de la semana")
"""

#elif (Estructura de control): Si no se cumple la condición "if" se pasa a comprobar la condición elif

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
elif dia == list(6,7):
    print("Es fin de semana")
else:
    print("No es un dia de la semana")


#Ejemplo 5
print("\n########## EJEMPLO 5 ##########")

edad_minima = 18
edad_maxima = 65
edad_oficial = 18
#edad_oficial = int(input("¿Cuál es tu edad?" " "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("¡¡Esta en edad de trabajar!!")
else:
    print("¡¡No esta en edad de trabajar!!")

#Ejemplo 6 (Operador logico "or")
print("\n########## EJEMPLO 6 ##########")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colomia":
    print(f"{pais} es un pais de habla hispana !!")
else:
    print(f"{pais} no es un pais de habla hispana !!")

#Ejemplo 7 (Operador logico "not")
print("\n########## EJEMPLO 7 ##########")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colomia"):
    print(f"{pais} no es un pais de habla hispana !!")
else:
    print(f"{pais} es un pais de habla hispana !!")

#Ejemplo 8 (Operador logico "!")
print("\n########## EJEMPLO 8 ##########")

pais = "EU"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} no es un pais de habla hispana !!")
else:
    print(f"{pais} es un pais de habla hispana !!")