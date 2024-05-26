import pygame


class Personaje:
    def __init__(self, x, y, animation_move, animtion_idle):
        self.flip = False
        self.animation_move = animation_move
        self.animation_idle = animtion_idle
        self.animation = self.animation_idle
        self.frame = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation[self.frame]
        self.forma = pygame.Rect(0, 0, 50, 50)
        self.forma.center = (x, y)

    def mover(self, delta_x, delta_y):
        if delta_x > 0:
            self.flip = False
        elif delta_x < 0:
            self.flip = True
        self.forma.x += delta_x
        self.forma.y += delta_y

    def update(self, moving):
        cooldown = 300
        self.image = self.animation[self.frame]
        if pygame.time.get_ticks() - self.update_time >= cooldown:
            self.frame += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame >= len(self.animation):
            self.frame = 0

        if moving and self.animation != self.animation_move:
            self.animation = self.animation_move
            self.frame = 0
        elif not moving and self.animation != self.animation_idle:
            self.animation = self.animation_idle
            self.frame = 0

    def dibujar(self, screen):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(imagen_flip, self.forma)
