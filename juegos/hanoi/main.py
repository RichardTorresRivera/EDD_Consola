import pygame
import os
import sys
import config
from Menu.paneles.panel_pause import main_panel_pause
from common.colores import *
from common.utils import mensaje_final
from common.music_config import cargar_configuracion, cargar_vfx
from juegos.hanoi.recursos.hanoi import Hanoi
from juegos.hanoi.recursos.torre import Disco, Torre
from juegos.hanoi.recursos import constantes
from common.pause_button import cargar_boton_pausa, dibujar_boton_pausa, manejar_eventos_boton_pausa

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

def manejar_eventos(hanoi, torres, discos, sounds, estado, button_pause_rect):
    for event in pygame.event.get():
        manejar_eventos_boton_pausa(event, estado, button_pause_rect)
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
                            else:
                                print("Movimiento invalido: La torre esta vacia, no hay discos para mover")
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
                                    print("Mmmm")
                                else:
                                    print("Bien hecho")
                            else:
                                print("Movimiento invalido: El peso del disco a mover es mayor al disco de la torre destino")

def actualizar(discos):
    for i in range(len(discos)):
        discos[i].actualizar()

def dibujar(screen, fondo, torres, discos, img_boton_pausa, boton_pausa):
    screen.blit(fondo, (0,0))
    for i in range(3):
        torres[i].dibujar(screen)
    for i in range(len(discos)):
        discos[i].dibujar(screen)

    dibujar_boton_pausa(screen, img_boton_pausa)

    mouse_pos = pygame.mouse.get_pos()
    if any(torre.forma.collidepoint(mouse_pos) for torre in torres):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif boton_pausa.collidepoint(mouse_pos):
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

    # Cargar imagen y rectangulo del boton pause
    img_boton_pausa, button_pause_rect = cargar_boton_pausa()
    
    jugar_hanoi = True
    while jugar_hanoi:
        if estado[0] == config.SCREEN_GAME:
            manejar_eventos(hanoi, torres, discos, sounds, estado, button_pause_rect)
            actualizar(discos)
            dibujar(screen, img_fondo, torres, discos, img_boton_pausa, button_pause_rect)
            if hanoi.game_over(n):
                jugar_hanoi = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                pygame.time.delay(2000)
                mensaje = "¡Felicidades lograste completar el desafio!$" + "Numero de movimientos: " + str(hanoi.get_movimientos())
                mensaje_final(screen, mensaje, GOLD, reloj, fuente)
                estado[0] = config.SCREEN_MAPA
                # pygame.quit()
                # sys.exit()
        elif estado[0] == config.SCREEN_PANEL_PAUSE:
            main_panel_pause(screen, reloj, estado)
        elif estado[0] == config.SCREEN_MAPA:
            jugar_hanoi = False
        reloj.tick(config.FPS)


if __name__ == '__main__':
    main_hanoi()
