import pygame
import os
import sys
import config

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Initialization Pygame
pygame.init()
screen = pygame.display.set_mode((config.ANCHO_VENTANA, config.ALTO_VENTANA))
pygame.display.set_caption('Libro Instrucciones')
clock = pygame.time.Clock()
FPS = 60
# End of initialization

background_default = pygame.image.load(os.path.join(config.LIBROS_DIR, "LibroVacio.png"))
background_hanoi = pygame.image.load(os.path.join(config.LIBROS_DIR, "LibroHanoi.png"))

context = 'hanoi'


def librohanoi():
    global context
    context = 'hanoi'


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

    if context == 'hanoi':
        background = background_hanoi
    else:
        background = background_default

    screen.blit(background, [0, 0])
    pygame.display.flip()
    clock.tick(FPS)
