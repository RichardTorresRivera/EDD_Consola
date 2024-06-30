import pygame
import os
import config

from common.utils import escalar_imagen, mostrar_indicador_mouse

def manejar_eventos_panel_help(estado, buttons):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("saliendo panel help")
                estado[0] = config.SCREEN_MAPA
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Click izquierdo
            if event.button == 1:
                mouse_pos = event.pos
                # Boton ok
                if buttons[0].collidepoint(mouse_pos):
                    print("saliendo panel help")
                    estado[0] = config.SCREEN_MAPA

def dibujar_panel_help(screen, img_help):
    screen.blit(img_help, (400, 65))
    #img_rect = pygame.Rect(400, 65, img_help.get_width(), img_help.get_height())
    #pygame.display.update(img_rect)
    pygame.display.flip()

def main_panel_help(screen, reloj, estado):
    # Botones
    button_ok = pygame.Rect(625, 558, 50, 40)
    buttons_panel_help = [button_ok]
    # Imagenes
    img_help_path = os.path.join(config.GENERAL_DIR, "help.png")
    img_help = pygame.image.load(img_help_path)
    img_help = escalar_imagen(img_help, 0.9)
    # Bucle principal
    run_panel_help = True
    while run_panel_help:
        if estado[0] == config.SCREEN_PANEL_HELP:
            manejar_eventos_panel_help(estado, buttons_panel_help)
            mostrar_indicador_mouse(buttons_panel_help)
            dibujar_panel_help(screen, img_help)
        elif estado[0] == config.SCREEN_MAPA:
            run_panel_help = False
        reloj.tick(config.FPS)