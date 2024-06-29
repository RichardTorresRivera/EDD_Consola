# Archivo principal del juego
"""
from juegos.hanoi.main import main_hanoi
from juegos.decisiones.main import main_decisiones
from menu.inicio import Menu

def main():
    menu = Menu()
    nivel_seleccionado = menu.mostrar_menu() # Comentar si quieres probar el main de tu archivo

if __name__ == "__main__":
    main()
"""

#"""
import os
import sys
import pygame
import config

from menu.play import main_play

# Inicializacion de Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((config.ANCHO_VENTANA, config.ALTO_VENTANA))
pygame.display.set_caption('Stack Adventure')
reloj = pygame.time.Clock()
# Fin de inicializacion

def manejar_eventos_inicio(estado, buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Click izquierdo del raton
            if event.button == 1:
                mouse_pos = event.pos
                # Boton jugar
                if buttons[0].collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    print("Mostrando game")
                    estado[0] = config.SCREEN_PLAY
                # Boton salir
                elif buttons[1].collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    pygame.quit()
                    sys.exit()


def dibujar_inicio(screen, fondo, buttons):
    screen.blit(fondo, (0,0))
    mouse_pos = pygame.mouse.get_pos()
    if any(boton.collidepoint(mouse_pos) for boton in buttons):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.display.flip()


def main():
    # Ambiente
    pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Inicio - Barracuda.mp3"))
    pygame.mixer.music.play(-1)
    # Botones
    boton_jugar = pygame.Rect(535, 330, 210, 85)
    boton_salir = pygame.Rect(535, 430, 210, 85)
    buttons_inicio = [boton_jugar, boton_salir]
    # Imagen
    img_menu_path = os.path.join(config.MENU_DIR, "menu.png")
    img_menu = pygame.image.load(img_menu_path)
    # Estado de juego (arreglo por referencia)
    estado = [config.SCREEN_INICIO]
    # Bucle principal
    while True:
        if estado[0] == config.SCREEN_INICIO:
            manejar_eventos_inicio(estado, buttons_inicio)
            dibujar_inicio(screen, img_menu, buttons_inicio)
        elif estado[0] == config.SCREEN_PLAY:
            main_play(screen, reloj, estado)
        reloj.tick(config.FPS)

if __name__ == "__main__":
    main()
#"""