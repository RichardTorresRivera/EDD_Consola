class Decisiones:
    def __init__(self, iterador):
        self.iterador = iterador
    
    def get_iterador(self):
        return self.iterador
    
    def set_iterador(self, iterador):
        self.iterador = iterador

    def get_fondo(self):
        return self.iterador.img
    
    def get_msg(self):
        return self.iterador.msg
    
    def get_opc_a(self):
        return self.iterador.opc_a
    
    def get_opc_b(self):
        return self.iterador.opc_b
    
    def opc_a(self):
        self.iterador = self.iterador.izq

    def opc_b(self):
        self.iterador = self.iterador.der

    def game_over(self):
        if self.iterador.izq is None and self.iterador.der is None:
            return True
        else:
            return False