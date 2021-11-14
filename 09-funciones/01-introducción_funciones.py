print("\n==*== TEMA: Funciones ==*==")

print("\nEjemplo 1")
#Definir finción
def muenstraNombres():
    print("Lalo")
    print("Francisco")
    print("Pedro")
    print("\n")
#Invocar función
muenstraNombres()

print("\nEJEMPLO 2")
#Parámetros
def favType(type):
    print(f"Yor fav face is: {type}")
type = input("What's your fav face? ")
favType(type)

print("---------------------")

def yourBook(book):
    print(f"You've read {book} books, that sounds great!")
book = input("How many books you've read this year: ")
yourBook(book)

