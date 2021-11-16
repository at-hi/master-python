print('\n===*=== LISTADO DE CONTACTOS===*===')

contactos = [
    [
        "Antonio",
        "antonio@web.com"
    ],
    [
        "Josh",
        "Josh@web.com"
    ],
    [
        "Driven",
        "Driven@web.com"
    ]
]

for contacto in contactos: #recorreo todos los <contactos> y crea una variable <contacto> por cada uno de los contactos
    for elemento in contacto: #para mostrar de forma automatica <nombre> y <mail>
            if contacto.index(elemento) == 0:
                print("Nombre: " + elemento)
            else:
                print("Email: " + elemento)
    print("\n")


#print(contactos[1][1])