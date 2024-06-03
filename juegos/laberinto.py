from edd.grafo import Grafo

def main_lab():
    filas = 10
    columnas = 10
    lab = Grafo(filas, columnas)
    pos_jugador = (0, 0)

    while True:
        lab.mostrar_lab(pos_jugador)
        mov_val = lab.obtener_mov_validos(pos_jugador)
        if pos_jugador == lab.salida:
            print("¡Felicidades, has llegado a la salida!")
            break
        if not mov_val:
            print("¡No hay movimientos válidos!")
            break

        mov = input("Ingrese su movimiento (WASD): ").upper()
        dx, dy = 0, 0
        if mov == 'W':
            dx, dy = -1, 0
        elif mov == 'S':
            dx, dy = 1, 0
        elif mov == 'A':
            dx, dy = 0, -1
        elif mov == 'D':
            dx, dy = 0, 1

        nueva_pos = (pos_jugador[0] + dx, pos_jugador[1] + dy)
        if nueva_pos in mov_val:
            pos_jugador = nueva_pos
        else:
            print("Movimiento inválido. Inténtelo de nuevo.")
