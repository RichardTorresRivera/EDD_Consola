import pygame
import os
import sys
import config
from common.utils import mostrar_indicador_mouse
from menu.level import main_level

def manejar_eventos_play(estado, buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Click izquierdo del raton
            if event.button == 1:
                mouse_pos = event.pos
                # Boton nuevo
                if buttons[0].collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    print("Mostrando levels")
                    estado[0] = config.SCREEN_LEVEL
                # Boton cargar
                elif buttons[1].collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    print("Cargando partida")
                    # Aniadir logia :)
                # Boton volver
                elif buttons[2].collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    estado[0] = config.SCREEN_INICIO

def dibujar_play(screen, fondo):
    screen.blit(fondo, (0,0))
    pygame.display.flip()

def main_play(screen, reloj, estado):
    # Botones
    boton_nuevo = pygame.Rect(535, 275, 210, 85)
    boton_cargar = pygame.Rect(535, 375, 210, 85)
    boton_volver = pygame.Rect(535, 475, 210, 85)
    buttons_game = [boton_nuevo, boton_cargar, boton_volver]
    # Imagen
    img_game_path = os.path.join(config.MENU_DIR, "game.png")
    img_game = pygame.image.load(img_game_path)
    # Bucle principal
    run_game = True
    while run_game:
        if estado[0] == config.SCREEN_PLAY:
            manejar_eventos_play(estado, buttons_game)
            mostrar_indicador_mouse(buttons_game)
            dibujar_play(screen, img_game)
        elif estado[0] == config.SCREEN_INICIO:
            run_game = False
        elif estado[0] == config.SCREEN_LEVEL:
            main_level(screen, reloj, estado)
        reloj.tick(config.FPS)
