def calculadora(num1, num2, basicas = False):

    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    divi = num1 / num2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"

    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(divi)
        cadena += "\n"

    return cadena

print(calculadora(5, 5, False))

#En este ejemplo estamos usando un FLAG (Algo que da True o False)
