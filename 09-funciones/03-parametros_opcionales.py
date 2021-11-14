def getEmpleado(nombre, DNI = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if DNI != None:
        print(f"DNI: {DNI}")

getEmpleado("Felipe", 23444)
