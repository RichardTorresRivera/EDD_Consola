import os
import config
import pygame

def images_fondo_load():
    animation_load = []
    for i in range(6):
        img_path = os.path.join(config.TOSHI_DIR, "loading", f"load{i}.png")
        img = pygame.image.load(img_path)
        animation_load.append(img)
    return animation_load

def escalar_imagen(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    return new_image

def mostrar_indicador_mouse(buttons):
    mouse_pos = pygame.mouse.get_pos()
    if any(boton.collidepoint(mouse_pos) for boton in buttons):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

def fondo_loading(screen):
    pygame.mixer.music.stop()
    animation_load = images_fondo_load()
    for frame in animation_load:
        screen.blit(frame, (0, 0))
        pygame.display.flip()
        pygame.time.delay(500)