import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
MAPA_DIR = os.path.join(IMAGES_DIR, "mapa")
TOSHI_DIR = os.path.join(IMAGES_DIR, "toshi")
GENERAL_DIR = os.path.join(IMAGES_DIR, "general")
MENU_DIR = os.path.join(IMAGES_DIR, "menu")


ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
FPS = 60