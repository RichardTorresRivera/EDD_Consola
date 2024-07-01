import pygame
import random
import sys
import os
import config
from common.utils import mensaje_final

# Inicialización de Pygame
pygame.init()

# Definición de las Listas Enlazadas
class Nodo:
    def __init__(self, valor, imagen):
        self.valor = valor
        self.imagen = imagen
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor, imagen):
        if not self.cabeza:
            self.cabeza = Nodo(valor, imagen)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(valor, imagen)

    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual)
            actual = actual.siguiente
        return elementos

    def ordenar(self):
        if not self.cabeza or not self.cabeza.siguiente:
            return

        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            while siguiente:
                if actual.valor > siguiente.valor:
                    actual.valor, siguiente.valor = siguiente.valor, actual.valor
                    actual.imagen, siguiente.imagen = siguiente.imagen, actual.imagen
                siguiente = siguiente.siguiente
            actual = actual.siguiente

# Funciones del Juego
def crear_cartas(nivel):
    cartas_info = [
        [("Semilla", "Semilla.png"), ("Planta", "Planta.png"), ("Flor", "Flor.png")],
        [("Nube", "Nube.png"), ("Relámpago", "Relámpago.png"), ("Lluvia", "Lluvia.png"), ("Sol", "Sol.png"), ("Arcoíris", "Arcoiris.png")],
        [("Héroe", "Héroe.png"), ("Casa", "Casa.png"), ("Brujo", "Brujo.png"), ("Pregunta", "Pregunta.png"), ("Check", "Check.png"), ("Llave", "Llave.png"), ("Puerta", "Puerta.png")]
    ]
    cartas = cartas_info[nivel[0] - 1]  # Ajuste aquí para usar nivel-1 como índice
    random.shuffle(cartas)
    lista_enlazada = ListaEnlazada()
    for valor, imagen in cartas:
        lista_enlazada.agregar(valor, imagen)

    return lista_enlazada

def mostrar_mensaje_pantalla(screen, font, mensaje, color, y_offset):
    texto = font.render(mensaje, True, color)
    text_rect = texto.get_rect(center=(screen.get_width() // 2, y_offset))
    screen.blit(texto, text_rect)

def esperar_enter():
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    esperando = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def manejar_eventos(cartas, mouse_pos, dragging, selected_card):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for carta in cartas:
                if carta["rect"].collidepoint(mouse_pos):
                    dragging = True
                    selected_card = carta
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            selected_card = None
        elif event.type == pygame.MOUSEMOTION and dragging:
            selected_card["rect"].center = event.pos

    return dragging, selected_card

def verificar_orden(cartas, nivel):
    orden_correcto = [
        ["Semilla", "Planta", "Flor"],
        ["Nube", "Relámpago", "Lluvia", "Sol", "Arcoíris"],
        ["Héroe", "Casa", "Brujo", "Pregunta", "Check", "Llave", "Puerta"]
    ]
    for i, carta in enumerate(cartas):
        if carta["valor"] != orden_correcto[nivel[0] - 1][i]:  # Ajuste aquí para usar nivel-1 como índice
            return False
    return True

def jugar_nivel(screen, font, nivel, fondo_img, estado):
    screen.blit(fondo_img, (0, 0))
    frases = [
        "Una Planta Crece",
        "Una tormenta comienza y termina con un arcoíris",
        "El héroe responde al brujo acierta y recibe una llave que da a una puerta"
    ]
    mostrar_mensaje_pantalla(screen, font, frases[nivel[0] - 1], (255, 255, 255), 650)  # Ajuste aquí para usar nivel-1 como índice
    mostrar_mensaje_pantalla(screen, font, "Presiona Enter para comprobar si está bien", (255, 255, 255), 700)
    
    cartas = crear_cartas(nivel)
    cartas_desordenadas = cartas.mostrar()
    cartas_pos_y = 300
    
    carta_imgs = []
    num_cartas = len(cartas_desordenadas)
    total_ancho_cartas = num_cartas * 100
    inicio_x = (1200 - total_ancho_cartas) // 2

    for i, carta in enumerate(cartas_desordenadas):
        imagen = pygame.image.load(os.path.join(config.CARTASIN_DIR, "recursos", carta.imagen)).convert_alpha()
        imagen = pygame.transform.scale(imagen, (100, 150))
        rect = imagen.get_rect(topleft=(inicio_x + i * 100, cartas_pos_y))
        carta_imgs.append({"img": imagen, "rect": rect, "valor": carta.valor})
    
    dragging = False
    selected_card = None
    nivel_completado = False
    
    while not nivel_completado:
        screen.blit(fondo_img, (0, 0))
        mostrar_mensaje_pantalla(screen, font, frases[nivel[0] - 1], (255, 255, 255), 650)  # Ajuste aquí para usar nivel-1 como índice
        mostrar_mensaje_pantalla(screen, font, "Presiona Enter para comprobar si está bien", (255, 255, 255), 700)
        
        mouse_pos = pygame.mouse.get_pos()
        dragging, selected_card = manejar_eventos(carta_imgs, mouse_pos, dragging, selected_card)
        
        for carta in carta_imgs:
            screen.blit(carta["img"], carta["rect"])
        
        pygame.display.flip()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            carta_imgs.sort(key=lambda x: x["rect"].x)
            if verificar_orden(carta_imgs, nivel):
                screen.blit(fondo_img, (0, 0))
                mostrar_mensaje_pantalla(screen, font, "¡Correcto! Presiona Enter para continuar...", (255, 255, 255), 450)
                pygame.display.flip()
                esperar_enter()
                nivel_completado = True

def main_cartas(screen, reloj, estado, dificultad):
    # Ambiente
    pygame.mixer.music.load(os.path.join(config.SOUNDTRACK_DIR, 'Cartas - Hungarian Dance No.5.mp3'))
    pygame.mixer.music.play(-1)
    
    fondo_img = pygame.image.load(os.path.join(config.FONDOS_DIR, 'cartasHD.png')).convert()
    fondo_img = pygame.transform.scale(fondo_img, (1280, 720))
    
    font = pygame.font.Font(None, 36)
    
    jugar_nivel(screen, font, dificultad, fondo_img, estado)
    
    screen.blit(fondo_img, (0, 0))
    mostrar_mensaje_pantalla(screen, font, "¡Felicidades! Has completado el nivel del juego de emparejamiento de cartas.", (255, 255, 255), 200)
    mostrar_mensaje_pantalla(screen, font, "Puedes avanzar al siguiente desafío.", (255, 255, 255), 250)
    mostrar_mensaje_pantalla(screen, font, "Presiona Enter para salir...", (255, 255, 255), 300)
    pygame.display.flip()
    
    esperar_enter()
    
    estado[0] = config.SCREEN_MAPA

if __name__ == "__main__":
    main_cartas(pygame.display.set_mode((1280, 720)), pygame.time.Clock(), [0], 1)
