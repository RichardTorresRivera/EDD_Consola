import pygame
import os
import sys
import config

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
pygame.init()
"""
# Initialization Pygame

screen = pygame.display.set_mode((config.ANCHO_VENTANA, config.ALTO_VENTANA))
pygame.display.set_caption('Libro Instrucciones')
clock = pygame.time.Clock()
FPS = 60
# End of initialization
"""

# Backgrounds
backgroundDefault = pygame.image.load(os.path.join(config.LIBROS_DIR, "LibroVacio.png"))
backgroundHanoi = pygame.image.load(os.path.join(config.LIBROS_DIR, "LibroHanoi.png"))
backgroundDecision = pygame.image.load(os.path.join(config.LIBROS_DIR, "LibroDecision.png"))
backgroundWords = pygame.image.load(os.path.join(config.LIBROS_DIR, "LibroWords.png"))
backgroundMinesWeeper = pygame.image.load(os.path.join(config.LIBROS_DIR, "LibroMinesWeeper.png"))
backgroundCards = pygame.image.load(os.path.join(config.LIBROS_DIR, "LibroCards.png"))
backgroundLabyrinth = pygame.image.load(os.path.join(config.LIBROS_DIR, "LibroLabyrinth.png"))

# Context variable
context = 'labyrinth'

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


def hanoi_book(screen):
    screen.blit(backgroundHanoi, [0, 0])
    screen.blit(text_learn, (180, 100))
    screen.blit(text_game, (853, 100))

    text_concept = "Pilas: Lista donde el ultimo\nelemento ingresado es el\nprimero en salir."
    text_operation1 = "Apilar (push): Introducir un\nelemento dentro de la\npila, hasta llegar a un tope."
    text_operation2 = "Desapilar (pop): Retirar\ncada elemento. Solo se\npuede desde el extremo\nen que se ingreso."
    text_inst1 = "Lleva los discos del\npunto A al punto C,\npasando por B.\nOrdenar del\nmayor al menor."
    text_inst2 = "Desapila y apila\ncada disco. Al\napilar se considera\nun movimiento."
    text_inst3 = "Calcula los\nmovimientos, ya\nque para cada\ncaso existe una\nminima cantidad."

    render_multiline_text(text_concept, myFontParagraph, (0, 0, 0), screen, 100, 220, 22)
    render_multiline_text(text_operation1, myFontParagraph, (0, 0, 0), screen, 100, 390, 22)
    render_multiline_text(text_operation2, myFontParagraph, (0, 0, 0), screen, 100, 530, 22)
    render_multiline_text(text_inst1, myFontParagraph, (0, 0, 0), screen, 710, 190, 22)
    render_multiline_text(text_inst2, myFontParagraph, (0, 0, 0), screen, 710, 360, 22)
    render_multiline_text(text_inst3, myFontParagraph, (0, 0, 0), screen, 710, 500, 22)


def decision_book(screen):
    screen.blit(backgroundDecision, [0, 0])
    screen.blit(text_learn, (180, 100))
    screen.blit(text_game, (853, 100))

    text_concept = "Arboles: Estructura no\nlineal conformada\npor elementos\nllamados nodos y lineas\nllamadas ramas."
    text_operation1 = "Cada nodo tiene un\nunico camino que\ncomienza desde el\nprimer nodo\n(raiz o padre)."
    text_operation2 = "Arbol Binario: Mas\nconocido y usado, tiene\nmaximo 2 nodos hijos,\n2 opciones para\nrecorrer."
    text_inst1 = "Estas en la etapa\nfinal del juego, ahora\neres tu quien decide\nel final de la aventura."
    text_inst2 = "Escoge alguna de\nlas 2 opciones y\ndescubre a que te\nlleva cada escenario."
    text_inst3 = "Puede ser un final\nbueno o malo.\nEscoge con sabiduria."

    render_multiline_text(text_concept, myFontParagraph, (0, 0, 0), screen, 100, 190, 22)
    render_multiline_text(text_operation1, myFontParagraph, (0, 0, 0), screen, 100, 340, 22)
    render_multiline_text(text_operation2, myFontParagraph, (0, 0, 0), screen, 100, 500, 22)
    render_multiline_text(text_inst1, myFontParagraph, (0, 0, 0), screen, 710, 190, 22)
    render_multiline_text(text_inst2, myFontParagraph, (0, 0, 0), screen, 710, 340, 22)
    render_multiline_text(text_inst3, myFontParagraph, (0, 0, 0), screen, 710, 520, 22)


def words_book(screen):
    screen.blit(backgroundWords, [0, 0])
    screen.blit(text_learn, (180, 100))
    screen.blit(text_game, (853, 100))

    text_concept = "Vector: Estructura\nunidimensional. Se\ndefine su longitud al\ninicio, pero no\nen la ejecucion."
    text_operation1 = "Cada elemento se\nalmacena en una\nposicion (desde 0\nhasta n)."
    text_operation2 = "Para modificar un\nelemento, se busca\nla posicion deseada."
    text_inst1 = "Hay letras que han\nsido atrapadas en\njaulas por los Shu."
    text_inst2 = "Debes completar\nla palabra del\ncontenedor usando\nlas letras."
    text_inst3 = "Pista: Cada palabra\nesta relacionada con\nlas estructuras\nde datos."

    render_multiline_text(text_concept, myFontParagraph, (0, 0, 0), screen, 100, 190, 22)
    render_multiline_text(text_operation1, myFontParagraph, (0, 0, 0), screen, 100, 370, 22)
    render_multiline_text(text_operation2, myFontParagraph, (0, 0, 0), screen, 100, 530, 22)
    render_multiline_text(text_inst1, myFontParagraph, (0, 0, 0), screen, 710, 190, 22)
    render_multiline_text(text_inst2, myFontParagraph, (0, 0, 0), screen, 710, 340, 22)
    render_multiline_text(text_inst3, myFontParagraph, (0, 0, 0), screen, 710, 520, 22)


def minesweeper_book(screen):
    screen.blit(backgroundMinesWeeper, [0, 0])
    screen.blit(text_learn, (180, 100))
    screen.blit(text_game, (853, 100))

    text_concept = "Matriz: Estructura\nbidimensional. Define\nsu longitud al inicio."
    text_operation1 = "Cuenta con 2 indices\n(desde 0,0 hasta n,m)."
    text_operation2 = "Para modificar un\nelemento, se busca\nla posicion deseada."
    text_inst1 = "Toshi llega a una\nmina, que contiene\nbombas en algunas\nposiciones."
    text_inst2 = "Excava las posiciones\nvacias y coloca\nbanderas donde\nhaya bombas."
    text_inst3 = "Los extremos indican\ncon un numero la\ncantidad de espacios.\nTen cuidado con\nexplotar una bomba."

    render_multiline_text(text_concept, myFontParagraph, (0, 0, 0), screen, 100, 190, 22)
    render_multiline_text(text_operation1, myFontParagraph, (0, 0, 0), screen, 100, 370, 22)
    render_multiline_text(text_operation2, myFontParagraph, (0, 0, 0), screen, 100, 500, 22)
    render_multiline_text(text_inst1, myFontParagraph, (0, 0, 0), screen, 710, 190, 22)
    render_multiline_text(text_inst2, myFontParagraph, (0, 0, 0), screen, 710, 340, 22)
    render_multiline_text(text_inst3, myFontParagraph, (0, 0, 0), screen, 710, 500, 22)


def card_book(screen):
    screen.blit(backgroundCards, [0, 0])

    text_concept = "Lista enlazada: Secuencia\nde nodos conectados\nmediante enlaces\n(dato - puntero)."
    text_operation1 = "Insertar:  Agrega un\nnuevo nodo, puede\nser al inicio o al\nfinal."
    text_operation2 = "Ordenar: Busca el\ndato del nodo y lo\nintercambia con el\nsiguiente."
    text_inst1 = "En la mesa hay\nuna cantidad de\ncartas."
    text_inst2 = "El brujo te dara\nuna frase que\ninvolucra esas cartas."
    text_inst3 = "Colocar en el orden\ncorrecto para ganar\nel nivel."

    render_multiline_text(text_concept, myFontParagraph, (0, 0, 0), screen, 100, 190, 22)
    render_multiline_text(text_operation1, myFontParagraph, (0, 0, 0), screen, 100, 370, 22)
    render_multiline_text(text_operation2, myFontParagraph, (0, 0, 0), screen, 100, 500, 22)
    render_multiline_text(text_inst1, myFontParagraph, (0, 0, 0), screen, 710, 190, 22)
    render_multiline_text(text_inst2, myFontParagraph, (0, 0, 0), screen, 710, 340, 22)
    render_multiline_text(text_inst3, myFontParagraph, (0, 0, 0), screen, 710, 500, 22)


def labyrinth_book(screen):
    screen.blit(backgroundLabyrinth, [0, 0])
    screen.blit(text_learn, (180, 100))
    screen.blit(text_game, (853, 100))

    text_concept = "Esta formado por un\nconjunto de vertices\ny aristas."
    text_operation1 = "Se dividen en grafos\ndirigidos (con flecha)\ny no dirigidos\n(sin flecha)."
    text_operation2 = "El camino es la\nsecuencia de vertices\ndesde el primero\n(V0) hasta el ultimo\n(Vn)."
    text_inst1 = "Toshi se enfrenta\na un laberinto\nmisterioso para\nllegar hacia la\naldea de los Shu."
    text_inst2 = "Halla el camino\ncorrecto que Toshi\ndebe seguir."
    text_inst3 = "Ten cuidado,\npuedes perderte\nen el proceso."

    render_multiline_text(text_concept, myFontParagraph, (0, 0, 0), screen, 100, 190, 22)
    render_multiline_text(text_operation1, myFontParagraph, (0, 0, 0), screen, 100, 350, 22)
    render_multiline_text(text_operation2, myFontParagraph, (0, 0, 0), screen, 100, 490, 22)
    render_multiline_text(text_inst1, myFontParagraph, (0, 0, 0), screen, 710, 190, 22)
    render_multiline_text(text_inst2, myFontParagraph, (0, 0, 0), screen, 710, 360, 22)
    render_multiline_text(text_inst3, myFontParagraph, (0, 0, 0), screen, 710, 500, 22)

"""
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

    if context == 'hanoi':
        hanoi_book()
    elif context == 'decision':
        decision_book()
    elif context == 'words':
        words_book()
    elif context == 'minesweeper':
        minesweeper_book()
    elif context == 'cards':
        card_book()
    elif context == 'labyrinth':
        labyrinth_book()
    else:
        screen.blit(backgroundDefault, [0, 0])

    screen.blit(text_learn, (180, 100))
    screen.blit(text_game, (853, 100))
    pygame.display.flip()
    clock.tick(FPS)
"""
