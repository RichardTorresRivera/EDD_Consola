import pygame
import os
import config

from common.utils import mostrar_indicador_mouse

def manejar_eventos_panel_pause(estado, buttons):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("saliendo de panel pause")
                estado[0] = config.SCREEN_GAME
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Click izquierdo
            if event.button == 1:
                mpos = pygame.mouse.get_pos()
                print("Pos del mouse:", mpos)
                mouse_pos = event.pos
                # Boton continuar
                if buttons[0].collidepoint(mouse_pos):
                    print("mostrando juego ...")
                    estado[0] = config.SCREEN_GAME
                # Boton salir
                elif buttons[1].collidepoint(mouse_pos):
                    print("saliendo del juego, mostrar mapa")
                    estado[0] = config.SCREEN_MAPA

def dibujar_panel_pause(screen, img):
    screen.blit(img, (480, 195))
    #img_rect = pygame.Rect(480, 195, img.get_width(), img.get_height())
    #pygame.display.update(img_rect)
    pygame.display.flip() # Dibujar todo y evitar pantalla negra XD

def main_panel_pause(screen, reloj, estado):
    # Botonoes
    button_continuar = pygame.Rect(560, 340, 180, 40)
    button_salir = pygame.Rect(580, 400, 130, 40)
    buttons_pause = [button_continuar, button_salir]
    # Imagenes
    img_pause_path = os.path.join(config.GENERAL_DIR, "opcion_pausa.png")
    img_pause = pygame.image.load(img_pause_path)
    # Bucle principal
    run_panel_pause = True
    while run_panel_pause:
        if estado[0] == config.SCREEN_PANEL_PAUSE:
            manejar_eventos_panel_pause(estado, buttons_pause)
            mostrar_indicador_mouse(buttons_pause)
            dibujar_panel_pause(screen, img_pause)
        elif estado[0] == config.SCREEN_MAPA or estado[0] == config.SCREEN_GAME:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            run_panel_pause = False
        reloj.tick(config.FPS)