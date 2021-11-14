print("El usuario ingresa el número de la tabla")

def table(number):
    print(f"\nTable number: {number}")
    print(".....................................")

    for count in range (11):
        operation = number*count
        print(f"{number} X {count} = {operation}")
    
number = int(input("\nWhat table you like? "))
table(number)

print("\nSacar las tablas en un rango de 1 a 10")

#Sacar todas las tablas de multiplicar utilizando la misma función
for table_number in range (1, 11):
    table(table_number)