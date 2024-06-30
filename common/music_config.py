import os
import pygame
import config

vfx_sounds = []

def cargar_vfx(nombre_archivo, estado):
    sonido = pygame.mixer.Sound(os.path.join(config.SFX_DIR, nombre_archivo))
    sonido.set_volume(estado[2])
    vfx_sounds.append(sonido)
    return sonido

def cargar_configuracion(estado):
    with open(os.path.join(config.DATA_DIR, "config_volume.txt"), "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            if key == "volumen":
                estado[1] = float(value)
            elif key == "vfx":
                estado[2] = float(value)
    pygame.mixer.music.set_volume(estado[1])
    for sonido in vfx_sounds:
        sonido.set_volume(estado[2])