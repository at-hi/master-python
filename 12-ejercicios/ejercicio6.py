"""
Crear una lista con el contenido de esta tabla de video juegos:

ACCION      AVENTURA    DEPORTES
GTA         ASSINS      FIFA 21
GOD         CRASH       PES 12
PUGB        POP         MOTO GP 21

Mostrar esta info ordenada

"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "GOD", "PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSINS", "CRASH", "POP"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PES 12", "MOTO GP 21"]
    }
]

for categoria in tabla:
    print(f"-------{categoria['categoria']}-------")
    for juego in categoria['juegos']:
        print(juego)