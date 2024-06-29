import sys
import os
import csv
import pygame
import config
from common import colores
from juegos.decisiones.recursos.arbol import ArbolBinario, Nodo
from juegos.decisiones.recursos.contenedor import Contenedor
from juegos.decisiones.recursos.decisiones import Decisiones
from juegos.decisiones.recursos import constantes

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
    fade.fill(colores.BLANCO)
    for alpha in range(0, 255, speed):
        fade.set_alpha(alpha)
        screen.fill(colores.NEGRO)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.time.delay(15)

def manejar_eventos(screen, decisiones, botones):
    for event in pygame.event.get():
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
                        transicion(screen, 5)

def actualizar(decisiones, mensaje, boton_opcion_a, boton_opcion_b):
    mensaje.actualizar(decisiones.get_msg())
    boton_opcion_a.actualizar(decisiones.get_opc_a())
    boton_opcion_b.actualizar(decisiones.get_opc_b())

def dibujar(screen, fondo, mensaje, botones):
    screen.blit(fondo, (0, 0))
    for boton in botones:
        if boton.get_texto() != "":
            boton.dibujar(screen)
    mensaje.dibujar(screen)
    mouse_pos = pygame.mouse.get_pos()
    if any(boton.forma.collidepoint(mouse_pos) for boton in botones):
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
    botones = [boton_opcion_a, boton_opcion_b]

    pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, "Toma Decisiones - Raincloud.mp3"))
    pygame.mixer.music.play(-1)
    while jugar_decisiones:
        manejar_eventos(screen, decisiones, botones)
        actualizar(decisiones, mensaje, boton_opcion_a, boton_opcion_b)
        dibujar(screen, decisiones.get_fondo(), mensaje, botones)
        if decisiones.game_over():
            jugar_decisiones = False
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            pygame.time.delay(4000)
            print("Fin del juego")
            estado[0] = config.SCREEN_MAPA
            #pygame.quit()
            #sys.exit()
        reloj.tick(config.FPS)

if __name__ == '__main__':
    main_decisiones()