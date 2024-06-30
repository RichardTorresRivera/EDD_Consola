import pygame
import os
import sys
import config

from common.utils import mostrar_indicador_mouse

def manejar_eventos_panel_exit(estado, buttons):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("saliendo de mostrar panel")
                estado[0] = config.SCREEN_MAPA
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Click izquierdo
            if event.button == 1:
                mouse_pos = event.pos
                # Boton menu
                if buttons[0].collidepoint(mouse_pos):
                    print("mostrando menu ...")
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Inicio - Barracuda.mp3"))
                    pygame.mixer.music.play(-1)
                    estado[0] = config.SCREEN_INICIO
                # Boton escritorio
                elif buttons[1].collidepoint(mouse_pos):
                    print("Saliendo del juego...")
                    pygame.quit()
                    sys.exit()
                # Boton cancelar
                elif buttons[2].collidepoint(mouse_pos):
                    print("saliendo de mostrar panel")
                    estado[0] = config.SCREEN_MAPA

def dibujar_panel_exit(screen, img_exit):
    screen.blit(img_exit, (480, 195))
    #img_rect = pygame.Rect(480, 195, img_exit.get_width(), img_exit.get_height())
    #pygame.display.update(img_rect)
    pygame.display.flip()

def main_panel_exit(screen, reloj, estado):
    # Botones
    button_main_exit = pygame.Rect(570, 290, 160, 50)
    button_desktop_exit = pygame.Rect(570, 375, 160, 50)
    button_cancel = pygame.Rect(630, 460, 30, 30)
    buttons_panel_exit = [button_main_exit, button_desktop_exit, button_cancel]
    # Imagenes
    img_exit_path = os.path.join(config.GENERAL_DIR, "exit.png")
    img_exit = pygame.image.load(img_exit_path)
    # Bucle principal
    run_panel_exit = True
    while run_panel_exit:
        if estado[0] == config.SCREEN_PANEL_EXIT:
            manejar_eventos_panel_exit(estado, buttons_panel_exit)
            mostrar_indicador_mouse(buttons_panel_exit)
            dibujar_panel_exit(screen, img_exit)
        elif estado[0] == config.SCREEN_MAPA or estado[0] == config.SCREEN_INICIO:
            run_panel_exit = False
        reloj.tick(config.FPS)