class Nodo:
    def __init__(self, dato):
        # Crear un nodo
        self.dato = dato
        self.sgte = None

class Pila:
    def __init__(self):
        # Crea una pila vacia
        self.cima = None
        self.tamanio = 0
        
    def apilar(self, dato):
        # Apilar dato en la cima de la pila
        nodo = Nodo(dato)
        nodo.sgte = self.cima
        self.cima = nodo
        self.tamanio += 1

    def desapilar(self):
        # Desapila el elemento y lo devuelve
        x = self.cima.dato
        self.cima = self.cima.sgte
        self.tamanio -= 1
        return x

    def estaVacia(self):
        # Devuelve True si la lista esta vacia
        return self.cima is None

    def datoCima(self):
        # Devuelve el valor de la cima
        if self.cima is not None:
            return self.cima.dato
        else:
            return None

    def tamanio(self):
        # Devuelve el tamaño de la pila
        return self.tamanio

    def mostrar(self):
        # Muestra los valores de la pila
        if (self.estaVacia()):
            print("NULL\n")
        else:
            paux = Pila()
            while not self.estaVacia():
                dato = self.desapilar()
                print(dato)
                paux.apilar(dato)
            print()
            while not paux.estaVacia():
                dato = paux.desapilar()
                self.apilar(dato)
