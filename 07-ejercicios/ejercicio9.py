"""
Ejercicio 9: Hacer un programa que pida numeros
al usuario indefinidamente, hasta que introduzca el numero 111
"""

contador = 1
while contador < 100:
    numero = int(input("Introduce el número correcto: "))

    if numero == 111:
        print(f"Felicitaciones, el número {numero} ¡es correcto!")
        break
    else:
        print(f"El numero {numero} es incorrecto. ¡Sigue intentando!")

