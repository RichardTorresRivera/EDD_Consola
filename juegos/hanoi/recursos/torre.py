import pygame

from juegos.hanoi.recursos.pila import Nodo, Pila

class Disco(Nodo):
    def __init__(self, peso, image):
        super().__init__(peso)
        self.image = image
        self.forma = self.image.get_rect()
        self.pos = 0
        self.torre = None

    def set_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos
    
    def set_torre(self, torre):
        self.torre = torre

    def get_torre(self):
        return self.torre
    
    def actualizar(self):
        self.forma.center = self.torre.forma.center
        self.forma.top = 240 - self.pos*40

    def dibujar(self, screen):
        screen.blit(self.image, self.forma)
        #pygame.draw.rect(screen, (255,255,0), self.forma, 1)

class Torre(Pila):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.x = x
        self.y = y
        self.forma = self.image.get_rect()
        self.forma.topleft = (self.x, self.y)


    def dibujar(self, screen):
        screen.blit(self.image, self.forma)
        pygame.draw.rect(screen, (255,0,0), self.forma, 1)
