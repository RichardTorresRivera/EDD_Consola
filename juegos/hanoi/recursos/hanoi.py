class Hanoi():
    def __init__(self, torres):
        self.flotando = False
        self.disco_mover = None
        self.torre_origen = None
        self.torre_destino = None
        self.torres = torres
        self.movimientos = 0
    
    def get_flotando(self):
        return self.flotando

    def set_flotando(self, valor):
        self.flotando = valor
    
    def get_disco_mover(self):
        return self.disco_mover
    
    def set_disco_mover(self, disco):
        self.disco_mover = disco
    
    def get_torre_origen(self):
        return self.torre_origen
    
    def set_torre_origen(self, torre_origen):
        self.torre_origen = torre_origen

    def get_torre_destino(self):
        return self.torre_destino
    
    def set_torre_destino(self, torre_destino):
        self.torre_destino = torre_destino

    def get_movimientos(self):
        return self.movimientos

    def movimiento_valido(self):
        if self.torre_destino.esta_vacia() or self.disco_mover.peso <= self.torre_destino.get_cima():
            self.movimientos += 1
            return True
        else:
            return False
        
    def game_over(self, n):
        if self.torres[0].esta_vacia() and self.torres[1].esta_vacia() and self.torres[2].get_tamanio() == n:
            return True
        else:
            return False