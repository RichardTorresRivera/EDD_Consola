import os
import sys
import pygame

# Agregar el directorio del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora se puede importar config
import config

pygame.init()
pygame.mixer.init()

font = pygame.font.Font(None, 36)

boton_jugar = pygame.Rect(535, 330, 210, 85)
boton_salir = pygame.Rect(535, 430, 210, 85)
boton_nuevo = pygame.Rect(535, 275, 210, 85)
boton_cargar = pygame.Rect(535, 375, 210, 85)
boton_volver = pygame.Rect(535, 475, 210, 85)

img_path = os.path.join(config.MENU_DIR, "menu.png")
img = pygame.image.load(img_path)

game_path = os.path.join(config.MENU_DIR, "game.png")
game = pygame.image.load(game_path)

screen = pygame.display.set_mode((1280, 720))

def inicio():
    running = True
    while running:
        screen.blit(img, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        if boton_jugar.collidepoint(mouse_pos) or boton_salir.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if boton_jugar.collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    running = False
                    screen.blit(game, (0, 0))
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = event.pos
                                if boton_nuevo.collidepoint(mouse_pos) or boton_cargar.collidepoint(mouse_pos):
                                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                                    running = False
                                elif boton_volver.collidepoint(mouse_pos):
                                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                                    running = True
                                    while running:
                                        inicio()
                        pygame.display.update()
                elif boton_salir.collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    running = False
                    pygame.quit()
                    sys.exit()

        pygame.display.update()