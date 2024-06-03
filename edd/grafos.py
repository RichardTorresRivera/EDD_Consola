import random

class Laberinto:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.grafo = {}
        self.salida = None
        self.generar_lab()

    def agregar_aristas(self, vertice):
        direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(direcciones)
        for dx, dy in direcciones:
            x, y = vertice
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.filas and 0 <= ny < self.columnas and (nx, ny) not in self.grafo:
                self.grafo[vertice].append((nx, ny))
                self.grafo[(nx, ny)] = [(x, y)]
                self.agregar_aristas((nx, ny))

    def generar_lab(self):
        inicio = (0, 0)
        self.grafo[inicio] = []
        self.agregar_aristas(inicio)

        self.salida = (random.randint(0, self.filas - 1), random.randint(0, self.columnas - 1))
        while self.salida == inicio or self.salida not in self.grafo:
            self.salida = (random.randint(0, self.filas - 1), random.randint(0, self.columnas - 1))

    def mostrar_lab(self, jugador):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if (fila, columna) == jugador:
                    print("P", end=" ")
                elif (fila, columna) == self.salida:
                    print("S", end=" ")
                elif (fila, columna) in self.grafo[jugador]:
                    print(" ", end=" ")
                else:
                    print("#", end=" ")
            print()

    def obtener_mov_validos(self, posicion):
        return self.grafo[posicion]