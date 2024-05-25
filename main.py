from otros import entrada
from juegos.hanoi import mainHanoi 
from juegos.decisiones import mainDecisiones
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
        mainHanoi()
    elif (opc == 2):
        mainDecisiones()
    elif (opc == 0):
        print("Saliendo ...")
        break