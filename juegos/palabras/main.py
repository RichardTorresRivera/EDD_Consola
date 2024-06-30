import pygame
from levels import LevelManager
from tutorials import show_tutorial
import os

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Stack Adventure")

    # Cargar y reproducir la música de fondo
    pygame.mixer.music.load(os.path.join('recursos', 'Contar Palabras - Words.mp3'))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # Mostrar el tutorial inicial
    show_tutorial(screen)

    # Inicialización de niveles
    level_manager = LevelManager(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            level_manager.handle_events(event)

        level_manager.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
