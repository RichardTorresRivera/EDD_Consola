import pygame


class Personaje:
    def __init__(self, x, y, animation_move, animation_idle, path):
        self.flip = False
        self.animation_move = animation_move
        self.animation_idle = animation_idle
        self.animation = self.animation_idle
        self.frame = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation[self.frame]
        self.cambiar_forma(x, y, 50, 50)
        self.path = path
        self.current_point_index = 0
        self.moving = False

    def cambiar_forma(self, x, y, width, height):
        self.forma = pygame.Rect(x, y, width, height)

    def move_to_next_point(self):
        if self.current_point_index < len(self.path) - 1:
            self.current_point_index += 1
            self.moving = True
            print(f'Moving to next point: {self.path[self.current_point_index]}')

    def move_to_previous_point(self):
        if self.current_point_index > 0:
            self.current_point_index -= 1
            self.moving = True
            print(f'Moving to previous point: {self.path[self.current_point_index]}')

    def mover(self, target_x, target_y):
        moved = False
        if self.forma.x != target_x:
            self.cambiar_forma(self.forma.x + (5 if self.forma.x < target_x else -5), self.forma.y, self.forma.width,
                               self.forma.height)
            moved = True
        elif self.forma.y != target_y:
            self.cambiar_forma(self.forma.x, self.forma.y + (5 if self.forma.y < target_y else -5), self.forma.width,
                               self.forma.height)
            moved = True

        print(f'Current position: ({self.forma.x}, {self.forma.y}), Target: ({target_x}, {target_y})')

        if self.forma.x == target_x and self.forma.y == target_y:
            self.moving = False
            print('Reached target')

        return moved

    def update(self):
        if self.moving:
            target_x, target_y = self.path[self.current_point_index]
            self.mover(target_x, target_y)

        cooldown = 300
        self.image = self.animation[self.frame]
        if pygame.time.get_ticks() - self.update_time >= cooldown:
            self.frame += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame >= len(self.animation):
            self.frame = 0

        if self.moving and self.animation != self.animation_move:
            self.animation = self.animation_move
            self.frame = 0
        elif not self.moving and self.animation != self.animation_idle:
            self.animation = self.animation_idle
            self.frame = 0

    def dibujar(self, screen):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(imagen_flip, self.forma.topleft)
