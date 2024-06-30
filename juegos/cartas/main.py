import pygame
import random
import sys
import os

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
    cartas = cartas_info[nivel]
    random.shuffle(cartas)
    lista_enlazada = ListaEnlazada()
    for valor, imagen in cartas:
        lista_enlazada.agregar(valor, imagen)
    return lista_enlazada

def mostrar_mensaje_pantalla(screen, font, mensaje, color, pos):
    texto = font.render(mensaje, True, color)
    screen.blit(texto, pos)

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
        if carta["valor"] != orden_correcto[nivel][i]:
            return False
    return True

def jugar_nivel(screen, font, nivel, fondo_img):
    screen.blit(fondo_img, (0, 0))
    mostrar_mensaje_pantalla(screen, font, f"--- Nivel {nivel + 1} ---", (255, 255, 255), (50, 50))
    frases = [
        "Una Planta Crece",
        "Una tormenta comienza y termina con un arcoíris",
        "El héroe responde al brujo acierta y recibe una llave que da a una puerta"
    ]
    mostrar_mensaje_pantalla(screen, font, frases[nivel], (255, 255, 255), (50, 100))
    
    cartas = crear_cartas(nivel)
    cartas_desordenadas = cartas.mostrar()
    cartas_pos_y = 300
    
    carta_imgs = []
    num_cartas = len(cartas_desordenadas)
    espacio_disponible = 1200 - 100 * num_cartas
    espacio_entre_cartas = espacio_disponible // (num_cartas + 1)
    
    for i, carta in enumerate(cartas_desordenadas):
        imagen = pygame.image.load(os.path.join('recursos', carta.imagen)).convert_alpha()
        imagen = pygame.transform.scale(imagen, (100, 150))
        rect = imagen.get_rect(center=(espacio_entre_cartas * (i + 1) + 100 * (i + 0.5), cartas_pos_y))
        carta_imgs.append({"img": imagen, "rect": rect, "valor": carta.valor})
    
    dragging = False
    selected_card = None
    nivel_completado = False
    
    while not nivel_completado:
        screen.blit(fondo_img, (0, 0))
        mostrar_mensaje_pantalla(screen, font, f"--- Nivel {nivel + 1} ---", (255, 255, 255), (50, 50))
        mostrar_mensaje_pantalla(screen, font, frases[nivel], (255, 255, 255), (50, 100))
        
        mouse_pos = pygame.mouse.get_pos()
        dragging, selected_card = manejar_eventos(carta_imgs, mouse_pos, dragging, selected_card)
        
        for carta in carta_imgs:
            screen.blit(carta["img"], carta["rect"])
        
        pygame.display.flip()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            carta_imgs.sort(key=lambda x: x["rect"].x)
            if verificar_orden(carta_imgs, nivel):
                mostrar_mensaje_pantalla(screen, font, "¡Correcto! Presiona Enter para continuar...", (255, 255, 255), (50, 400))
                pygame.display.flip()
                esperar_enter()
                nivel_completado = True

def juego_emparejamiento_cartas():
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Juego de Emparejamiento de Cartas")
    font = pygame.font.Font(None, 36)
    
    fondo_img = pygame.image.load(os.path.join('recursos', 'cartasHD.png')).convert()
    fondo_img = pygame.transform.scale(fondo_img, (1200, 600))
    
    pygame.mixer.music.load(os.path.join('recursos', 'Cartas - Hungarian Dance No.5.mp3'))
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
    
    niveles = 3
    for nivel in range(niveles):
        jugar_nivel(screen, font, nivel, fondo_img)
    
    screen.fill((0, 0, 0))
    mostrar_mensaje_pantalla(screen, font, "¡Felicidades! Has completado todos los niveles del juego de emparejamiento de cartas.", (255, 255, 255), (50, 200))
    mostrar_mensaje_pantalla(screen, font, "Puedes avanzar al siguiente desafío.", (255, 255, 255), (50, 250))
    mostrar_mensaje_pantalla(screen, font, "Presiona Enter para salir...", (255, 255, 255), (50, 300))
    pygame.display.flip()
    
    esperar_enter()
    
    pygame.quit()

def main():
    juego_emparejamiento_cartas()
    while True:
        opcion = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
        if opcion == 's':
            juego_emparejamiento_cartas()
        else:
            print("Gracias por jugar. ¡Hasta la proxima!")
            break

if __name__ == "__main__":
    main()
