import pygame
from personaje import Personaje

pygame.init()
screen = pygame.display.set_mode((1280, 720))
run = True

wallpaper = pygame.image.load("mapa.png")

pygame.display.set_caption("Stack Adventure")


def escalar_imagen(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
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

path_segments = [
    [(130, 70), (190, 70)],
    [(190, 70), (440, 70)],
    [(440, 70), (500, 70), (500, 140), (650, 140)],
    [(650, 140), (685, 140), (690, 390)],
    [(690, 390), (690, 350), (875, 350), (875, 440), (910, 440)],
    [(910, 440), (1230, 440)]
]

player = Personaje(path_segments[0][0][0], path_segments[0][0][1], animation_move, animation_idle, path_segments)

reloj = pygame.time.Clock()

while run:
    reloj.tick(30)

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
