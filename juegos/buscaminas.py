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
    flag = True
    while flag and not matriz.comprobar():
        matriz.mostrar()
        print("Selecciona una acción:")
        print("\t1. Revelar celda")
        print("\t2. Colocar/Quitar bandera")
        accion = int(input("-> Acción: "))
        if accion == 1:
            x = int(input("\tX: "))
            y = int(input("\tY: "))
            flag = matriz.revelar(x, y)
        elif accion == 2:
            x = int(input("\tX: "))
            y = int(input("\tY: "))
            matriz.colocar_bandera(x, y)

    if flag:
        print("Ganaste")
    else:
        print("Perdiste")
        matriz.revelar_todas_las_minas()
        matriz.mostrar()
