"""
Ejercicio 10 (COMO LO HIZO EL PROFE)
El programa tiene que pedir la nota de 15 alumnos
y sacar por pantalla cuántos aprobaron y cuántos reprobaron
"""

contador = 0
aprobados = 0
reprobados = 0

alumnos = int(input("¿Cuántos alumnos tienes? "))

while contador <= alumnos:
    nota = int(input(f"¿Qué nota quieres ponerle al alumno '{contador}' ? "))
    
    if nota >= 5:
        aprobados += 1
    else:
        reprobados += 1

    contador += 1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")
