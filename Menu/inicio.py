import os
import sys
import config
import pygame
from mapa import Juego

# Agregar el directorio del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class Menu:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((1280, 720))
        self.font = pygame.font.Font(None, 36)

        self.inicio = 0
        self.level = 1
        self.choose_level = 2
        self.screen_status = self.inicio

        self.boton_jugar = pygame.Rect(535, 330, 210, 85)
        self.boton_salir = pygame.Rect(535, 430, 210, 85)
        self.boton_nuevo = pygame.Rect(535, 275, 210, 85)
        self.boton_cargar = pygame.Rect(535, 375, 210, 85)
        self.boton_volver = pygame.Rect(535, 475, 210, 85)
        self.nivel_facil = pygame.Rect(535, 275, 210, 85)
        self.nivel_medio = pygame.Rect(535, 375, 210, 85)
        self.nivel_dificil = pygame.Rect(535, 475, 210, 85)

        img_path = os.path.join(config.MENU_DIR, "menu.png")
        self.img = pygame.image.load(img_path)

        game_path = os.path.join(config.MENU_DIR, "game.png")
        self.game = pygame.image.load(game_path)

        levels_path = os.path.join(config.MENU_DIR, "levels.png")
        self.levels = pygame.image.load(levels_path)

        pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Inicio - Barracuda.mp3"))
        pygame.mixer.music.play(-1)

    def mostrar_menu(self):
        running = True

        while running:
            if self.screen_status == self.inicio:
                mouse_pos = pygame.mouse.get_pos()
                self.screen.blit(self.img, (0, 0))
                if self.boton_jugar.collidepoint(mouse_pos) or self.boton_salir.collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            elif self.screen_status == self.level:
                self.screen.blit(self.game, (0, 0))
                mouse_pos = pygame.mouse.get_pos()
                if (self.boton_nuevo.collidepoint(mouse_pos) or self.boton_cargar.collidepoint(mouse_pos)
                        or self.boton_volver.collidepoint(mouse_pos)):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.boton_jugar.collidepoint(mouse_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                        running = False
                        self.screen_status = self.level
                        self.screen.blit(self.game, (0, 0))
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse_pos = event.pos
                                    if self.boton_nuevo.collidepoint(mouse_pos):
                                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                                        self.screen.blit(self.levels, (0, 0))
                                        self.screen_status = self.choose_level
                                        pygame.display.update()
                                        running = False
                                        # Agrega un nuevo bucle de eventos para manejar los clics en los niveles
                                        while self.screen_status == self.choose_level:
                                            for event in pygame.event.get():
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                    mouse_pos = event.pos
                                                    if self.nivel_facil.collidepoint(mouse_pos):
                                                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                                                        self.level = 1
                                                        juego = Juego()
                                                        juego.mapa()
                                                        return self.level
                                                    elif self.nivel_medio.collidepoint(mouse_pos):
                                                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                                                        self.level = 2
                                                        return self.level
                                                    elif self.nivel_dificil.collidepoint(mouse_pos):
                                                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                                                        self.level = 3
                                                        return self.level
                                            pygame.display.update()
                                    elif self.boton_cargar.collidepoint(mouse_pos):
                                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                                        # Lógica para cargar el juego
                                    elif self.boton_volver.collidepoint(mouse_pos):
                                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                                        self.screen_status = self.inicio
                                        running = True
                            if running:
                                break
                            pygame.display.update()

                    elif self.boton_salir.collidepoint(mouse_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                        pygame.quit()
                        sys.exit()
            pygame.display.update()


if __name__ == "__main__":
    menu = Menu()
    nivel_seleccionado = menu.mostrar_menu()