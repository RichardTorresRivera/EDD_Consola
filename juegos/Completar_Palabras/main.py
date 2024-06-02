import pygame
from levels import LevelManager
from tutorials import show_tutorial

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Stack Adventure")

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
