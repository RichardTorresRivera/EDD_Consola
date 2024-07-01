import pygame
import os
import sys
import config
from Menu.paneles.panel_pause import main_panel_pause
from Menu.paneles.panel_book import main_panel_book
from common.music_config import cargar_configuracion, cargar_vfx
from common.utils import mensaje_final
from common.colores import *
from juegos.buscaminas.recursos.matriz import Matriz
from juegos.buscaminas.recursos import constantes
from common.pause_button import cargar_boton_pausa, dibujar_boton_pausa, manejar_eventos_boton_pausa
from common.help_button import cargar_boton_help, dibujar_boton_help, manejar_eventos_boton_help

def main_buscaminas(screen, reloj, estado, dificultad):
    # Ambiente
    cargar_configuracion(estado)
    pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Buscaminas - Sympathy For The Devil.mp3"))
    pygame.mixer.music.play(-1)
    # Carga de sonidos
    sonido_click = cargar_vfx("Buscaminas - Grass.mp3", estado)
    sonido_bomba = cargar_vfx("Buscaminas - Bomb.mp3", estado)
    # Fondo
    fondo_img = pygame.image.load(os.path.join(config.FONDOS_DIR, "buscaminasHD.png"))
    # Fuente
    fuente = pygame.font.Font(os.path.join(config.FONTS_DIR, "minecraft.ttf"), 30)
    fuente_minas = pygame.font.Font(os.path.join(config.FONTS_DIR, "minecraft.ttf"), 24)
    # Tablero
    filas = (dificultad[0] + 1)*3
    columnas = (dificultad[0] + 1)*3
    minas = int(((dificultad[0] + 1)*3)**2/4) - 3
    # Crea la matriz con los valores
    matriz = Matriz(filas, columnas, minas)
    tamaño_celda = constantes.TAMANIO_CELDA
    # Calcular margen_x y margen_y para centrar el tablero en la pantalla
    tablero_ancho = columnas * tamaño_celda
    tablero_alto = filas * tamaño_celda
    margen_x = (config.ANCHO_VENTANA - tablero_ancho) // 2
    margen_y = (config.ALTO_VENTANA - tablero_alto) // 2 + 60
    # Cargar imagen y rectangulo del boton pause y help
    img_boton_pausa, boton_pausa = cargar_boton_pausa()
    img_boton_book, boton_book = cargar_boton_help()
    # Bucle principal
    juagar_buscaminas = True
    estado[0] = config.SCREEN_PANEL_BOOK
    while juagar_buscaminas:
        if estado[0] == config.SCREEN_GAME:
            for evento in pygame.event.get():
                manejar_eventos_boton_pausa(evento, estado, boton_pausa)
                manejar_eventos_boton_help(evento, estado, boton_book)
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    columna = (pos[0] - margen_x) // tamaño_celda
                    fila = (pos[1] - margen_y) // tamaño_celda

                    # Verificar que el clic esté dentro de los límites del tablero
                    if 0 <= fila < filas and 0 <= columna < columnas:
                        if evento.button == 1:  # Botón izquierdo del ratón
                            if not matriz.revelado[fila][columna]:
                                if not matriz.revelar(fila, columna):
                                    sonido_bomba.play()
                                    matriz.mostrar_bombas(screen, tamaño_celda, margen_x, margen_y)
                                    pygame.display.flip()
                                    pygame.time.delay(2000)
                                    juagar_buscaminas = False
                                else:
                                    sonido_click.play()
                        elif evento.button == 3:  # Botón derecho del ratón
                            matriz.colocar_bandera(fila, columna)

            screen.blit(fondo_img, (0, 0))  # Dibujar la imagen de fondo
            matriz.mostrar(screen, tamaño_celda, margen_x, margen_y)  # Pasar margen_x y margen_y a la función mostrar

            # Dibujar el cuadro en la parte superior derecha
            cuadro_ancho, cuadro_alto = 200, 100
            cuadro_x, cuadro_y = 10, 10
            pygame.draw.rect(screen, MARRON_CLARO, (cuadro_x, cuadro_y, cuadro_ancho, cuadro_alto))
            pygame.draw.rect(screen, NEGRO, (cuadro_x, cuadro_y, cuadro_ancho, cuadro_alto), 3)

            # Dibujar el texto "Buscaminas"
            texto_buscaminas = fuente.render("Buscaminas", True, GOLD)
            screen.blit(texto_buscaminas, (cuadro_x + 10, cuadro_y + 10))

            # Dibujar el texto de minas restantes
            minas_restantes = matriz.contar_minas_restantes()
            texto_minas = fuente_minas.render(f"Minas: {minas_restantes}", True, NEGRO)
            screen.blit(texto_minas, (cuadro_x + 10, cuadro_y + 60))
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

            # Verificar si se ha ganado
            if matriz.ganaste():
                juagar_buscaminas = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                pygame.time.delay(2000)
                mensaje = "¡Felicidades, ganaste!$"
                mensaje_final(screen, mensaje, GOLD, reloj, fuente)
                estado[0] = config.SCREEN_MAPA

            if juagar_buscaminas == False:
                pygame.time.delay(2000) 
                matriz.mostrar_bombas(screen, tamaño_celda, margen_x, margen_y)
                mensaje = "¡Tocaste una bomba!$"
                mensaje_final(screen, mensaje, ROJO, reloj, fuente)
                estado[0] = config.SCREEN_MAPA
                
        elif estado[0] == config.SCREEN_PANEL_PAUSE:
            main_panel_pause(screen, reloj, estado)
        elif estado[0] == config.SCREEN_PANEL_BOOK:
            main_panel_book(screen, reloj, estado)
        elif estado[0] == config.SCREEN_MAPA:
            juagar_buscaminas = False
        reloj.tick(config.FPS)

if __name__ == "__main__":
    main_buscaminas()