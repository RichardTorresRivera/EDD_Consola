import pygame
import os
import config
from common.utils import escalar_imagen

def dibujar_boton_pausa(screen, img_boton_pausa):
    # Dibujar el botón de pausa en la esquina superior derecha
    screen.blit(img_boton_pausa, (1180, 20))

def manejar_eventos_boton_pausa(event, estado, button_pause_rect):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Click izquierdo
            mouse_pos = event.pos
            if button_pause_rect.collidepoint(mouse_pos):
                estado[0] = config.SCREEN_PANEL_PAUSE
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                estado[0] = config.SCREEN_PANEL_PAUSE

def cargar_boton_pausa():
    img_boton_pausa_path = os.path.join(config.GENERAL_DIR, "boton pausa.png")
    img_boton_pausa = pygame.image.load(img_boton_pausa_path)
    img_boton_pausa = escalar_imagen(img_boton_pausa, 0.07)
    button_pause_rect = pygame.Rect(1181, 20, 50, 50)
    return img_boton_pausa, button_pause_rect
