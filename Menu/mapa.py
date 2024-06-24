import os
import sys
import pygame
from personaje import Personaje
from juegos.hanoi.main import main_hanoi
from juegos.decisiones.main import main_decisiones

# Agregar el directorio del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora se puede importar config
import config

class Juego:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Stack Adventure")

        self.run = True
        self.show_settings = False
        self.show_help = False
        self.vfx_volume = 0.5
        self.music_volume = 0.5
        self.slider_dragging = False

        self.map_frames = []
        for i in range(4):
            wallpaper_path = os.path.join(config.MAPA_DIR, f"map_frame{i}.png")
            wallpaper = pygame.image.load(wallpaper_path)
            self.map_frames.append(wallpaper)

        self.settings_button = pygame.Rect(1181, 20, 50, 50)
        self.help_button = pygame.Rect(1101, 20, 50, 50)
        self.vfx_slider = pygame.Rect(563, 330, 160, 16)
        self.music_slider = pygame.Rect(563, 408, 160, 16)
        self.ok_button = pygame.Rect(625, 558, 50, 40)
        self.no_button = pygame.Rect(630, 460, 30, 30)
        self.main_exit = pygame.Rect(570, 290, 160, 50)
        self.desktop_exit = pygame.Rect(570, 375, 160, 50)
        self.accept_button = pygame.Rect(593, 460, 30, 30)
        self.cancel_button = pygame.Rect(658, 460, 30, 30)

        self.animation_move = []
        self.animation_idle = []
        self.animation_load = []

        for i in range(4):
            img_path = os.path.join(config.TOSHI_DIR, "moving", f"frame{i}.png")
            img = pygame.image.load(img_path)
            img = self.escalar_imagen(img, 0.04)
            self.animation_move.append(img)

        for i in range(2):
            img_path = os.path.join(config.TOSHI_DIR, "stop", f"frameS{i}.png")
            img = pygame.image.load(img_path)
            img = self.escalar_imagen(img, 0.04)
            self.animation_idle.append(img)

        for i in range(6):
            img_path = os.path.join(config.TOSHI_DIR, "loading", f"load{i}.png")
            img = pygame.image.load(img_path)
            self.animation_load.append(img)

        # IMAGENES DE LA CONFIGURACION
        img_config_path = os.path.join(config.GENERAL_DIR, "boton ajustes.png")
        self.img_config = pygame.image.load(img_config_path)
        self.img_config = self.escalar_imagen(self.img_config, 0.07)

        img_book_path = os.path.join(config.GENERAL_DIR, "libro.png")
        self.img_book = pygame.image.load(img_book_path)
        self.img_book = self.escalar_imagen(self.img_book, 0.08)

        img_panel_config_path = os.path.join(config.GENERAL_DIR, "panel_config.png")
        self.img_panel_config = pygame.image.load(img_panel_config_path)

        img_help_path = os.path.join(config.GENERAL_DIR, "help.png")
        self.img_help = pygame.image.load(img_help_path)
        self.img_help = self.escalar_imagen(self.img_help, 0.9)

        img_handle_path = os.path.join(config.GENERAL_DIR, "slide_button.png")
        self.img_handle = pygame.image.load(img_handle_path)

        img_exit_path = os.path.join(config.GENERAL_DIR, "exit.png")
        self.img_exit = pygame.image.load(img_exit_path)

        # IMAGENES DE LOS NIVELES
        nombres_archivos_preview = ["palabras.png", "buscaminas.png", "hanoi.png", "cartas.png", "laberinto.png",
                                    "decisiones.png"]

        self.areas_colision = [
            pygame.Rect(180, 75, 20, 20),
            pygame.Rect(430, 75, 20, 20),
            pygame.Rect(650, 140, 20, 20),
            pygame.Rect(690, 380, 20, 20),
            pygame.Rect(905, 445, 20, 20),
            pygame.Rect(1240, 445, 20, 20)
        ]

        assert len(nombres_archivos_preview) == len(self.areas_colision)
        self.preview_areas = []
        self.level_button = []
        self.init_game = [main_hanoi, main_decisiones, main_decisiones, main_decisiones, main_decisiones, main_decisiones]

        for i in range(len(nombres_archivos_preview)):
            img_preview_path = os.path.join(config.NIVELES_DIR, nombres_archivos_preview[i])
            img_preview = pygame.image.load(img_preview_path)
            img_preview = self.escalar_imagen(img_preview, 1.4)
            self.preview_areas.append((self.areas_colision[i], img_preview))

        self.level_button = pygame.Rect(158, 655, 85, 30)

        self.preview_position = (0, 350)

        path_segments = [
            [(130, 75), (180, 75)],
            [(180, 75), (430, 75)],
            [(430, 75), (500, 75), (500, 140), (650, 140)],
            [(650, 140), (690, 140), (690, 380)],
            [(690, 380), (690, 350), (875, 350), (875, 445), (905, 445)],
            [(905, 445), (1240, 445)]
        ]

        self.player = Personaje(path_segments[0][0][0], path_segments[0][0][1], self.animation_move, self.animation_idle, path_segments)

        self.current_frame = 0

        self.reloj_personaje = pygame.time.Clock()
        self.reloj_mapa = pygame.time.Clock()

        self.fps_personaje = 30
        self.fps_mapa = 3

        self.last_map_update = pygame.time.get_ticks()
        self.map_update_interval = 1000 // self.fps_mapa

        self.original_music_volume = self.music_volume
        self.original_vfx_volume = self.vfx_volume

        self.mostrar_inicio = True
        self.show_exit = False

        try:
            with open(os.path.join(config.DATA_DIR, 'config_volume.txt'), 'r') as f:
                lines = f.readlines()
                for line in lines:
                    key, value = line.strip().split('=')
                    if key == 'music_volume':
                        self.music_volume = float(value)
                        pygame.mixer.music.set_volume(self.music_volume)
        except FileNotFoundError:
            self.music_volume = 0.5
            pygame.mixer.music.set_volume(self.music_volume)

        self.handle_x = 563

    def escalar_imagen(self, image, scale):
        w = image.get_width()
        h = image.get_height()
        new_image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
        return new_image

    def mapa(self):
        while self.run:
            if self.mostrar_inicio:
                self.mostrar_inicio = False
                pygame.mixer.music.stop()
                for frame in self.animation_load:
                    self.screen.blit(frame, (0, 0))
                    pygame.display.update()
                    pygame.time.delay(500)

                pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Menu - Super Mario World.mp3"))
                pygame.mixer.music.play(-1)
            else:
                self.screen.blit(self.map_frames[self.current_frame], (0, 0))
                self.screen.blit(self.img_config, (1180, 20))
                self.screen.blit(self.img_book, (1100, 20))

                self.reloj_personaje.tick(self.fps_personaje)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            self.player.move_to_next_point()
                        if event.key == pygame.K_LEFT:
                            self.player.move_to_previous_point()
                        if event.key == pygame.K_ESCAPE:
                            self.show_exit = True

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.level_button.collidepoint(event.pos):
                            for i, (area, game) in enumerate(zip(self.areas_colision, self.init_game)):
                                if area.collidepoint(self.player.forma.topleft):
                                    game()
                                    break

                        if self.settings_button.collidepoint(event.pos) and not self.show_help:
                            self.show_settings = not self.show_settings

                        if self.show_settings:
                            if self.vfx_slider.collidepoint(event.pos):
                                self.slider_dragging = 'vfx'
                            elif self.music_slider.collidepoint(event.pos):
                                self.slider_dragging = 'music'

                            if self.accept_button.collidepoint(event.pos):
                                self.show_settings = False
                                with open(os.path.join(config.DATA_DIR, "config_volume.txt"), "w") as f:
                                    f.write(f"music_volume={self.music_volume}\n")
                                    self.handle_x = self.music_slider.x + int(
                                        self.music_volume * (self.music_slider.width - self.img_handle.get_width()))
                                    f.write(f"music_slider_pos={self.handle_x}\n")
                            elif self.cancel_button.collidepoint(event.pos):
                                self.music_volume = self.original_music_volume
                                pygame.mixer.music.set_volume(self.music_volume)
                                self.show_settings = False

                        if self.help_button.collidepoint(event.pos) and not self.show_settings:
                            self.show_help = not self.show_help

                        if self.show_help and self.ok_button.collidepoint(event.pos):
                            self.show_help = False

                        if self.show_exit:
                            if self.main_exit.collidepoint(event.pos):
                                pygame.mixer.music.stop()
                                for frame in self.animation_load:
                                    self.screen.blit(frame, (0, 0))
                                    pygame.display.update()
                                    pygame.time.delay(500)
                                self.mostrar_inicio = True
                                self.show_exit = False
                            elif self.desktop_exit.collidepoint(event.pos):
                                self.run = False
                            if self.no_button.collidepoint(event.pos):
                                self.show_exit = False

                    if event.type == pygame.MOUSEBUTTONUP:
                        self.slider_dragging = False

                    if event.type == pygame.MOUSEMOTION and self.slider_dragging:
                        mouse_x = event.pos[0]
                        if self.slider_dragging == 'vfx':
                            self.vfx_volume = (mouse_x - self.vfx_slider.x) / self.vfx_slider.width
                            self.vfx_volume = max(0, min(self.vfx_volume, 1))
                        elif self.slider_dragging == 'music':
                            self.music_volume = (mouse_x - self.music_slider.x) / self.music_slider.width
                            self.music_volume = max(0, min(self.music_volume, 1))
                            pygame.mixer.music.set_volume(self.music_volume)
                            self.handle_x = self.music_slider.x + int(self.music_volume * (self.music_slider.width - self.img_handle.get_width()))
                            with open(os.path.join(config.DATA_DIR, "config_volume.txt"), "w") as f:
                                f.write(f"music_volume={self.music_volume}\n")
                                f.write(f"music_slider_pos={self.handle_x}\n")

                current_time = pygame.time.get_ticks()
                if current_time - self.last_map_update > self.map_update_interval:
                    self.current_frame = (self.current_frame + 1) % len(self.map_frames)
                    self.last_map_update = current_time

                self.player.update()
                self.player.dibujar(self.screen)

                for area, img_preview in self.preview_areas:
                    if area.collidepoint(self.player.forma.topleft):
                        self.screen.blit(img_preview, self.preview_position)

                if self.show_settings:
                    pygame.draw.rect(self.screen, (200, 200, 200), self.vfx_slider)
                    pygame.draw.rect(self.screen, (200, 200, 200), self.music_slider)
                    self.screen.blit(self.img_panel_config, (500, 195))

                    handle_x = self.vfx_slider.x + int(self.vfx_volume * (self.vfx_slider.width - self.img_handle.get_width()))
                    handle_y = self.vfx_slider.y + (self.vfx_slider.height // 2) - (self.img_handle.get_height() // 2)
                    self.screen.blit(self.img_handle, (handle_x, handle_y))

                    handle_x = self.music_slider.x + int(self.music_volume * (self.music_slider.width - self.img_handle.get_width()))
                    handle_y = self.music_slider.y + (self.music_slider.height // 2) - (self.img_handle.get_height() // 2)
                    self.screen.blit(self.img_handle, (handle_x, handle_y))
                if self.show_help:
                    self.screen.blit(self.img_help, (400, 65))
                if self.show_exit:
                    self.screen.blit(self.img_exit, (480, 195))

                pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    juego = Juego()
    juego.mapa()
