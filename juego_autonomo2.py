# Proyecto Snake - avance 4
# Uso de variables, condicionales y bucle while

seguir = "si"

while seguir == "si":
    
    jugador = input("Ingrese el nombre del jugador: ")
    
    pos_x = 5
    pos_y = 5
    puntaje = 0

    print("Bienvenido al juego Snake,", jugador)

    direccion = input("Ingrese dirección (arriba, abajo, izquierda, derecha): ")

    if direccion == "arriba":
        pos_y -= 1
    elif direccion == "abajo":
        pos_y += 1
    elif direccion == "izquierda":
        pos_x -= 1
    elif direccion == "derecha":
        pos_x += 1
    else:
        print("Dirección no válida")

    print("Nueva posición:", pos_x, pos_y)

    seguir = input("¿Quieres jugar otra vez? (si/no): ")
