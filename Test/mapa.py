import pygame
from personaje import Personaje

pygame.init()
screen = pygame.display.set_mode((1280, 720))
run = True

map_frames = []
for i in range(4):
    wallpaper = pygame.image.load(f"Mapa//map_frame{i}.png")
    map_frames.append(wallpaper)

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
    [(130, 75), (180, 75)],
    [(180, 75), (430, 75)],
    [(440, 75), (500, 75), (500, 140), (650, 140)],
    [(650, 140), (685, 140), (690, 380)],
    [(690, 380), (690, 350), (875, 350), (875, 445), (905, 445)],
    [(905, 445), (1240, 445)]
]

player = Personaje(path_segments[0][0][0], path_segments[0][0][1], animation_move, animation_idle, path_segments)

current_frame = 0

reloj_personaje = pygame.time.Clock()
reloj_mapa = pygame.time.Clock()

fps_personaje = 30
fps_mapa = 3

last_map_update = pygame.time.get_ticks()
map_update_interval = 1000 // fps_mapa

while run:

    reloj_personaje.tick(fps_personaje)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.move_to_next_point()
            if event.key == pygame.K_LEFT:
                player.move_to_previous_point()

    player.update()

    current_time = pygame.time.get_ticks()
    if current_time - last_map_update > map_update_interval:
        current_frame = (current_frame + 1) % len(map_frames)
        last_map_update = current_time

    screen.blit(map_frames[current_frame], (0, 0))
    player.dibujar(screen)

    pygame.display.update()

pygame.quit()
