from otros import entrada
from edd.arbol import ArbolBinario

def jugar(nodo):
    if nodo.izq is None and nodo.der is None:
        print(nodo)
        print("FIN DEL JUEGO")
    else:
        print(nodo)
        respuesta = entrada.arbol_opcion()
        print()
        if respuesta == "a":
            jugar(nodo.izq)
        else:
            jugar(nodo.der)

def menu():
    print("\n----------------------------")
    print("|     AVENTURA DE TOSHI     |")
    print("-----------------------------")
                
def mainDecisiones():
    # Lista de mensajes para el árbol de decisiones
    lista = [
        {"msg": "Toshi logra encontrar la aldea de la tribu Shu, pero esta se encuentra vigilada por un guardia", "opc_a":"Persuadir al guardia para obtener ayuda", "opc_b": "Amenazarlo para obtener información"},
        {"msg": "El guardia está de tu lado y te proporciona un mapa con la ubicacion del contenedor. Te diriges a la ubicacion y se encuentra vigilada por el ladron", "opc_a":"Luchar directamente", "opc_b":"Intentar una emboscada"},
        {"msg":"El guardia enfurece y Toshi es capturado"},
        {"msg":"Ganas el respeto del ladron y recuperas el contenedor"},
        {"msg":"Fuiste capturado y encarcelado"}
    ]

    # Crear el árbol de decisiones y jugar
    arbol = ArbolBinario(lista)
    menu()
    jugar(arbol.raiz)

