# Return: Devolver un dato que este dentro de la función, afuera de la función cuando se invoque

def saludame(nombre):
    saludo = f"Hola, Saludos {nombre}"

    return saludo

print(saludame("Romy"))

print("\n------ DESARROLLO AUTONOMO ------")

def cumple(nombre, edad):
    cumpleanos = f"{nombre} esta cumpliendo {edad} años"

    return cumpleanos

print(cumple("Annie", 3))