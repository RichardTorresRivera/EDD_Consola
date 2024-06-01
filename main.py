from otros import entrada
from juegos.hanoi import main_hanoi
from juegos.decisiones import main_decisiones

def menu():
    print("\n-----------------------------------")
    print("|  JUEGOS DE ESTRUCTURA DE DATOS  |")
    print("-----------------------------------")
    print("| 1. Torres de Hanoi              |")
    print("| 2. Decisiones de Toshi          |")
    print("| 0. Salir                        |")
    print("-----------------------------------\n")
    
while True:
    menu()
    opc = entrada.menu_opcion(2)
    print()
    if (opc == 1):
        main_hanoi()
    elif (opc == 2):
        main_decisiones()
    elif (opc == 0):
        print("Saliendo ...")
        break