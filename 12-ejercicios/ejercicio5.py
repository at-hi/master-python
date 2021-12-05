"""
- Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano
- Que imprima un mensaje segun el tipo de dato de cada variable
"""

# esto es una funcion para traducir el tipo de dato mas real
def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "NUMERO ENTERO"
    elif tipo == bool:
        result = "DECIMAL"

    return result

#este es el script
def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)

    result = ""

    if test:
        result = f"Este dato es del tipo {traducirTipo(tipo)}"
    else:
        result = "El tipo de dato no es correcto"
    
    return result

mi_lista = ["annie", 33]
juegos = ("el juego favorito de Annie es el lego")
mi_edad = 34
verdadero = True

print(comprobarTipado(mi_lista, list))
print(comprobarTipado(juegos, str))
print(comprobarTipado(mi_edad, int))
print(comprobarTipado(verdadero, bool))