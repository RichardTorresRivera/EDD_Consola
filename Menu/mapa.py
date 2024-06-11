# PARA CORRER EL ARCHIVO: en la carpeta de proyecto ejecutar: py menu/mapa.py

import os
import sys
import pygame
from personaje import Personaje
from inicio import inicio

# Agregar el directorio del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora se puede importar config
import config

pygame.init()
screen = pygame.display.set_mode((1280, 720))
run = True

show_settings = False
show_help = False
vfx_volume = 0.5
music_volume = 0.5
slider_dragging = False

map_frames = []
for i in range(4):
    wallpaper_path = os.path.join(config.MAPA_DIR,f"map_frame{i}.png")
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


animation_move = []
animation_idle = []

for i in range(4):
    img_path = os.path.join(config.TOSHI_DIR,"moving",f"frame{i}.png")
    img = pygame.image.load(img_path)
    img = escalar_imagen(img, 0.04)
    animation_move.append(img)

for i in range(2):
    img_path = os.path.join(config.TOSHI_DIR,"stop",f"frameS{i}.png")
    img = pygame.image.load(img_path)
    img = escalar_imagen(img, 0.04)
    animation_idle.append(img)

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

# IMAGENES DE LOS NIVELES

img_palabras_path = os.path.join(config.NIVELES_DIR, "palabras.png")
img_palabras = pygame.image.load(img_palabras_path)
img_palabras = escalar_imagen(img_palabras, 1.2)

preview_areas = [
    pygame.Rect(180, 75, 50, 50)
]

path_segments = [
    [(130, 75), (180, 75)],
    [(180, 75), (430, 75)],
    [(430, 75), (500, 75), (500, 140), (650, 140)],
    [(650, 140), (690, 140), (690, 380)],
    [(690, 380), (690, 350), (875, 350), (875, 445), (905, 445)],
    [(905, 445), (1240, 445)]
]

player = Personaje(path_segments[0][0][0], path_segments[0][0][1], animation_move, animation_idle, path_segments)

current_frame = 0

reloj_personaje = pygame.time.Clock()
reloj_mapa = pygame.time.Clock()

fps_personaje = 30
fps_mapa = 3

last_map_update = pygame.time.get_ticks()
map_update_interval = 1000 // fps_mapa

mostrar_inicio = True

while run:
    if mostrar_inicio:
        inicio()
        mostrar_inicio = False
    else:
        screen.blit(map_frames[current_frame], (0, 0))
        screen.blit(img_config, (1180, 20))
        screen.blit(img_book, (1100, 20))

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

        reloj_personaje.tick(fps_personaje)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move_to_next_point()
                if event.key == pygame.K_LEFT:
                    player.move_to_previous_point()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings_button.collidepoint(event.pos) and not show_help:
                    show_settings = not show_settings

                if show_settings:
                    if vfx_slider.collidepoint(event.pos):
                        slider_dragging = 'vfx'
                    elif music_slider.collidepoint(event.pos):
                        slider_dragging = 'music'

                if help_button.collidepoint(event.pos) and not show_settings:
                    show_help = not show_help

                if show_help and ok_button.collidepoint(event.pos):
                    show_help = False

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

        current_time = pygame.time.get_ticks()
        if current_time - last_map_update > map_update_interval:
            current_frame = (current_frame + 1) % len(map_frames)
            last_map_update = current_time

        player.update()
        player.dibujar(screen)

        for area in preview_areas:
            if area.collidepoint(player.forma.topleft):
                screen.blit(img_palabras, (area.x - 180, area.y + 310))

        pygame.display.update()

pygame.quit()
