""" 
Una variable es un contenedor de información
que dentro guardara un dato, se puede crear
muchas variables y que cada una tenga un dato distinto.
"""

#crear variables y asignarles un valor
texto = "Master en python"
texto2 = "Con Victor Robles"
numero = 45
decimal = 6.7

#mostrar valor de las varialbes
print(texto)
print(texto2)
print(numero)
print(decimal)

print("------------------")

#reasignado valores
numero = 77
decimal = 8.9
print(numero)
print(decimal)

print("------------------")
 
#Concatenación
nombre = "Victor"
apellidos = "Robles"
web = "victorroblesweb.es"

#3 formas diferentes para concatenar

#con las comillas se agregan espacios
print(nombre + " " + apellidos + " - " + web)
"""
esta manera es mas limpia utilizando la "f" y la doble llave "{}",
la "f" permite incluir/sustituir/interpolar directamente dentro de otro texto
cualquier variable
"""
print(f"{nombre} {apellidos} - {web}")
print("hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))

print("-------Practica-------")

nombre = "Annie"
apellidos = "Calderón"
colegio = "Philadelphia Internacional"

print(nombre + " " + apellidos + " - " + colegio)
print(f"{nombre} {apellidos} - {colegio}")
print("Hola, me llamo {} {} y mi colegio es: {}".format(nombre, apellidos, colegio))

