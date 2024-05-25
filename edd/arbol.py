import textwrap

class Nodo:
    def __init__(self, msg, opc_a = None, opc_b = None):
        self.msg = msg
        self.opc_a = opc_a
        self.opc_b = opc_b
        self.izq = None
        self.der = None

    def __str__(self):
        msg_formatted = textwrap.fill(self.msg, width=36)
        opc_a_formatted = textwrap.fill(self.opc_a, width=36) if self.opc_a else ""
        opc_b_formatted = textwrap.fill(self.opc_b, width=36) if self.opc_b else ""

        if self.opc_a == "" and self.opc_b == "":
            return f"Mensaje: {msg_formatted}"
        else:
            return (f"Mensaje: {msg_formatted}\n"
                    f"¿Qué debería hacer Toshi?\n"
                    f"Opción a: {opc_a_formatted}\n"
                    f"Opción b: {opc_b_formatted}")

class ArbolBinario:
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

    def recorrido_inorden(self, nodo):
        if nodo is not None:
            self.recorrido_inorden(nodo.izq)
            print(nodo)
            self.recorrido_inorden(nodo.der)