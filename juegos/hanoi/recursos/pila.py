class Nodo:
    """
    Clase para representar un nodo en una pila.
    """
    def __init__(self, peso):
        """
        Inicializa un nodo con un peso y un puntero al siguiente nodo.
        
        Args:
            disco: Valor del nodo.
        """
        self.peso = peso
        self.sgte = None
    
    def get_peso(self):
        return self.peso


class Pila:
    """
    Clase para representar una pila.
    """
    def __init__(self):
        """
        Inicializa una pila vacía.
        """
        self.cima = None
        self.num_discos = 0
        
    def apilar(self, nodo):
        """
        Apila un peso en la cima de la pila.
        
        Args:
            peso: Valor a apilar.
        """
        nodo.sgte = self.cima
        self.cima = nodo
        self.num_discos += 1

    def desapilar(self):
        """
        Desapila el elemento de la cima de la pila y lo devuelve.
        
        Returns:
            El valor desapilado.
        """
        x = self.cima
        self.cima = self.cima.sgte
        self.num_discos -= 1
        return x

    def esta_vacia(self):
        """
        Verifica si la pila está vacía.
        
        Returns:
            bool: True si la pila está vacía, False en caso contrario.
        """
        return self.cima is None

    def get_cima(self):
        """
        Devuelve el peso de la cima de la pila.
        
        Returns:
            Valor de la cima o None si la pila está vacía.
        """
        if self.cima is not None:
            return self.cima.peso
        else:
            return None
    
    def get_tamanio(self):
        """
        Devuelve el numero de discos de la pila

        Returns:
            Numero de discos de la pila
        """
        return self.num_discos