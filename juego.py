# Proyecto Snake - avance 3
# Uso de variables, entrada de datos, salida de datos,
# estructuras condicionales y comentarios

# Se pide el nombre del jugador
jugador = input("Ingrese el nombre del jugador: ")

# Variables iniciales de la serpiente
pos_x = 5
pos_y = 5
puntaje = 0

# Se muestran datos iniciales
print("Bienvenido al juego Snake,", jugador)
print("Posición inicial de la serpiente:", pos_x, ",", pos_y)
print("Puntaje inicial:", puntaje)

# Se pide la dirección de movimiento
direccion = input("Ingrese una dirección (arriba, abajo, izquierda, derecha): ")

# Condicionales para mover la serpiente
if direccion == "arriba":
    pos_y = pos_y - 1
    print("La serpiente se movió hacia arriba")
elif direccion == "abajo":
    pos_y = pos_y + 1
    print("La serpiente se movió hacia abajo")
elif direccion == "izquierda":
    pos_x = pos_x - 1
    print("La serpiente se movió hacia la izquierda")
elif direccion == "derecha":
    pos_x = pos_x + 1
    print("La serpiente se movió hacia la derecha")
else:
    print("Dirección no válida")

# Se imprime la nueva posición
print("Nueva posición de la serpiente:", pos_x, ",", pos_y)

# Posición fija de la comida
comida_x = 6
comida_y = 5

# Se verifica si la serpiente encontró la comida
if pos_x == comida_x and pos_y == comida_y:
    puntaje = puntaje + 1
    print("La serpiente encontró la comida")
else:
    print("La serpiente no encontró la comida")

# Se imprime el puntaje final
print("Puntaje actual:", puntaje)