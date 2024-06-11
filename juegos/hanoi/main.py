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

def manejar_eventos(hanoi, torres, discos):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for torre in torres:
                if torre.forma.collidepoint(mouse_pos):
                    if not hanoi.flotando:
                        if not torre.esta_vacia():
                            disco = torre.desapilar()
                            hanoi.disco_mover = disco
                            index = disco.get_peso()-1
                            hanoi.indice_disco_mover = index
                            discos[index] = disco
                            discos[index].set_pos(4.5)
                            hanoi.flotando = True
                        else:
                            print("La torre esta vacia, movimiento invalido")
                    else:
                        index = hanoi.indice_disco_mover 
                        disco = hanoi.disco_mover
                        discos[index].set_torre(torre) # asociar disco a torre
                        discos[index].set_pos(torre.get_tamanio())
                        discos[index].set_torre(torre)
                        torre.apilar(disco)
                        hanoi.flotando = False

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

    pygame.display.flip()  # Actualizar la pantalla

def cargar_imagen(path, nombre, ancho = None, alto = None):
    img_path = os.path.join(path, nombre+".png")
    img = pygame.image.load(img_path)
    if (ancho is not None and alto is not None):
        img = pygame.transform.scale(img, (ancho, alto))

    return img

def main_hanoi():
    img_fondo = cargar_imagen(config.FONDOS_DIR, "hanoiHD")
    img_torre = cargar_imagen(config.HANOI_DIR, "soporte", constantes.ANCHO_TORRE, constantes.ALTO_TORRE)
    
    torres = crear_torres(img_torre)
    discos = llenar_torre(5, torres[0]) #Numero de discos

    hanoi = Hanoi() # Objeto hanoi

    while True:
        manejar_eventos(hanoi, torres, discos)
        actualizar(discos)
        dibujar(screen, img_fondo, torres, discos)
        reloj.tick(FPS)

if __name__ == '__main__':
    main_hanoi()
