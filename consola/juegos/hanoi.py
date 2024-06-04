import copy

from edd.pila import Pila
from otros import entrada

def crear_discos(n):
    """
    Crea una representación visual de los discos para las Torres de Hanoi.
    
    Args:
        n (int): Número de discos.
        
    Returns:
        list: Representación de las torres con discos.
    """
    torre = [[]]
    t = n
    for i in range(2 * n + 3):
        if i == (2 * n + 3) // 2:
            torre[0].append("|")
        else:
            torre[0].append(" ")

    for i in range(1, n + 1):
        torre.append([])
        for j in range(2 * n + 3):
            if j < t - 1 or j > (2 * i + t + 1):
                torre[i].append(" ")
            elif j == t - 1:
                torre[i].append("[")
            elif j == (2 * i + t + 1):
                torre[i].append("]")
            else:
                torre[i].append("=")
        t -= 1
    return torre


def llenar_torre(n, pila):
    """
    Llena una pila con discos.
    
    Args:
        n (int): Número de discos.
        pila (Pila): Objeto de la clase Pila.
    """
    for i in range(n, 0, -1):
        pila.apilar(i)


def mostrar_torres(n, pilas, torre):
    """
    Muestra el estado actual de las torres de Hanoi.
    
    Args:
        n (int): Número de discos.
        pilas (list): Lista de objetos de la clase Pila.
        torre (list): Representación de las torres con discos.
    """
    nombres = ["Pila A", "Pila B", "Pila C"]
    temp = copy.deepcopy(pilas)

    for _ in range(3):
        dibujar_discos(0, torre)
    print()

    for i in range(n, 0, -1):
        for j in range(3):
            if temp[j].tamanio < i:
                dibujar_discos(0, torre)
            else:
                dibujar_discos(temp[j].desapilar(), torre)
        print()

    for i in range(3):
        print(" " * (n - 3), nombres[i], " " * (n - 2), end="")
    print()


def dibujar_discos(n_discos, torre):
    """
    Dibuja los discos en la torre.
    
    Args:
        n_discos (int): Número de discos.
        torre (list): Representación de las torres con discos.
    """
    for i in torre[n_discos]:
        print(i, end="")


def mover_discos(pila1, pila2, mov):
    """
    Mueve un disco de una pila a otra si es válido.
    
    Args:
        pila1 (Pila): Pila de origen.
        pila2 (Pila): Pila de destino.
        mov (list): Contador de movimientos.
    """
    if not pila1.esta_vacia():
        if pila2.esta_vacia() or pila1.dato_cima() < pila2.dato_cima():
            disco = pila1.desapilar()
            pila2.apilar(disco)
            mov[0] += 1
        else:
            print("Movimiento invalido:\nEl peso del disco a mover es mayor\nal disco superior de la torre destino.\n")
    else:
        print("Movimiento invalido:\nLa pila está vacía, no hay discos\npara mover.\n")


def menu():
    """
    Muestra el menú de opciones del juego.
    """
    print("\n---------------------------------")
    print("|      LAS TORRES DE HANOI      |")
    print("---------------------------------")
    print("| 1. Mover disco de torre A a B |")
    print("| 2. Mover disco de torre A a C |")
    print("| 3. Mover disco de torre B a A |")
    print("| 4. Mover disco de torre B a C |")
    print("| 5. Mover disco de torre C a A |")
    print("| 6. Mover disco de torre C a B |")
    print("| 0. Salir                      |")
    print("---------------------------------\n")


def numero_discos():
    """
    Solicita al usuario ingresar el número de discos hasta que sea válido.
    
    Returns:
        int: Número de discos.
    """
    flag = True
    while flag:
        discos = entrada.num_entero("Ingrese el número de discos: ")
        print()
        if discos >= 3:
            flag = False
        else:
            print("ERROR: El número de discos es menor a 3")
    return discos


def fin_juego(pilas):
    """
    Verifica si el juego ha terminado.
    
    Args:
        pilas (list): Lista de objetos de la clase Pila.
    
    Returns:
        bool: True si el juego ha terminado, False en caso contrario.
    """
    if pilas[0].esta_vacia() and pilas[1].esta_vacia():
        print("\n-----FELICIDADES, FIN DEL JUEGO-----")
        return True
    else:
        return False


def main_hanoi():
    """
    Función principal para ejecutar el juego de las Torres de Hanoi.
    """
    print("\n---------------------------------")
    print("|      LAS TORRES DE HANOI      |")
    print("---------------------------------\n")
    n = numero_discos()
    torre = crear_discos(n)
    pilas = [Pila(), Pila(), Pila()]
    llenar_torre(n, pilas[0])
    mostrar_torres(n, pilas, torre)
    mov = [0]

    jugando = True
    while jugando:
        menu()
        opc = entrada.menu_opcion(6)
        print()
        if opc == 1:
            mover_discos(pilas[0], pilas[1], mov)
        elif opc == 2:
            mover_discos(pilas[0], pilas[2], mov)
        elif opc == 3:
            mover_discos(pilas[1], pilas[0], mov)
        elif opc == 4:
            mover_discos(pilas[1], pilas[2], mov)
        elif opc == 5:
            mover_discos(pilas[2], pilas[0], mov)
        elif opc == 6:
            mover_discos(pilas[2], pilas[1], mov)
        elif opc == 0:
            print("Saliendo del juego ...")
            break
        mostrar_torres(n, pilas, torre)
        jugando = not fin_juego(pilas)
        print("\nNúmero de movimientos: ", mov[0])