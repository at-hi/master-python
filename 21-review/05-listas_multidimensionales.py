print('\n===*=== LISTADO DE CONTACTOS===*===')

contactos = [
    [
        'Antonio',
        'antonio@gmail.com'
    ],
    [
        'Luis',
        'luis@gmail.com'
    ],
    [
        'Andrea',
        'andrea@gmail.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")

#print(contactos[1][1])