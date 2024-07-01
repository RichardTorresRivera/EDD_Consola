import pygame
import os
import config
from common.instructions_text import words_book, minesweeper_book, hanoi_book, labyrinth_book, decision_book
from common.utils import mostrar_indicador_mouse, escalar_imagen

def manejar_eventos_panel_book(estado, buttons):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("saliendo de panel book")
                estado[0] = config.SCREEN_GAME
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Click izquierdo
            if event.button == 1:
                mpos = pygame.mouse.get_pos()
                print("Pos del mouse:", mpos)
                mouse_pos = event.pos
                # Boton ok
                if buttons[0].collidepoint(mouse_pos):
                    print("mostrando juego ...")
                    estado[0] = config.SCREEN_GAME


def main_panel_book(screen, reloj, estado):
    # Botones
    button_ok = pygame.Rect(1092, 124, 55, 41) # cambiar
    buttons_panel_book = [button_ok]
    #estado[9] #num_game
    nombres_book = ["LibroWords.png","LibroMinesWeeper.png","LibroHanoi.png","LibroVacio.png","LibroLabyrinth.png","LibroDecision.png"]
    # Imagenes
    img_book_path = os.path.join(config.LIBROS_DIR, nombres_book[estado[9]])
    img_book = pygame.image.load(img_book_path)
    img_book = escalar_imagen(img_book, 0.9)
    # Bucle principal
    run_panel_book = True
    while run_panel_book:
        if estado[0] == config.SCREEN_PANEL_BOOK:
            manejar_eventos_panel_book(estado, buttons_panel_book)
            mostrar_indicador_mouse(buttons_panel_book)
            if estado[9] == 0:
                words_book(screen)
            elif estado[9] == 1:
                minesweeper_book(screen)
            elif estado[9] == 2:
                hanoi_book(screen)
            elif estado[9] == 4:
                labyrinth_book(screen)
            elif estado[9] == 5:
                decision_book(screen)
            pygame.display.flip()
        elif estado[0] == config.SCREEN_GAME:
            run_panel_book = False
        reloj.tick(config.FPS)
