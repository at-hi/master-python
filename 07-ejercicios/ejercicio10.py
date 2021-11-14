"""
Ejercicio 10 (COMO LO ENTENDÍ)
El programa tiene que pedir la nota de 15 alumnos
y sacar por pantalla cuántos aprobaron y cuántos reprobaron
"""

alumno = 1

while alumno < 16:

    alumno = int(input("¿De cuál alumno quieres saber la nota?: "))

    if alumno >= 0 and alumno <= 10:
        print(f"El alumno {alumno} ✓ APROBÓ ✓ el curso")
    elif alumno >= 11 and alumno <= 16:
        print(f"El alumno {alumno} × REPROBÓ × el curso")
    else:
        if alumno > 16:
            print(f"El grupo solo tiene 16 alumnos")