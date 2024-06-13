class Nodo:
    def __init__(self, img, msg, opc_a, opc_b):
        self.img = img
        self.msg = msg
        self.opc_a = opc_a
        self.opc_b = opc_b
        self.izq = None
        self.der = None
    
class ArbolBinario():
    def __init__(self, nodos):
        if not nodos:
            self.raiz = None
        else:
            for i in range(len(nodos)):
                izq_index = 2 * i + 1
                der_index = 2 * i + 2

                if izq_index < len(nodos):
                    nodos[i].izq = nodos[izq_index]
                if der_index < len(nodos):
                    nodos[i].der = nodos[der_index]

            self.raiz = nodos[0]
    
    def get_raiz(self):
        return self.raiz