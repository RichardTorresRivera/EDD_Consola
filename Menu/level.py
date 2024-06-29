import pygame
import os
import sys
import config
from menu.mapa2 import main_mapa

def manejar_eventos_play(estado, buttons, dificultad):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Click izquierdo del raton
            if event.button == 1:
                mouse_pos = event.pos
                # Boton Facil
                if buttons[0].collidepoint(mouse_pos):
                    print("Mostrando mapa, dificultad 1")
                    estado[0] = config.SCREEN_MAPA
                    dificultad[0] = 1
                # Boton Medio
                if buttons[1].collidepoint(mouse_pos):
                    print("Mostrando mapa, dificultad 2")
                    estado[0] = config.SCREEN_MAPA
                    dificultad[0] = 2
                # Boton Dificil
                elif buttons[2].collidepoint(mouse_pos):
                    print("Mostrando mapa, dificultad 3")
                    estado[0] = config.SCREEN_MAPA
                    dificultad[0] = 3

def dibujar_level(screen, fondo, buttons):
    screen.blit(fondo, (0,0))
    mouse_pos = pygame.mouse.get_pos()
    if any(boton.collidepoint(mouse_pos) for boton in buttons):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.display.flip()

def main_level(screen, reloj, estado):
    # Botones
    nivel_facil = pygame.Rect(535, 275, 210, 85)
    nivel_medio = pygame.Rect(535, 375, 210, 85)
    nivel_dificil = pygame.Rect(535, 475, 210, 85)
    buttons_level = [nivel_facil, nivel_medio, nivel_dificil]
    # Imagen
    img_level_path = os.path.join(config.MENU_DIR, "levels.png")
    img_level = pygame.image.load(img_level_path)
    # Bucle principal
    run_level = True
    dificultad = [1]
    while run_level:
        if estado[0] == config.SCREEN_LEVEL:
            manejar_eventos_play(estado, buttons_level, dificultad)
            dibujar_level(screen, img_level, buttons_level)
        elif estado[0] == config.SCREEN_MAPA:
            main_mapa(screen, reloj, estado, dificultad)
        reloj.tick(config.FPS)