from otros import entrada
from juegos.completar_palabras import main_palabras
from juegos.buscaminas import main_minas
from juegos.cartas import main_cartas
from juegos.hanoi import main_hanoi
from juegos.laberinto import main_lab
from juegos.decisiones import main_decisiones

def menu():
    print("\n-----------------------------------")
    print("|  JUEGOS DE ESTRUCTURA DE DATOS  |")
    print("-----------------------------------")
    print("| 1. Completar palabras           |")
    print("| 2. Buscaminas                   |")
    print("| 3. Emparejamiento de cartas     |")
    print("| 4. Torres de Hanoi              |")
    print("| 5. Laberinto                    |")
    print("| 6. Decisiones de Toshi          |")
    print("| 0. Salir                        |")
    print("-----------------------------------\n")

def main():
    while True:
        menu()
        opc = entrada.menu_opcion(6)
        print()
        if (opc == 1):
            main_palabras()
        elif (opc == 2):
            main_minas()
        elif (opc == 3):
            main_cartas()
        elif (opc == 4):
            main_hanoi()
        elif (opc == 5):
            main_lab()
        elif (opc == 6):
            main_decisiones()
        elif (opc == 0):
            print("Saliendo ...")
            break

if __name__ == '__main__':
    main()