import os
import sys
import pygame

# Agregar el directorio del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora se puede importar config
import config

pygame.init()

font = pygame.font.Font(None, 36)

boton_jugar = pygame.Rect(535, 330, 210, 85)
boton_salir = pygame.Rect(535, 430, 210, 85)

img_path = os.path.join(config.MENU_DIR,"menu.png")
img = pygame.image.load(img_path)

screen = pygame.display.set_mode((1280, 720))


def inicio():
    running = True
    while running:
        pygame.draw.rect(screen, (255, 255, 255), boton_jugar)
        pygame.draw.rect(screen, (255, 255, 255), boton_salir)

        screen.blit(img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if boton_jugar.collidepoint(mouse_pos):
                    running = False
                elif boton_salir.collidepoint(mouse_pos):
                    running = False
                    pygame.quit()
                    sys.exit()

        pygame.display.update()