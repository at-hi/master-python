"""
Operadores lógicos:(En python hay menos operadores logicos
que en otros lenguajes de programacion pero igual sirven para lo mismo)

and Y
or  O
!   NEGACION
not  NO
"""

print("==*== EJEMPLO DE USO DE OPERADORES LÓGICOS EN UN IF ANINADOS ==*==")

edad_maxima = 18
edad_maxima = 65
edad_oficial = 22

if edad_oficial >= 18 and edad_oficial <= 65: #Se pueden agregar las condiciones que uno quiera
    print("¡¡Esta en edad de trabajar!!")
else:
    print("¡¡No esta en edad de trabajar!!")