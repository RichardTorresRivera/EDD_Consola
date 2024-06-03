import pygame

pygame.init()

font = pygame.font.Font(None, 36)

boton_jugar = pygame.Rect(535, 330, 210, 85)
boton_salir = pygame.Rect(535, 430, 210, 85)

img = pygame.image.load("Elementos//menu.png")

screen = pygame.display.set_mode((1280, 720))


def inicio():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if boton_jugar.collidepoint(mouse_pos):
                    running = False
                elif boton_salir.collidepoint(mouse_pos):
                    pygame.quit()

        pygame.draw.rect(screen, (255, 255, 255), boton_jugar)
        pygame.draw.rect(screen, (255, 255, 255), boton_salir)

        screen.blit(img, (0, 0))

        pygame.display.update()