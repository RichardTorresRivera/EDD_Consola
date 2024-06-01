import textwrap

class Nodo:
    """
    Clase para representar un nodo en un árbol binario.

    Attributes:
        msg (str): Mensaje del nodo.
        opc_a (str): Opción a del nodo.
        opc_b (str): Opción b del nodo.
        izq (Nodo): Nodo hijo izquierdo.
        der (Nodo): Nodo hijo derecho.
    """
    def __init__(self, msg, opc_a=None, opc_b=None):
        """
        Inicializa un nodo con un mensaje y dos opciones.

        Args:
            msg (str): Mensaje del nodo.
            opc_a (str, optional): Opción a del nodo. Por defecto es None.
            opc_b (str, optional): Opción b del nodo. Por defecto es None.
        """
        self.msg = msg
        self.opc_a = opc_a
        self.opc_b = opc_b
        self.izq = None
        self.der = None

    def __str__(self):
        """
        Representación en cadena del nodo.

        Returns:
            str: Representación formateada del nodo.
        """
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
    """
    Clase para representar un árbol binario.

    Attributes:
        raiz (Nodo): Nodo raíz del árbol.
    """
    def __init__(self, nodos):
        """
        Inicializa un árbol binario con una lista de nodos.

        Args:
            nodos (list): Lista de nodos para construir el árbol.
        """
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
        """
        Realiza un recorrido inorden del árbol.

        Args:
            nodo (Nodo): Nodo desde el cual comenzar el recorrido.
        """
        if nodo is not None:
            self.recorrido_inorden(nodo.izq)
            print(nodo)
            self.recorrido_inorden(nodo.der)
