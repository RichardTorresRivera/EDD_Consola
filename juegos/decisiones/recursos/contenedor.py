import sys
import os
import config
import pygame
import textwrap

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Contenedor:
    def __init__(self, x, y, ancho, alto, color, texto):
        self.forma = pygame.Rect(x, y, ancho, alto)
        self.color = color
        self.texto = texto
        self.fuente = pygame.font.Font(os.path.join(config.FONTS_DIR, "minecraft.ttf"), 23)
    
    def dibujar(self, screen):
        pygame.draw.rect(screen, self.color, self.forma, border_radius = 20)
        lineas = textwrap.wrap(self.texto, width=30 if self.forma.width < 1000 else 90)

        y_offset = (self.forma.height - len(lineas) * self.fuente.get_height()) // 2
        for linea in lineas:
            text_superficie = self.fuente.render(linea, False, (255, 255, 255))
            text_superficie_rect = text_superficie.get_rect(centerx=self.forma.centerx)
            text_superficie_rect.y = self.forma.y + y_offset
            screen.blit(text_superficie, text_superficie_rect)
            y_offset += text_superficie.get_height()
    
    def get_texto(self):
        return self.texto
    
    def actualizar(self, texto):
        self.texto = texto
    