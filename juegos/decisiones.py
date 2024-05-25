import csv
from otros import entrada
from edd.arbol import ArbolBinario, Nodo

def jugar(nodo):
    if nodo.izq is None and nodo.der is None:
        print(nodo)
        print("\n----------------FIN DEL JUEGO----------------")
    else:
        print(nodo)
        respuesta = entrada.arbol_opcion()
        print()
        if respuesta == "a":
            jugar(nodo.izq)
        elif respuesta == "b":
            jugar(nodo.der)
        else:
            print("Saliendo del juego ...")

def menu():
    print("\n----------------------------------------------")
    print("|              AVENTURA DE TOSHI             |")
    print("----------------------------------------------")
    print("| Toshi, una pila de la tribu de los Dianchi |")
    print("| fue testigo del robo de su contenedor de   |")
    print("| dióxido de manganeso (MnO2) por un miembro |")
    print("| de la tribu de los árboles amarillo (Shu). |")
    print("| Toshi emprendera un viaje para recuperar   |")
    print("| su contenedor.                             |")
    print("----------------------------------------------\n")

def nodos_arbol(nombre_archivo):
    lista = []
    with open(nombre_archivo, mode='r', newline='') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            lista.append({
                "msg": fila["msg"],
                "opc_a": fila["opc_a"],
                "opc_b": fila["opc_b"]
            })
    nodos = [Nodo(**item) for item in lista]
    
    return nodos
                
def mainDecisiones():
    nodos = nodos_arbol("otros\\data_decisiones.csv")

    # Crear el árbol de decisiones y jugar
    arbol = ArbolBinario(nodos)
    menu()
    jugar(arbol.raiz)

