import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Directorio de assets
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")
DATA_DIR = os.path.join(ASSETS_DIR, "data")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")
VIDEO_DIR = os.path.join(ASSETS_DIR, "video")

# Directorio de images
FONDOS_DIR = os.path.join(IMAGES_DIR, "fondos")
GENERAL_DIR = os.path.join(IMAGES_DIR, "general")
MAPA_DIR = os.path.join(IMAGES_DIR, "mapa")
MENU_DIR = os.path.join(IMAGES_DIR, "menu")
TOSHI_DIR = os.path.join(IMAGES_DIR, "toshi")
NIVELES_DIR = os.path.join(IMAGES_DIR, "niveles")
LIBROS_DIR = os.path.join(IMAGES_DIR, "libros_instrucciones")
ESCENARIOS_DIR = os.path.join(IMAGES_DIR, "escenarios")

# Directorio de juegos
JUEGOS_DIR = os.path.join(IMAGES_DIR, "juegos")
BUSCAMINAS_DIR = os.path.join(JUEGOS_DIR, "buscaminas")
CARTAS_DIR = os.path.join(JUEGOS_DIR, "cartas")
HANOI_DIR = os.path.join(JUEGOS_DIR, "hanoi")
LABERINTOS_DIR = os.path.join(JUEGOS_DIR, "laberintos")

JUEGOIN_DIR = os.path.join(PROJECT_DIR, "juegos")
CARTASIN_DIR = os.path.join(JUEGOIN_DIR, "cartas")

# Directorio de musica
SFX_DIR = os.path.join(SOUNDS_DIR, "sound effects")
SOUNDTRACK_DIR = os.path.join(SOUNDS_DIR, "soundtrack 8-bits")

# Pantallas
SCREEN_INICIO = 0
SCREEN_PLAY = 1
SCREEN_LEVEL = 2
SCREEN_MAPA = 3
SCREEN_GAME = 4
SCREEN_PANEL_HELP = 5
SCREEN_PANEL_CONFIG = 6
SCREEN_PANEL_EXIT = 7
SCREEN_PANEL_PAUSE = 8
SCREEN_PANEL_BOOK = 9
VOLUME_INIT = 0.5
VFX_INIT = 0.5
SLIDER_POS_INIT = 0.5

ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
FPS = 60