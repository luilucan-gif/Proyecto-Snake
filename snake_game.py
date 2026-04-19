import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de pantalla
ANCHO = 600
ALTO = 400
TAM_BLOQUE = 20
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Snake")

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)
ROJO = (200, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (40, 40, 40)

# Fuente
FUENTE = pygame.font.SysFont("arial", 24)
RELOJ = pygame.time.Clock()
VELOCIDAD = 10


def mostrar_texto(texto, color, x, y):
    superficie = FUENTE.render(texto, True, color)
    VENTANA.blit(superficie, (x, y))


def generar_comida():
    x = random.randrange(0, ANCHO, TAM_BLOQUE)
    y = random.randrange(0, ALTO, TAM_BLOQUE)
    return (x, y)


def dibujar_serpiente(lista_serpiente):
    for bloque in lista_serpiente:
        pygame.draw.rect(VENTANA, VERDE, (bloque[0], bloque[1], TAM_BLOQUE, TAM_BLOQUE))


def mover_cabeza(cabeza, direccion):
    x, y = cabeza

    if direccion == "ARRIBA":
        y -= TAM_BLOQUE
    elif direccion == "ABAJO":
        y += TAM_BLOQUE
    elif direccion == "IZQUIERDA":
        x -= TAM_BLOQUE
    elif direccion == "DERECHA":
        x += TAM_BLOQUE

    return (x, y)


def detectar_colision_bordes(cabeza):
    x, y = cabeza
    return x < 0 or x >= ANCHO or y < 0 or y >= ALTO


def detectar_colision_cuerpo(cabeza, cuerpo):
    return cabeza in cuerpo


def mostrar_pantalla_final(puntaje):
    VENTANA.fill(NEGRO)
    mostrar_texto("Game Over", ROJO, ANCHO // 2 - 70, ALTO // 2 - 50)
    mostrar_texto(f"Puntaje final: {puntaje}", BLANCO, ANCHO // 2 - 90, ALTO // 2)
    mostrar_texto("Presione R para reiniciar o Q para salir", BLANCO, 100, ALTO // 2 + 50)
    pygame.display.update()


def juego():
    while True:
        # Posición inicial de la serpiente
        serpiente = [(100, 100), (80, 100), (60, 100)]
        direccion = "DERECHA"
        comida = generar_comida()
        puntaje = 0
        jugando = True

        while jugando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP and direccion != "ABAJO":
                        direccion = "ARRIBA"
                    elif evento.key == pygame.K_DOWN and direccion != "ARRIBA":
                        direccion = "ABAJO"
                    elif evento.key == pygame.K_LEFT and direccion != "DERECHA":
                        direccion = "IZQUIERDA"
                    elif evento.key == pygame.K_RIGHT and direccion != "IZQUIERDA":
                        direccion = "DERECHA"

            nueva_cabeza = mover_cabeza(serpiente[0], direccion)

            # Detectar colisiones
            if detectar_colision_bordes(nueva_cabeza) or detectar_colision_cuerpo(nueva_cabeza, serpiente):
                jugando = False
                break

            serpiente.insert(0, nueva_cabeza)

            # Comer comida
            if nueva_cabeza == comida:
                puntaje += 1
                comida = generar_comida()
            else:
                serpiente.pop()

            # Dibujar
            VENTANA.fill(GRIS)
            pygame.draw.rect(VENTANA, ROJO, (comida[0], comida[1], TAM_BLOQUE, TAM_BLOQUE))
            dibujar_serpiente(serpiente)
            mostrar_texto(f"Puntaje: {puntaje}", BLANCO, 10, 10)
            pygame.display.update()
            RELOJ.tick(VELOCIDAD)

        # Pantalla final
        esperando = True
        while esperando:
            mostrar_pantalla_final(puntaje)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        esperando = False
                    elif evento.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()


if __name__ == "__main__":
    juego()


