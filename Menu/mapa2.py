import pygame
import os
import sys
import config

from menu.personaje import Personaje

# Cambiar a funciones general
def escalar_imagen(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    return new_image

def images_mapa():
    map_frames = []
    for i in range(4):
        wallpaper_path = os.path.join(config.MAPA_DIR, f"map_frame{i}.png")
        wallpaper = pygame.image.load(wallpaper_path)
        map_frames.append(wallpaper)
    return map_frames

def images_toshi_move():
    animation_move = []
    for i in range(4):
        img_path = os.path.join(config.TOSHI_DIR, "moving", f"frame{i}.png")
        img = pygame.image.load(img_path)
        img = escalar_imagen(img, 0.04)
        animation_move.append(img)
    return animation_move

def images_toshi_stop():
    animation_idle = []
    for i in range(2):
        img_path = os.path.join(config.TOSHI_DIR, "stop", f"frameS{i}.png")
        img = pygame.image.load(img_path)
        img = escalar_imagen(img, 0.04)
        animation_idle.append(img)
    return animation_idle

def images_fondo_load():
    animation_load = []
    for i in range(6):
        img_path = os.path.join(config.TOSHI_DIR, "loading", f"load{i}.png")
        img = pygame.image.load(img_path)
        animation_load.append(img)
    return animation_load

def manejar_eventos_mapa():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Click izquierdo del raton
            if event.button == 1:
                mouse_pos = event.pos
                # Boton Facil
                

def dibujar_mapa(screen, fondo, images_buttons, buttons, toshi):
    screen.blit(fondo[0], (0,0)) # es animacion
    mouse_pos = pygame.mouse.get_pos()
    for i in range(2):
        screen.blit(images_buttons[i], (1100+i*80,20))

    toshi.dibujar(screen)
    if any(boton.collidepoint(mouse_pos) for boton in buttons):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.display.flip()

def main_mapa(screen, reloj, estado, dificultad):
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    # Cargando
    pygame.mixer.music.stop()
    animation_load = images_fondo_load()
    for frame in animation_load:
        screen.blit(frame, (0, 0))
        pygame.display.flip()
        pygame.time.delay(500)
    # Ambiente
    pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Menu - Super Mario World.mp3"))
    pygame.mixer.music.play(-1)
    # Botones
    img_book_path = os.path.join(config.GENERAL_DIR, "libro.png")
    img_book = pygame.image.load(img_book_path)
    img_book = escalar_imagen(img_book, 0.08)
    help_button = pygame.Rect(1101, 20, 50, 50)

    img_config_path = os.path.join(config.GENERAL_DIR, "boton ajustes.png")
    img_config = pygame.image.load(img_config_path)
    img_config = escalar_imagen(img_config, 0.07)
    settings_button = pygame.Rect(1181, 20, 50, 50)

    images_buttons = [img_book, img_config]
    buttons_mapa = [help_button, settings_button]
    # Fondo
    mapa_fondo = images_mapa()
    # Jugador
    toshi_move = images_toshi_move()
    toshi_stop = images_toshi_stop()
    path_segments = [
            [(130, 75), (180, 75)],
            [(180, 75), (430, 75)],
            [(430, 75), (500, 75), (500, 140), (650, 140)],
            [(650, 140), (690, 140), (690, 380)],
            [(690, 380), (690, 350), (875, 350), (875, 445), (905, 445)],
            [(905, 445), (1240, 445)]
        ]
    toshi = Personaje(path_segments[0][0][0], path_segments[0][0][1], toshi_move, toshi_stop, path_segments)
    # Cards
    run_mapa = True
    while run_mapa:
        manejar_eventos_mapa()
        dibujar_mapa(screen, mapa_fondo, images_buttons, buttons_mapa, toshi)
        reloj.tick(config.FPS)