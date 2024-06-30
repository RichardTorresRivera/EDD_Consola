import sys
import os
import csv
import pygame
import config
from Menu.paneles.panel_pause import main_panel_pause
from Menu.paneles.panel_book import main_panel_book
from common.colores import *
from common.utils import mensaje_final
from common.music_config import cargar_configuracion, cargar_vfx
from juegos.decisiones.recursos.arbol import ArbolBinario, Nodo
from juegos.decisiones.recursos.contenedor import Contenedor
from juegos.decisiones.recursos.decisiones import Decisiones
from juegos.decisiones.recursos import constantes
from common.pause_button import cargar_boton_pausa, dibujar_boton_pausa, manejar_eventos_boton_pausa
from common.help_button import cargar_boton_help, dibujar_boton_help, manejar_eventos_boton_help

# Inicialización de Pygame
#pygame.init()
#screen = pygame.display.set_mode((config.ANCHO_VENTANA, config.ALTO_VENTANA))
#pygame.display.set_caption('Decisiones de Hanoi')
#reloj = pygame.time.Clock()
#FPS = 60
# Fin de inicialización

def get_nodos(nombre_archivo, escenarios):
        lista = []
        i = 0
        with open(nombre_archivo, mode = 'r', newline='') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                lista.append({
                    "img": escenarios[i],
                    "msg": fila["msg"],
                    "opc_a": fila["opc_a"],
                    "opc_b": fila["opc_b"]
                })
                i += 1
        nodos = [Nodo(**item) for item in lista]

        return nodos

def crear_escenarios(lista_imagenes):
    escenarios = []
    for archivo in lista_imagenes:
        img = pygame.image.load(os.path.join(config.ESCENARIOS_DIR) + "\\" + archivo).convert()
        escenarios.append(img)
    return escenarios

def transicion(screen, speed):
    fade = pygame.Surface(screen.get_size())
    fade.fill(BLANCO)
    for alpha in range(0, 255, speed):
        fade.set_alpha(alpha)
        screen.fill(NEGRO)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.time.delay(15)

def manejar_eventos(screen, decisiones, botones, sound, estado, button_pause_rect, button_book_rect):
    for event in pygame.event.get():
        manejar_eventos_boton_pausa(event, estado, button_pause_rect)
        manejar_eventos_boton_help(event, estado, button_book_rect)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                for boton in botones:
                    if boton.forma.collidepoint(mouse_pos):
                        if boton.texto == decisiones.get_opc_a():
                            decisiones.opc_a()
                        else:
                            decisiones.opc_b()
                        sound.play()
                        transicion(screen, 5)

def actualizar(decisiones, mensaje, boton_opcion_a, boton_opcion_b):
    mensaje.actualizar(decisiones.get_msg())
    boton_opcion_a.actualizar(decisiones.get_opc_a())
    boton_opcion_b.actualizar(decisiones.get_opc_b())

def dibujar(screen, fondo, mensaje, botones, img_boton_pausa, boton_pausa, img_boton_help, boton_book):
    screen.blit(fondo, (0, 0))
    for boton in botones:
        if boton.get_texto() != "":
            boton.dibujar(screen)
    mensaje.dibujar(screen)
    dibujar_boton_pausa(screen, img_boton_pausa)
    dibujar_boton_help(screen, img_boton_help)
    mouse_pos = pygame.mouse.get_pos()
    if any(boton.forma.collidepoint(mouse_pos) for boton in botones):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif boton_pausa.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif boton_book.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.display.flip()

def main_decisiones(screen, reloj, estado, dificultad):
    nombre_escenarios = []
    for i in range(15):
        nombre_escenarios.append("escenario"+str(i+1)+".png")

    jugar_decisiones = True
    # Iniciar clases
    archivo = os.path.join(config.DATA_DIR, "data_decisiones.csv")
    escenarios = crear_escenarios(nombre_escenarios)
    nodos = get_nodos(archivo, escenarios)
    arbol = ArbolBinario(nodos)
    decisiones = Decisiones(arbol.get_raiz())
    mensaje = Contenedor(constantes.POSX_MENSAJE, constantes.POSY_MENSAJE, constantes.ANCHO_MENSAJE, constantes.ALTO_MENSAJE, constantes.CR_MSG, decisiones.get_msg())
    boton_opcion_a = Contenedor(150, constantes.POSY_BOTON, constantes.ANCHO_BOTON, constantes.ALTO_BOTON, constantes.CR_OPC_A, decisiones.get_opc_a())
    boton_opcion_b = Contenedor(680, constantes.POSY_BOTON, constantes.ANCHO_BOTON, constantes.ALTO_BOTON, constantes.CR_OPC_B, decisiones.get_opc_b())
    # Ambiente
    cargar_configuracion(estado)
    sound_click = cargar_vfx("Decisiones - Click.mp3", estado)

    pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Toma Decisiones - Raincloud.mp3"))
    pygame.mixer.music.play(-1)

    fuente = pygame.font.Font(os.path.join(config.FONTS_DIR, "minecraft.ttf"), 45)
    img_boton_pausa, button_pause_rect = cargar_boton_pausa()
    img_boton_book, button_book_rect = cargar_boton_help()
    # Lista de botones
    botones = [boton_opcion_a, boton_opcion_b]
    while jugar_decisiones:
        if estado[0] == config.SCREEN_GAME:
            manejar_eventos(screen, decisiones, botones, sound_click, estado, button_pause_rect, button_book_rect)
            actualizar(decisiones, mensaje, boton_opcion_a, boton_opcion_b)
            dibujar(screen, decisiones.get_fondo(), mensaje, botones, img_boton_pausa, button_pause_rect, img_boton_book, button_book_rect)
            if decisiones.game_over():
                jugar_decisiones = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                pygame.time.delay(3000)
                mensaje_final(screen, "Felicidades, diste fin a la aventura", GOLD, reloj, fuente)
                estado[0] = config.SCREEN_MAPA
                estado[8].add("decisiones")
                #pygame.quit()
                #sys.exit()
        elif estado[0] == config.SCREEN_PANEL_PAUSE:
            main_panel_pause(screen, reloj, estado)
        elif estado[0] == config.SCREEN_PANEL_BOOK:
            main_panel_book(screen, reloj, estado)
        elif estado[0] == config.SCREEN_MAPA:
            jugar_decisiones = False
        reloj.tick(config.FPS)

if __name__ == '__main__':
    main_decisiones()