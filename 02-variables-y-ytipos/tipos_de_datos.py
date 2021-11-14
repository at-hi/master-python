print("-------Tipos de datos------")

#Tipo de dato:NoneType
nada = None

#Tipo de dato: String (str) Significa cadena de texto
cadena = "Hola soy Felipe Calderon"
cadena = "Desarrollador web"

#Tipo de dato: Int
entero = 200

#Tipo de dato: float
flotante = 30.5

#tipo de dato: bool
booleano = True

#tipo de dato: List
lista = [10, 20, 100, 5000]
listaString = [20, "roman", 90, "nicole"]

#tipo de dato: tuple
tuplaNoCambia = ("master", "en", "python")

#tipo de dato: dict
diccionario = {
    "nombre": "Nicole",
    "apellido": "Caicedo",
    "parentesco": "Esposa" 
}

#tipo de dato: range
rango = range(9)

#tipo de dato: bytes
dato_byte = b"Probando"

# imprimir variable
print(dato_byte)

#mostrar tipo de dato
print(type(dato_byte))


print("-------Convertir datos------")

texto = "Hola soy un texto"
numerito = str(776)
print(type(numerito))
#En lugar de imrpimir 776, imprime "776"

print(texto + " " + numerito)

numerito = int(776)
print(type(numerito))

numerito = float(776) 
print(type(numerito))

