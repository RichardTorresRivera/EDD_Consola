import sys
import csv
import pygame
import config
from juegos.decisiones.recursos.arbol import ArbolBinario, Nodo
from juegos.decisiones.recursos.contenedor import Contenedor
from juegos.decisiones.recursos.decisiones import Decisiones
from juegos.decisiones.recursos import constantes

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((config.ANCHO_VENTANA, config.ALTO_VENTANA))
pygame.display.set_caption('Decisiones de Hanoi')
reloj = pygame.time.Clock()
FPS = 60
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

def crear_escenarios(screen, lista):
    escenarios = []
    for i in range(len(lista)):
        escena = pygame.Surface(screen.get_size())
        escena = escena.convert()
        escena.fill(lista[i])
        escenarios.append(escena)
    return escenarios

def transicion(screen, speed):
    fade = pygame.Surface(screen.get_size())
    fade.fill(constantes.BLANCO)
    for alpha in range(0, 255, speed):
        fade.set_alpha(alpha)
        screen.fill(constantes.NEGRO)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.time.delay(15)

def manejar_eventos(decisiones, botones):
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

def main_decisiones():
    COLORES = [
        (0, 255, 0),     # Verde
        (255, 0, 0),     # Rojo
        (0, 0, 255),     # Azul
        (255, 255, 0),   # Amarillo
        (255, 140, 0),   # Naranja
        (0, 255, 255),   # Cian
        (255, 0, 255),   # Magenta
        (192, 192, 192), # Gris claro
        (128, 0, 0),     # Marrón
        (128, 128, 128), # Gris
        (128, 128, 0),   # Oliva
        (0, 128, 0),     # Verde oscuro
        (128, 0, 128),   # Púrpura
        (0, 128, 128),   # Verde azulado
        (0, 0, 128)      # Azul oscuro
    ]

    jugar_decisiones = True
    # Iniciar clases
    archivo = "assets/data/data_decisiones.csv"
    escenarios = crear_escenarios(screen, COLORES)
    nodos = get_nodos(archivo, escenarios)
    arbol = ArbolBinario(nodos)
    decisiones = Decisiones(arbol.get_raiz())
    mensaje = Contenedor(constantes.POSX_MENSAJE, constantes.POSY_MENSAJE, constantes.ANCHO_MENSAJE, constantes.ALTO_MENSAJE, constantes.NEGRO, decisiones.get_msg())
    boton_opcion_a = Contenedor(150, constantes.POSY_BOTON, constantes.ANCHO_BOTON, constantes.ALTO_BOTON, constantes.NEGRO, decisiones.get_opc_a())
    boton_opcion_b = Contenedor(680, constantes.POSY_BOTON, constantes.ANCHO_BOTON, constantes.ALTO_BOTON, constantes.NEGRO, decisiones.get_opc_b())
    botones = [boton_opcion_a, boton_opcion_b]

    while jugar_decisiones:
        manejar_eventos(decisiones, botones)
        actualizar(decisiones, mensaje, boton_opcion_a, boton_opcion_b)
        dibujar(screen, decisiones.get_fondo(), mensaje, botones)
        if decisiones.game_over():
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            pygame.time.delay(4000)
            print("Fin del juego")
            jugar_decisiones = False
            pygame.quit()
            sys.exit()
        reloj.tick(FPS)

if __name__ == '__main__':
    main_decisiones()