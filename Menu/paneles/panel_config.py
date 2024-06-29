import pygame
import os
import config

from common.utils import mostrar_indicador_mouse

def manejar_eventos_panel_config(estado, buttons):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("saliendo panel config")
                estado[0] = config.SCREEN_MAPA
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Agregar el boton indicador de sonido
            # Click izquierdo
            if event.button == 1:
                mouse_pos = event.pos
                # Boton aceptar
                if buttons[0].collidepoint(mouse_pos):
                    print("Nuevos ajustes")
                    estado[0] = config.SCREEN_MAPA
                # Boton cancelar
                elif buttons[1].collidepoint(mouse_pos):
                    print("cancelando config")
                    estado[0] = config.SCREEN_MAPA

def actualizar_panel_config():
    pass

def dibujar_panel_config(screen, img_config):
    screen.blit(img_config, (500, 195))
    img_rect = pygame.Rect(500, 195, img_config.get_width(), img_config.get_height())
    pygame.display.update(img_rect)

def main_panel_config(screen, reloj, estado):
    # Botones
    button_aceptar = pygame.Rect(593, 460, 30, 30)
    button_cancel = pygame.Rect(658, 460, 30, 30)
    buttons_panel_config = [button_aceptar, button_cancel]
    # Imagenes
    img_config_path = os.path.join(config.GENERAL_DIR, "panel_config.png")
    img_config = pygame.image.load(img_config_path)
    img_handle_path = os.path.join(config.GENERAL_DIR, "slide_button.png")
    img_handle = pygame.image.load(img_handle_path)
    # Bucle principal
    run_panel_config = True
    while run_panel_config:
        if estado[0] == config.SCREEN_PANEL_CONFIG:
            manejar_eventos_panel_config(estado, buttons_panel_config)
            mostrar_indicador_mouse(buttons_panel_config)
            actualizar_panel_config()
            dibujar_panel_config(screen, img_config)
        elif estado[0] == config.SCREEN_MAPA:
            run_panel_config = False
        reloj.tick(config.FPS)

