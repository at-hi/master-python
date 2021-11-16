#creamos una variable y abrimos una lista
contactos = [
    #dentro la la lista abrimos un dict
    {
        "nombre": "Willian",
        "email": "caslon@gmail.com"
    },
    {
        "nombre": "Bodoni",
        "email": "bodoni@gmail.com"
    },
    {
        "nombre": "dwiggins",
        "email": "dwigg@gmail.com"
    }
]

#Para cambiar el valor a una propiedad
contactos[2]["nombre"] = "Romelu"

#Imprimir la variable, acceder a la lista [] y luego acceder al dict []
print(contactos[0]["nombre"])   

print("\nLista de contactos: ")
print(f"-----------------------------")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Emaill del contacto: {contacto['email']}")
    print(f"-----------------------------")
