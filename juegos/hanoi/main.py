import pygame
import os
import sys
import config
from Menu.paneles.panel_pause import main_panel_pause
from Menu.paneles.panel_book import main_panel_book
from common.colores import *
from common.utils import mensaje_final
from common.music_config import cargar_configuracion, cargar_vfx
from juegos.hanoi.recursos.hanoi import Hanoi
from juegos.hanoi.recursos.torre import Disco, Torre
from juegos.hanoi.recursos import constantes
from common.pause_button import cargar_boton_pausa, dibujar_boton_pausa, manejar_eventos_boton_pausa
from common.help_button import cargar_boton_help, dibujar_boton_help, manejar_eventos_boton_help

# Inicialización de Pygame
#pygame.init()
#screen = pygame.display.set_mode((config.ANCHO_VENTANA, config.ALTO_VENTANA))
#pygame.display.set_caption('Torres de Hanoi')
#reloj = pygame.time.Clock()
#FPS = 60
# Fin de inicialización


def imagenes_dicos(n):
    img_discos = []
    for i in range(n, 0, -1):
        img_disco = cargar_imagen(config.HANOI_DIR+"\\discos", "disco"+str((i)), constantes.ANCHO_DISCO-i*20, constantes.ALTO_DISCO)
        img_discos.append(img_disco)
    return img_discos

def crear_discos(n):
    discos = []
    img = imagenes_dicos(n)
    for i in range(n):
        discos.append(Disco((i+1), img[i]))
    return discos

def crear_torres(img):
    torres = []
    for i in range(3):
        torres.append(Torre(img, (i+1)*270, 70))
    return torres

def llenar_torre(n, torre):
    discos = crear_discos(n)
    for i in range(n, 0, -1):
        discos[i-1].set_pos(torre.get_tamanio())
        discos[i-1].set_torre(torre)
        torre.apilar(discos[i-1])
    return discos

def manejar_eventos(hanoi, torres, discos, sounds, estado, button_pause_rect, button_book_rect, images, img_actual):
    for event in pygame.event.get():
        manejar_eventos_boton_pausa(event, estado, button_pause_rect)
        manejar_eventos_boton_help(event, estado, button_book_rect)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                for torre in torres:
                    if torre.forma.collidepoint(mouse_pos):
                        if not hanoi.get_flotando():
                            if not torre.esta_vacia():
                                disco = torre.desapilar()
                                index = disco.get_indice()
                                discos[index] = disco
                                discos[index].set_pos(constantes.DISCO_FLOTAR)
                                hanoi.set_disco_mover(disco)
                                hanoi.set_torre_origen(torre)
                                hanoi.set_flotando(True)
                                sounds[0].play()
                                img_actual = images[4]
                            else:
                                print("Movimiento invalido: La torre esta vacia, no hay discos para mover")
                                img_actual = images[0]
                        else:
                            hanoi.set_torre_destino(torre)
                            if hanoi.movimiento_valido():
                                disco = hanoi.get_disco_mover()
                                index = disco.get_indice()
                                discos[index].set_torre(torre)
                                discos[index].set_pos(torre.get_tamanio())
                                discos[index].set_torre(torre)
                                torre.apilar(disco)
                                hanoi.set_flotando(False)
                                sounds[1].play()
                                if (hanoi.get_torre_origen() == hanoi.get_torre_destino()):
                                    hanoi.movimientos -= 1
                                    print("Mmmm")
                                    img_actual = images[1]
                                else:
                                    print("Bien hecho")
                                    img_actual = images[2]
                            else:
                                print("Movimiento invalido: El peso del disco a mover es mayor al disco de la torre destino")
                                img_actual = images[3]
    return img_actual

def actualizar(discos):
    for i in range(len(discos)):
        discos[i].actualizar()

def dibujar(screen, fondo, torres, discos, img_boton_pausa, boton_pausa, img_boton_help, boton_book, movimientos, fuente, img_actual):
    screen.blit(fondo, (0,0))
    for i in range(3):
        torres[i].dibujar(screen)
    for i in range(len(discos)):
        discos[i].dibujar(screen)

    dibujar_boton_pausa(screen, img_boton_pausa)
    dibujar_boton_help(screen, img_boton_help)
    if (movimientos <= 3):
        texto = fuente.render(f"Movimientos restantes: {movimientos}", True, ROJO)
    else:
        texto = fuente.render(f"Movimientos restantes: {movimientos}", True, BLANCO)
    screen.blit(texto, (config.ANCHO_VENTANA // 2 - texto.get_width() // 2, 10))

    if img_actual:
        screen.blit(img_actual, (0, 0))

    mouse_pos = pygame.mouse.get_pos()
    if any(torre.forma.collidepoint(mouse_pos) for torre in torres):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif boton_pausa.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif boton_book.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    pygame.display.flip()

def cargar_imagen(path, nombre, ancho = None, alto = None):
    img_path = os.path.join(path, nombre+".png")
    img = pygame.image.load(img_path)
    if (ancho is not None and alto is not None):
        img = pygame.transform.scale(img, (ancho, alto))

    return img

def main_hanoi(screen, reloj, estado, dificultad):
    n = dificultad[0]+2
    img_fondo = cargar_imagen(config.FONDOS_DIR, "hanoiHD")
    img_torre = cargar_imagen(config.HANOI_DIR, "soporte", constantes.ANCHO_TORRE, constantes.ALTO_TORRE)
    
    torres = crear_torres(img_torre)
    discos = llenar_torre(n, torres[0])

    hanoi = Hanoi(torres)
    cargar_configuracion(estado)
    pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Torre Hanoi - Stairway to Heaven.mp3"))
    pygame.mixer.music.play(-1)
    sound_pop = cargar_vfx("Hanoi y Cartas - Pop.mp3", estado)
    sound_push = cargar_vfx("Hanoi - Push.mp3", estado)
    sounds = [sound_pop, sound_push]

    fuente = pygame.font.Font(os.path.join(config.FONTS_DIR, "minecraft.ttf"), 45)

    fuente_mov = pygame.font.Font(os.path.join(config.FONTS_DIR, "minecraft.ttf"), 25)

    # Cargar imagen y rectangulo del boton pause y help
    img_boton_pausa, button_pause_rect = cargar_boton_pausa()
    img_boton_book, button_book_rect = cargar_boton_help()

    # Imagenes de toshi
    img_torre_vacia = cargar_imagen(config.TOSHI_DIR + "\\hanoi", "torre_vacia")
    img_mmm = cargar_imagen(config.TOSHI_DIR + "\\hanoi", "pensando")
    img_bien_hecho = cargar_imagen(config.TOSHI_DIR + "\\hanoi", "bien_hecho")
    img_mov_invalido = cargar_imagen(config.TOSHI_DIR + "\\hanoi", "mov_invalido")
    img_defecto = cargar_imagen(config.TOSHI_DIR + "\\hanoi", "defecto")

    images = [img_torre_vacia, img_mmm, img_bien_hecho, img_mov_invalido, img_defecto]

    img_actual = images[4]
    estado[0] = config.SCREEN_PANEL_BOOK
    jugar_hanoi = True
    while jugar_hanoi:
        if estado[0] == config.SCREEN_GAME:
            img_actual = manejar_eventos(hanoi, torres, discos, sounds, estado, button_pause_rect, button_book_rect, images, img_actual)
            actualizar(discos)
            dibujar(screen, img_fondo, torres, discos, img_boton_pausa, button_pause_rect, img_boton_book, button_book_rect, pow(2, n)-1-hanoi.get_movimientos(), fuente_mov, img_actual)
            if hanoi.game_over(n):
                jugar_hanoi = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                pygame.time.delay(1000)
                mensaje = "¡Felicidades lograste completar el desafio!$" + "Numero de movimientos: " + str(hanoi.get_movimientos())
                mensaje_final(screen, mensaje, GOLD, reloj, fuente)
                estado[0] = config.SCREEN_MAPA
                estado[8].add("hanoi")
                # pygame.quit()
                # sys.exit()
            elif hanoi.get_movimientos() == pow(2, n)-1:
                jugar_hanoi = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                pygame.time.delay(1000)
                mensaje = "¡Perdiste, no superaste el desafio con el minimo$numero de movimientos!$$" + "Numero de movimientos minimos: " + str(hanoi.get_movimientos())
                mensaje_final(screen, mensaje, ROJO, reloj, fuente)
                estado[0] = config.SCREEN_MAPA
        elif estado[0] == config.SCREEN_PANEL_PAUSE:
            main_panel_pause(screen, reloj, estado)
        elif estado[0] == config.SCREEN_PANEL_BOOK:
            main_panel_book(screen, reloj, estado)
        elif estado[0] == config.SCREEN_MAPA:
            jugar_hanoi = False
        reloj.tick(config.FPS)


if __name__ == '__main__':
    main_hanoi()
