from juegos.laberinto import main_lab
from otros import entrada
from juegos.hanoi import main_hanoi
from juegos.decisiones import main_decisiones
from juegos.buscaminas import main_minas

def menu():
    print("\n-----------------------------------")
    print("|  JUEGOS DE ESTRUCTURA DE DATOS  |")
    print("-----------------------------------")
    print("| 1. Torres de Hanoi              |")
    print("| 2. Decisiones de Toshi          |")
    print("| 3. Buscaminas                   |")
    print("| 4. Laberinto                    |")
    print("| 0. Salir                        |")
    print("-----------------------------------\n")
    
while True:
    menu()
    opc = entrada.menu_opcion(4)
    print()
    if (opc == 1):
        main_hanoi()
    elif (opc == 2):
        main_decisiones()
    elif (opc == 3):
        main_minas()
    elif (opc == 4):
        main_lab()
    elif (opc == 0):
        print("Saliendo ...")
        break