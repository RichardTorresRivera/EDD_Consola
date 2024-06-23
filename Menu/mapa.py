# PARA CORRER EL ARCHIVO: en la carpeta de proyecto ejecutar: py menu/mapa.py

import os
import sys
import pygame
from personaje import Personaje
from inicio import inicio
from juegos.hanoi.main import main_hanoi
from juegos.decisiones.main import main_decisiones

# Agregar el directorio del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora se puede importar config
import config

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280, 720))
run = True

show_settings = False
show_help = False
vfx_volume = 0.5
music_volume = 0.5
slider_dragging = False

map_frames = []
for i in range(4):
    wallpaper_path = os.path.join(config.MAPA_DIR, f"map_frame{i}.png")
    wallpaper = pygame.image.load(wallpaper_path)
    map_frames.append(wallpaper)

pygame.display.set_caption("Stack Adventure")


def escalar_imagen(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    return new_image


settings_button = pygame.Rect(1181, 20, 50, 50)
help_button = pygame.Rect(1101, 20, 50, 50)
vfx_slider = pygame.Rect(563, 330, 160, 16)
music_slider = pygame.Rect(563, 408, 160, 16)
ok_button = pygame.Rect(625, 558, 50, 40)
no_button = pygame.Rect(630, 460, 30, 30)
main_exit = pygame.Rect(570, 290, 160, 50)
desktop_exit = pygame.Rect(570, 375, 160, 50)
accept_button = pygame.Rect(593, 460, 30, 30)
cancel_button = pygame.Rect(658, 460, 30, 30)

animation_move = []
animation_idle = []
animation_load = []

for i in range(4):
    img_path = os.path.join(config.TOSHI_DIR, "moving", f"frame{i}.png")
    img = pygame.image.load(img_path)
    img = escalar_imagen(img, 0.04)
    animation_move.append(img)

for i in range(2):
    img_path = os.path.join(config.TOSHI_DIR, "stop", f"frameS{i}.png")
    img = pygame.image.load(img_path)
    img = escalar_imagen(img, 0.04)
    animation_idle.append(img)

for i in range(6):
    img_path = os.path.join(config.TOSHI_DIR, "loading", f"load{i}.png")
    img = pygame.image.load(img_path)
    animation_load.append(img)

# IMAGENES DE LA CONFIGURACION
img_config_path = os.path.join(config.GENERAL_DIR, "boton ajustes.png")
img_config = pygame.image.load(img_config_path)
img_config = escalar_imagen(img_config, 0.07)

img_book_path = os.path.join(config.GENERAL_DIR, "libro.png")
img_book = pygame.image.load(img_book_path)
img_book = escalar_imagen(img_book, 0.08)

img_panel_config_path = os.path.join(config.GENERAL_DIR, "panel_config.png")
img_panel_config = pygame.image.load(img_panel_config_path)

img_help_path = os.path.join(config.GENERAL_DIR, "help.png")
img_help = pygame.image.load(img_help_path)
img_help = escalar_imagen(img_help, 0.9)

img_handle_path = os.path.join(config.GENERAL_DIR, "slide_button.png")
img_handle = pygame.image.load(img_handle_path)

img_exit_path = os.path.join(config.GENERAL_DIR, "exit.png")
img_exit = pygame.image.load(img_exit_path)

# IMAGENES DE LOS NIVELES
nombres_archivos_preview = ["palabras.png", "buscaminas.png", "hanoi.png", "cartas.png", "laberinto.png",
                            "decisiones.png"]

areas_colision = [
    pygame.Rect(180, 75, 20, 20),
    pygame.Rect(430, 75, 20, 20),
    pygame.Rect(650, 140, 20, 20),
    pygame.Rect(690, 380, 20, 20),
    pygame.Rect(905, 445, 20, 20),
    pygame.Rect(1240, 445, 20, 20)
]

assert len(nombres_archivos_preview) == len(areas_colision)
preview_areas = []
level_button = []
init_game = [main_hanoi, main_decisiones, main_decisiones, main_decisiones, main_decisiones, main_decisiones]

for i in range(len(nombres_archivos_preview)):
    img_preview_path = os.path.join(config.NIVELES_DIR, nombres_archivos_preview[i])
    img_preview = pygame.image.load(img_preview_path)
    img_preview = escalar_imagen(img_preview, 1.4)
    preview_areas.append((areas_colision[i], img_preview))

level_button = pygame.Rect(158, 655, 85, 30)

preview_position = (0, 350)

path_segments = [
    [(130, 75), (180, 75)],
    [(180, 75), (430, 75)],
    [(430, 75), (500, 75), (500, 140), (650, 140)],
    [(650, 140), (690, 140), (690, 380)],
    [(690, 380), (690, 350), (875, 350), (875, 445), (905, 445)],
    [(905, 445), (1240, 445)]
]

# level_button = [pygame.Rect(158, 655, 85, 30) for area, img_preview in preview_areas]

player = Personaje(path_segments[0][0][0], path_segments[0][0][1], animation_move, animation_idle, path_segments)

current_frame = 0

reloj_personaje = pygame.time.Clock()
reloj_mapa = pygame.time.Clock()

fps_personaje = 30
fps_mapa = 3

last_map_update = pygame.time.get_ticks()
map_update_interval = 1000 // fps_mapa

original_music_volume = music_volume
original_vfx_volume = vfx_volume

mostrar_inicio = True
show_exit = False

try:
    with open(os.path.join(config.DATA_DIR, 'config_volume.txt'), 'r') as f:
        lines = f.readlines()
        for line in lines:
            key, value = line.strip().split('=')
            if key == 'music_volume':
                music_volume = float(value)
                pygame.mixer.music.set_volume(music_volume)
except FileNotFoundError:
    music_volume = 0.5
    pygame.mixer.music.set_volume(music_volume)

handle_x = 563

while run:
    if mostrar_inicio:
        pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Inicio - Barracuda.mp3"))
        pygame.mixer.music.play(-1)
        inicio()
        mostrar_inicio = False
        pygame.mixer.music.stop()
        for frame in animation_load:
            screen.blit(frame, (0, 0))
            pygame.display.update()
            pygame.time.delay(500)

        pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Menu - Super Mario World.mp3"))
        pygame.mixer.music.play(-1)
    else:
        screen.blit(map_frames[current_frame], (0, 0))
        screen.blit(img_config, (1180, 20))
        screen.blit(img_book, (1100, 20))

        reloj_personaje.tick(fps_personaje)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move_to_next_point()
                if event.key == pygame.K_LEFT:
                    player.move_to_previous_point()
                if event.key == pygame.K_ESCAPE:
                    show_exit = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if level_button.collidepoint(event.pos):
                    for i, (area, game) in enumerate(zip(areas_colision, init_game)):
                        if area.collidepoint(player.forma.topleft):
                            game()
                            break

                if settings_button.collidepoint(event.pos) and not show_help:
                    show_settings = not show_settings

                if show_settings:
                    if vfx_slider.collidepoint(event.pos):
                        slider_dragging = 'vfx'
                    elif music_slider.collidepoint(event.pos):
                        slider_dragging = 'music'

                    if accept_button.collidepoint(event.pos):
                        show_settings = False
                        with open(os.path.join(config.DATA_DIR, "config_volume.txt"), "w") as f:
                            f.write(f"music_volume={music_volume}\n")
                            handle_x = music_slider.x + int(
                                music_volume * (music_slider.width - img_handle.get_width()))
                            f.write(f"music_slider_pos={handle_x}\n")
                    elif cancel_button.collidepoint(event.pos):
                        music_volume = original_music_volume
                        pygame.mixer.music.set_volume(music_volume)
                        show_settings = False

                if help_button.collidepoint(event.pos) and not show_settings:
                    show_help = not show_help

                if show_help and ok_button.collidepoint(event.pos):
                    show_help = False

                if show_exit:
                    if main_exit.collidepoint(event.pos):
                        pygame.mixer.music.stop()
                        for frame in animation_load:
                            screen.blit(frame, (0, 0))
                            pygame.display.update()
                            pygame.time.delay(500)
                        mostrar_inicio = True
                        show_exit = False
                    elif desktop_exit.collidepoint(event.pos):
                        run = False
                    if no_button.collidepoint(event.pos):
                        show_exit = False

            if event.type == pygame.MOUSEBUTTONUP:
                slider_dragging = False

            if event.type == pygame.MOUSEMOTION and slider_dragging:
                mouse_x = event.pos[0]
                if slider_dragging == 'vfx':
                    vfx_volume = (mouse_x - vfx_slider.x) / vfx_slider.width
                    vfx_volume = max(0, min(vfx_volume, 1))
                elif slider_dragging == 'music':
                    music_volume = (mouse_x - music_slider.x) / music_slider.width
                    music_volume = max(0, min(music_volume, 1))
                    pygame.mixer.music.set_volume(music_volume)
                    handle_x = music_slider.x + int(music_volume * (music_slider.width - img_handle.get_width()))
                    with open(os.path.join(config.DATA_DIR, "config_volume.txt"), "w") as f:
                        f.write(f"music_volume={music_volume}\n")
                        f.write(f"music_slider_pos={handle_x}\n")

        current_time = pygame.time.get_ticks()
        if current_time - last_map_update > map_update_interval:
            current_frame = (current_frame + 1) % len(map_frames)
            last_map_update = current_time

        player.update()
        player.dibujar(screen)

        for area, img_preview in preview_areas:
            if area.collidepoint(player.forma.topleft):
                screen.blit(img_preview, preview_position)

        if show_settings:
            pygame.draw.rect(screen, (200, 200, 200), vfx_slider)
            pygame.draw.rect(screen, (200, 200, 200), music_slider)
            screen.blit(img_panel_config, (500, 195))

            handle_x = vfx_slider.x + int(vfx_volume * (vfx_slider.width - img_handle.get_width()))
            handle_y = vfx_slider.y + (vfx_slider.height // 2) - (img_handle.get_height() // 2)
            screen.blit(img_handle, (handle_x, handle_y))

            handle_x = music_slider.x + int(music_volume * (music_slider.width - img_handle.get_width()))
            handle_y = music_slider.y + (music_slider.height // 2) - (img_handle.get_height() // 2)
            screen.blit(img_handle, (handle_x, handle_y))
        if show_help:
            screen.blit(img_help, (400, 65))
        if show_exit:
            screen.blit(img_exit, (480, 195))

        pygame.display.update()

pygame.quit()
