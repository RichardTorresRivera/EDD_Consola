import pygame
import random
import os
import config
from juegos.buscaminas.recursos.constantes import *
from common.colores import *

bomba_img = pygame.image.load('assets/images/juegos/buscaminas/bomba.png')
bomba_img = pygame.transform.scale(bomba_img, (20, 20))

class Matriz:
    def __init__(self, filas, columnas, minas):
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
        self.revelado = [[False for _ in range(columnas)] for _ in range(filas)]
        self.bandera = [[False for _ in range(columnas)] for _ in range(filas)]
        self.map = [[0 for _ in range(columnas)] for _ in range(filas)]
        self.colocar_minas()
        self.calcular_numeros()
        self.bandera_img = pygame.image.load('assets/images/juegos/buscaminas/bandera.png')
        self.bandera_img = pygame.transform.scale(self.bandera_img, (20, 20))

    def colocar_minas(self):
        count = 0
        while count < self.minas:
            x = random.randint(0, self.filas - 1)
            y = random.randint(0, self.columnas - 1)
            if self.tablero[x][y] == 0:
                self.tablero[x][y] = -1
                count += 1

    def calcular_numeros(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero[i][j] == -1:
                    continue
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < self.filas and 0 <= nj < self.columnas and self.tablero[ni][nj] == -1:
                            count += 1
                self.map[i][j] = count

    def revelar(self, x, y):
        if self.tablero[x][y] == -1:
            return False
        elif self.tablero[x][y] > 0:
            self.revelado[x][y] = True
            return True
        else:
            self.flood_fill(x, y)
            return True

    def flood_fill(self, x, y):
        if x < 0 or x >= self.filas or y < 0 or y >= self.columnas or self.revelado[x][y]:
            return
        
        self.revelado[x][y] = True
        
        if self.map[x][y] == 0:
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    ni, nj = x + di, y + dj
                    if 0 <= ni < self.filas and 0 <= nj < self.columnas:
                        self.flood_fill(ni, nj)

    def colocar_bandera(self, x, y):
        self.bandera[x][y] = not self.bandera[x][y]

    def contar_minas_restantes(self):
        count = self.minas
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.bandera[i][j]:
                    count -= 1
        return count

    def contar_bombas(self):
        count = 0
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero[i][j] == -1:
                    count += 1
        return count

    def todas_reveladas(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.map[i][j] > 0 and not self.revelado[i][j]:
                    return False
        return True

    def mostrar(self, pantalla, tamaño_celda, margen_x, margen_y):
        fuente = pygame.font.Font(os.path.join(config.FONTS_DIR, "minecraft.ttf"), 30)

        # Calcula la posición del tablero para centrarlo en la pantalla
        tablero_ancho = self.columnas * tamaño_celda
        tablero_alto = self.filas * tamaño_celda

        # Dibuja el borde alrededor del tablero
        borde_ancho = 5
        pygame.draw.rect(pantalla, MARRON_CLARO, (margen_x - borde_ancho, margen_y - borde_ancho, tablero_ancho + 2 * borde_ancho, tablero_alto + 2 * borde_ancho))

        for i in range(self.filas):
            for j in range(self.columnas):
                if self.revelado[i][j]:
                    color = MARRON  # Color marrón cuando la casilla está revelada
                else:
                    color = MARRON_CLARO  # Color marrón claro cuando la casilla no está revelada

                x = margen_x + j * tamaño_celda
                y = margen_y + i * tamaño_celda

                pygame.draw.rect(pantalla, color, (x, y, tamaño_celda, tamaño_celda))
                pygame.draw.rect(pantalla, NEGRO, (x, y, tamaño_celda, tamaño_celda), 3)
                if self.revelado[i][j] and self.map[i][j] != 0:
                    texto = str(self.map[i][j])  # Convertir el número a cadena para renderizar
                    color_numero = COLORES_NUMEROS.get(self.map[i][j], NEGRO)
                    texto_renderizado = fuente.render(texto, True, color_numero)
                    pantalla.blit(texto_renderizado, (x + 10, y + 10))
                elif self.bandera[i][j]:
                    pantalla.blit(self.bandera_img, (x + 10, y + 10))

    def ganaste(self):
        return self.todas_reveladas() and not self.hay_bomba_revelada()

    def hay_bomba_revelada(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero[i][j] == -1 and self.revelado[i][j]:
                    return True
        return False
    
    def mostrar_bombas(self, pantalla, tamaño_celda, margen_x, margen_y):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero[i][j] == -1:
                    x = margen_x + j * tamaño_celda
                    y = margen_y + i * tamaño_celda
                    pantalla.blit(bomba_img, (x + 10, y + 10))