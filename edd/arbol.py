class Nodo:
    def __init__(self, msg, opc_a = None, opc_b = None):
        self.msg = msg
        self.opc_a = opc_a
        self.opc_b = opc_b
        self.izq = None
        self.der = None

    def __str__(self):
        if self.opc_a is None and self.opc_b is None:
            return f"Mensaje: {self.msg}"
        else:
            return f"Mensaje: {self.msg}\n¿Que deberia hacer Toshi?\nOpcion a: {self.opc_a}\nOpcion b: {self.opc_b}"

class ArbolBinario:
    def __init__(self, lista):
        if not lista:
            self.raiz = None
        else:
            nodos = [Nodo(**item) for item in lista]
            
            for i in range(len(nodos)):
                izq_index = 2 * i + 1
                der_index = 2 * i + 2

                if izq_index < len(nodos):
                    nodos[i].izq = nodos[izq_index]
                if der_index < len(nodos):
                    nodos[i].der = nodos[der_index]

            self.raiz = nodos[0]

    def recorrido_inorden(self, nodo):
        if nodo is not None:
            self.recorrido_inorden(nodo.izq)
            print(nodo)
            self.recorrido_inorden(nodo.der)