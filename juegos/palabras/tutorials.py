import pygame
import os

def show_tutorial(screen):
    # Cargar el fondo de pantalla
    background = pygame.image.load(os.path.join('recursos', 'palabrasHD.png')).convert()
    background = pygame.transform.scale(background, (800, 600))

    font = pygame.font.Font(None, 36)
    text_lines = [
        "Toshi, el protagonista, llega a un pueblo misterioso",
        "donde las palabras están atrapadas. Para liberarlas debe",
        "adivinar una serie de claves que le faltan caracteres",
        "con ayuda de las palabras atrapadas. Las letras a adivinar",
        "están relacionadas con estructuras de datos.",
        "",
        "Presiona cualquier tecla para comenzar."
    ]

    screen.blit(background, (0, 0))

    y_offset = 150
    for line in text_lines:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (50, y_offset))
        y_offset += 40

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
