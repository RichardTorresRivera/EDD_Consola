import pygame
import sys
import os
import config
from juegos.laberinto.recursos.constantes import *
from juegos.laberinto.recursos.grafo import Grafo

def main_lab(screen, reloj, estado, dificultad):
    pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Laberinto - Enjoy The Silence.mp3"))
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
    fondo_img = pygame.image.load(os.path.join(config.FONDOS_DIR, "laberintoHD.png"))
    fondo_img = pygame.transform.scale(fondo_img, (ANCHO_VENTANA, ALTO_VENTANA))

    # Fuente para el texto
    fuente = pygame.font.Font(ruta_fuente, 30)
    titulo_fuente = pygame.font.Font(ruta_fuente, 48)

    # Cargar las imágenes del jugador
    jugador_imgs = [
        pygame.image.load(os.path.join(config.TOSHI_DIR, "stop", "frameS0.png")).convert_alpha(),
        pygame.image.load(os.path.join(config.TOSHI_DIR, "stop", "frameS1.png")).convert_alpha()
    ]
    jugador_imgs = [pygame.transform.scale(img, (TAMANIO_CELDA, TAMANIO_CELDA)) for img in jugador_imgs]
    filas = (dificultad[0] + 2)*3
    columnas = (dificultad[0] + 2)*3
    lab = Grafo(filas, columnas)
    pos_jugador = (0, 0)
    indice_frame = 0  # Indice inicial del frame

    # Calcular el tamaño total del laberinto
    ancho_laberinto = columnas * TAMANIO_CELDA
    alto_laberinto = filas * TAMANIO_CELDA

    # Calcular los márgenes para centrar el laberinto en la pantalla
    margen_x = (ANCHO_VENTANA - ancho_laberinto) // 2
    margen_y = (ALTO_VENTANA - alto_laberinto) // 2 + 30

    # Cargar la imagen de fondo para "Laberinto"
    fondo_laberinto_img = pygame.image.load(os.path.join(config.GENERAL_DIR, "cuadro.png"))
    fondo_laberinto_img = pygame.transform.scale(fondo_laberinto_img, (300, 70))
    jugar_lab = True

    while jugar_lab:
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
            mensaje_final(screen, "¡Felicidades, has llegado a la salida!", VERDE, reloj, fuente)
            jugar_lab = False
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            pygame.time.delay(2000)
            estado[0] = config.SCREEN_MAPA
            print("FELICIDADES")

        # Actualizar el índice del frame para la animación
        indice_frame = (indice_frame + 1) % len(jugador_imgs)

        # Dibujar el laberinto centrado en la pantalla
        screen.blit(fondo_img, (0, 0))  # Fondo del laberinto
        screen.blit(fondo_laberinto_img, ((ANCHO_VENTANA - fondo_laberinto_img.get_width()) // 2, 5))  # Fondo para "Laberinto"

        # Dibujar el título "Laberinto" en la parte superior
        texto_titulo = titulo_fuente.render("Laberinto", True, BLANCO)
        screen.blit(texto_titulo, ((ANCHO_VENTANA - texto_titulo.get_width()) // 2, 20))

        lab.mostrar_lab(screen, pos_jugador, margen_x, margen_y, jugador_imgs[indice_frame])  # Pasar la imagen del jugador como argumento

        pygame.display.flip()
        reloj.tick(8)

def mensaje_final(screen, mensaje, color, reloj, fuente):
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                return

        screen.fill(VERDE_O)
        texto = fuente.render(mensaje, True, color)
        screen.blit(texto, (ANCHO_VENTANA // 2 - texto.get_width() // 2, ALTO_VENTANA // 2 - texto.get_height() // 2))

        texto_continuar = fuente.render("Presiona Enter para continuar", True, color)
        screen.blit(texto_continuar, (ANCHO_VENTANA // 2 - texto_continuar.get_width() // 2, ALTO_VENTANA // 2 + 40))

        pygame.display.flip()
        reloj.tick(config.FPS)
