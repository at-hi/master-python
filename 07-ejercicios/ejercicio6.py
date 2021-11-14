"""Mostrar todas las tablas de multiplicar del 1 al 10.
mostrando el título de la tabla y las multiplicaciones del 1 al 10"""

print("===MI SOLUCIÓN===")

multiplicando = int(1)
if multiplicando < 1:
    multiplicando = 1
print(f"=== Tabla del {multiplicando} ===")
for multiplicador in range(1, 11):
    if multiplicando >= 10:
        break
    print(f"{multiplicando} x {multiplicador} = {multiplicando*multiplicador}")

multiplicando = int(2)
if multiplicando < 1:
    multiplicando = 1
print(f"\n=== Tabla del {multiplicando} ===")
for multiplicador in range(1, 11):
    if multiplicando >= 10:
        break
    print(f"{multiplicando} x {multiplicador} = {multiplicando*multiplicador}")

multiplicando = int(3)
if multiplicando < 1:
    multiplicando = 1
print(f"\n=== Tabla del {multiplicando} ===")
for multiplicador in range(1, 11):
    if multiplicando >= 10:
        break
    print(f"{multiplicando} x {multiplicador} = {multiplicando*multiplicador}")

multiplicando = int(4)
if multiplicando < 1:
    multiplicando = 1
print(f"\n=== Tabla del {multiplicando} ===")
for multiplicador in range(1, 11):
    if multiplicando >= 10:
        break
    print(f"{multiplicando} x {multiplicador} = {multiplicando*multiplicador}")

multiplicando = int(5)
if multiplicando < 1:
    multiplicando = 1
print(f"\n=== Tabla del {multiplicando} ===")
for multiplicador in range(1, 11):
    if multiplicando >= 10:
        break
    print(f"{multiplicando} x {multiplicador} = {multiplicando*multiplicador}")

multiplicando = int(6)
if multiplicando < 1:
    multiplicando = 1
print(f"\n=== Tabla del {multiplicando} ===")
for multiplicador in range(1, 11):
    if multiplicando >= 10:
        break
    print(f"{multiplicando} x {multiplicador} = {multiplicando*multiplicador}")

multiplicando = int(7)
if multiplicando < 1:
    multiplicando = 1
print(f"\n=== Tabla del {multiplicando} ===")
for multiplicador in range(1, 11):
    if multiplicando >= 10:
        break
    print(f"{multiplicando} x {multiplicador} = {multiplicando*multiplicador}")

multiplicando = int(8)
if multiplicando < 1:
    multiplicando = 1
print(f"\n=== Tabla del {multiplicando} ===")
for multiplicador in range(1, 11):
    if multiplicando >= 10:
        break
    print(f"{multiplicando} x {multiplicador} = {multiplicando*multiplicador}")

multiplicando = int(9)
if multiplicando < 1:
    multiplicando = 1
print(f"\n=== Tabla del {multiplicando} ===")
for multiplicador in range(1, 11):
    if multiplicando >= 10:
        break
    print(f"{multiplicando} x {multiplicador} = {multiplicando*multiplicador}")

multiplicando = int(10)
if multiplicando < 1:
    multiplicando = 1
print(f"\n=== Tabla del {multiplicando} ===")
for multiplicador in range(1, 11):
    if multiplicando >= 11:
        break

print("\n")

print("===SOLUCIÓN DEL PROFE===")
print("\n")
for multiplicando in range(1, 11):
    print(f"=== Tabla del {multiplicando} ===")

    for multiplicador in range(1, 11):
        print(f"{multiplicador} X {multiplicando} = {multiplicador*multiplicando}")
    
    print("\n")
