import pygame
import os
import config
from common.utils import escalar_imagen

def dibujar_boton_help(screen, img):
    screen.blit(img, (1100, 20))

def manejar_eventos_boton_help(event, estado, button_rect):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Click izquierdo
            mouse_pos = event.pos
            if button_rect.collidepoint(mouse_pos):
                estado[0] = config.SCREEN_PANEL_BOOK
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                estado[0] = config.SCREEN_PANEL_BOOK

def cargar_boton_help():
    img_path = os.path.join(config.GENERAL_DIR, "libro.png")
    img = pygame.image.load(img_path)
    img = escalar_imagen(img, 0.08)
    button_rect = pygame.Rect(1100, 20, 50, 50)
    return img, button_rect