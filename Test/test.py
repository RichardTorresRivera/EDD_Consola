import pygame

from Test.personaje import Personaje

pygame.init()
screen = pygame.display.set_mode((1280, 720))
run = True

wallpaper = pygame.image.load("wp.png")

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
    img = escalar_imagen(img, 0.1)
    animation_move.append(img)

for i in range(2):
    img = pygame.image.load(f"Toshi//Stop//FrameS{i}.png")
    img = escalar_imagen(img, 0.1)
    animation_idle.append(img)

player = Personaje(43, 360, animation_move, animation_idle)

reloj = pygame.time.Clock()

move_up = False
move_down = False
move_left = False
move_right = False

while run:

    reloj.tick(60)
    screen.fill((255, 255, 255))
    x = 0
    y = 0
    if move_right:
        x += 5
    if move_left:
        x -= 5
    if move_up:
        y -= 5
    if move_down:
        y += 5

    player.mover(x, y)
    moving = move_up or move_down or move_left or move_right
    player.update(moving)

    screen.blit(wallpaper, (0, 0))

    player.dibujar(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False

    pygame.display.update()
