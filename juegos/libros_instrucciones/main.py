import pygame
import os
import sys
import config

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Initialization Pygame
pygame.init()
screen = pygame.display.set_mode((config.ANCHO_VENTANA, config.ALTO_VENTANA))
pygame.display.set_caption('Libro Instrucciones')
clock = pygame.time.Clock()
FPS = 60
# End of initialization

# Backgrounds
backgroundDefault = pygame.image.load(os.path.join(config.LIBROS_DIR, "LibroVacio.png"))
backgroundHanoi = pygame.image.load(os.path.join(config.LIBROS_DIR, "LibroHanoi.png"))

# Context variable
context = 'hanoi'

# Fonts Instructions
myFontTitles = pygame.font.Font(os.path.join(config.FONTS_DIR, "minecraft.ttf"), 30)
myFontParagraph = pygame.font.Font(os.path.join(config.FONTS_DIR, "minecraft.ttf"), 24)

# General texts
text_learn = myFontTitles.render("HORA DE APRENDER", 0, (0, 0, 0))
text_game = myFontTitles.render("EN EL JUEGO", 0, (0, 0, 0))


def render_multiline_text(text, font, color, surface, x, y, line_height):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_surface = font.render(line, True, color)
        surface.blit(line_surface, (x, y + i * line_height))


def hanoi_book():
    screen.blit(backgroundHanoi, [0, 0])

    text_concept = "Pilas: Lista donde el ultimo\nelemento ingresado es el\nprimero en salir."
    text_operation1 = "Apilar (push): Introducir un\nelemento dentro de la\npila, hasta llegar a un tope."
    text_operation2 = "Desapilar (pop): Retirar\ncada elemento. Solo se\npuede desde el extremo\nen que se ingreso."
    text_inst1 = "Lleva los discos del\npunto A al punto C,\npasando por B.\nOrdenar del\nmayor al menor."
    text_inst2 = "Desapila y apila\ncada disco. Al\napilar se considera\nun movimiento."
    text_inst3 = "Calcula los\nmovimientos, ya\nque para cada\ncaso existe una\nmínima cantidad."

    render_multiline_text(text_concept, myFontParagraph, (0, 0, 0), screen, 100, 220, 22)
    render_multiline_text(text_operation1, myFontParagraph, (0, 0, 0), screen, 100, 390, 22)
    render_multiline_text(text_operation2, myFontParagraph, (0, 0, 0), screen, 100, 530, 22)
    render_multiline_text(text_inst1, myFontParagraph, (0, 0, 0), screen, 710, 190, 22)
    render_multiline_text(text_inst2, myFontParagraph, (0, 0, 0), screen, 710, 360, 22)
    render_multiline_text(text_inst3, myFontParagraph, (0, 0, 0), screen, 710, 500, 22)


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

    if context == 'hanoi':
        hanoi_book()
    else:
        screen.blit(backgroundDefault, [0, 0])

    screen.blit(text_learn, (180, 100))
    screen.blit(text_game, (853, 100))
    pygame.display.flip()
    clock.tick(FPS)
