"""
Variable local: Se definen dentro de la función y no se puede usar fuera
de ella, solo están disponibles dentro. A no ser que hagamos return

Variable globales: Son las que se declaran fuera de una función y estan
disponibles dentro y fuera de ellas
"""
# Variable global
frase = "Agua que salió por aquí y cate que no te ví"
print(frase)

def saludo():
    #Variable local
    frase = "Hola"
    print("Dentro: ")
    print(frase)

    year = 2021
    print(year)

    global web #con la palabra "global" la variable cambia de local a global
    web = "x.com"
    print("Dentro:" , web)

    return "Dato devuelto: " + str(year)

print(saludo())
print("Fuera:", web)