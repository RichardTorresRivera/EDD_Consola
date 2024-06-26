import pygame
import sys
import os
import config
from Menu.paneles.panel_pause import main_panel_pause
from Menu.paneles.panel_book import main_panel_book
from common.utils import mensaje_final
from common.music_config import cargar_configuracion
from juegos.laberinto.recursos.constantes import *
from juegos.laberinto.recursos.grafo import Grafo
from common.pause_button import cargar_boton_pausa, dibujar_boton_pausa, manejar_eventos_boton_pausa
from common.help_button import cargar_boton_help, dibujar_boton_help, manejar_eventos_boton_help

def main_lab(screen, reloj, estado, dificultad):
    cargar_configuracion(estado)
    pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Laberinto - Enjoy The Silence.mp3"))
    pygame.mixer.music.play(-1)
    fondo_img = pygame.image.load(os.path.join(config.FONDOS_DIR, "laberintoHD.png"))
    fondo_img = pygame.transform.scale(fondo_img, (ANCHO_VENTANA, ALTO_VENTANA))

    # Fuente para el texto
    fuente = pygame.font.Font(ruta_fuente, 45)
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
    # Cargar imagen y rectangulo del boton pause y help
    img_boton_pausa, boton_pausa = cargar_boton_pausa()
    img_boton_book, boton_book = cargar_boton_help()
    # Bucle principal
    jugar_lab = True
    estado[0] = config.SCREEN_PANEL_BOOK
    while jugar_lab:
        if estado[0] == config.SCREEN_GAME:
            for evento in pygame.event.get():
                manejar_eventos_boton_pausa(evento, estado, boton_pausa)
                manejar_eventos_boton_help(evento, estado, boton_book)
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Obtener el estado del teclado
            teclas = pygame.key.get_pressed()

            # Manejar el movimiento del jugador
            dx, dy = 0, 0
            if teclas[pygame.K_w] or teclas[pygame.K_UP]:
                dx, dy = -1, 0
            elif teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
                dx, dy = 1, 0
            elif teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
                dx, dy = 0, -1
            elif teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
                dx, dy = 0, 1

            nueva_pos = (pos_jugador[0] + dx, pos_jugador[1] + dy)
            if nueva_pos in lab.obtener_mov_validos(pos_jugador):
                pos_jugador = nueva_pos

            # Actualizar el índice del frame para la animación
            indice_frame = (indice_frame + 1) % len(jugador_imgs)

            # Dibujar el laberinto centrado en la pantalla
            screen.blit(fondo_img, (0, 0))  # Fondo del laberinto
            screen.blit(fondo_laberinto_img, ((ANCHO_VENTANA - fondo_laberinto_img.get_width()) // 2, 5))  # Fondo para "Laberinto"
            # Dibujar el título "Laberinto" en la parte superior
            texto_titulo = titulo_fuente.render("Laberinto", True, BLANCO)
            screen.blit(texto_titulo, ((ANCHO_VENTANA - texto_titulo.get_width()) // 2, 20))
            lab.mostrar_lab(screen, pos_jugador, margen_x, margen_y, jugador_imgs[indice_frame])  # Pasar la imagen del jugador como argumento
            # Dibujar boton pausa y help
            dibujar_boton_pausa(screen, img_boton_pausa)
            dibujar_boton_help(screen, img_boton_book)
            mouse_pos = pygame.mouse.get_pos()
            if boton_pausa.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            elif boton_book.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            pygame.display.flip()
            if pos_jugador == lab.salida:
                jugar_lab = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                pygame.time.delay(1000)
                mensaje_final(screen, "¡Felicidades, has llegado a la salida!", GOLD, reloj, fuente)
                estado[0] = config.SCREEN_MAPA
                print("FELICIDADES")
                estado[8].add("laberinto")
        elif estado[0] == config.SCREEN_PANEL_PAUSE:
            main_panel_pause(screen, reloj, estado)
        elif estado[0] == config.SCREEN_PANEL_BOOK:
            main_panel_book(screen, reloj, estado)
        elif estado[0] == config.SCREEN_MAPA:
            jugar_lab = False
        reloj.tick(8)
