# Proyecto Snake - avance 2
# Se solicita el nombre del jugador y una dirección
# Se usan variables, entrada de datos, salida de datos y condicionales

jugador = input("Ingrese el nombre del jugador: ")
print("Bienvenido al juego Snake,", jugador)

direccion = input("Ingrese una dirección (arriba, abajo, izquierda, derecha): ")

if direccion == "arriba":
    print("La serpiente se movió hacia arriba")
elif direccion == "abajo":
    print("La serpiente se movió hacia abajo")
elif direccion == "izquierda":
    print("La serpiente se movió hacia la izquierda")
elif direccion == "derecha":
    print("La serpiente se movió hacia la derecha")
else:
    print("Dirección no válida")