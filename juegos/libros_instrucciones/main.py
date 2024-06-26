import pygame
import os
import sys
import config

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Inicialización Pygame
pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Libro Instrucciones')
clock = pygame.time.Clock()
FPS = 60
# Fin de inicialización

background = pygame.image.load(os.path.join(config.LIBROS_DIR,"LibroVacio.png"))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()
    screen.blit(background, [0,0])
    clock.tick(FPS)

# def infoHanoi()

# def infoBuscaminas()

# def infoCartas()

# def infoLaberintos()

# def infoDecisiones()

# def infoPalabras()