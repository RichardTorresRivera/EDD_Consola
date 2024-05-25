from edd.pila import Pila
from otros import entrada
import copy

def crearDiscos(n):
    torre=[[]]
    t = n
    for i in range(2*n+3):
        if (i == (2*n+3)//2):
            torre[0].append("|")
        else:
            torre[0].append(" ")

    for i in range(1,n+1):
        torre.append([])
        for j in range(2*n+3):
            if (j < t-1 or j > (2*i+t+1)):
                torre[i].append(" ")
            elif (j == t-1):
                torre[i].append("[")
            elif (j == (2*i+t+1)):
                torre[i].append("]")
            else:
                torre[i].append("=")
        t -= 1
    return torre

def llenarTorre(n, pila):
    for i in range(n,0,-1):
        pila.apilar(i)

def mostrarTorres(n, pilas, torre):
    nombres = ["Pila A", "Pila B", "Pila C"]
    temp = copy.deepcopy(pilas)
    
    for i in range(3):
        dibujarDiscos(0, torre)
    print()
    
    for i in range(n,0,-1):
        for j in range(3):
            if (temp[j].tamanio < i):
                dibujarDiscos(0, torre)
            else:
                dibujarDiscos(temp[j].desapilar(), torre)
        print()
        
    for i in range(3):
        print(" "*(n-3), nombres[i], " "*(n-2), end="")
    print()

def dibujarDiscos(n_discos, torre):
    for i in torre[n_discos]:
        print(i, end = "")

def moverDiscos(pila1, pila2, mov):
    if (not pila1.estaVacia()):
        if (pila2.estaVacia() or pila1.datoCima() < pila2.datoCima()):
            disco = pila1.desapilar()
            pila2.apilar(disco)
            mov[0] += 1
        else:
            print("Movimiento invalido, el peso del disco a mover es mayor al disco superior de la torre destino")
    else:
        print("La pila esta vacia, no hay discos para mover")
    

def menu():
    print("\n---------------------------------")
    print("|      LAS TORRES DE HANOI      |")
    print("---------------------------------")
    print("| 1. Mover disco de torre A a B |")
    print("| 2. Mover disco de torre A a C |")
    print("| 3. Mover disco de torre B a A |")
    print("| 4. Mover disco de torre B a C |")
    print("| 5. Mover disco de torre C a A |")
    print("| 6. Mover disco de torre C a B |")
    print("| 0. Salir")
    print("-----------------------------")

def numeroDiscos():
    flag = True
    while flag:
        discos = entrada.num_entero("Ingrese el numero de discos: ")
        print()
        if discos >= 3:
            flag = False
        else:
            print("ERROR: El numero de discos es menor a 3")
    return discos
    
def finJuego(pilas):
    if (pilas[0].estaVacia() and pilas[1].estaVacia()):
        print("\nFELICIDADES, FIN DEL JUEGO")
        return True
    else:
        return False

def mainHanoi():
    print("\n---------------------------------")
    print("|      LAS TORRES DE HANOI      |")
    print("---------------------------------")
    n = numeroDiscos()
    torre = crearDiscos(n)
    pilas = [Pila(), Pila(), Pila()]
    llenarTorre(n, pilas[0])
    mostrarTorres(n, pilas, torre)
    mov = [0]

    jugando = True
    while jugando:
        menu()
        opc = entrada.menu_opcion(6)
        print()
        if (opc == 1):
            moverDiscos(pilas[0], pilas[1], mov)
        elif (opc == 2):
            moverDiscos(pilas[0], pilas[2], mov)
        elif (opc == 3):
            moverDiscos(pilas[1], pilas[0], mov)
        elif (opc == 4):
            moverDiscos(pilas[1], pilas[2], mov)
        elif (opc == 5):
            moverDiscos(pilas[2], pilas[0], mov)
        elif (opc == 6):
            moverDiscos(pilas[2], pilas[1], mov)
        elif(opc == 0):
            break
        mostrarTorres(n, pilas, torre)
        jugando = not finJuego(pilas)
        print("\nNumero de movimientos: ", mov[0])
