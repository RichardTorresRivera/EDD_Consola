class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        if not self.cabeza:
            self.cabeza = Nodo(valor)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(valor)

    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos

    def ordenar(self):
        if not self.cabeza or not self.cabeza.siguiente:
            return

        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            while siguiente:
                if actual.valor > siguiente.valor:
                    actual.valor, siguiente.valor = siguiente.valor, actual.valor
                siguiente = siguiente.siguiente
            actual = actual.siguiente