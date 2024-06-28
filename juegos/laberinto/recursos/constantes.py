import os
import sys
import config

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Configuración de colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
VERDE_O = (24, 51, 11)
VERDE_P = (89, 117, 44)

# Configuración de pantalla
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720

# Tamaño de celda
TAMAÑO_CELDA = 40

# Fuente
ruta_fuente = os.path.join(config.FONTS_DIR, "minecraft.ttf")