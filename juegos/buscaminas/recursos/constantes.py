# constantes.py
# Configuración de colores
import os
import sys
import config

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

NEGRO = (38, 32, 23)
BLANCO = (255, 255, 255)
GRIS = (200, 200, 200)
ROJO = (255, 0, 0)
MARRON_CLARO = (156, 108, 37)
MARRON = (139, 69, 19)
GOLD = (255, 201, 14)

# Colores para los números
COLORES_NUMEROS = {
    1: (255, 201, 14),
    2: (190, 149, 10),
    3: (255, 142, 85),
    4: (204, 144, 68),
    5: (255, 64, 44),
    6: (217, 54, 37),
    7: (165, 0, 255),
    8: (117, 0, 181)
}

# Configuración de pantalla
ANCHO = 1280
ALTO = 720
TAMAÑO_CELDA = 40

ruta_fuente = os.path.join(config.FONTS_DIR, "minecraft.ttf")
