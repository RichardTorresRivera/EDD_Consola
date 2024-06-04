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


img_config_path = os.path.join(config.GENERAL_DIR,"boton ajustes.png")
img_config = pygame.image.load(img_config_path)
img_config = escalar_imagen(img_config, 0.07)

img_book_path = os.path.join(config.GENERAL_DIR,"libro.png")
img_book = pygame.image.load(img_book_path)
img_book = escalar_imagen(img_book, 0.08)

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
        reloj_personaje.tick(fps_personaje)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move_to_next_point()
                if event.key == pygame.K_LEFT:
                    player.move_to_previous_point()

        player.update()

        current_time = pygame.time.get_ticks()
        if current_time - last_map_update > map_update_interval:
            current_frame = (current_frame + 1) % len(map_frames)
            last_map_update = current_time

        screen.blit(map_frames[current_frame], (0, 0))
        screen.blit(img_config, (1180, 20))
        screen.blit(img_book, (1100, 20))
        player.dibujar(screen)

        pygame.display.update()

pygame.quit()