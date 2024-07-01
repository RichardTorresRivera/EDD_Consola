import pygame
import os
import sys
import config
from common.music_config import cargar_configuracion
from common.utils import escalar_imagen, mostrar_indicador_mouse, fondo_loading, historia_loading
from juegos.buscaminas.main import main_buscaminas
from juegos.hanoi.main import main_hanoi
from juegos.laberinto.main import main_lab
from juegos.decisiones.main import main_decisiones
from Menu.paneles.panel_config import main_panel_config
from Menu.paneles.panel_exit import main_panel_exit
from Menu.paneles.panel_help import main_panel_help
from Menu.personaje import Personaje
from juegos.cartas.main import main_cartas
num_game = [0]

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

def images_previews_game(nombres, areas):
    images_areas_game = []
    for i in range(len(nombres)):
            img_preview_path = os.path.join(config.NIVELES_DIR, nombres[i])
            img_preview = pygame.image.load(img_preview_path)
            img_preview = escalar_imagen(img_preview, 1.4)
            images_areas_game.append((areas[i], img_preview))
    return images_areas_game

def manejar_eventos_mapa(estado, buttons, toshi, areas_colision, num_game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Click izquierdo del raton
            if event.button == 1:
                mouse_pos = event.pos
                # Boton libro
                if buttons[0].collidepoint(mouse_pos):
                    print("mostrando libro")
                    estado[0] = config.SCREEN_PANEL_HELP
                # Boton ajustes
                elif buttons[1].collidepoint(mouse_pos):
                    print("Mostrando ajustes")
                    estado[0] = config.SCREEN_PANEL_CONFIG
                # Boton level
                elif buttons[2].collidepoint(mouse_pos):
                    print("Boton jugar apretado")
                    i = 0
                    for area in (areas_colision):
                        if area.collidepoint(toshi.forma.topleft):
                            num_game[0] = i
                            estado[0] = config.SCREEN_GAME
                            estado[9] = i
                            break
                        i += 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                toshi.move_to_next_point()
            elif event.key == pygame.K_LEFT:
                toshi.move_to_previous_point()
            elif event.key == pygame.K_h:
                print("mostrando libro")
                estado[0] = config.SCREEN_PANEL_HELP
            elif event.key == pygame.K_s:
                print("Mostrando ajustes")
                estado[0] = config.SCREEN_PANEL_CONFIG
            elif event.key == pygame.K_ESCAPE:
                print("mostrando salir")
                estado[0] = config.SCREEN_PANEL_EXIT
            elif event.key == pygame.K_RETURN:
                i = 0
                for area in (areas_colision):
                    if area.collidepoint(toshi.forma.topleft):
                        num_game[0] = i
                        estado[0] = config.SCREEN_GAME
                        estado[9] = i
                        break
                    i += 1
            # Manejo de teclas 1 a 6
            elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6]:
                keys_to_indices = {
                    pygame.K_1: 0,
                    pygame.K_2: 1,
                    pygame.K_3: 2,
                    pygame.K_4: 3,
                    pygame.K_5: 4,
                    pygame.K_6: 5
                }
                index = keys_to_indices[event.key]
                if index < len(areas_colision):
                    target_x, target_y = areas_colision[index].topleft
                    toshi.mover_a_punto(target_x, target_y)


def actualizar_mapa(toshi):
    toshi.update()

def dibujar_mapa(screen, fondo, images_buttons, toshi, current_frame, preview_areas, buttons_mapa):
    screen.blit(fondo[current_frame], (0,0))
    for i in range(2):
        screen.blit(images_buttons[i], (1100+i*80,20))
    toshi.dibujar(screen)
    level_button = pygame.Rect(-1, -1, 85, 30)
    buttons_mapa[2] = level_button
    for area, img_preview in preview_areas:
        if area.collidepoint(toshi.forma.topleft):
            screen.blit(img_preview, (0,350))
            level_button = pygame.Rect(158, 655, 85, 30)
            buttons_mapa[2] = level_button
    pygame.display.flip()

def main_mapa(screen, reloj, estado, dificultad):
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    # Cargando
    fondo_loading(screen)
    ruta_video = "prueba.mp4"
    historia_loading(screen, ruta_video, reloj)
    fondo_loading(screen)
    # Ambiente
    pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Menu - Super Mario World.mp3"))
    pygame.mixer.music.play(-1)
    # Seccion de mostrar imagenes previas
    level_button = pygame.Rect(-1, -1, 85, 30)
    # Areas de colison jugar
    areas_colision = [
        pygame.Rect(180, 75, 20, 20),
        pygame.Rect(430, 75, 20, 20),
        pygame.Rect(650, 140, 20, 20),
        pygame.Rect(690, 380, 20, 20),
        pygame.Rect(905, 445, 20, 20),
        pygame.Rect(1240, 445, 20, 20)
    ]


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
    buttons_mapa = [help_button, settings_button, level_button]
    # Fondo
    current_frame = 0
    frame_time = 0
    frame_interval = 200
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
    # Juegos
    init_game = [main_hanoi, main_buscaminas, main_hanoi,main_cartas, main_hanoi, main_lab, main_decisiones]
    
    run_mapa = True
    while run_mapa:
        # Imagenes previas
        nombres_archivos_preview = ["palabras", "buscaminas", "hanoi", "cartas", "laberinto", "decisiones"]
        nombres_niveles = []
        for nivel in nombres_archivos_preview:
            if nivel in estado[8]:
                nombres_niveles.append(f'{nivel}_completo.png')
            else:
                nombres_niveles.append(f'{nivel}_incompleto.png')
        preview_areas = images_previews_game(nombres_niveles, areas_colision)

        if estado[0] == config.SCREEN_MAPA:
            manejar_eventos_mapa(estado, buttons_mapa, toshi, areas_colision, num_game)
            mostrar_indicador_mouse(buttons_mapa)
            actualizar_mapa(toshi)
            # Actualizar frame
            frame_time += reloj.get_time()
            if frame_time >= frame_interval:
                current_frame = (current_frame + 1) % len(mapa_fondo)
                frame_time = 0
            dibujar_mapa(screen, mapa_fondo, images_buttons, toshi, current_frame, preview_areas, buttons_mapa)
        elif estado[0] == config.SCREEN_PANEL_EXIT:
            main_panel_exit(screen, reloj, estado)
        elif estado[0] == config.SCREEN_PANEL_HELP:
            main_panel_help(screen, reloj, estado)
        elif estado[0] == config.SCREEN_PANEL_CONFIG:
            main_panel_config(screen, reloj, estado)
        elif estado[0] == config.SCREEN_INICIO:
            run_mapa = False
        elif estado[0] == config.SCREEN_GAME:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            fondo_loading(screen)
            cargar_configuracion(estado)
            init_game[num_game[0]](screen, reloj, estado, dificultad)
            fondo_loading(screen)
            cargar_configuracion(estado)
            pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Menu - Super Mario World.mp3"))
            pygame.mixer.music.play(-1)
        reloj.tick(config.FPS)