import random

class Matriz:
    def __init__(self, filas, columnas, minas):
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.map = [[0 for _ in range(columnas)] for _ in range(filas)]
        self.no_map = [["- " for _ in range(columnas)] for _ in range(filas)]
        self.llenar_mapa()
        self.llenar_pistas()

    def int_to_string(self, num):
        return str(num)

    def comprobar(self):
        for x in range(self.filas):
            for y in range(self.columnas):
                if self.no_map[x][y] == "- " and self.map[x][y] != 9:
                    return False
        return True

    def mostrar(self):
        for x in range(self.filas):
            for y in range(self.columnas):
                print(self.no_map[x][y], end=" ")
            print()

    def flood_fill(self, x, y):
        if x < 0 or x >= self.filas or y < 0 or y >= self.columnas or self.no_map[x][y] != "- " or self.map[x][y] == 9:
            return

        self.no_map[x][y] = self.int_to_string(self.map[x][y]) + " "

        if self.map[x][y] == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i != 0 or j != 0:
                        self.flood_fill(x + i, y + j)

    def llenar_pistas(self):
        for x in range(self.filas):
            for y in range(self.columnas):
                if self.map[x][y] == 9:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= x + i < self.filas and 0 <= y + j < self.columnas:
                                if self.map[x + i][y + j] != 9:
                                    self.map[x + i][y + j] += 1

    def llenar_mapa(self):
        c = 0
        while c != self.minas:
            pos_x = random.randint(0, self.filas - 1)
            pos_y = random.randint(0, self.columnas - 1)
            if self.map[pos_x][pos_y] != 9:
                self.map[pos_x][pos_y] = 9
                c += 1

    def revelar(self, x, y):
        if x < 0 or x >= self.filas or y < 0 or y >= self.columnas:
            print("Coordenadas fuera de rango, intenta de nuevo.")
            return False
        if self.map[x][y] == 9:
            return False
        elif self.map[x][y] == 0:
            self.flood_fill(x, y)
        else:
            self.no_map[x][y] = self.int_to_string(self.map[x][y]) + " "
        return True

    def colocar_bandera(self, x, y):
        if self.no_map[x][y] == "- ":
            self.no_map[x][y] = "F "
        elif self.no_map[x][y] == "F ":
            self.no_map[x][y] = "- "

    def revelar_todas_las_minas(self):
        for x in range(self.filas):
            for y in range(self.columnas):
                if self.map[x][y] == 9:
                    self.no_map[x][y] = "9 "