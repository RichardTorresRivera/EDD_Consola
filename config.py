import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Directorio de assets
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")

# Directorio de images
FONDOS_DIR = os.path.join(IMAGES_DIR, "fondos")
GENERAL_DIR = os.path.join(IMAGES_DIR, "general")
MAPA_DIR = os.path.join(IMAGES_DIR, "mapa")
MENU_DIR = os.path.join(IMAGES_DIR, "menu")
TOSHI_DIR = os.path.join(IMAGES_DIR, "toshi")
NIVELES_DIR = os.path.join(IMAGES_DIR, "niveles")

# Directorio de juegos
JUEGOS_DIR = os.path.join(IMAGES_DIR, "juegos")
BUSCAMINAS_DIR = os.path.join(JUEGOS_DIR, "buscaminas")
CARTAS_DIR = os.path.join(JUEGOS_DIR, "cartas")
HANOI_DIR = os.path.join(JUEGOS_DIR, "hanoi")
LABERINTOS_DIR = os.path.join(JUEGOS_DIR, "laberintos")

#Directorio de musica
SFX_DIR = os.path.join(SOUNDS_DIR, "sound effects")
SOUNDTRACK_DIR = os.path.join(SOUNDS_DIR, "soundtrack 8-bits")


ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
FPS = 60