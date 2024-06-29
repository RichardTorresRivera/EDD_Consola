import pygame
import os
import sys
import config
from juegos.hanoi.recursos.hanoi import Hanoi
from juegos.hanoi.recursos.torre import Disco, Torre
from juegos.hanoi.recursos import constantes

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((config.ANCHO_VENTANA, config.ALTO_VENTANA))
pygame.display.set_caption('Torres de Hanoi')
reloj = pygame.time.Clock()
FPS = 60
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

def manejar_eventos(hanoi, torres, discos, sounds):
    for event in pygame.event.get():
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

def dibujar(screen, fondo, torres, discos):
    screen.blit(fondo, (0,0))
    for i in range(3):
        torres[i].dibujar(screen)
    for i in range(len(discos)):
        discos[i].dibujar(screen)

    mouse_pos = pygame.mouse.get_pos()
    if any(torre.forma.collidepoint(mouse_pos) for torre in torres):
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

def main_hanoi():
    n = 3
    img_fondo = cargar_imagen(config.FONDOS_DIR, "hanoiHD")
    img_torre = cargar_imagen(config.HANOI_DIR, "soporte", constantes.ANCHO_TORRE, constantes.ALTO_TORRE)
    
    torres = crear_torres(img_torre)
    discos = llenar_torre(n, torres[0])

    hanoi = Hanoi(torres)
    pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Torre Hanoi - Stairway to Heaven.mp3"))
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
    sound_push = pygame.mixer.Sound(os.path.join(config.SFX_DIR, "Hanoi - Push.mp3"))
    sound_pop = pygame.mixer.Sound(os.path.join(config.SFX_DIR, "Hanoi y Cartas - Pop.mp3"))
    sound_push.set_volume(0.5)
    sound_pop.set_volume(0.5)
    sounds = [sound_push, sound_pop]
    
    jugar_hanoi = True
    while jugar_hanoi:
        manejar_eventos(hanoi, torres, discos, sounds)
        actualizar(discos)
        dibujar(screen, img_fondo, torres, discos)
        if hanoi.game_over(n):
            jugar_hanoi = False
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            pygame.time.delay(2000)
            print("FELICIDADES")
            print("Numero de movimiento: ", hanoi.get_movimientos())
            # pygame.quit()
            # sys.exit()
        reloj.tick(FPS)

if __name__ == '__main__':
    main_hanoi()
