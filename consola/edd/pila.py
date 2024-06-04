class Nodo:
    """
    Clase para representar un nodo en una pila.
    """
    def __init__(self, dato):
        """
        Inicializa un nodo con un dato y un puntero al siguiente nodo.
        
        Args:
            dato: Valor del nodo.
        """
        self.dato = dato
        self.sgte = None


class Pila:
    """
    Clase para representar una pila.
    """
    def __init__(self):
        """
        Inicializa una pila vacía.
        """
        self.cima = None
        self.tamanio = 0
        
    def apilar(self, dato):
        """
        Apila un dato en la cima de la pila.
        
        Args:
            dato: Valor a apilar.
        """
        nodo = Nodo(dato)
        nodo.sgte = self.cima
        self.cima = nodo
        self.tamanio += 1

    def desapilar(self):
        """
        Desapila el elemento de la cima de la pila y lo devuelve.
        
        Returns:
            El valor desapilado.
        """
        x = self.cima.dato
        self.cima = self.cima.sgte
        self.tamanio -= 1
        return x

    def esta_vacia(self):
        """
        Verifica si la pila está vacía.
        
        Returns:
            bool: True si la pila está vacía, False en caso contrario.
        """
        return self.cima is None

    def dato_cima(self):
        """
        Devuelve el valor de la cima de la pila.
        
        Returns:
            Valor de la cima o None si la pila está vacía.
        """
        if self.cima is not None:
            return self.cima.dato
        else:
            return None

    def mostrar(self):
        """
        Muestra los valores en la pila.
        """
        if self.esta_vacia():
            print("NULL\n")
        else:
            paux = Pila()
            while not self.esta_vacia():
                dato = self.desapilar()
                print(dato)
                paux.apilar(dato)
            print()
            while not paux.esta_vacia():
                dato = paux.desapilar()
                self.apilar(dato)