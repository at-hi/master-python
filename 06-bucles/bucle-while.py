"""
WHILE
Es una estructura de control que itera o repite la ejecucucion de una
serie de instrucciones tantas veces como sea necesario,
hasta que deja de cumplirse la conducion

While condicion:
    bloque de instrucciones
    actualización de contador

"""
contador = 1

while contador <= 100:
    print(f"Estoy en el numero {contador}")
    contador += contador

print("----------------------------")

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)

print("-------- EJEMPLO -----------")

numero_usuario = int(input("¿De qué número quieres la tabla? "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"=*= Tabla del {numero_usuario} =*=")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} X {numero_usuario} = {numero_usuario*contador}")
    contador += 1

else:
    print("Tabla terminada")

