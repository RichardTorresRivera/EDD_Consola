from edd.matriz import Matriz

def main_minas():
    dificultad = int(input("Elige la dificultad:\n1. Facil\n2. Dificil\n-> Opción: "))
    if dificultad == 1:
        tam_x, tam_y, minas = 8, 10, 10
    elif dificultad == 2:
        tam_x, tam_y, minas = 13, 17, 40
    else:
        print("Opción no válida.")
        return

    matriz = Matriz(tam_x, tam_y, minas)
    posicion_x, posicion_y = 0, 0
    flag = True
    while flag and not matriz.comprobar():
        matriz.mostrar(posicion_x, posicion_y)
        print("Moverse: w/a/s/d | Revelar celda: r | Colocar/Quitar bandera: f |")
        accion = input("-> Acción: ").strip().lower()
        if accion in ['w', 'a', 's', 'd']:
            posicion_x, posicion_y = mover_jugador(accion, posicion_x, posicion_y, tam_x, tam_y)
        elif accion == 'r':
            flag = matriz.revelar(posicion_x, posicion_y)
        elif accion == 'f':
            matriz.colocar_bandera(posicion_x, posicion_y)

    if flag:
        print("*******")
        print("Ganaste")
        print("*******")
    else:
        print("********")
        print("Perdiste")
        print("********")
        matriz.revelar_todas_las_minas()
        matriz.mostrar(posicion_x, posicion_y)

def mover_jugador(direccion, posicion_x, posicion_y, tam_x, tam_y):
    if direccion == 'w' and posicion_x > 0:
        posicion_x -= 1
    elif direccion == 'a' and posicion_y > 0:
        posicion_y -= 1
    elif direccion == 's' and posicion_x < tam_x - 1:
        posicion_x += 1
    elif direccion == 'd' and posicion_y < tam_y - 1:
        posicion_y += 1
    return posicion_x, posicion_y