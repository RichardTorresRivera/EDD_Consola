import pygame
from personaje import Personaje

pygame.init()
screen = pygame.display.set_mode((1280, 720))
run = True

wallpaper = pygame.image.load("mapa.png")

pygame.display.set_caption("Prueba Toshi")

def escalar_imagen(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (w * scale, h * scale))
    return new_image

animation_move = []
animation_idle = []

for i in range(4):
    img = pygame.image.load(f"Toshi//Moving//Frame{i}.png")
    img = escalar_imagen(img, 0.04)
    animation_move.append(img)

for i in range(2):
    img = pygame.image.load(f"Toshi//Stop//FrameS{i}.png")
    img = escalar_imagen(img, 0.04)
    animation_idle.append(img)

# Definir el camino
path = [
    (130, 80),
    (200, 80),
    (440, 80),
    (300, 250),
    (350, 300),
    (400, 350),
    (450, 400),
    (500, 450)
]

player = Personaje(path[0][0], path[0][1], animation_move, animation_idle, path)

reloj = pygame.time.Clock()

move_up = False
move_down = False
move_left = False
move_right = False

while run:
    reloj.tick(30)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.move_to_next_point()
            if event.key == pygame.K_LEFT:
                player.move_to_previous_point()

    player.update()

    screen.blit(wallpaper, (0, 0))
    player.dibujar(screen)

    pygame.display.update()

pygame.quit()
