import pygame
import os
import config

from common.utils import mostrar_indicador_mouse

pygame.mixer.init()

def cargar_estado():
    estado = [config.SCREEN_PANEL_CONFIG, config.VOLUME_INIT, config.VFX_INIT, False,
              config.VOLUME_INIT, config.VFX_INIT, config.SLIDER_POS_INIT, config.SLIDER_POS_INIT]
    try:
        with open(os.path.join(config.DATA_DIR, "config_volume.txt"), "r") as file:
            for line in file:
                name, value = line.strip().split("=")
                if name == "volumen":
                    estado[1] = float(value)
                    estado[4] = estado[1]
                    pygame.mixer.music.set_volume(estado[1])
                elif name == "vfx":
                    estado[2] = float(value)
                    estado[5] = estado[2]
                elif name == "slider_volumen_pos":
                    estado[6] = float(value)
                elif name == "slider_vfx_pos":
                    estado[7] = float(value)
    except FileNotFoundError:
        print("No se encontró archivo de configuración")
        pass
    return estado

estado = cargar_estado()

def manejar_eventos_panel_config(estado, buttons, sliders):
    volumen_original = estado[4]
    vfx_original = estado[5]
    slider_volumen_original = estado[6]
    slider_vfx_original = estado[7]

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Saliendo del panel de configuración")
                estado[0] = config.SCREEN_MAPA
                estado[1] = volumen_original
                estado[2] = vfx_original
                estado[6] = slider_volumen_original
                estado[7] = slider_vfx_original
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                if buttons[0].collidepoint(mouse_pos):
                    print("Nuevos ajustes")
                    estado[0] = config.SCREEN_MAPA
                    with open(os.path.join(config.DATA_DIR, "config_volume.txt"), "w") as file:
                        file.write(f"volumen={estado[1]}\n")
                        file.write(f"vfx={estado[2]}\n")
                        file.write(f"slider_volumen_pos={estado[6]}\n")
                        file.write(f"slider_vfx_pos={estado[7]}\n")
                elif buttons[1].collidepoint(mouse_pos):
                    print("Cancelando configuración")
                    estado[0] = config.SCREEN_MAPA
                    estado[1] = volumen_original
                    estado[2] = vfx_original
                    estado[6] = slider_volumen_original
                    estado[7] = slider_vfx_original
                    pygame.mixer.music.set_volume(0.5)
                elif sliders[0].collidepoint(mouse_pos):
                    print("Cambiando volumen")
                    estado[3] = 'volumen'
                elif sliders[1].collidepoint(mouse_pos):
                    print("Cambiando vfx")
                    estado[3] = 'vfx'
        elif event.type == pygame.MOUSEBUTTONUP:
            estado[3] = False
        elif event.type == pygame.MOUSEMOTION and estado[3]:
            mouse_x = event.pos[0]
            if estado[3] == 'volumen':
                estado[1] = (mouse_x - sliders[0].x) / sliders[0].width
                estado[1] = max(0, min(estado[1], 1))
                estado[6] = estado[1]
                pygame.mixer.music.set_volume(estado[1])
            elif estado[3] == 'vfx':
                estado[2] = (mouse_x - sliders[1].x) / sliders[1].width
                estado[2] = max(0, min(estado[2], 1))
                estado[7] = estado[2]

def actualizar_panel_config():
    pass

def dibujar_panel_config(screen, img_config, sliders, img_handle, estado):
    pygame.draw.rect(screen, (200, 200, 200), sliders[0])
    pygame.draw.rect(screen, (200, 200, 200), sliders[1])
    #img_rect = pygame.Rect(500, 195, img_config.get_width(), img_config.get_height())
    screen.blit(img_config, (500, 195))

    handle_x = sliders[0].x + int(estado[1] * (sliders[0].width - img_handle.get_width()))
    handle_y = sliders[0].y + (sliders[0].height - img_handle.get_height()) // 2
    screen.blit(img_handle, (handle_x, handle_y))

    handle_x = sliders[1].x + int(estado[2] * (sliders[1].width - img_handle.get_width()))
    handle_y = sliders[1].y + (sliders[1].height - img_handle.get_height()) // 2
    screen.blit(img_handle, (handle_x, handle_y))
    #pygame.display.update(img_rect)
    pygame.display.flip()

def main_panel_config(screen, reloj, estado):
    button_aceptar = pygame.Rect(593, 460, 30, 30)
    button_cancel = pygame.Rect(658, 460, 30, 30)
    buttons_panel_config = [button_aceptar, button_cancel]

    slider_volumen = pygame.Rect(563, 408, 160, 16)
    slider_vfx = pygame.Rect(563, 330, 160, 16)
    slider_panel_config = [slider_volumen, slider_vfx]

    img_config_path = os.path.join(config.GENERAL_DIR, "panel_config.png")
    img_config = pygame.image.load(img_config_path)
    img_handle_path = os.path.join(config.GENERAL_DIR, "slide_button.png")
    img_handle = pygame.image.load(img_handle_path)

    run_panel_config = True
    while run_panel_config:
        if estado[0] == config.SCREEN_PANEL_CONFIG:
            manejar_eventos_panel_config(estado, buttons_panel_config, slider_panel_config)
            mostrar_indicador_mouse(buttons_panel_config)
            actualizar_panel_config()
            dibujar_panel_config(screen, img_config, slider_panel_config, img_handle, estado)
        elif estado[0] == config.SCREEN_MAPA:
            run_panel_config = False
        reloj.tick(config.FPS)
