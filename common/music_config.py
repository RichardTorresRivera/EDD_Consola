import os
import pygame
import config

def cargar_configuracion(estado):
    with open(os.path.join(config.DATA_DIR, "config_volume.txt"), "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            if key == "volumen":
                estado[1] = float(value)
            elif key == "vfx":
                estado[2] = float(value)
    pygame.mixer.music.set_volume(estado[1])
    # Logica de vfx