import pygame
import sys
from recursos.constantes import *
from recursos.grafo import Grafo

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Laberinto")

fondo_img = pygame.image.load('assets/images/fondos/laberintoHD.png')
fondo_img = pygame.transform.scale(fondo_img, (ANCHO_VENTANA, ALTO_VENTANA))

# Fuente para el texto
fuente = pygame.font.Font(ruta_fuente, 30)
titulo_fuente = pygame.font.Font(ruta_fuente, 48)

# Cargar las imágenes del jugador
jugador_imgs = [
    pygame.image.load('assets/images/toshi/stop/frameS0.png').convert_alpha(),
    pygame.image.load('assets/images/toshi/stop/frameS1.png').convert_alpha()
]
jugador_imgs = [pygame.transform.scale(img, (TAMAÑO_CELDA, TAMAÑO_CELDA)) for img in jugador_imgs]

def main_lab(filas,columnas):
    reloj = pygame.time.Clock()

    lab = Grafo(filas, columnas)
    pos_jugador = (0, 0)
    indice_frame = 0  # Indice inicial del frame

    # Calcular el tamaño total del laberinto
    ancho_laberinto = columnas * TAMAÑO_CELDA
    alto_laberinto = filas * TAMAÑO_CELDA

    # Calcular los márgenes para centrar el laberinto en la pantalla
    margen_x = (ANCHO_VENTANA - ancho_laberinto) // 2
    margen_y = (ALTO_VENTANA - alto_laberinto) // 2 + 30

    # Cargar la imagen de fondo para "Laberinto"
    fondo_laberinto_img = pygame.image.load('assets/images/general/cuadro.png')
    fondo_laberinto_img = pygame.transform.scale(fondo_laberinto_img, (300, 70))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Obtener el estado del teclado
        teclas = pygame.key.get_pressed()

        # Manejar el movimiento del jugador
        dx, dy = 0, 0
        if teclas[pygame.K_w]:
            dx, dy = -1, 0
        elif teclas[pygame.K_s]:
            dx, dy = 1, 0
        elif teclas[pygame.K_a]:
            dx, dy = 0, -1
        elif teclas[pygame.K_d]:
            dx, dy = 0, 1

        nueva_pos = (pos_jugador[0] + dx, pos_jugador[1] + dy)
        if nueva_pos in lab.obtener_mov_validos(pos_jugador):
            pos_jugador = nueva_pos

        if pos_jugador == lab.salida:
            mensaje_final(pantalla, "¡Felicidades, has llegado a la salida!", VERDE)
            return

        # Actualizar el índice del frame para la animación
        indice_frame = (indice_frame + 1) % len(jugador_imgs)

        # Dibujar el laberinto centrado en la pantalla
        pantalla.blit(fondo_img, (0, 0))  # Fondo del laberinto
        pantalla.blit(fondo_laberinto_img, ((ANCHO_VENTANA - fondo_laberinto_img.get_width()) // 2, 5))  # Fondo para "Laberinto"

        # Dibujar el título "Laberinto" en la parte superior
        texto_titulo = titulo_fuente.render("Laberinto", True, BLANCO)
        pantalla.blit(texto_titulo, ((ANCHO_VENTANA - texto_titulo.get_width()) // 2, 20))

        lab.mostrar_lab(pantalla, pos_jugador, margen_x, margen_y, jugador_imgs[indice_frame])  # Pasar la imagen del jugador como argumento

        pygame.display.flip()
        reloj.tick(5)

def mensaje_final(pantalla, mensaje, color):
    reloj = pygame.time.Clock()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                return

        pantalla.fill(VERDE_O)
        texto = fuente.render(mensaje, True, color)
        pantalla.blit(texto, (ANCHO_VENTANA // 2 - texto.get_width() // 2, ALTO_VENTANA // 2 - texto.get_height() // 2))

        texto_continuar = fuente.render("Presiona Enter para continuar", True, color)
        pantalla.blit(texto_continuar, (ANCHO_VENTANA // 2 - texto_continuar.get_width() // 2, ALTO_VENTANA // 2 + 40))

        pygame.display.flip()
        reloj.tick(30)

if __name__ == "__main__":
    filas = 9 # 9 12 15
    columnas = 9 # 9 12 15
    main_lab(filas,columnas)
